from datetime import datetime

from pydantic import BaseModel, Field

from app.etl.base.base_validator import BaseValidator


class GenerationRecordSchema(BaseModel):
    """Pydantic schema for raw Generation data."""

    timestamp: datetime
    state_abbreviation: str = Field(..., min_length=2, max_length=10)
    fuel_type: str = Field(..., min_length=2)
    generation_mw: float = Field(..., ge=0, description="Generation must be positive")


class GenerationValidator(BaseValidator):
    @property
    def schema(self) -> type[BaseModel]:
        return GenerationRecordSchema
