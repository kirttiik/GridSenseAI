import uuid
from datetime import datetime

from sqlalchemy import Float, String, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDPrimaryKeyMixin
from app.db.types import UTCDateTime


class PowerSystemPosition(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Stores Power System Position data: demand met, shortage, etc.
    """
    __tablename__ = "power_system_position"

    timestamp: Mapped[datetime] = mapped_column(UTCDateTime(timezone=True), index=True)
    region: Mapped[str] = mapped_column(String(100), index=True)
    peak_demand_mw: Mapped[float] = mapped_column(Float, nullable=True)
    energy_met_mu: Mapped[float] = mapped_column(Float, nullable=True)
    shortage_mu: Mapped[float] = mapped_column(Float, nullable=True)
    frequency_stats: Mapped[str] = mapped_column(String(255), nullable=True)

    __table_args__ = (
        Index("ix_psp_timestamp_region", "timestamp", "region"),
    )
