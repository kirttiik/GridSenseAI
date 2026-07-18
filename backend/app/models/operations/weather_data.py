import uuid
from datetime import datetime

from sqlalchemy import Float, String, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDPrimaryKeyMixin
from app.db.types import UTCDateTime


class WeatherData(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Stores meteorological data such as temperature, irradiance, and wind speed.
    """
    __tablename__ = "weather_data"

    timestamp: Mapped[datetime] = mapped_column(UTCDateTime(timezone=True), index=True)
    region: Mapped[str] = mapped_column(String(100), index=True)
    temperature_celsius: Mapped[float] = mapped_column(Float, nullable=True)
    irradiance_w_m2: Mapped[float] = mapped_column(Float, nullable=True)
    wind_speed_m_s: Mapped[float] = mapped_column(Float, nullable=True)
    humidity_percent: Mapped[float] = mapped_column(Float, nullable=True)

    __table_args__ = (
        Index("ix_weather_data_timestamp_region", "timestamp", "region"),
    )
