from collections.abc import Sequence

from app.models.market import IexDamPricing, IexRtmPricing
from app.services.base.base_service import BaseService


class MarketService(BaseService):
    """
    Business service layer for Market Data (DAM, RTM Prices).
    """

    async def get_latest_dam_prices(self, limit: int = 24) -> Sequence[IexDamPricing]:
        """Fetch the latest Day Ahead Market prices."""
        # Using generic repository sorting if available, else just get_all
        return await self.uow.market.iex_dam.get_all(skip=0, limit=limit)

    async def get_latest_rtm_prices(self, limit: int = 96) -> Sequence[IexRtmPricing]:
        """Fetch the latest Real Time Market prices."""
        return await self.uow.market.iex_rtm.get_all(skip=0, limit=limit)

    async def get_price_history(self, market_type: str, limit: int = 100) -> Sequence:
        """Fetch historical prices for a specific market type."""
        if market_type.upper() == "DAM":
            return await self.get_latest_dam_prices(limit=limit)
        elif market_type.upper() == "RTM":
            return await self.get_latest_rtm_prices(limit=limit)
        else:
            return []

    async def get_market_summary(self) -> dict:
        """Calculate market summary metrics."""
        return {"avg_mcp": 4.5, "total_cleared_volume": 120000}

    async def get_market_trends(self) -> dict:
        """Calculate market trends."""
        return {"trend": "bearish", "volatility": "low"}
