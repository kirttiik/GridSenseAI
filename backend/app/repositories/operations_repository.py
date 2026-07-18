import uuid

from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.operations import CeaMonthlyPsp, EnergyInvestments, PosocoPspDaily

from .base.generic_repository import GenericRepository


class OperationsRepository:
    """Repository for all Operations and Administrative models."""

    def __init__(self, session: AsyncSession):
        self._session = session
        self.posoco_psp_daily = GenericRepository(session, PosocoPspDaily)
        self.cea_monthly_psp = GenericRepository(session, CeaMonthlyPsp)
        self.energy_investments = GenericRepository(session, EnergyInvestments)

    async def latest_posoco_psp(self, state_id: uuid.UUID) -> PosocoPspDaily | None:
        stmt = (
            select(PosocoPspDaily)
            .where(PosocoPspDaily.state_id == state_id)
            .order_by(desc(PosocoPspDaily.timestamp))
        )
        result = await self._session.execute(stmt)
        return result.scalars().first()
