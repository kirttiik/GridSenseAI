from typing import Any

from app.sdk.energy_atlas.models import SDKResponse


class GridModule:
    """SDK module for National Grid Analytics."""

    def __init__(self, client: Any):
        self._client = client

    async def get_frequency(
        self, limit: int | None = None, offset: int | None = None, state: str | None = None
    ) -> SDKResponse[Any]:
        """Fetch latest grid frequency data."""
        params = {"limit": limit, "offset": offset, "state": state}
        return await self._client.get("/api/intelligence/grid-frequency", params=params)

    async def get_frequency_15min(
        self, limit: int | None = None, offset: int | None = None, state: str | None = None
    ) -> SDKResponse[Any]:
        """Fetch 15-minute resolution grid frequency data."""
        params = {"resolution": "15m", "limit": limit, "offset": offset, "state": state}
        return await self._client.get("/api/intelligence/grid-frequency", params=params)
