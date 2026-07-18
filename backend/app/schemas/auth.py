from uuid import UUID

from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: str | None = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserRegister(BaseModel):
    email: EmailStr
    password: str
    role_name: str = "Viewer"


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    is_active: bool
    role_name: str

    class Config:
        from_attributes = True
