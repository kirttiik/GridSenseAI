from fastapi import HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader

from app.core.settings import settings

api_key_header = APIKeyHeader(name=settings.API_KEY_HEADER, auto_error=False)


async def verify_api_key(api_key_header: str = Security(api_key_header)):
    """Validate API key for external SDK consumers."""
    if not api_key_header:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="API Key missing")

    allowed_keys = [k.strip() for k in settings.ALLOWED_API_KEYS.split(",")]
    if api_key_header not in allowed_keys:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid or inactive API Key"
        )
    return api_key_header
