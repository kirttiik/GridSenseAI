from sqlalchemy.ext.asyncio import AsyncSession

from app.models.market.market_data import MarketData
from .base.generic_repository import GenericRepository


class MarketRepository(GenericRepository[MarketData]):
    """Repository for MVP MarketData model."""
    def __init__(self, session: AsyncSession):
        super().__init__(session, MarketData)
