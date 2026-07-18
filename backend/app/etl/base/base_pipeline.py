import json
import logging
import time
from datetime import UTC, datetime

from app.etl.base.base_extractor import BaseExtractor
from app.etl.base.base_loader import BaseLoader
from app.etl.base.base_transformer import BaseTransformer
from app.etl.base.base_validator import BaseValidator
from app.repositories.base.unit_of_work import UnitOfWork

logger = logging.getLogger(__name__)


class BasePipeline:
    """
    Standard ETL Pipeline orchestrating Extractor -> Validator -> Transformer -> Loader.
    Produces structured RefreshHistory application logs.
    """

    def __init__(
        self,
        dataset_name: str,
        extractor: BaseExtractor,
        validator: BaseValidator,
        transformer: BaseTransformer,
        loader: BaseLoader,
    ):
        self.dataset_name = dataset_name
        self.extractor = extractor
        self.validator = validator
        self.transformer = transformer
        self.loader = loader

    async def execute(self, uow: UnitOfWork, **kwargs) -> dict:
        """
        Execute the pipeline flow.
        """
        logger.info(f"Starting pipeline execution for {self.dataset_name}")
        start_time = time.time()
        start_ts = datetime.now(UTC).isoformat()

        status = "SUCCESS"
        rows_fetched = 0
        rows_validated = 0
        rows_inserted = 0
        rows_rejected = 0
        error_msg = None

        try:
            # 1. Extract
            raw_data = await self.extractor.execute(uow, **kwargs)
            if not isinstance(raw_data, list):
                raw_data = [raw_data]
            rows_fetched = len(raw_data)

            # 2. Validate
            valid_records, invalid_records = self.validator.validate(raw_data)
            rows_validated = len(valid_records)
            rows_rejected = len(invalid_records)

            # Application Logging for Validation Errors (instead of DB table)
            if invalid_records:
                for inv in invalid_records:
                    logger.warning(
                        json.dumps(
                            {
                                "event": "ValidationErrorLog",
                                "dataset_name": self.dataset_name,
                                "timestamp": datetime.now(UTC).isoformat(),
                                "record_index": inv["record_index"],
                                "errors": inv["errors"],
                            }
                        )
                    )

            # 3. Transform
            if valid_records:
                transformed_records = await self.transformer.transform(uow, valid_records)

                # 4. Load
                rows_inserted = await self.loader.load(uow, transformed_records)
                await uow.commit()

        except Exception as e:
            status = "FAILED"
            error_msg = str(e)
            logger.error(f"Pipeline {self.dataset_name} failed: {e}")
            await uow.rollback()
            raise
        finally:
            end_time = time.time()
            end_ts = datetime.now(UTC).isoformat()
            duration_ms = int((end_time - start_time) * 1000)

            # Emitting structured RefreshHistory application log
            refresh_log = {
                "event": "RefreshHistory",
                "dataset_name": self.dataset_name,
                "start_time": start_ts,
                "end_time": end_ts,
                "status": status,
                "rows_fetched": rows_fetched,
                "rows_validated": rows_validated,
                "rows_inserted": rows_inserted,
                "rows_rejected": rows_rejected,
                "execution_duration_ms": duration_ms,
            }
            if error_msg:
                refresh_log["error"] = error_msg

            logger.info(json.dumps(refresh_log))

        return refresh_log
