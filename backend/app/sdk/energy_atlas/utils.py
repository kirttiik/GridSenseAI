from typing import Any
from urllib.parse import urlencode


def build_query_string(params: dict[str, Any]) -> str:
    """Build a query string dropping None values."""
    filtered_params = {k: v for k, v in params.items() if v is not None}
    if not filtered_params:
        return ""
    return "?" + urlencode(filtered_params)


def extract_pagination_metadata(response_data: Any) -> dict[str, Any] | None:
    """Extract standard pagination fields (count, limit, offset, total) if present."""
    if not isinstance(response_data, dict):
        return None

    metadata = {}
    for key in ["count", "limit", "offset", "total"]:
        if key in response_data:
            metadata[key] = response_data[key]

    return metadata if metadata else None
