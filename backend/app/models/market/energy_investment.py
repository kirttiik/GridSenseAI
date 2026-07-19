import uuid
from datetime import datetime

from sqlalchemy import Float, String, Index, Date
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class EnergyInvestment(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """
    Stores Energy Sector Investments data.
    """
    __tablename__ = "energy_investments"

    deal_value_inr: Mapped[float] = mapped_column(Float, nullable=True)
    investor: Mapped[str] = mapped_column(String(255), index=True, nullable=True)
    technology: Mapped[str] = mapped_column(String(100), index=True, nullable=True)
    state: Mapped[str] = mapped_column(String(100), index=True, nullable=True)
    status: Mapped[str] = mapped_column(String(50), nullable=True)
    date: Mapped[datetime] = mapped_column(Date, index=True, nullable=True)

    __table_args__ = (
        Index("ix_energy_investments_tech_state", "technology", "state"),
    )
