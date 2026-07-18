from app.repositories.base.unit_of_work import UnitOfWork
from app.seeders.base import BaseSeeder


class CompaniesSeeder(BaseSeeder):
    @property
    def name(self) -> str:
        return "Companies Seeder"

    @property
    def priority(self) -> int:
        return 20

    async def execute(self, uow: UnitOfWork) -> None:
        operators = [
            {"name": "NTPC Limited", "created_by": "system", "updated_by": "system"},
            {"name": "NHPC Limited", "created_by": "system", "updated_by": "system"},
            {"name": "Adani Power", "created_by": "system", "updated_by": "system"},
            {"name": "Tata Power", "created_by": "system", "updated_by": "system"},
            {"name": "JSW Energy", "created_by": "system", "updated_by": "system"},
            {"name": "Torrent Power", "created_by": "system", "updated_by": "system"},
        ]
        await uow.reference.operator.upsert(index_elements=["name"], values=operators)

        transmission_owners = [
            {
                "name": "Power Grid Corporation of India",
                "created_by": "system",
                "updated_by": "system",
            },
            {"name": "Adani Transmission", "created_by": "system", "updated_by": "system"},
            {"name": "Sterlite Power", "created_by": "system", "updated_by": "system"},
        ]
        await uow.reference.transmission_owner.upsert(
            index_elements=["name"], values=transmission_owners
        )

        discoms = [
            {"name": "BSES Rajdhani", "created_by": "system", "updated_by": "system"},
            {"name": "BSES Yamuna", "created_by": "system", "updated_by": "system"},
            {"name": "Tata Power DDL", "created_by": "system", "updated_by": "system"},
            {"name": "BESCOM", "created_by": "system", "updated_by": "system"},
            {"name": "TANGEDCO", "created_by": "system", "updated_by": "system"},
            {"name": "MSEDCL", "created_by": "system", "updated_by": "system"},
        ]
        await uow.reference.distribution_company.upsert(index_elements=["name"], values=discoms)
