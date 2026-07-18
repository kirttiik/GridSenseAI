from app.db.enums import FuelCategory, MarketType, OwnershipType, PlantStatus, SourceSystem
from app.repositories.base.unit_of_work import UnitOfWork
from app.seeders.base import BaseSeeder


class EnumsSeeder(BaseSeeder):
    @property
    def name(self) -> str:
        return "Reference Enums Seeder"

    @property
    def priority(self) -> int:
        return 5

    async def execute(self, uow: UnitOfWork) -> None:
        # Source Systems
        source_systems = [
            {"name": SourceSystem.ENERGY_ATLAS, "created_by": "system", "updated_by": "system"},
            {"name": SourceSystem.GRID_INDIA, "created_by": "system", "updated_by": "system"},
            {"name": SourceSystem.CEA, "created_by": "system", "updated_by": "system"},
            {"name": SourceSystem.POSOCO, "created_by": "system", "updated_by": "system"},
            {"name": SourceSystem.MANUAL, "created_by": "system", "updated_by": "system"},
            {"name": SourceSystem.FORECAST, "created_by": "system", "updated_by": "system"},
        ]
        await uow.reference._session.flush()  # ensure cleanlyness
        await uow.reference.source_system.upsert(index_elements=["name"], values=source_systems)

        # Fuel Types
        fuel_types = [
            {
                "name": "Coal",
                "category": FuelCategory.THERMAL,
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Lignite",
                "category": FuelCategory.THERMAL,
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Gas",
                "category": FuelCategory.THERMAL,
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Diesel",
                "category": FuelCategory.THERMAL,
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Nuclear",
                "category": FuelCategory.NUCLEAR,
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Hydro",
                "category": FuelCategory.HYDRO,
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Solar",
                "category": FuelCategory.RENEWABLE,
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Wind",
                "category": FuelCategory.RENEWABLE,
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "name": "Biomass",
                "category": FuelCategory.RENEWABLE,
                "created_by": "system",
                "updated_by": "system",
            },
        ]
        await uow.reference.fuel_type.upsert(index_elements=["name"], values=fuel_types)

        # Market Types
        market_types = [
            {"name": MarketType.DAM, "created_by": "system", "updated_by": "system"},
            {"name": MarketType.RTM, "created_by": "system", "updated_by": "system"},
            {"name": MarketType.GDAM, "created_by": "system", "updated_by": "system"},
        ]
        await uow.reference.market_type.upsert(index_elements=["name"], values=market_types)

        # Ownership Types
        ownership_types = [
            {"name": OwnershipType.CENTRAL, "created_by": "system", "updated_by": "system"},
            {"name": OwnershipType.STATE, "created_by": "system", "updated_by": "system"},
            {"name": OwnershipType.PRIVATE, "created_by": "system", "updated_by": "system"},
        ]
        await uow.reference.ownership_type.upsert(index_elements=["name"], values=ownership_types)

        # Plant Statuses
        plant_statuses = [
            {"name": PlantStatus.ACTIVE, "created_by": "system", "updated_by": "system"},
            {"name": PlantStatus.DECOMMISSIONED, "created_by": "system", "updated_by": "system"},
            {"name": PlantStatus.MAINTENANCE, "created_by": "system", "updated_by": "system"},
            {"name": PlantStatus.PLANNED, "created_by": "system", "updated_by": "system"},
        ]
        await uow.reference.plant_status.upsert(index_elements=["name"], values=plant_statuses)

        # Energy Sources (General categories)
        energy_sources = [
            {"name": "Thermal", "created_by": "system", "updated_by": "system"},
            {"name": "Renewable", "created_by": "system", "updated_by": "system"},
            {"name": "Nuclear", "created_by": "system", "updated_by": "system"},
            {"name": "Hydro", "created_by": "system", "updated_by": "system"},
        ]
        await uow.reference.energy_source.upsert(index_elements=["name"], values=energy_sources)

        # Voltage Levels
        voltage_levels = [
            {"level_kv": 765.0, "created_by": "system", "updated_by": "system"},
            {"level_kv": 400.0, "created_by": "system", "updated_by": "system"},
            {"level_kv": 220.0, "created_by": "system", "updated_by": "system"},
            {"level_kv": 132.0, "created_by": "system", "updated_by": "system"},
            {"level_kv": 66.0, "created_by": "system", "updated_by": "system"},
        ]
        await uow.reference.voltage_level.upsert(index_elements=["level_kv"], values=voltage_levels)
