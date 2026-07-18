import asyncio
import logging
from collections.abc import Callable
from functools import wraps
from typing import Any

from app.etl.exceptions import RateLimitError, RecoverableETLError

logger = logging.getLogger(__name__)


def with_retry(max_retries: int = 3, base_delay: int = 2):
    """
    Retry decorator for async functions facing RecoverableETLError.
    Uses exponential backoff.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            retries = 0
            while True:
                try:
                    return await func(*args, **kwargs)
                except (RecoverableETLError, RateLimitError) as e:
                    retries += 1
                    if retries > max_retries:
                        logger.error(
                            f"Max retries ({max_retries}) reached for {func.__name__}. Failing."
                        )
                        raise

                    delay = base_delay**retries
                    logger.warning(
                        f"Recoverable error in {func.__name__}: {e}. Retrying in {delay}s... ({retries}/{max_retries})"
                    )
                    await asyncio.sleep(delay)

        return wrapper

    return decorator
