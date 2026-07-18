import asyncio
import logging

from sqlalchemy import text

from app.db.engine import engine
from app.db.session import AsyncSessionLocal

logger = logging.getLogger(__name__)

async def check_connection():
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        logger.info("Database connection successful.")
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise

async def init_db():
    logger.info("Initializing database...")
    await check_connection()
    logger.info("Database initialization complete.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(init_db())
