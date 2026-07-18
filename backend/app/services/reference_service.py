from collections.abc import Sequence

from app.models.reference import EnergySource, FuelType, Region, State
from app.services.base.base_service import BaseService


class ReferenceService(BaseService):
    """
    Business service layer for Reference Data (Geography, Enums).
    """

    async def get_states(self, skip: int = 0, limit: int = 100) -> Sequence[State]:
        """Fetch all states."""
        return await self.uow.reference.states.get_all(skip=skip, limit=limit)

    async def get_state(self, state_id: str) -> State:
        """Fetch a single state by ID."""
        return await self.get_or_404(self.uow.reference.states, state_id)

    async def get_regions(self, skip: int = 0, limit: int = 100) -> Sequence[Region]:
        """Fetch all regions."""
        return await self.uow.reference.regions.get_all(skip=skip, limit=limit)

    async def get_fuel_types(self, skip: int = 0, limit: int = 100) -> Sequence[FuelType]:
        """Fetch all fuel types."""
        return await self.uow.reference.fuel_types.get_all(skip=skip, limit=limit)

    async def get_energy_sources(self, skip: int = 0, limit: int = 100) -> Sequence[EnergySource]:
        """Fetch all energy sources."""
        return await self.uow.reference.energy_sources.get_all(skip=skip, limit=limit)
