import asyncio
import logging
import sys

# Ensure proper path
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app.etl.orchestrator import ETLOrchestrator
# Import pipelines to trigger registration
import app.etl.pipelines.demand_pipeline
import app.etl.pipelines.generation_pipeline

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def main():
    logger.info("Testing ETL Orchestrator...")
    orchestrator = ETLOrchestrator()
    
    # Run the orchestrator for all registered pipelines
    results = await orchestrator.run_all()
    
    logger.info("ETL Test Complete.")
    for dataset, res in results.items():
        logger.info(f"Dataset {dataset} result: {res}")

if __name__ == "__main__":
    asyncio.run(main())
