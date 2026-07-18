class GridSenseException(Exception):
    """Base exception class for all custom GridSense AI errors."""

    def __init__(self, message: str, status_code: int = 500, code: str = "INTERNAL_ERROR"):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.code = code


class DatabaseError(GridSenseException):
    """Raised when a database operation fails."""

    def __init__(self, message: str):
        super().__init__(message, status_code=500, code="DATABASE_ERROR")


class ValidationError(GridSenseException):
    """Raised when data validation fails before reaching Pydantic/DB constraints."""

    def __init__(self, message: str):
        super().__init__(message, status_code=422, code="VALIDATION_ERROR")


class SDKError(GridSenseException):
    """Raised when the Energy Atlas SDK encounters an upstream failure."""

    def __init__(self, message: str):
        super().__init__(message, status_code=502, code="SDK_ERROR")


class ConfigurationError(GridSenseException):
    """Raised when environment variables or configurations are missing/invalid."""

    def __init__(self, message: str):
        super().__init__(message, status_code=500, code="CONFIGURATION_ERROR")


class RepositoryError(GridSenseException):
    """Raised when a repository layer operation fails (e.g., entity not found)."""

    def __init__(self, message: str):
        super().__init__(message, status_code=400, code="REPOSITORY_ERROR")


class IngestionError(GridSenseException):
    """Raised when an ETL ingestion pipeline fails."""

    def __init__(self, message: str):
        super().__init__(message, status_code=500, code="INGESTION_ERROR")


class BusinessRuleError(GridSenseException):
    """Raised when a domain business rule is violated."""

    def __init__(self, message: str):
        super().__init__(message, status_code=409, code="BUSINESS_RULE_ERROR")


class APIError(GridSenseException):
    """Raised for general HTTP API errors."""

    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message, status_code=status_code, code="API_ERROR")
