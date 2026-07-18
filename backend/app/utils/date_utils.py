from datetime import UTC, datetime


def to_utc(dt: datetime) -> datetime:
    """
    Ensures a datetime object is timezone-aware and set to UTC.
    If the datetime is naive, it assumes it is UTC.
    """
    if dt.tzinfo is None:
        return dt.replace(tzinfo=UTC)
    return dt.astimezone(UTC)


def generate_date_key(dt: datetime) -> int:
    """
    Generates a Kimball-style integer date key (e.g. 20260717)
    from a datetime object. Used for the time_dimension table.
    """
    return int(dt.strftime("%Y%m%d"))
