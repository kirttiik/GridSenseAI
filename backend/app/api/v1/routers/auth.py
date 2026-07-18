from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select

from app.db.session import AsyncSessionLocal
from app.models.role import Role
from app.models.user import User
from app.schemas.auth import Token, UserRegister, UserResponse
from app.schemas.responses import SuccessResponse
from app.security.authentication.passwords import get_password_hash, verify_password
from app.security.permissions.deps import get_current_active_user
from app.security.tokens.jwt import create_access_token

router = APIRouter()


@router.post("/login/access-token", response_model=Token)
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests.
    """
    async with AsyncSessionLocal() as session:
        stmt = select(User).where(User.email == form_data.username)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()

        if not user or not verify_password(form_data.password, user.password_hash):
            raise HTTPException(status_code=400, detail="Incorrect email or password")
        elif not user.is_active:
            raise HTTPException(status_code=400, detail="Inactive user")

        access_token = create_access_token(subject=str(user.id))
        return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", response_model=SuccessResponse[UserResponse])
async def register(user_in: UserRegister) -> Any:
    """
    Register a new user.
    """
    async with AsyncSessionLocal() as session:
        stmt = select(User).where(User.email == user_in.email)
        result = await session.execute(stmt)
        if result.scalar_one_or_none():
            raise HTTPException(
                status_code=400, detail="The user with this username already exists in the system."
            )

        role_stmt = select(Role).where(Role.name == user_in.role_name)
        role_result = await session.execute(role_stmt)
        role = role_result.scalar_one_or_none()
        if not role:
            # Create role on the fly if it doesn't exist for simplicity
            role = Role(name=user_in.role_name)
            session.add(role)
            await session.flush()

        new_user = User(
            email=user_in.email,
            password_hash=get_password_hash(user_in.password),
            role_id=role.id,
            is_active=True,
        )
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        return SuccessResponse(
            data=UserResponse(
                id=new_user.id,
                email=new_user.email,
                is_active=new_user.is_active,
                role_name=role.name,
            )
        )


@router.get("/me", response_model=SuccessResponse[UserResponse])
async def read_users_me(current_user: User = Depends(get_current_active_user)) -> Any:
    """
    Get current user profile.
    """
    return SuccessResponse(
        data=UserResponse(
            id=current_user.id,
            email=current_user.email,
            is_active=current_user.is_active,
            role_name=current_user.role.name if current_user.role else "Unknown",
        )
    )
