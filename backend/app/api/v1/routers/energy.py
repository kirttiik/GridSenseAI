from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc

from app.db.session import get_db
from app.schemas.energy import EnergyDataResponse
from app.schemas.responses import SuccessResponse, PaginatedResponse
from app.models.energy.energy_data import EnergyData

router = APIRouter()

@router.get("/current", response_model=SuccessResponse[list[EnergyDataResponse]])
async def get_current_energy(session: AsyncSession = Depends(get_db)):
    """
    Fetch the latest available energy records.
    """
    stmt = select(EnergyData).order_by(desc(EnergyData.timestamp)).limit(20)
    result = await session.execute(stmt)
    data = result.scalars().all()
    return SuccessResponse(data=list(data))

@router.get("/history", response_model=PaginatedResponse[EnergyDataResponse])
async def get_energy_history(
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    session: AsyncSession = Depends(get_db)
):
    """
    Fetch historical energy records.
    """
    offset = (page - 1) * page_size
    
    # Get total count
    count_stmt = select(EnergyData)
    total = len((await session.execute(count_stmt)).scalars().all()) # not efficient, but MVP scale
    
    # Get paginated data
    stmt = select(EnergyData).order_by(desc(EnergyData.timestamp)).offset(offset).limit(page_size)
    result = await session.execute(stmt)
    data = result.scalars().all()
    
    return PaginatedResponse(data=list(data), total=total, page=page, size=page_size)
