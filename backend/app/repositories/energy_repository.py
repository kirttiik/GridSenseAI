from sqlalchemy.ext.asyncio import AsyncSession

from app.models.energy.energy_data import EnergyData
from .base.generic_repository import GenericRepository


class EnergyRepository(GenericRepository[EnergyData]):
    """Repository for MVP EnergyData model."""
    def __init__(self, session: AsyncSession):
        super().__init__(session, EnergyData)
