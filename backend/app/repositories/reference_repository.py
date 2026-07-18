from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.reference import EnergySource, FuelType, Region, State

from .base.generic_repository import GenericRepository


class ReferenceRepository:
    """Repository for all Reference dimensions."""

    def __init__(self, session: AsyncSession):
        self._session = session
        self.states = GenericRepository(session, State)
        self.regions = GenericRepository(session, Region)
        self.fuel_types = GenericRepository(session, FuelType)
        self.energy_sources = GenericRepository(session, EnergySource)

    async def get_state_by_abbreviation(self, abbreviation: str) -> State | None:
        stmt = select(State).where(State.abbreviation == abbreviation.upper())
        result = await self._session.execute(stmt)
        return result.scalars().first()

    async def get_fuel_type_by_name(self, name: str) -> FuelType | None:
        stmt = select(FuelType).where(FuelType.name == name)
        result = await self._session.execute(stmt)
        return result.scalars().first()
