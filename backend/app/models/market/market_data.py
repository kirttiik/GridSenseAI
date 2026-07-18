import uuid
from datetime import datetime

from sqlalchemy import Float, String, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDPrimaryKeyMixin
from app.db.types import UTCDateTime


class MarketData(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Stores DAM and RTM clearing prices.
    """
    __tablename__ = "market_data"

    timestamp: Mapped[datetime] = mapped_column(UTCDateTime(timezone=True), index=True)
    region: Mapped[str] = mapped_column(String(100), index=True)
    market_type: Mapped[str] = mapped_column(String(50))  # e.g., DAM, RTM
    price_inr: Mapped[float] = mapped_column(Float)
    volume_mwh: Mapped[float] = mapped_column(Float, nullable=True)

    __table_args__ = (
        Index("ix_market_data_timestamp_region", "timestamp", "region"),
    )
