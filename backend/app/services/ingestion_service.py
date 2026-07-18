from collections.abc import Sequence

from app.models.ingestion import ApiRequestLog, DatasetRegistry
from app.services.base.base_service import BaseService


class IngestionService(BaseService):
    """
    Business service layer for Dataset Registry and ETL API logs.
    """

    async def get_datasets(self, skip: int = 0, limit: int = 100) -> Sequence[DatasetRegistry]:
        """Fetch all registered datasets."""
        return await self.uow.ingestion.dataset_registry.get_all(skip=skip, limit=limit)

    async def get_dataset(self, dataset_id: str) -> DatasetRegistry:
        """Fetch a specific dataset by ID."""
        return await self.get_or_404(self.uow.ingestion.dataset_registry, dataset_id)

    async def get_active_datasets(self) -> Sequence[DatasetRegistry]:
        """Fetch active datasets that need processing."""
        return await self.uow.ingestion.get_active_datasets()

    async def get_latest_refresh(self, dataset_name: str) -> ApiRequestLog | None:
        """Fetch the most recent refresh log for a dataset."""
        return await self.uow.ingestion.latest_refresh(dataset_name)

    async def get_recent_api_requests(self, limit: int = 100) -> Sequence[ApiRequestLog]:
        """Fetch recent API requests across all datasets."""
        return await self.uow.ingestion.api_request_logs.get_all(skip=0, limit=limit)
