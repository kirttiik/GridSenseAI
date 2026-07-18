from app.db.enums import SourceSystem
from app.repositories.base.unit_of_work import UnitOfWork
from app.seeders.base import BaseSeeder


class DatasetRegistrySeeder(BaseSeeder):
    @property
    def name(self) -> str:
        return "Dataset Registry Seeder"

    @property
    def priority(self) -> int:
        return 30

    async def execute(self, uow: UnitOfWork) -> None:
        source_systems_db = await uow.reference.source_system.get_all()
        source_system_map = {ss.name: ss.id for ss in source_systems_db}

        datasets = [
            {
                "dataset_name": "GRID_INDIA_DEMAND",
                "display_name": "Grid India Real-Time Demand",
                "description": "Real-time MW demand from Grid India SCADA.",
                "sdk_method": "get_demand",
                "refresh_frequency": "15m",
                "destination_table": "energy.demand_timeseries",
                "source_system_id": source_system_map[SourceSystem.GRID_INDIA],
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "dataset_name": "GRID_INDIA_GENERATION",
                "display_name": "Grid India Real-Time Generation",
                "description": "Real-time MW generation by fuel type from Grid India SCADA.",
                "sdk_method": "get_generation",
                "refresh_frequency": "15m",
                "destination_table": "energy.generation_timeseries",
                "source_system_id": source_system_map[SourceSystem.GRID_INDIA],
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "dataset_name": "IEX_DAM_PRICES",
                "display_name": "IEX Day-Ahead Market Prices",
                "description": "Day Ahead Market clearing prices.",
                "sdk_method": "get_dam_prices",
                "refresh_frequency": "1d",
                "destination_table": "market.iex_dam_pricing",
                "source_system_id": source_system_map.get(
                    "IEX", source_system_map[SourceSystem.MANUAL]
                ),
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "dataset_name": "CEA_MONTHLY_PSP",
                "display_name": "CEA Monthly Power Supply Position",
                "description": "Monthly PSP report data.",
                "sdk_method": "get_monthly_psp",
                "refresh_frequency": "1M",
                "destination_table": "operations.cea_monthly_psp",
                "source_system_id": source_system_map[SourceSystem.CEA],
                "created_by": "system",
                "updated_by": "system",
            },
            {
                "dataset_name": "POSOCO_PSP_DAILY",
                "display_name": "POSOCO Daily PSP",
                "description": "Daily Power Supply Position data.",
                "sdk_method": "get_daily_psp",
                "refresh_frequency": "1d",
                "destination_table": "operations.posoco_psp_daily",
                "source_system_id": source_system_map[SourceSystem.POSOCO],
                "created_by": "system",
                "updated_by": "system",
            },
        ]

        await uow.ingestion.dataset_registry.upsert(
            index_elements=["dataset_name"], values=datasets
        )
