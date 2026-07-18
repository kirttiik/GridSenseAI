from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from app.db.session import get_db
from app.schemas.dashboard import DashboardOverviewResponse
from app.schemas.responses import SuccessResponse
from app.models.energy.energy_data import EnergyData
from app.models.grid.grid_status import GridStatus
from app.models.market.market_data import MarketData

router = APIRouter()

@router.get("/overview", response_model=SuccessResponse[DashboardOverviewResponse])
async def get_overview(session: AsyncSession = Depends(get_db)):
    """
    Fetch comprehensive dashboard overview metrics from MVP schemas.
    """
    # 1. Total Energy Records count
    energy_count_stmt = select(func.count()).select_from(EnergyData)
    total_energy_records = (await session.execute(energy_count_stmt)).scalar_one()

    # 2. Latest Grid Status
    grid_stmt = select(GridStatus).order_by(GridStatus.timestamp.desc()).limit(1)
    latest_grid_status = (await session.execute(grid_stmt)).scalar_one_or_none()

    # 3. Latest Market Info
    market_stmt = select(MarketData).order_by(MarketData.timestamp.desc()).limit(1)
    latest_market_info = (await session.execute(market_stmt)).scalar_one_or_none()
    
    # 4. Latest Energy Info
    energy_stmt = select(EnergyData).order_by(EnergyData.timestamp.desc()).limit(1)
    latest_energy_info = (await session.execute(energy_stmt)).scalar_one_or_none()
    
    # Check last sync time (using greatest of the three)
    timestamps = [
        t for t in [
            latest_grid_status.timestamp if latest_grid_status else None,
            latest_market_info.timestamp if latest_market_info else None,
            latest_energy_info.timestamp if latest_energy_info else None
        ] if t is not None
    ]
    
    last_sync_time = max(timestamps) if timestamps else None

    overview = DashboardOverviewResponse(
        total_energy_records=total_energy_records,
        latest_grid_status=latest_grid_status,
        latest_market_info=latest_market_info,
        latest_energy_info=latest_energy_info,
        last_sync_time=last_sync_time
    )

    return SuccessResponse(data=overview)
