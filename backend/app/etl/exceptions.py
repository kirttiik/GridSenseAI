class ETLError(Exception):
    """Base exception for all ETL errors."""

    pass


class FatalETLError(ETLError):
    """
    Exception raised when a pipeline encounters an unrecoverable error.
    e.g., Schema mismatch, missing configuration, validation failure on critical fields.
    """

    pass


class RecoverableETLError(ETLError):
    """
    Exception raised for temporary issues like network timeouts.
    Can be retried.
    """

    pass


class RateLimitError(RecoverableETLError):
    """
    Exception raised specifically for API rate limits to trigger backoff.
    """

    pass


class ValidationError(FatalETLError):
    """
    Exception raised during data validation.
    """

    def __init__(self, message: str, errors: list = None):
        super().__init__(message)
        self.errors = errors or []
