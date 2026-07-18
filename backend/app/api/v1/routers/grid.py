from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc

from app.db.session import get_db
from app.schemas.grid import GridStatusResponse
from app.schemas.responses import SuccessResponse, PaginatedResponse
from app.models.grid.grid_status import GridStatus

router = APIRouter()

@router.get("/current", response_model=SuccessResponse[list[GridStatusResponse]])
async def get_current_grid(session: AsyncSession = Depends(get_db)):
    """
    Fetch the latest available grid records.
    """
    stmt = select(GridStatus).order_by(desc(GridStatus.timestamp)).limit(20)
    result = await session.execute(stmt)
    data = result.scalars().all()
    return SuccessResponse(data=list(data))

@router.get("/history", response_model=PaginatedResponse[GridStatusResponse])
async def get_grid_history(
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    session: AsyncSession = Depends(get_db)
):
    """
    Fetch historical grid records.
    """
    offset = (page - 1) * page_size
    count_stmt = select(GridStatus)
    total = len((await session.execute(count_stmt)).scalars().all())
    
    stmt = select(GridStatus).order_by(desc(GridStatus.timestamp)).offset(offset).limit(page_size)
    result = await session.execute(stmt)
    data = result.scalars().all()
    
    return PaginatedResponse(data=list(data), total=total, page=page, size=page_size)
