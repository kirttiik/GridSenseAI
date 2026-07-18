from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.environment import EnvironmentType


import time

class Settings(BaseSettings):
    """
    Core application settings, leveraging pydantic-settings to automatically
    load from environment variables or .env files.
    """

    START_TIME: float = time.time()

    # Environment
    ENVIRONMENT: EnvironmentType = EnvironmentType.DEVELOPMENT

    # Application
    PROJECT_NAME: str = "GridSense AI"
    API_V1_STR: str = "/api/v1"
    VERSION: str = "1.0.0"
    DEBUG: bool = False

    # Security / CORS
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:8000"]
    SECRET_KEY: str = "SUPER_SECRET_CHANGE_IN_PRODUCTION"  # Placeholder
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30  # 30 days
    API_KEY_HEADER: str = "X-API-Key"
    ALLOWED_API_KEYS: str = "demo-key,admin-key"  # Comma separated
    RATE_LIMIT_PER_MINUTE: int = 60

    # PostgreSQL Database
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "gridsense"
    POSTGRES_PORT: int = 5432

    DATABASE_URL: str | None = None

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        """Assembles the async PostgreSQL database URI or returns DATABASE_URL."""
        if self.DATABASE_URL:
            # SQLAlchemy 2.0 requires asyncpg
            if self.DATABASE_URL.startswith("postgres://"):
                return self.DATABASE_URL.replace("postgres://", "postgresql+asyncpg://")
            if self.DATABASE_URL.startswith("postgresql://"):
                return self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
            return self.DATABASE_URL

        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # Energy Atlas SDK Configuration (Pass-throughs)
    ENERGY_ATLAS_API_KEY: str = ""
    ENERGY_ATLAS_API_URL: str = "https://api.energyatlas.io"

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Retry and Execution
    MAX_RETRIES: int = 3
    RETRY_BACKOFF_FACTOR: float = 0.5

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True, extra="ignore"
    )


settings = Settings()
