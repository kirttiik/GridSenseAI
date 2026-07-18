from collections.abc import Generator

import httpx


class EnergyAtlasAuth(httpx.Auth):
    """
    Custom HTTPX Auth that dynamically applies the correct authentication scheme
    based on the endpoint URL.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key

    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
        url_path = request.url.path.lower()

        # Developer APIs use X-API-Key
        if "/developer/v1/" in url_path:
            request.headers["X-API-Key"] = self.api_key
        else:
            # Intelligence and all other APIs use Bearer token
            request.headers["Authorization"] = f"Bearer {self.api_key}"

        yield request
