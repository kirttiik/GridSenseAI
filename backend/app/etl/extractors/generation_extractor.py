import asyncio
import random
from datetime import UTC, datetime, timedelta
from typing import Any

from app.etl.base.base_extractor import BaseExtractor


class GenerationExtractor(BaseExtractor):
    def __init__(self, dataset_id: str):
        super().__init__(dataset_id=dataset_id)

    def get_endpoint(self) -> str:
        return "https://api.grid-india.in/v1/generation"

    def get_http_method(self) -> str:
        return "GET"

    async def extract_data(self, **kwargs) -> Any:
        """
        Mock SDK call to fetch generation data.
        """
        await asyncio.sleep(0.5)
        now = datetime.now(UTC)

        data = []
        for i in range(24):
            ts = now - timedelta(hours=i)
            # Generating mock generation for Gujarat
            data.append(
                {
                    "timestamp": ts.isoformat(),
                    "state_abbreviation": "GJ",
                    "fuel_type": "Coal",
                    "generation_mw": 8000 + random.uniform(-100, 200),
                }
            )
            data.append(
                {
                    "timestamp": ts.isoformat(),
                    "state_abbreviation": "GJ",
                    "fuel_type": "Solar",
                    "generation_mw": 2000 + random.uniform(-50, 50)
                    if ts.hour > 6 and ts.hour < 18
                    else 0,
                }
            )

        return data
