from datetime import UTC, datetime, timedelta

import jwt
from pydantic import ValidationError

from app.core.settings import settings


def create_access_token(subject: str, expires_delta: timedelta | None = None) -> str:
    """Create a JWT access token for a given subject (user ID)."""
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: str, expires_delta: timedelta | None = None) -> str:
    """Create a JWT refresh token for a given subject."""
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expire, "sub": str(subject), "refresh": True}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> str | None:
    """
    Verify a token and return the subject (user ID) if valid.
    Returns None if token is invalid or expired.
    """
    try:
        decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return decoded_data.get("sub")
    except jwt.PyJWTError:
        return None
    except ValidationError:
        return None
