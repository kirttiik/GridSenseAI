import asyncio
import logging

from sqlalchemy import text
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core.config import get_settings
from app.models.role import Role
from app.models.state import State

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

settings = get_settings()

engine = create_async_engine(settings.database_url)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def seed_roles(session):
    """Seed default roles."""
    roles = [
        {"name": "Admin"},
        {"name": "Analyst"},
        {"name": "Viewer"},
    ]

    logger.info("Seeding roles...")
    for role_data in roles:
        stmt = insert(Role).values(**role_data)
        # Use ON CONFLICT DO NOTHING to ensure idempotency
        stmt = stmt.on_conflict_do_nothing(index_elements=["name"])
        await session.execute(stmt)
    await session.commit()
    logger.info("Roles seeded successfully.")


async def seed_states(session):
    """Seed sample Indian states with MultiPolygon geometries."""

    # We use well-known text (WKT) for the MULTIPOLYGON geometries
    # These are very rough approximate bounding boxes for demonstration.
    # In production, accurate shapefiles should be loaded via ST_GeomFromGeoJSON or similar.
    states = [
        {
            "name": "Gujarat",
            "state_code": "GJ",
            "region": "Western",
            "geom": "SRID=4326;MULTIPOLYGON(((68.0 20.0, 74.0 20.0, 74.0 24.0, 68.0 24.0, 68.0 20.0)))",
        },
        {
            "name": "Maharashtra",
            "state_code": "MH",
            "region": "Western",
            "geom": "SRID=4326;MULTIPOLYGON(((72.0 15.0, 80.0 15.0, 80.0 22.0, 72.0 22.0, 72.0 15.0)))",
        },
    ]

    logger.info("Seeding states...")
    for state_data in states:
        stmt = insert(State).values(**state_data)
        stmt = stmt.on_conflict_do_nothing(index_elements=["state_code"])
        await session.execute(stmt)
    await session.commit()
    logger.info("States seeded successfully.")


async def main():
    """Run database seeder."""
    logger.info("Starting database seeder...")

    # Ensure PostGIS extension is created (requires superuser,
    # but the docker container initializes it or we can try)
    try:
        async with engine.begin() as conn:
            await conn.execute(text("CREATE EXTENSION IF NOT EXISTS postgis;"))
    except Exception as e:
        logger.warning(f"Could not ensure PostGIS extension: {e}")

    async with AsyncSessionLocal() as session:
        await seed_roles(session)
        await seed_states(session)

    logger.info("Database seeding complete!")


if __name__ == "__main__":
    asyncio.run(main())
