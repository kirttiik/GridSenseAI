class ServiceException(Exception):
    """Base exception for all business service layer errors."""

    pass


class ResourceNotFound(ServiceException):
    """Raised when a requested resource (e.g., ID) cannot be found."""

    def __init__(self, message: str = "Resource not found"):
        super().__init__(message)


class ValidationError(ServiceException):
    """Raised when business validation rules fail."""

    def __init__(self, message: str = "Validation failed"):
        super().__init__(message)


class BusinessRuleViolation(ServiceException):
    """Raised when an operation violates a domain business rule."""

    def __init__(self, message: str = "Business rule violation"):
        super().__init__(message)


class ServiceUnavailable(ServiceException):
    """Raised when a required external or internal service is unavailable."""

    def __init__(self, message: str = "Service unavailable"):
        super().__init__(message)


class ConflictError(ServiceException):
    """Raised when an operation conflicts with existing data (e.g., duplicates)."""

    def __init__(self, message: str = "Resource conflict"):
        super().__init__(message)


class DataNotAvailable(ServiceException):
    """Raised when data requested is not available (e.g., future forecasting)."""

    def __init__(self, message: str = "Data not available"):
        super().__init__(message)
