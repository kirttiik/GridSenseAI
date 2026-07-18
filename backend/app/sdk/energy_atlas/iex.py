from typing import Any

from app.sdk.energy_atlas.models import SDKResponse


class IexModule:
    """SDK module for IEX Market Analytics."""

    def __init__(self, client: Any):
        self._client = client

    async def get_dam(
        self, limit: int | None = None, offset: int | None = None
    ) -> SDKResponse[Any]:
        """Fetch Day Ahead Market (DAM) data."""
        params = {"market_type": "DAM", "limit": limit, "offset": offset}
        params = {k: v for k, v in params.items() if v is not None}
        return await self._client.get("/developer/v1/market/iex/latest", params=params)

    async def get_rtm(
        self, limit: int | None = None, offset: int | None = None
    ) -> SDKResponse[Any]:
        """Fetch Real Time Market (RTM) data."""
        params = {"market_type": "RTM", "limit": limit, "offset": offset}
        params = {k: v for k, v in params.items() if v is not None}
        return await self._client.get("/developer/v1/market/iex/latest", params=params)

    async def get_gdam(
        self, limit: int | None = None, offset: int | None = None
    ) -> SDKResponse[Any]:
        """Fetch Green Day Ahead Market (GDAM) data."""
        params = {"limit": limit, "offset": offset}
        params = {k: v for k, v in params.items() if v is not None}
        return await self._client.get("/api/intelligence/iex-green-market", params=params)

