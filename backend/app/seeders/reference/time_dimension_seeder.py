from datetime import date, timedelta

from app.repositories.base.unit_of_work import UnitOfWork
from app.seeders.base import BaseSeeder


class TimeDimensionSeeder(BaseSeeder):
    @property
    def name(self) -> str:
        return "Time Dimension Seeder"

    @property
    def priority(self) -> int:
        return 15

    async def execute(self, uow: UnitOfWork) -> None:
        start_date = date(2024, 1, 1)
        end_date = date(2030, 12, 31)

        delta = end_date - start_date

        values = []
        for i in range(delta.days + 1):
            curr_date = start_date + timedelta(days=i)
            # key format: YYYYMMDD
            date_key = curr_date.year * 10000 + curr_date.month * 100 + curr_date.day
            values.append(
                {
                    "date_key": date_key,
                    "date": curr_date,
                    "year": curr_date.year,
                    "month": curr_date.month,
                    "day": curr_date.day,
                }
            )

        # Bulk upsert
        await uow.reference._session.flush()  # ensure cleanlyness
        await uow.reference.time_dimension.upsert(index_elements=["date_key"], values=values)
