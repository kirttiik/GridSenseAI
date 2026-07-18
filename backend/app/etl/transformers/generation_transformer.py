from typing import Any

from app.db.enums import SourceSystem
from app.etl.base.base_transformer import BaseTransformer
from app.repositories.base.unit_of_work import UnitOfWork


class GenerationTransformer(BaseTransformer):
    async def transform(
        self, uow: UnitOfWork, valid_records: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        # Fetch states and fuel types
        states = await uow.reference.state.get_all()
        fuel_types = await uow.reference.fuel_type.get_all()

        state_map = {s.abbreviation: s.id for s in states}
        fuel_map = {f.name: f.id for f in fuel_types}

        transformed = []
        for record in valid_records:
            state_id = state_map.get(record["state_abbreviation"])
            fuel_type_id = fuel_map.get(record["fuel_type"])

            if not state_id or not fuel_type_id:
                continue

            ts = record["timestamp"]
            date_key = ts.year * 10000 + ts.month * 100 + ts.day

            transformed.append(
                {
                    "timestamp": ts,
                    "state_id": state_id,
                    "date_key": date_key,
                    "fuel_type_id": fuel_type_id,
                    "generation_mw": record["generation_mw"],
                    "source_system": SourceSystem.GRID_INDIA,
                }
            )

        return transformed
