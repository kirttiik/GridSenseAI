import uuid
from datetime import datetime

from sqlalchemy import Float, String, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDPrimaryKeyMixin
from app.db.types import UTCDateTime


class GridStatus(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Stores real-time telemetry like frequency and stability indices.
    """
    __tablename__ = "grid_status"

    timestamp: Mapped[datetime] = mapped_column(UTCDateTime(timezone=True), index=True)
    region: Mapped[str] = mapped_column(String(100), index=True)
    frequency_hz: Mapped[float] = mapped_column(Float)
    stability_index: Mapped[float] = mapped_column(Float)
    voltage_kv: Mapped[float] = mapped_column(Float, nullable=True)

    __table_args__ = (
        Index("ix_grid_status_timestamp_region", "timestamp", "region"),
    )
