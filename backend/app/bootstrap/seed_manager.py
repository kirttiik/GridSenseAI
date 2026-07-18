import logging
import time

from app.db.session import AsyncSessionLocal
from app.repositories.base.unit_of_work import UnitOfWork
from app.seeders.base import BaseSeeder
from app.seeders.development.sample_assets_seeder import SampleAssetsSeeder
from app.seeders.development.sample_energy_seeder import SampleEnergySeeder
from app.seeders.ingestion.dataset_registry_seeder import DatasetRegistrySeeder
from app.seeders.reference.companies_seeder import CompaniesSeeder

# Seeders
from app.seeders.reference.enums_seeder import EnumsSeeder
from app.seeders.reference.geography_seeder import GeographySeeder
from app.seeders.reference.time_dimension_seeder import TimeDimensionSeeder

logger = logging.getLogger(__name__)


class SeedManager:
    """
    Manages the registration, ordering, and execution of database seeders.
    """

    def __init__(self, environment: str = "development"):
        self.environment = environment
        self._seeders: list[BaseSeeder] = []
        self._register_default_seeders()

    def _register_default_seeders(self):
        """Register all defined seeders."""
        self.register(EnumsSeeder())
        self.register(GeographySeeder())
        self.register(CompaniesSeeder())
        self.register(TimeDimensionSeeder())
        self.register(DatasetRegistrySeeder())
        self.register(SampleAssetsSeeder())
        self.register(SampleEnergySeeder())

    def register(self, seeder: BaseSeeder):
        """Register a new seeder."""
        self._seeders.append(seeder)

    async def execute(self, dry_run: bool = False):
        """
        Execute all registered seeders ordered by priority.
        Filters out seeders that shouldn't run in the current environment.
        """
        # Sort seeders by priority
        seeders_to_run = sorted(
            [s for s in self._seeders if self.environment in s.environments],
            key=lambda s: s.priority,
        )

        logger.info(f"Starting database seeding for environment: {self.environment}")
        logger.info(f"Seeders to run: {len(seeders_to_run)}")

        if dry_run:
            logger.info("DRY-RUN MODE ACTIVE: No changes will be committed.")

        overall_start_time = time.time()

        for seeder in seeders_to_run:
            logger.info(f"--> Executing Seeder: {seeder.name} (Priority: {seeder.priority})")
            start_time = time.time()

            async with AsyncSessionLocal() as session:
                async with UnitOfWork(session) as uow:
                    try:
                        await seeder.execute(uow)

                        if not dry_run:
                            await uow.commit()
                            logger.info(
                                f"    [OK] {seeder.name} committed in {time.time() - start_time:.2f}s"
                            )
                        else:
                            await uow.rollback()
                            logger.info(
                                f"    [DRY-RUN] {seeder.name} rolled back in {time.time() - start_time:.2f}s"
                            )

                    except Exception as e:
                        logger.error(f"    [FAILED] {seeder.name} failed: {e}")
                        await uow.rollback()
                        raise

        logger.info(f"Seeding completed successfully in {time.time() - overall_start_time:.2f}s")
