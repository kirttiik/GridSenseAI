import logging

from alembic.config import Config

from alembic import command
from app.bootstrap.seed_manager import SeedManager

logger = logging.getLogger(__name__)


def get_alembic_config() -> Config:
    alembic_cfg = Config("alembic.ini")
    return alembic_cfg


def run_migrations():
    """Run Alembic upgrades to head."""
    logger.info("Running database migrations...")
    try:
        command.upgrade(get_alembic_config(), "head")
        logger.info("Database migrations completed successfully.")
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


def reset_migrations():
    """Run Alembic downgrades to base."""
    logger.info("Resetting database migrations to base...")
    try:
        command.downgrade(get_alembic_config(), "base")
        logger.info("Database reset completed successfully.")
    except Exception as e:
        logger.error(f"Database reset failed: {e}")
        raise


async def initialize_database(environment: str = "development", dry_run: bool = False):
    """
    Complete initialization flow:
    1. Run Migrations
    2. Seed Database
    """
    logger.info("Starting Database Initialization...")
    run_migrations()

    manager = SeedManager(environment=environment)
    await manager.execute(dry_run=dry_run)
    logger.info("Database Initialization Complete.")


async def rebuild_database(environment: str = "development"):
    """
    Complete rebuild flow:
    1. Reset Migrations
    2. Run Migrations
    3. Seed Database
    """
    logger.info("Starting Database Rebuild...")
    reset_migrations()
    await initialize_database(environment=environment)
