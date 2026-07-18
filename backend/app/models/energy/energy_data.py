import uuid
from datetime import datetime

from sqlalchemy import Float, String, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDPrimaryKeyMixin
from app.db.types import UTCDateTime


class EnergyData(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Stores generation and demand metrics by timestamp and region.
    """
    __tablename__ = "energy_data"

    timestamp: Mapped[datetime] = mapped_column(UTCDateTime(timezone=True), index=True)
    region: Mapped[str] = mapped_column(String(100), index=True)
    source_type: Mapped[str] = mapped_column(String(50))  # e.g., Solar, Wind, Thermal, Demand
    value_mw: Mapped[float] = mapped_column(Float)

    __table_args__ = (
        Index("ix_energy_data_timestamp_region", "timestamp", "region"),
    )
