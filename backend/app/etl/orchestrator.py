import asyncio
import logging
from typing import Any

from app.db.session import AsyncSessionLocal
from app.etl.registry import PipelineRegistry
from app.repositories.base.unit_of_work import UnitOfWork

logger = logging.getLogger(__name__)


class ETLOrchestrator:
    """
    Orchestrates the execution of ETL pipelines.
    Supports running a single pipeline or running multiple concurrently.
    """

    async def run_pipeline(self, dataset_name: str, **kwargs) -> dict[str, Any]:
        """Run a single ETL pipeline by dataset name."""
        pipeline_class = PipelineRegistry.get_pipeline(dataset_name)

        # Instantiate pipeline (dependencies should be injected or handled by the pipeline init itself)
        pipeline = pipeline_class()

        async with AsyncSessionLocal() as session:
            async with UnitOfWork(session) as uow:
                result = await pipeline.execute(uow, **kwargs)
                return result

    async def run_all(
        self, datasets: list[str] = None, concurrency: int = 3, **kwargs
    ) -> dict[str, Any]:
        """
        Run multiple pipelines in parallel with a concurrency limit.
        If datasets is None, runs all registered datasets.
        """
        if not datasets:
            datasets = PipelineRegistry.list_datasets()

        logger.info(f"Orchestrating {len(datasets)} pipelines with concurrency {concurrency}...")

        semaphore = asyncio.Semaphore(concurrency)
        results = {}

        async def _run_with_semaphore(dataset: str):
            async with semaphore:
                try:
                    res = await self.run_pipeline(dataset, **kwargs)
                    results[dataset] = res
                except Exception as e:
                    logger.error(f"Orchestration of {dataset} failed: {e}")
                    results[dataset] = {"status": "FAILED", "error": str(e)}

        tasks = [_run_with_semaphore(ds) for ds in datasets]
        await asyncio.gather(*tasks)

        return results
