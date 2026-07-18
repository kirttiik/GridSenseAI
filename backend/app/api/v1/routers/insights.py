from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc

from app.db.session import get_db
from app.schemas.insights import AIInsightResponse
from app.schemas.responses import SuccessResponse, PaginatedResponse
from app.models.ml.ai_insight import AIInsight

router = APIRouter()

@router.get("/current", response_model=SuccessResponse[list[AIInsightResponse]])
async def get_current_insights(session: AsyncSession = Depends(get_db)):
    stmt = select(AIInsight).order_by(desc(AIInsight.timestamp)).limit(20)
    result = await session.execute(stmt)
    data = result.scalars().all()
    return SuccessResponse(data=list(data))

@router.get("/history", response_model=PaginatedResponse[AIInsightResponse])
async def get_insights_history(
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    session: AsyncSession = Depends(get_db)
):
    offset = (page - 1) * page_size
    count_stmt = select(AIInsight)
    total = len((await session.execute(count_stmt)).scalars().all())
    
    stmt = select(AIInsight).order_by(desc(AIInsight.timestamp)).offset(offset).limit(page_size)
    result = await session.execute(stmt)
    data = result.scalars().all()
    
    return PaginatedResponse(data=list(data), total=total, page=page, size=page_size)
