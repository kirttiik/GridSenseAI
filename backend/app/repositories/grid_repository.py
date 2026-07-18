from sqlalchemy.ext.asyncio import AsyncSession

from app.models.grid.grid_status import GridStatus
from .base.generic_repository import GenericRepository


class GridRepository(GenericRepository[GridStatus]):
    """Repository for MVP GridStatus model."""
    def __init__(self, session: AsyncSession):
        super().__init__(session, GridStatus)
