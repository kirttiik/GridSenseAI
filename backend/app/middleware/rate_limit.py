import time

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from app.core.settings import settings

# In-memory dictionary for rate limiting: {ip_or_token: (count, timestamp)}
# Not suitable for multi-worker production without Redis, but works for foundational implementation.
_RATE_LIMIT_STORE: dict[str, tuple[int, float]] = {}


class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        # Extract client IP
        client_ip = request.client.host if request.client else "unknown"

        # If API Key is present, we could limit by API key instead, but we'll use IP for general limiting.
        api_key = request.headers.get(settings.API_KEY_HEADER)
        identifier = api_key if api_key else client_ip

        current_time = time.time()

        # Clean up old entries occasionally (simple approach)
        if len(_RATE_LIMIT_STORE) > 10000:
            _RATE_LIMIT_STORE.clear()

        record = _RATE_LIMIT_STORE.get(identifier)
        if record:
            count, start_time = record
            if current_time - start_time > 60:
                # Reset window
                _RATE_LIMIT_STORE[identifier] = (1, current_time)
            else:
                if count >= settings.RATE_LIMIT_PER_MINUTE:
                    return JSONResponse(
                        status_code=429,
                        content={
                            "success": False,
                            "error": {
                                "code": "TOO_MANY_REQUESTS",
                                "message": "Rate limit exceeded. Try again later.",
                            },
                        },
                    )
                _RATE_LIMIT_STORE[identifier] = (count + 1, start_time)
        else:
            _RATE_LIMIT_STORE[identifier] = (1, current_time)

        response = await call_next(request)
        return response
