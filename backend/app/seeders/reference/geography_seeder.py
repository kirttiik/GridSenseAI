from app.repositories.base.unit_of_work import UnitOfWork
from app.seeders.base import BaseSeeder


class GeographySeeder(BaseSeeder):
    @property
    def name(self) -> str:
        return "Geography Seeder"

    @property
    def priority(self) -> int:
        return 10

    async def execute(self, uow: UnitOfWork) -> None:
        # Regions
        regions = [
            {"name": "Northern", "created_by": "system", "updated_by": "system"},
            {"name": "Western", "created_by": "system", "updated_by": "system"},
            {"name": "Southern", "created_by": "system", "updated_by": "system"},
            {"name": "Eastern", "created_by": "system", "updated_by": "system"},
            {"name": "North-Eastern", "created_by": "system", "updated_by": "system"},
        ]
        await uow.reference.region.upsert(index_elements=["name"], values=regions)

        # Grid Zones
        grid_zones = [
            {"name": "N1", "created_by": "system", "updated_by": "system"},
            {"name": "N2", "created_by": "system", "updated_by": "system"},
            {"name": "N3", "created_by": "system", "updated_by": "system"},
            {"name": "W1", "created_by": "system", "updated_by": "system"},
            {"name": "W2", "created_by": "system", "updated_by": "system"},
            {"name": "S1", "created_by": "system", "updated_by": "system"},
            {"name": "S2", "created_by": "system", "updated_by": "system"},
            {"name": "E1", "created_by": "system", "updated_by": "system"},
            {"name": "E2", "created_by": "system", "updated_by": "system"},
        ]
        await uow.reference.grid_zone.upsert(index_elements=["name"], values=grid_zones)

        # We need Region IDs to seed States
        db_regions = await uow.reference.region.get_all()
        region_map = {r.name: r.id for r in db_regions}

        states = [
            # Northern
            {
                "name": "Delhi",
                "abbreviation": "DL",
                "region_id": region_map["Northern"],
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Haryana",
                "abbreviation": "HR",
                "region_id": region_map["Northern"],
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Punjab",
                "abbreviation": "PB",
                "region_id": region_map["Northern"],
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Rajasthan",
                "abbreviation": "RJ",
                "region_id": region_map["Northern"],
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Uttar Pradesh",
                "abbreviation": "UP",
                "region_id": region_map["Northern"],
                "created_by": "system",
                "updated_by": "system",
            },
            # Western
            {
                "name": "Gujarat",
                "abbreviation": "GJ",
                "region_id": region_map["Western"],
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Maharashtra",
                "abbreviation": "MH",
                "region_id": region_map["Western"],
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Madhya Pradesh",
                "abbreviation": "MP",
                "region_id": region_map["Western"],
                "created_by": "system",
                "updated_by": "system",
            },
            # Southern
            {
                "name": "Karnataka",
                "abbreviation": "KA",
                "region_id": region_map["Southern"],
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Kerala",
                "abbreviation": "KL",
                "region_id": region_map["Southern"],
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Tamil Nadu",
                "abbreviation": "TN",
                "region_id": region_map["Southern"],
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Telangana",
                "abbreviation": "TG",
                "region_id": region_map["Southern"],
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Andhra Pradesh",
                "abbreviation": "AP",
                "region_id": region_map["Southern"],
                "created_by": "system",
                "updated_by": "system",
            },
            # Eastern
            {
                "name": "Bihar",
                "abbreviation": "BR",
                "region_id": region_map["Eastern"],
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Odisha",
                "abbreviation": "OR",
                "region_id": region_map["Eastern"],
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "West Bengal",
                "abbreviation": "WB",
                "region_id": region_map["Eastern"],
                "created_by": "system",
                "updated_by": "system",
            },
        ]

        await uow.reference.state.upsert(index_elements=["name"], values=states)
