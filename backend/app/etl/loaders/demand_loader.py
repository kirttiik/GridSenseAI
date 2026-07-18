from typing import Any

from app.etl.base.base_loader import BaseLoader
from app.repositories.base.unit_of_work import UnitOfWork


class DemandLoader(BaseLoader):
    @property
    def index_elements(self) -> list[str]:
        return ["timestamp", "state_id"]  # The unique constraint in demand_timeseries

    async def load(self, uow: UnitOfWork, records: list[dict[str, Any]]) -> int:
        await uow.energy.demand.upsert(index_elements=self.index_elements, values=records)
        return len(records)
