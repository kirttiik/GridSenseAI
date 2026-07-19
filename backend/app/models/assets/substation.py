import uuid

from sqlalchemy import Float, String, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class Substation(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Stores Substation registries.
    """
    __tablename__ = "substations"

    name: Mapped[str] = mapped_column(String(255), index=True)
    voltage_kv: Mapped[float] = mapped_column(Float, nullable=True)
    capacity_mva: Mapped[float] = mapped_column(Float, nullable=True)
    lat: Mapped[float] = mapped_column(Float, nullable=True)
    lon: Mapped[float] = mapped_column(Float, nullable=True)

    __table_args__ = (
        Index("ix_substations_voltage", "voltage_kv"),
    )
