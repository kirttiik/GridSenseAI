from collections.abc import Sequence

from app.models.operations import CeaMonthlyPsp, EnergyInvestments, PosocoPspDaily
from app.services.base.base_service import BaseService


class OperationsService(BaseService):
    """
    Business service layer for Grid Operations (CEA, POSOCO data).
    """

    async def get_cea_monthly_psp(self, limit: int = 12) -> Sequence[CeaMonthlyPsp]:
        """Fetch CEA monthly power supply position data."""
        return await self.uow.operations.cea_monthly_psp.get_all(skip=0, limit=limit)

    async def get_posoco_daily_psp(self, limit: int = 30) -> Sequence[PosocoPspDaily]:
        """Fetch POSOCO daily power supply position data."""
        return await self.uow.operations.posoco_psp_daily.get_all(skip=0, limit=limit)

    async def get_energy_investments(self, limit: int = 100) -> Sequence[EnergyInvestments]:
        """Fetch energy investments tracking data."""
        return await self.uow.operations.energy_investments.get_all(skip=0, limit=limit)
