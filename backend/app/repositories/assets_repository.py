import uuid
from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.assets import PowerPlant, Substation, TransmissionLine

from .base.generic_repository import GenericRepository


class AssetsRepository:
    """Repository for all Asset physical models."""

    def __init__(self, session: AsyncSession):
        self._session = session
        self.power_plants = GenericRepository(session, PowerPlant)
        self.substations = GenericRepository(session, Substation)
        self.transmission_lines = GenericRepository(session, TransmissionLine)

    async def plants_by_state(self, state_id: uuid.UUID) -> Sequence[PowerPlant]:
        stmt = (
            select(PowerPlant)
            .where(PowerPlant.state_id == state_id)
            .options(selectinload(PowerPlant.fuel_type))
        )
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def plants_by_operator(self, operator_id: uuid.UUID) -> Sequence[PowerPlant]:
        stmt = select(PowerPlant).where(PowerPlant.operator_id == operator_id)
        result = await self._session.execute(stmt)
        return result.scalars().all()
