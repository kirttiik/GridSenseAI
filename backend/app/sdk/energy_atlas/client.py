import asyncio
import logging
import time
import uuid
from typing import Any

import httpx

from app.sdk.energy_atlas.auth import EnergyAtlasAuth
from app.sdk.energy_atlas.config import config
from app.sdk.energy_atlas.exceptions import (
    AuthenticationError,
    EnergyAtlasError,
    RateLimitError,
    ServerError,
    TimeoutError,
    UnexpectedResponseError,
)
from app.sdk.energy_atlas.models import ResponseMetadata, SDKResponse
from app.sdk.energy_atlas.utils import extract_pagination_metadata

logger = logging.getLogger(__name__)


class BaseClient:
    """Core HTTP client for the Energy Atlas SDK handling retries, timeouts, and structured logging."""

    def __init__(self, client: httpx.AsyncClient | None = None):
        if client is None:
            # Create a reusable client session
            self.client = httpx.AsyncClient(
                base_url=config.base_url,
                timeout=httpx.Timeout(
                    config.timeout, connect=config.connect_timeout, read=config.read_timeout
                ),
                auth=EnergyAtlasAuth(config.api_key),
            )
            self._owns_client = True
        else:
            self.client = client
            self._owns_client = False

    async def close(self):
        if self._owns_client:
            await self.client.aclose()

    async def _request(
        self, method: str, path: str, params: dict[str, Any] | None = None
    ) -> SDKResponse[Any]:
        """
        Execute an HTTP request with advanced features:
        - Request ID correlation
        - Detailed execution time tracking
        - Configurable exponential backoff & Retry-After header parsing
        - Standardized metadata extraction
        """
        request_id = str(uuid.uuid4())
        max_retries = config.max_retries

        # Determine authentication mode for logging
        auth_mode = "X-API-Key" if "/developer/v1/" in path.lower() else "Bearer"

        for attempt in range(max_retries):
            start_time = time.perf_counter()
            response_size = 0

            try:
                response = await self.client.request(method, path, params=params)

                execution_time_ms = int((time.perf_counter() - start_time) * 1000)
                response_size = len(response.content) if hasattr(response, "content") else 0

                # Structured Logging
                logger.info(
                    f"{method} {path} | {response.status_code} {response.reason_phrase} | "
                    f"{execution_time_ms} ms | Retry={attempt} | Auth={auth_mode} | RequestID={request_id}"
                )

                # Handle rate limiting
                if response.status_code == 429:
                    retry_after = response.headers.get("Retry-After")
                    if retry_after and retry_after.isdigit():
                        wait_seconds = float(retry_after)
                        logger.warning(
                            f"Rate limited on {path}. Retry-After specifies {wait_seconds}s wait."
                        )
                    else:
                        wait_seconds = min(config.backoff_factor * (2**attempt), config.max_backoff)
                        logger.warning(
                            f"Rate limited on {path}. No Retry-After header, applying backoff of {wait_seconds}s."
                        )

                    if attempt < max_retries - 1:
                        await asyncio.sleep(wait_seconds)
                        continue
                    else:
                        raise RateLimitError(
                            "Rate limit exceeded for Energy Atlas API.", request_id=request_id
                        )

                # Check for authentication errors
                if response.status_code in (401, 403):
                    raise AuthenticationError(
                        f"Authentication failed: {response.status_code}", request_id=request_id
                    )

                # For 5xx errors, retry
                if response.status_code >= 500:
                    if attempt < max_retries - 1:
                        wait_seconds = min(config.backoff_factor * (2**attempt), config.max_backoff)
                        logger.warning(
                            f"Server error {response.status_code} on {path}. Retrying in {wait_seconds}s..."
                        )
                        await asyncio.sleep(wait_seconds)
                        continue
                    else:
                        raise ServerError(
                            f"Server error {response.status_code}",
                            status_code=response.status_code,
                            request_id=request_id,
                        )

                # Raise for any other 4xx errors (don't retry)
                if 400 <= response.status_code < 500:
                    try:
                        payload = response.json()
                    except Exception:
                        payload = {"raw_text": response.text}
                    raise UnexpectedResponseError(
                        f"Client error {response.status_code} for path {path}",
                        status_code=response.status_code,
                        payload=payload,
                        request_id=request_id,
                    )

                try:
                    data = response.json()
                except ValueError:
                    raise UnexpectedResponseError(
                        "Failed to parse JSON response.",
                        status_code=response.status_code,
                        payload={"raw_text": response.text},
                        request_id=request_id,
                    )

                # Construct ResponseMetadata
                metadata = ResponseMetadata(
                    endpoint=path,
                    http_status=response.status_code,
                    execution_time_ms=execution_time_ms,
                    authentication_mode=auth_mode,
                    response_size_bytes=response_size,
                    pagination=extract_pagination_metadata(data),
                    request_id=request_id,
                )

                # Standardize the payload output by extracting "items" array if present
                actual_data = data.get("items", data) if isinstance(data, dict) else data

                return SDKResponse(success=True, data=actual_data, metadata=metadata)

            except (httpx.TimeoutException, httpx.ConnectError) as e:
                execution_time_ms = int((time.perf_counter() - start_time) * 1000)
                logger.warning(
                    f"Network/Timeout error on {path} | {execution_time_ms} ms | Retry={attempt} | RequestID={request_id}"
                )

                if attempt == max_retries - 1:
                    raise TimeoutError(
                        f"Request to {path} timed out after {max_retries} attempts.",
                        request_id=request_id,
                    ) from e

                wait_seconds = min(config.backoff_factor * (2**attempt), config.max_backoff)
                logger.info(f"Retrying in {wait_seconds} seconds...")
                await asyncio.sleep(wait_seconds)

            except EnergyAtlasError:
                # Re-raise known exceptions without further wrapping
                raise

        raise EnergyAtlasError("Max retries exceeded.", request_id=request_id)

    async def get(self, path: str, params: dict[str, Any] | None = None) -> SDKResponse[Any]:
        return await self._request("GET", path, params=params)
