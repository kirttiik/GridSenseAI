from typing import Any

from app.db.enums import SourceSystem
from app.etl.base.base_transformer import BaseTransformer
from app.repositories.base.unit_of_work import UnitOfWork


class DemandTransformer(BaseTransformer):
    async def transform(
        self, uow: UnitOfWork, valid_records: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        # Fetch states to resolve state_id
        states = await uow.reference.state.get_all()
        state_map = {s.abbreviation: s.id for s in states}

        transformed = []
        for record in valid_records:
            # Resolve State
            state_id = state_map.get(record["state_abbreviation"])
            if not state_id:
                # Skip or handle missing reference data (could log a fatal error or just skip)
                continue

            ts = record["timestamp"]
            date_key = ts.year * 10000 + ts.month * 100 + ts.day

            transformed.append(
                {
                    "timestamp": ts,
                    "state_id": state_id,
                    "date_key": date_key,
                    "demand_mw": record["demand_mw"],
                    "source_system": SourceSystem.GRID_INDIA,
                }
            )

        return transformed
