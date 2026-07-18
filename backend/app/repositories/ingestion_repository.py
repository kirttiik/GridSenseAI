from collections.abc import Sequence

from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.ingestion import ApiRequestLog, ApiResponseLog, DatasetRegistry

from .base.generic_repository import GenericRepository


class IngestionRepository:
    """Repository for Ingestion orchestration and logging models."""

    def __init__(self, session: AsyncSession):
        self._session = session
        self.dataset_registry = GenericRepository(session, DatasetRegistry)
        self.api_request_logs = GenericRepository(session, ApiRequestLog)
        self.api_response_logs = GenericRepository(session, ApiResponseLog)

    async def get_active_datasets(self) -> Sequence[DatasetRegistry]:
        """Fetch all datasets that are configured to be ingested."""
        # Future: Filter by an 'is_active' or similar flag if added to DatasetRegistry
        stmt = select(DatasetRegistry)
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def latest_refresh(self, dataset_name: str) -> ApiRequestLog | None:
        """Get the most recent API request log for a dataset."""
        stmt = (
            select(ApiRequestLog)
            .join(DatasetRegistry)
            .where(DatasetRegistry.dataset_name == dataset_name)
            .order_by(desc(ApiRequestLog.request_timestamp))
        )
        result = await self._session.execute(stmt)
        return result.scalars().first()
