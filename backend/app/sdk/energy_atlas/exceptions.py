from typing import Any


class EnergyAtlasError(Exception):
    """Base exception for all Energy Atlas SDK errors."""

    def __init__(self, message: str, request_id: str | None = None):
        super().__init__(message)
        self.request_id = request_id


class AuthenticationError(EnergyAtlasError):
    """Raised when authentication fails (401)."""

    pass


class AuthorizationError(EnergyAtlasError):
    """Raised when authorization fails (403)."""

    pass


class RateLimitError(EnergyAtlasError):
    """Raised when the API rate limit is exceeded (429)."""

    pass


class TimeoutError(EnergyAtlasError):
    """Raised when an API request times out."""

    pass


class EndpointUnavailableError(EnergyAtlasError):
    """Raised when the endpoint is not found (404)."""

    pass


class ValidationError(EnergyAtlasError):
    """Raised when the request payload or params are invalid (400, 422)."""

    pass


class ServerError(EnergyAtlasError):
    """Raised when the API returns a server error (500, 502, 503, 504)."""

    def __init__(self, message: str, status_code: int, request_id: str | None = None):
        super().__init__(message, request_id)
        self.status_code = status_code


class NetworkError(EnergyAtlasError):
    """Raised on connection drops or underlying network failures."""

    pass


class UnexpectedResponseError(EnergyAtlasError):
    """Raised when the API returns an unexpected response or payload format."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        payload: dict[str, Any] | None = None,
        request_id: str | None = None,
    ):
        super().__init__(message, request_id)
        self.status_code = status_code
        self.payload = payload or {}
