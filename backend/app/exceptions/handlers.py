import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.schemas.responses import ErrorResponse
from app.services.exceptions import (
    BusinessRuleViolation,
    ConflictError,
    DataNotAvailable,
    ResourceNotFound,
    ServiceException,
    ServiceUnavailable,
    ValidationError,
)

logger = logging.getLogger(__name__)


def setup_exception_handlers(app: FastAPI):
    """Register all global exception handlers."""

    @app.exception_handler(ResourceNotFound)
    async def resource_not_found_handler(request: Request, exc: ResourceNotFound):
        logger.warning(f"ResourceNotFound: {exc}")
        content = ErrorResponse(
            success=False, error=str(exc), code="RESOURCE_NOT_FOUND"
        ).model_dump()
        return JSONResponse(status_code=404, content=content)

    @app.exception_handler(ValidationError)
    async def validation_error_handler(request: Request, exc: ValidationError):
        logger.warning(f"ValidationError: {exc}")
        content = ErrorResponse(success=False, error=str(exc), code="VALIDATION_ERROR").model_dump()
        return JSONResponse(status_code=422, content=content)

    @app.exception_handler(BusinessRuleViolation)
    async def business_rule_violation_handler(request: Request, exc: BusinessRuleViolation):
        logger.warning(f"BusinessRuleViolation: {exc}")
        content = ErrorResponse(
            success=False, error=str(exc), code="BUSINESS_RULE_VIOLATION"
        ).model_dump()
        return JSONResponse(status_code=400, content=content)

    @app.exception_handler(ConflictError)
    async def conflict_error_handler(request: Request, exc: ConflictError):
        logger.warning(f"ConflictError: {exc}")
        content = ErrorResponse(success=False, error=str(exc), code="CONFLICT_ERROR").model_dump()
        return JSONResponse(status_code=409, content=content)

    @app.exception_handler(DataNotAvailable)
    async def data_not_available_handler(request: Request, exc: DataNotAvailable):
        logger.warning(f"DataNotAvailable: {exc}")
        content = ErrorResponse(
            success=False, error=str(exc), code="DATA_NOT_AVAILABLE"
        ).model_dump()
        return JSONResponse(status_code=404, content=content)

    @app.exception_handler(ServiceUnavailable)
    async def service_unavailable_handler(request: Request, exc: ServiceUnavailable):
        logger.error(f"ServiceUnavailable: {exc}")
        content = ErrorResponse(
            success=False, error=str(exc), code="SERVICE_UNAVAILABLE"
        ).model_dump()
        return JSONResponse(status_code=503, content=content)

    @app.exception_handler(ServiceException)
    async def base_service_exception_handler(request: Request, exc: ServiceException):
        logger.error(f"ServiceException: {exc}")
        content = ErrorResponse(
            success=False, error=str(exc), code="INTERNAL_SERVICE_ERROR"
        ).model_dump()
        return JSONResponse(status_code=500, content=content)

    @app.exception_handler(RequestValidationError)
    async def fastapi_validation_handler(request: Request, exc: RequestValidationError):
        logger.warning(f"RequestValidationError: {exc}")
        content = ErrorResponse(
            success=False, error="Invalid request payload", code="UNPROCESSABLE_ENTITY"
        ).model_dump()
        return JSONResponse(status_code=422, content=content)

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        content = ErrorResponse(
            success=False, error=str(exc.detail), code=f"HTTP_{exc.status_code}"
        ).model_dump()
        return JSONResponse(status_code=exc.status_code, content=content)

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        logger.exception(f"Unhandled Exception: {exc}")
        from app.core.settings import settings

        error_msg = str(exc) if settings.DEBUG else "An unexpected internal server error occurred"
        content = ErrorResponse(
            success=False, error=error_msg, code="INTERNAL_SERVER_ERROR"
        ).model_dump()
        return JSONResponse(status_code=500, content=content)
