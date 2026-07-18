from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import GridSenseException
from app.logging.logger import logger


def setup_exception_handlers(app: FastAPI):
    """
    Registers global exception handlers to standardize error responses.
    """

    @app.exception_handler(GridSenseException)
    async def gridsense_exception_handler(request: Request, exc: GridSenseException):
        """Catches all custom domain exceptions and formats them."""
        logger.warning(f"Domain Exception: {exc.code} - {exc.message}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": {"code": exc.code, "message": exc.message},
                "request_id": request.headers.get("X-Request-ID"),
            },
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        """Catches unexpected 500 errors."""
        logger.exception(f"Unhandled Exception: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": {
                    "code": "INTERNAL_SERVER_ERROR",
                    "message": "An unexpected error occurred.",
                },
                "request_id": request.headers.get("X-Request-ID"),
            },
        )
