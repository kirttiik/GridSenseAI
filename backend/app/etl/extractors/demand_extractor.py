import asyncio
import random
from datetime import UTC, datetime, timedelta
from typing import Any

from app.etl.base.base_extractor import BaseExtractor


class DemandExtractor(BaseExtractor):
    def __init__(self, dataset_id: str):
        super().__init__(dataset_id=dataset_id)

    def get_endpoint(self) -> str:
        return "https://api.grid-india.in/v1/demand"

    def get_http_method(self) -> str:
        return "GET"

    async def extract_data(self, **kwargs) -> Any:
        """
        Mock SDK call to fetch demand data.
        In a real scenario, this would import the Energy Atlas SDK.
        """
        await asyncio.sleep(0.5)  # Simulate network delay

        # Generating mock demand for Delhi
        now = datetime.now(UTC)

        data = []
        for i in range(24):  # Fetch last 24 hours
            ts = now - timedelta(hours=i)
            data.append(
                {
                    "timestamp": ts.isoformat(),
                    "state_abbreviation": "DL",
                    "demand_mw": 4500 + random.uniform(-500, 500),
                }
            )

        return data
