import abc
import logging
from typing import Any

from pydantic import BaseModel, ValidationError

logger = logging.getLogger(__name__)


class BaseValidator(abc.ABC):
    """
    Abstract base class for Validating raw datasets.
    """

    @property
    @abc.abstractmethod
    def schema(self) -> type[BaseModel]:
        """Return the Pydantic schema used for validation."""
        pass

    def validate(
        self, raw_data: list[dict[str, Any]]
    ) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        """
        Validates the incoming raw data against the schema.
        Returns a tuple: (valid_records, invalid_records)
        """
        logger.info(f"Validating {len(raw_data)} records...")
        valid_records = []
        invalid_records = []

        schema_cls = self.schema

        for index, record in enumerate(raw_data):
            try:
                # Use Pydantic to validate and construct the model
                validated = schema_cls(**record)
                # Export back to dict using Pydantic functionality
                valid_records.append(validated.model_dump())
            except ValidationError as e:
                # Format error for logging
                errors = e.errors()
                error_summary = [f"{err['loc'][0]}: {err['msg']}" for err in errors]
                invalid_records.append(
                    {"record_index": index, "record_data": record, "errors": error_summary}
                )

        logger.info(
            f"Validation complete: {len(valid_records)} valid, {len(invalid_records)} invalid."
        )
        return valid_records, invalid_records
