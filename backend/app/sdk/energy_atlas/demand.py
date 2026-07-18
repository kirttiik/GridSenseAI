from typing import Any

from app.sdk.energy_atlas.models import SDKResponse


class DemandModule:
    """SDK module for Power Demand Analytics."""

    def __init__(self, client: Any):
        self._client = client

    async def get_timeseries(
        self, limit: int | None = None, offset: int | None = None, state: str | None = None
    ) -> SDKResponse[Any]:
        """Fetch demand timeseries data."""
        params = {"limit": limit, "offset": offset, "state": state}
        return await self._client.get("/api/intelligence/demand-timeseries", params=params)
