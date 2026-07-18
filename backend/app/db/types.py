from datetime import UTC, datetime

from sqlalchemy import DateTime, Numeric, TypeDecorator


class UTCDateTime(TypeDecorator):
    """
    Forces all datetimes to be timezone-aware UTC objects.
    When retrieving from DB, attaches tzinfo=timezone.utc.
    """

    impl = DateTime
    cache_ok = True

    def process_bind_param(self, value: datetime | None, dialect) -> datetime | None:
        if value is not None:
            if value.tzinfo is None:
                value = value.replace(tzinfo=UTC)
            else:
                value = value.astimezone(UTC)
        return value

    def process_result_value(self, value: datetime | None, dialect) -> datetime | None:
        if value is not None:
            if value.tzinfo is None:
                value = value.replace(tzinfo=UTC)
        return value


class EnergyValue(TypeDecorator):
    """
    Standardized NUMERIC(12,2) for massive MW generation/demand values.
    """

    impl = Numeric(12, 2)
    cache_ok = True


class Capacity(TypeDecorator):
    """
    Standardized NUMERIC(12,2) for Plant Capacities.
    """

    impl = Numeric(12, 2)
    cache_ok = True


class Currency(TypeDecorator):
    """
    Standardized NUMERIC(12,2) for IEX Market Pricing.
    """

    impl = Numeric(12, 2)
    cache_ok = True


class EmissionValue(TypeDecorator):
    """
    Standardized NUMERIC(10,3) for exact Carbon Intensity tracking.
    """

    impl = Numeric(10, 3)
    cache_ok = True


class Percentage(TypeDecorator):
    """
    Standardized NUMERIC(5,2) for 0.00 to 100.00 values.
    """

    impl = Numeric(5, 2)
    cache_ok = True
