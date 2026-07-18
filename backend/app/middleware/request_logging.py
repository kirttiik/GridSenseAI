import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.logging.logger import logger, request_id_ctx_var


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware that generates a unique request ID, injects it into the context var
    for logging, tracks execution time, and returns the ID in the response headers.
    """

    async def dispatch(self, request: Request, call_next):
        # Extract existing X-Request-ID or generate a new UUID4
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))

        # Set context variable for the CorrelationIdFilter in logger
        token = request_id_ctx_var.set(request_id)

        start_time = time.time()

        try:
            logger.info(f"Incoming Request: {request.method} {request.url.path}")

            response = await call_next(request)

            process_time = (time.time() - start_time) * 1000
            logger.info(
                f"Completed Request: {request.method} {request.url.path} - Status: {response.status_code} - Time: {process_time:.2f}ms"
            )

            # Attach the request ID to the response header
            response.headers["X-Request-ID"] = request_id
            response.headers["X-Process-Time"] = str(process_time)

            return response

        except Exception as e:
            process_time = (time.time() - start_time) * 1000
            logger.error(
                f"Failed Request: {request.method} {request.url.path} - Error: {str(e)} - Time: {process_time:.2f}ms"
            )
            raise
        finally:
            request_id_ctx_var.reset(token)
