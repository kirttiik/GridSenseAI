from fastapi import Depends, HTTPException, status

from app.models.user import User
from app.security.permissions.deps import get_current_active_user


class RequireRole:
    """
    Dependency class to enforce Role-Based Access Control (RBAC).
    """

    def __init__(self, allowed_roles: list[str]):
        self.allowed_roles = [r.lower() for r in allowed_roles]

    async def __call__(self, current_user: User = Depends(get_current_active_user)) -> User:
        if not current_user.role or current_user.role.name.lower() not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Operation not permitted. Requires one of: {', '.join(self.allowed_roles)}",
            )
        return current_user
