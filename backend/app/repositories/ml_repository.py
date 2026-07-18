from sqlalchemy.ext.asyncio import AsyncSession

from app.models.ml.ai_insight import AIInsight
from .base.generic_repository import GenericRepository


class MlRepository(GenericRepository[AIInsight]):
    """Repository for MVP AIInsight model."""
    def __init__(self, session: AsyncSession):
        super().__init__(session, AIInsight)
