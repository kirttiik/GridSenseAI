import uuid

from sqlalchemy import Float, String, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class PowerPlant(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Stores Power Plant registries.
    """
    __tablename__ = "power_plants"

    name: Mapped[str] = mapped_column(String(255), index=True)
    state: Mapped[str] = mapped_column(String(100), index=True)
    region: Mapped[str] = mapped_column(String(100), index=True)
    installed_capacity_mw: Mapped[float] = mapped_column(Float)
    fuel_type: Mapped[str] = mapped_column(String(100), index=True)
    technology: Mapped[str] = mapped_column(String(100), nullable=True)
    lat: Mapped[float] = mapped_column(Float, nullable=True)
    lon: Mapped[float] = mapped_column(Float, nullable=True)

    __table_args__ = (
        Index("ix_power_plants_state_fuel", "state", "fuel_type"),
    )
