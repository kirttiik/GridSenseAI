import uuid
from collections.abc import Sequence

from app.models.energy import GenerationTimeseries
from app.services.base.base_service import BaseService


class EnergyService(BaseService):
    """
    Business service layer for Energy Data (Demand, Generation, Carbon).
    """

    async def get_current_generation(self) -> Sequence[GenerationTimeseries]:
        """Fetch the latest available generation record(s)."""
        return await self.uow.energy.latest_generation(limit=1)

    async def get_generation_history(self, limit: int = 100) -> Sequence[GenerationTimeseries]:
        """Fetch generation history."""
        return await self.uow.energy.generation_history(limit=limit)

    async def get_generation_by_region(
        self, region_id: uuid.UUID, limit: int = 100
    ) -> Sequence[GenerationTimeseries]:
        """Fetch generation filtered by Region."""
        return await self.uow.energy.generation_by_region(region_id, limit)

    async def get_generation_by_state(
        self, state_id: uuid.UUID, limit: int = 100
    ) -> Sequence[GenerationTimeseries]:
        """Fetch generation filtered by State."""
        return await self.uow.energy.generation_by_state(state_id, limit)

    async def get_generation_by_fuel(
        self, fuel_type_id: uuid.UUID
    ) -> Sequence[GenerationTimeseries]:
        """Fetch generation filtered by Fuel Type."""
        return await self.uow.energy.generation_by_fuel(fuel_type_id)

    async def get_generation_summary(self) -> dict:
        """Get aggregate generation summary."""
        total = await self.uow.energy.generation_summary()
        return {"total_generation_mw": total}

    async def get_generation_trends(self) -> dict:
        """Get a placeholder for trends logic."""
        # Future implementation for complex time-series trends
        return {"trend": "increasing", "percentage": 2.5}

    async def get_latest_generation(self, limit: int = 10) -> Sequence[GenerationTimeseries]:
        """Fetch latest N generation records."""
        return await self.uow.energy.latest_generation(limit=limit)
