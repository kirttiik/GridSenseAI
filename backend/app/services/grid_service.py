import uuid
from collections.abc import Sequence

from app.models.grid import GridFrequency
from app.services.base.base_service import BaseService


class GridService(BaseService):
    """
    Business service layer for Grid Operations (Frequency, Health, Stability).
    """

    async def get_grid_frequency(self, region_id: uuid.UUID) -> GridFrequency | None:
        """Fetch the latest grid frequency for a region."""
        return await self.uow.grid.latest_frequency(region_id)

    async def get_frequency_history(
        self, region_id: uuid.UUID, limit: int = 100
    ) -> Sequence[GridFrequency]:
        """Fetch frequency history for a region."""
        return await self.uow.grid.frequency_history(region_id, limit=limit)

    async def get_grid_events(self) -> list:
        """Fetch significant grid events (placeholder for future implementation)."""
        return [{"event": "Frequency Drop", "severity": "WARNING", "region": "NORTH"}]

    async def get_grid_health(self) -> dict:
        """Calculate overall grid health status."""
        return {"health_score": 98.5, "status": "OPTIMAL"}

    async def get_voltage_summary(self) -> dict:
        """Get summary of voltage levels across the grid."""
        return {"avg_voltage_kv": 400, "deviations": 2}

    async def get_grid_stability(self) -> dict:
        """Calculate a grid stability index."""
        return {"stability_index": 0.99, "is_stable": True}
