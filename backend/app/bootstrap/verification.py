import logging

from sqlalchemy import text

from app.db.session import AsyncSessionLocal
from app.repositories.base.unit_of_work import UnitOfWork

logger = logging.getLogger(__name__)


async def verify_database():
    """
    Verify the database structure and reference data.
    """
    logger.info("Starting Database Verification...")

    schemas_to_check = [
        "reference",
        "assets",
        "energy",
        "grid",
        "market",
        "operations",
        "ingestion",
        "ml",
    ]

    async with AsyncSessionLocal() as session:
        # Check Schemas
        for schema in schemas_to_check:
            result = await session.execute(
                text("SELECT schema_name FROM information_schema.schemata WHERE schema_name = :s"),
                {"s": schema},
            )
            if not result.scalar():
                logger.error(f"Schema missing: {schema}")
            else:
                logger.info(f"Schema verified: {schema}")

        # Check reference data counts
        async with UnitOfWork(session) as uow:
            counts = {
                "Fuel Types": await uow.reference._session.execute(
                    text("SELECT COUNT(*) FROM reference.fuel_types")
                ),
                "Market Types": await uow.reference._session.execute(
                    text("SELECT COUNT(*) FROM reference.market_types")
                ),
                "Regions": await uow.reference._session.execute(
                    text("SELECT COUNT(*) FROM reference.regions")
                ),
                "States": await uow.reference._session.execute(
                    text("SELECT COUNT(*) FROM reference.states")
                ),
                "Source Systems": await uow.reference._session.execute(
                    text("SELECT COUNT(*) FROM reference.source_systems")
                ),
                "Time Dimensions": await uow.reference._session.execute(
                    text("SELECT COUNT(*) FROM reference.time_dimensions")
                ),
                "Datasets": await uow.ingestion._session.execute(
                    text("SELECT COUNT(*) FROM ingestion.dataset_registry")
                ),
            }

            for entity, result in counts.items():
                count = result.scalar()
                if count == 0:
                    logger.warning(
                        f"No {entity} found in database. Seed may have failed or not run."
                    )
                else:
                    logger.info(f"Verified {entity}: {count} records loaded.")

    logger.info("Database Verification Complete.")
