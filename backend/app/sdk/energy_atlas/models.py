from datetime import UTC, datetime
from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class ResponseMetadata(BaseModel):
    """Metadata regarding the SDK request and response."""

    endpoint: str = Field(description="The API endpoint called.")
    http_status: int = Field(description="The HTTP status code returned.")
    execution_time_ms: int = Field(description="Time taken to execute the request in milliseconds.")
    authentication_mode: str = Field(
        description="The authentication method used (e.g., Bearer, X-API-Key)."
    )
    response_size_bytes: int | None = Field(
        default=None, description="Size of the response in bytes, if available."
    )
    pagination: dict[str, Any] | None = Field(
        default=None, description="Optional pagination information."
    )
    request_timestamp: str = Field(
        default_factory=lambda: datetime.now(UTC).isoformat(),
        description="When this response was generated.",
    )
    request_id: str | None = Field(
        default=None, description="Unique correlation ID for this request."
    )


class SDKResponse(BaseModel, Generic[T]):
    """
    Standardized, strongly-typed generic response wrapper for all Energy Atlas SDK methods.
    """

    success: bool = Field(description="Whether the API request was successful.")
    data: T = Field(description="The actual data payload from the API.")
    metadata: ResponseMetadata = Field(description="Metadata related to the request and response.")


# Backward compatibility alias
EnergyAtlasResponse = SDKResponse
