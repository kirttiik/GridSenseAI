from fastapi import Request, status
from fastapi.responses import JSONResponse


class GridSenseError(Exception):
    def __init__(self, message: str, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR) -> None:
        self.message = message
        self.status_code = status_code
        super().__init__(message)


async def gridsense_exception_handler(_: Request, exc: GridSenseError) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": exc.status_code,
                "message": exc.message,
            },
        },
    )
