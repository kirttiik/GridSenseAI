import uuid

from sqlalchemy import Float, String, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class TransmissionLine(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Stores Transmission Line registries.
    """
    __tablename__ = "transmission_lines"

    name: Mapped[str] = mapped_column(String(255), index=True)
    state: Mapped[str] = mapped_column(String(100), index=True, nullable=True)
    voltage_kv: Mapped[float] = mapped_column(Float, nullable=True)
    circuit_length_km: Mapped[float] = mapped_column(Float, nullable=True)

    __table_args__ = (
        Index("ix_transmission_lines_state_voltage", "state", "voltage_kv"),
    )
