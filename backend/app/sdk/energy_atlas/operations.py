from typing import Any

from app.sdk.energy_atlas.models import SDKResponse


class OperationsModule:
    """SDK module for Power System Operations Analytics."""

    def __init__(self, client: Any):
        self._client = client

    async def get_psp_daily(
        self, limit: int | None = None, offset: int | None = None
    ) -> SDKResponse[Any]:
        """Fetch POSOCO Daily Power Supply Position (PSP) data."""
        params = {"limit": limit, "offset": offset}
        return await self._client.get("/api/intelligence/posoco-psp", params=params)

    async def get_monthly_psp(
        self, limit: int | None = None, offset: int | None = None
    ) -> SDKResponse[Any]:
        """Fetch CEA Monthly Power Supply Position (PSP) data."""
        params = {"limit": limit, "offset": offset}
        return await self._client.get("/api/intelligence/cea-psp", params=params)

    async def get_energy_investments(
        self, limit: int | None = None, offset: int | None = None
    ) -> SDKResponse[Any]:
        """Fetch Energy Investments data."""
        params = {"limit": limit, "offset": offset}
        return await self._client.get("/api/intelligence/energy-investments", params=params)
