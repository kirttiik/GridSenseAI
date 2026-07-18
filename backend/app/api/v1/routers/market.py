from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc

from app.db.session import get_db
from app.schemas.market import MarketDataResponse
from app.schemas.responses import SuccessResponse, PaginatedResponse
from app.models.market.market_data import MarketData

router = APIRouter()

@router.get("/current", response_model=SuccessResponse[list[MarketDataResponse]])
async def get_current_market(session: AsyncSession = Depends(get_db)):
    """
    Fetch the latest available market records.
    """
    stmt = select(MarketData).order_by(desc(MarketData.timestamp)).limit(20)
    result = await session.execute(stmt)
    data = result.scalars().all()
    return SuccessResponse(data=list(data))

@router.get("/history", response_model=PaginatedResponse[MarketDataResponse])
async def get_market_history(
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    session: AsyncSession = Depends(get_db)
):
    """
    Fetch historical market records.
    """
    offset = (page - 1) * page_size
    count_stmt = select(MarketData)
    total = len((await session.execute(count_stmt)).scalars().all())
    
    stmt = select(MarketData).order_by(desc(MarketData.timestamp)).offset(offset).limit(page_size)
    result = await session.execute(stmt)
    data = result.scalars().all()
    
    return PaginatedResponse(data=list(data), total=total, page=page, size=page_size)
