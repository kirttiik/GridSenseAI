import logging
import sys
from contextvars import ContextVar
from logging.handlers import RotatingFileHandler

from app.core.settings import settings

# Context variable to store a unique request ID across async boundaries
request_id_ctx_var: ContextVar[str] = ContextVar("request_id", default="")


class CorrelationIdFilter(logging.Filter):
    """
    Injects the context-local request_id into the log record.
    """

    def filter(self, record):
        record.request_id = request_id_ctx_var.get()
        return True


def setup_logging():
    """
    Configures the root logger with both console and rotating file handlers,
    incorporating request correlation IDs.
    """
    logger = logging.getLogger("gridsense")
    logger.setLevel(settings.LOG_LEVEL)

    # Prevent duplicate logs if setup_logging is called multiple times
    if logger.handlers:
        return logger

    # Log Format
    # Example: 2026-07-17 12:00:00 - [REQ-123] - INFO - gridsense.api - This is a log message
    formatter = logging.Formatter(
        "%(asctime)s - [%(request_id)s] - %(levelname)s - %(name)s - %(message)s"
    )

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.addFilter(CorrelationIdFilter())
    logger.addHandler(console_handler)

    # File Handler (rotating, max 10MB per file, keep 5 backups)
    try:
        file_handler = RotatingFileHandler(
            "gridsense.log", maxBytes=10 * 1024 * 1024, backupCount=5
        )
        file_handler.setFormatter(formatter)
        file_handler.addFilter(CorrelationIdFilter())
        logger.addHandler(file_handler)
    except OSError:
        logger.warning("Could not set up file logging. Only console logging is available.")

    # Suppress noisy third-party loggers
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(
        logging.WARNING if not settings.DEBUG else logging.INFO
    )

    return logger


logger = setup_logging()
