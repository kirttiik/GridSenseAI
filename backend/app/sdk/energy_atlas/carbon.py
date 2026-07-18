from typing import Any

from app.sdk.energy_atlas.models import SDKResponse


class CarbonModule:
    """SDK module for Carbon Intensity Analytics."""

    def __init__(self, client: Any):
        self._client = client

    async def get_carbon_intensity(
        self, limit: int | None = None, offset: int | None = None, state: str | None = None
    ) -> SDKResponse[Any]:
        """Fetch carbon intensity timeseries data."""
        params = {"limit": limit, "offset": offset, "state": state}
        return await self._client.get("/api/intelligence/carbon-intensity", params=params)
