from typing import Optional

import httpx

from app.sdk.energy_atlas.assets import AssetsModule
from app.sdk.energy_atlas.carbon import CarbonModule
from app.sdk.energy_atlas.client import BaseClient
from app.sdk.energy_atlas.demand import DemandModule
from app.sdk.energy_atlas.exceptions import (
    AuthenticationError,
    AuthorizationError,
    EndpointUnavailableError,
    EnergyAtlasError,
    NetworkError,
    RateLimitError,
    ServerError,
    TimeoutError,
    UnexpectedResponseError,
    ValidationError,
)
from app.sdk.energy_atlas.generation import GenerationModule
from app.sdk.energy_atlas.grid import GridModule
from app.sdk.energy_atlas.iex import IexModule
from app.sdk.energy_atlas.models import EnergyAtlasResponse, ResponseMetadata, SDKResponse
from app.sdk.energy_atlas.operations import OperationsModule


class EnergyAtlasClient(BaseClient):
    """
    Top-level SDK Client for the India Energy Atlas API.

    Provides access to various domain modules. Example usage:
    ```
    atlas = EnergyAtlasClient()
    response = await atlas.grid.get_frequency()
    print(response.data)
    print(response.metadata.request_id)
    await atlas.close()
    ```
    """

    def __init__(self, client: httpx.AsyncClient | None = None):
        super().__init__(client=client)

        # Initialize domain modules
        self.grid = GridModule(self)
        self.demand = DemandModule(self)
        self.generation = GenerationModule(self)
        self.carbon = CarbonModule(self)
        self.iex = IexModule(self)
        self.assets = AssetsModule(self)
        self.operations = OperationsModule(self)


__all__ = [
    "EnergyAtlasClient",
    "SDKResponse",
    "EnergyAtlasResponse",
    "ResponseMetadata",
    "EnergyAtlasError",
    "AuthenticationError",
    "RateLimitError",
    "TimeoutError",
    "AuthorizationError",
    "EndpointUnavailableError",
    "ValidationError",
    "ServerError",
    "NetworkError",
    "UnexpectedResponseError",
]
