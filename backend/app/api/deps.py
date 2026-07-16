from collections.abc import AsyncGenerator

from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import DatabaseSessionManager


async def get_db_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    session_manager: DatabaseSessionManager = request.app.state.db
    async with session_manager.session() as session:
        yield session
