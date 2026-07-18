import uuid
from collections.abc import Sequence

from app.models.assets import PowerPlant, Substation, TransmissionLine
from app.services.base.base_service import BaseService


class AssetsService(BaseService):
    """
    Business service layer for Assets Data (Power Plants, Substations, Lines).
    """

    async def get_power_plants(self, skip: int = 0, limit: int = 100) -> Sequence[PowerPlant]:
        """Fetch all power plants."""
        return await self.uow.assets.power_plants.get_all(skip=skip, limit=limit)

    async def get_power_plant(self, plant_id: uuid.UUID) -> PowerPlant:
        """Fetch a single power plant by ID."""
        return await self.get_or_404(self.uow.assets.power_plants, plant_id)

    async def get_plants_by_state(self, state_id: uuid.UUID) -> Sequence[PowerPlant]:
        """Fetch power plants in a given state."""
        return await self.uow.assets.plants_by_state(state_id)

    async def get_plants_by_operator(self, operator_id: uuid.UUID) -> Sequence[PowerPlant]:
        """Fetch power plants operated by a specific operator."""
        return await self.uow.assets.plants_by_operator(operator_id)

    async def get_substations(self, skip: int = 0, limit: int = 100) -> Sequence[Substation]:
        """Fetch all substations."""
        return await self.uow.assets.substations.get_all(skip=skip, limit=limit)

    async def get_transmission_lines(
        self, skip: int = 0, limit: int = 100
    ) -> Sequence[TransmissionLine]:
        """Fetch all transmission lines."""
        return await self.uow.assets.transmission_lines.get_all(skip=skip, limit=limit)
