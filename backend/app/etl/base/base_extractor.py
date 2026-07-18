import abc
import logging
import time
from datetime import UTC
from typing import Any

from app.etl.utils import with_retry
from app.models.ingestion.api_request_logs import ApiRequestLog
from app.models.ingestion.api_response_logs import ApiResponseLog
from app.repositories.base.unit_of_work import UnitOfWork

logger = logging.getLogger(__name__)


class BaseExtractor(abc.ABC):
    """
    Abstract base class for all ETL Extractors.
    Handles SDK calls, rate limiting, and API logging.
    """

    def __init__(self, dataset_id: str):
        self.dataset_id = dataset_id

    @abc.abstractmethod
    async def extract_data(self, **kwargs) -> Any:
        """
        Implementation-specific logic to fetch data.
        Should raise RecoverableETLError or FatalETLError on failure.
        """
        pass

    @abc.abstractmethod
    def get_endpoint(self) -> str:
        """Return the API endpoint being called for logging."""
        pass

    @abc.abstractmethod
    def get_http_method(self) -> str:
        """Return the HTTP method being used (GET, POST, etc)."""
        return "GET"

    @with_retry(max_retries=3, base_delay=2)
    async def execute(self, uow: UnitOfWork, **kwargs) -> Any:
        """
        Wrapper to execute extraction and log request/response natively.
        """
        logger.info(f"Extracting data for dataset {self.dataset_id}...")

        # 1. Log API Request
        from datetime import datetime

        req_log = ApiRequestLog(
            dataset_id=self.dataset_id,
            endpoint=self.get_endpoint(),
            http_method=self.get_http_method(),
            request_timestamp=datetime.now(UTC),
        )
        await uow.ingestion.api_request_logs.create(req_log)
        await uow.commit()  # Commit request immediately to get ID

        start_time = time.time()

        try:
            # 2. Extract Data
            raw_data = await self.extract_data(**kwargs)

            # 3. Log API Response (Success)
            exec_time = int((time.time() - start_time) * 1000)
            payload_size = len(str(raw_data).encode("utf-8")) if raw_data else 0

            resp_log = ApiResponseLog(
                request_id=req_log.id,
                http_status=200,
                response_size=payload_size,
                execution_time_ms=exec_time,
                response_metadata={"records": len(raw_data) if isinstance(raw_data, list) else 1},
            )
            await uow.ingestion.api_response_logs.create(resp_log)
            await uow.commit()

            return raw_data

        except Exception as e:
            # Log Failure
            exec_time = int((time.time() - start_time) * 1000)
            resp_log = ApiResponseLog(
                request_id=req_log.id,
                http_status=500,  # Assuming 500 for generic failures if SDK doesn't expose status
                response_size=0,
                execution_time_ms=exec_time,
                response_metadata={"error": str(e)},
            )
            await uow.ingestion.api_response_logs.create(resp_log)
            await uow.commit()
            raise
