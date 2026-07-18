from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.db.session import AsyncSessionLocal
from app.models.user import User
from app.repositories import UnitOfWork
from app.security.tokens.jwt import verify_token

# This tells FastAPI where the login URL is for Swagger UI
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """Validate token and return current User."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user_id_str = verify_token(token)
    if not user_id_str:
        raise credentials_exception

    try:
        user_id = UUID(user_id_str)
    except ValueError:
        raise credentials_exception

    async with AsyncSessionLocal() as session:
        uow = UnitOfWork(session)
        # Using a raw query or repository if users repository existed
        # We will query directly for simplicity or build a quick users repo if it doesn't exist
        from sqlalchemy import select
        from sqlalchemy.orm import selectinload

        stmt = select(User).options(selectinload(User.role)).where(User.id == user_id)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()

        if user is None:
            raise credentials_exception

        return user


async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """Ensure current user is active."""
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
