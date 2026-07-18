from datetime import datetime
from pydantic import BaseModel
from typing import List

from app.schemas.energy import EnergyDataResponse
from app.schemas.grid import GridStatusResponse
from app.schemas.market import MarketDataResponse

class DashboardOverviewResponse(BaseModel):
    total_energy_records: int
    latest_grid_status: GridStatusResponse | None = None
    latest_market_info: MarketDataResponse | None = None
    latest_energy_info: EnergyDataResponse | None = None
    last_sync_time: datetime | None = None
