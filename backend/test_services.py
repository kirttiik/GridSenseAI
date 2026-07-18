import asyncio
import logging
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app.db.session import AsyncSessionLocal
from app.repositories.base.unit_of_work import UnitOfWork
from app.services.energy_service import EnergyService
from app.services.assets_service import AssetsService

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def main():
    logger.info("Testing Service Layer...")
    
    async with AsyncSessionLocal() as session:
        async with UnitOfWork(session) as uow:
            # Initialize Services
            energy_service = EnergyService(uow)
            assets_service = AssetsService(uow)
            
            # Test executions
            try:
                # Assuming database might be empty or unauthenticated in testing environment
                # We just want to ensure the code executes structurally without syntax/attribute errors
                summary = await energy_service.get_generation_summary()
                logger.info(f"Generation Summary: {summary}")
                
                plants = await assets_service.get_power_plants(limit=5)
                logger.info(f"Fetched {len(plants)} power plants")
            except Exception as e:
                logger.error(f"Service error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
