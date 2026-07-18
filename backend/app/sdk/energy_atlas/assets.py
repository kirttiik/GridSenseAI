from typing import Any

from app.sdk.energy_atlas.models import SDKResponse


class AssetsModule:
    """SDK module for Infrastructure and Assets Analytics."""

    def __init__(self, client: Any):
        self._client = client

    async def get_power_plants(
        self, limit: int | None = None, offset: int | None = None
    ) -> SDKResponse[Any]:
        """Fetch power plants data."""
        params = {"limit": limit, "offset": offset}
        return await self._client.get("/api/intelligence/power-plants", params=params)

    async def get_transmission_lines(
        self, limit: int | None = None, offset: int | None = None
    ) -> SDKResponse[Any]:
        """Fetch transmission lines data."""
        params = {"limit": limit, "offset": offset}
        return await self._client.get("/api/edges", params=params)

    async def get_substations(
        self, limit: int | None = None, offset: int | None = None
    ) -> SDKResponse[Any]:
        """Fetch substations data."""
        params = {"limit": limit, "offset": offset}
        return await self._client.get("/api/nodes", params=params)
