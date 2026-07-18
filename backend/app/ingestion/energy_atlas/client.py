import logging

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from app.core.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()


class EnergyAtlasClient:
    def __init__(self):
        self.base_url = settings.energy_atlas_api_url
        self.api_key = settings.energy_atlas_api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}" if self.api_key else "",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    @retry(
        wait=wait_exponential(multiplier=1, min=2, max=10),
        stop=stop_after_attempt(5),
        retry=retry_if_exception_type((httpx.RequestError, httpx.HTTPStatusError)),
        reraise=True,
    )
    async def request(self, method: str, endpoint: str, **kwargs) -> dict:
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        logger.debug(f"EnergyAtlas API Request: {method} {url}")

        async with httpx.AsyncClient(headers=self.headers, timeout=30.0) as client:
            response = await client.request(method, url, **kwargs)

            if response.status_code == 429:
                logger.warning(f"Rate limited by EnergyAtlas API. Status: {response.status_code}")
                response.raise_for_status()  # Trigger tenacity retry

            response.raise_for_status()
            return response.json()
