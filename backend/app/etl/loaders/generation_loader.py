from typing import Any

from app.etl.base.base_loader import BaseLoader
from app.repositories.base.unit_of_work import UnitOfWork


class GenerationLoader(BaseLoader):
    @property
    def index_elements(self) -> list[str]:
        return ["timestamp", "state_id", "fuel_type_id"]  # Unique constraint

    async def load(self, uow: UnitOfWork, records: list[dict[str, Any]]) -> int:
        await uow.energy.generation.upsert(index_elements=self.index_elements, values=records)
        return len(records)
