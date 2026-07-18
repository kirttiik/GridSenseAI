from typing import Any

from app.sdk.energy_atlas.models import SDKResponse


class GenerationModule:
    """SDK module for Power Generation Analytics."""

    def __init__(self, client: Any):
        self._client = client

    async def get_generation(
        self, limit: int | None = None, offset: int | None = None, state: str | None = None
    ) -> SDKResponse[Any]:
        """Fetch generation fuel-mix timeseries data."""
        params = {"limit": limit, "offset": offset, "state": state}
        return await self._client.get("/api/intelligence/fuel-mix-timeseries", params=params)
