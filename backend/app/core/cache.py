import functools
import time
from collections.abc import Callable
from typing import Any

from fastapi import Request

# Simple in-memory cache: { "key": (expiry_time, value) }
# In a real distributed production environment, this would be backed by Redis.
# This implementation provides zero-dependency caching for the API layer.
_CACHE_STORE: dict[str, tuple[float, Any]] = {}


def _generate_cache_key(func_name: str, args: tuple, kwargs: dict, request: Request = None) -> str:
    """Generates a stable cache key based on function name, arguments and query params."""
    key_parts = [func_name]

    # Simple argument serialization
    for arg in args:
        if hasattr(arg, "url"):  # Ignore FastAPI Request objects
            continue
        key_parts.append(str(arg))

    for k, v in sorted(kwargs.items()):
        if k == "request" or hasattr(v, "url"):
            continue
        key_parts.append(f"{k}={v}")

    if request:
        key_parts.append(str(request.url))

    return "::".join(key_parts)


def cache_response(ttl_seconds: int = 60):
    """
    Decorator to cache the response of async FastAPI endpoints.
    Args:
        ttl_seconds (int): Time-to-live for the cached item in seconds.
    """

    def decorator(func: Callable):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Extract request if available for full URL caching
            request = kwargs.get("request")
            if not request and args and hasattr(args[0], "url"):
                request = args[0]

            cache_key = _generate_cache_key(func.__name__, args, kwargs, request)

            # Check cache
            current_time = time.time()
            if cache_key in _CACHE_STORE:
                expiry, cached_value = _CACHE_STORE[cache_key]
                if current_time < expiry:
                    return cached_value
                else:
                    # Expired, clean it up
                    del _CACHE_STORE[cache_key]

            # Prevent unbounded memory growth
            if len(_CACHE_STORE) > 1000:
                # Basic cleanup of expired keys if cache grows too large
                keys_to_delete = [k for k, (exp, _) in _CACHE_STORE.items() if exp < current_time]
                for k in keys_to_delete:
                    del _CACHE_STORE[k]
                if len(_CACHE_STORE) > 1000:
                    _CACHE_STORE.clear()

            # Execute function
            result = await func(*args, **kwargs)

            # Store result
            _CACHE_STORE[cache_key] = (current_time + ttl_seconds, result)

            return result

        return wrapper

    return decorator
