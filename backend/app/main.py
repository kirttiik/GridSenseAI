import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app.api.v1.router import api_router
from app.core.settings import settings
from app.exceptions.handlers import setup_exception_handlers
from app.logging.logger import logger
from app.middleware.rate_limit import RateLimitMiddleware
from app.middleware.request_logging import RequestLoggingMiddleware
from app.middleware.security import SecurityHeadersMiddleware
from app.startup.lifespan import lifespan


def create_app() -> FastAPI:
    """
    Bootstraps and configures the FastAPI application instance.
    Includes middleware registration, routers, and exception handlers.
    """
    logger.info(f"Starting {settings.PROJECT_NAME} in {settings.ENVIRONMENT} mode.")

    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description="GridSense AI Core Backend API for Energy Intelligence",
        contact={
            "name": "GridSense AI Team",
            "url": "https://gridsense.io/contact",
            "email": "support@gridsense.io",
        },
        license_info={
            "name": "Proprietary",
            "url": "https://gridsense.io/license",
        },
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    # 1. Security & CORS Middleware
    app.add_middleware(RateLimitMiddleware)
    app.add_middleware(SecurityHeadersMiddleware)
    origins = [
        "http://localhost:3000",
        "https://grid-sense-ai-ebon.vercel.app",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_origin_regex=r"https://.*\.vercel\.app",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Optional: Restrict hosts in production
    if settings.ENVIRONMENT == "production":
        app.add_middleware(
            TrustedHostMiddleware, allowed_hosts=["api.gridsense.io", "*.gridsense.io"]
        )

    # 2. Performance Middleware
    app.add_middleware(GZipMiddleware, minimum_size=1000)

    # 3. Observability & Logging Middleware
    app.add_middleware(RequestLoggingMiddleware)

    # 4. Global Exception Handlers
    setup_exception_handlers(app)

    # 5. Routers
    app.include_router(api_router, prefix=settings.API_V1_STR)

    # Root health redirect or simple message
    @app.get("/", tags=["System"], include_in_schema=False)
    async def root():
        """Redirects or informs users where the docs are."""
        return {"message": f"Welcome to {settings.PROJECT_NAME}. Docs at /docs"}

    return app


# The ASGI application entry point
app = create_app()
