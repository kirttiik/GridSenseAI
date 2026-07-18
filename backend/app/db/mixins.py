import uuid
from datetime import UTC, datetime

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.db.types import UTCDateTime


def utc_now() -> datetime:
    """Helper to return current UTC datetime."""
    return datetime.now(UTC)


class UUIDPrimaryKeyMixin:
    """
    Provides a standard UUIDv4 primary key.
    """

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4, index=True)


class TimestampMixin:
    """
    Provides standard timestamps required by the database architecture.
    """

    created_at: Mapped[datetime] = mapped_column(
        UTCDateTime(timezone=True), default=utc_now, server_default=func.now(), nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        UTCDateTime(timezone=True),
        default=utc_now,
        onupdate=utc_now,
        server_default=func.now(),
        nullable=False,
    )


class AuditMixin:
    """
    Provides standard audit user tracking.
    Stored as generic VARCHAR(100) to support system strings ("Airflow", "FastAPI")
    without enforcing a strict FK to a Users table immediately.
    """

    created_by: Mapped[str] = mapped_column(String(100), nullable=False, default="system")
    updated_by: Mapped[str] = mapped_column(String(100), nullable=False, default="system")


class SoftDeleteMixin:
    """
    Replaces boolean is_active with a timestamp-based deleted_at column
    for precise historical auditing of soft deletes.
    """

    deleted_at: Mapped[datetime | None] = mapped_column(
        UTCDateTime(timezone=True), nullable=True, default=None
    )


class VersionMixin:
    """
    Provides optimistic locking support by tracking record versions.
    Automatically increments on update.
    """

    version: Mapped[int] = mapped_column(Integer, nullable=False, default=1, server_default="1")

    # In future model definitions, set __mapper_args__ = {"version_id_col": version}
    # to enforce optimistic concurrency control natively in SQLAlchemy.


class SourceSystemMixin:
    """
    Provides the source_system column mandated for all fact tables
    to support multi-vendor data integration.
    """

    source_system: Mapped[str] = mapped_column(String(50), nullable=False, default="EnergyAtlas")
