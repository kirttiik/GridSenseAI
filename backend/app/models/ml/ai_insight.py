import uuid
from datetime import datetime

from sqlalchemy import Float, String, Index, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDPrimaryKeyMixin
from app.db.types import UTCDateTime


class AIInsight(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Stores AI-generated predictions, recommendations, and confidence intervals.
    """
    __tablename__ = "ai_insight"

    timestamp: Mapped[datetime] = mapped_column(UTCDateTime(timezone=True), index=True)
    region: Mapped[str] = mapped_column(String(100), index=True)
    title: Mapped[str] = mapped_column(String(255))
    summary: Mapped[str] = mapped_column(Text)
    severity: Mapped[str] = mapped_column(String(50))  # e.g., low, medium, high, critical
    confidence: Mapped[int] = mapped_column(Integer)
    recommendation: Mapped[str] = mapped_column(Text, nullable=True)
    target_timeframe: Mapped[str] = mapped_column(String(100), nullable=True)

    __table_args__ = (
        Index("ix_ai_insight_timestamp_region", "timestamp", "region"),
    )
