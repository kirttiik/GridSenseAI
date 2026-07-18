import random
from datetime import UTC, datetime, timedelta

from app.db.enums import SourceSystem
from app.models.energy.demand_timeseries import DemandTimeseries
from app.repositories.base.unit_of_work import UnitOfWork
from app.seeders.base import BaseSeeder


class SampleEnergySeeder(BaseSeeder):
    @property
    def name(self) -> str:
        return "Sample Energy Seeder"

    @property
    def priority(self) -> int:
        return 50

    @property
    def environments(self) -> list[str]:
        return ["development"]

    async def execute(self, uow: UnitOfWork) -> None:
        count = await uow.energy.demand.count()
        if count > 0:
            return

        states = await uow.reference.state.get_all()
        state_map = {s.name: s.id for s in states}

        target_states = ["Delhi", "Maharashtra", "Gujarat"]

        start_time = datetime(2024, 1, 1, tzinfo=UTC)

        records = []
        for state_name in target_states:
            state_id = state_map.get(state_name)
            if not state_id:
                continue

            base_demand = 5000 if state_name == "Delhi" else 15000

            for i in range(24 * 7):  # 1 week of hourly data
                current_time = start_time + timedelta(hours=i)
                date_key = current_time.year * 10000 + current_time.month * 100 + current_time.day

                # synthetic variation
                demand_val = base_demand + random.uniform(-1000, 2000)

                records.append(
                    DemandTimeseries(
                        timestamp=current_time,
                        state_id=state_id,
                        date_key=date_key,
                        demand_mw=round(demand_val, 2),
                        source_system=SourceSystem.GRID_INDIA,
                        created_by="system",
                        updated_by="system",
                    )
                )

        if records:
            await uow.energy.demand.bulk_create(records)
