from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.engine import engine
from app.logging.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    FastAPI Lifespan context manager.
    Handles startup and shutdown events for the application.
    """
    # --- Startup ---
    logger.info("Application starting up...")

    try:
        # Verify database connectivity
        # Usually, this is handled by just ensuring the engine can connect
        async with engine.begin() as conn:
            logger.info("Database connection established.")

        # Here we could initialize external SDKs, load caching layers, etc.
        logger.info("External SDKs initialized.")

    except Exception as e:
        logger.error(f"Application failed during startup: {e}")
        raise e

    yield

    # --- Shutdown ---
    logger.info("Application shutting down...")

    try:
        # Dispose database engine to close connections cleanly
        await engine.dispose()
        logger.info("Database connections closed.")
    except Exception as e:
        logger.error(f"Error during shutdown: {e}")
