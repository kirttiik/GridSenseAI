import uuid
from datetime import datetime

from sqlalchemy import Float, String, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDPrimaryKeyMixin
from app.db.types import UTCDateTime


class CarbonIntensity(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Stores carbon intensity estimates for regions and states.
    """
    __tablename__ = "carbon_intensity"

    timestamp: Mapped[datetime] = mapped_column(UTCDateTime(timezone=True), index=True)
    region: Mapped[str] = mapped_column(String(100), index=True)
    value_gco2_kwh: Mapped[float] = mapped_column(Float)

    __table_args__ = (
        Index("ix_carbon_intensity_timestamp_region", "timestamp", "region"),
    )
