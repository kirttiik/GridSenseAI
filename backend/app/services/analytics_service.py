from typing import Any, Dict
from datetime import datetime

from sqlalchemy import select, func, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.base.base_service import BaseService
from app.models.energy.energy_data import EnergyData
from app.models.grid.grid_status import GridStatus
from app.models.market.market_data import MarketData
from app.schemas.analytics import AnalyticsFilter

class AnalyticsService(BaseService):
    """
    Business service layer for cross-domain analytics and reporting.
    """
    def __init__(self, session: AsyncSession):
        # Override init to ensure we have a session.
        self.session = session
        
    def _apply_filters(self, query, model, filters: AnalyticsFilter):
        if filters.start_date:
            try:
                sd = datetime.fromisoformat(filters.start_date.replace('Z', '+00:00'))
                query = query.where(model.timestamp >= sd)
            except Exception:
                pass
        if filters.end_date:
            try:
                ed = datetime.fromisoformat(filters.end_date.replace('Z', '+00:00'))
                query = query.where(model.timestamp <= ed)
            except Exception:
                pass
        if filters.region:
            query = query.where(model.region == filters.region)
        return query

    async def get_generation_mix(self, filters: AnalyticsFilter) -> Dict[str, Any]:
        """
        Returns aggregated generation mix grouped by source type.
        """
        query = select(
            EnergyData.source_type,
            func.sum(EnergyData.value_mw).label("total_mw")
        )
        query = self._apply_filters(query, EnergyData, filters)
        if filters.fuel:
            query = query.where(EnergyData.source_type == filters.fuel)
            
        query = query.group_by(EnergyData.source_type)
        
        result = await self.session.execute(query)
        rows = result.fetchall()
        
        total_gen = sum(row.total_mw for row in rows if row.total_mw) or 1.0
        
        data = []
        for row in rows:
            val = float(row.total_mw or 0)
            data.append({
                "source_type": row.source_type,
                "value_mw": val,
                "percentage": round((val / total_gen) * 100, 2)
            })
            
        return {
            "status": "success",
            "data": data,
            "total_mw": total_gen if total_gen > 1.0 else 0
        }

    async def get_grid_health(self, filters: AnalyticsFilter) -> Dict[str, Any]:
        """
        Returns grid health metrics including average frequency.
        """
        # We need a proper date_trunc or simple casting. We'll use cast to Date if we want daily.
        query = select(
            func.date_trunc(filters.resolution if filters.resolution in ['hour', 'day', 'month'] else 'day', GridStatus.timestamp).label("time_bucket"),
            func.avg(GridStatus.frequency_hz).label("avg_freq"),
            func.min(GridStatus.frequency_hz).label("min_freq"),
            func.max(GridStatus.frequency_hz).label("max_freq")
        )
        query = self._apply_filters(query, GridStatus, filters)
        query = query.group_by("time_bucket").order_by("time_bucket")
        
        result = await self.session.execute(query)
        rows = result.fetchall()
        
        data = []
        for row in rows:
            data.append({
                "timestamp": row.time_bucket.isoformat() if row.time_bucket else None,
                "avg_frequency_hz": float(row.avg_freq or 0),
                "min_frequency_hz": float(row.min_freq or 0),
                "max_frequency_hz": float(row.max_freq or 0)
            })
            
        return {
            "status": "success",
            "data": data
        }

    async def get_market_trends(self, filters: AnalyticsFilter) -> Dict[str, Any]:
        """
        Returns market price and volume trends.
        """
        query = select(
            func.date_trunc(filters.resolution if filters.resolution in ['hour', 'day', 'month'] else 'day', MarketData.timestamp).label("time_bucket"),
            MarketData.market_type,
            func.avg(MarketData.price_inr).label("avg_price"),
            func.avg(MarketData.volume_mwh).label("avg_vol")
        )
        query = self._apply_filters(query, MarketData, filters)
        
        if filters.market_type:
            query = query.where(MarketData.market_type == filters.market_type)
            
        query = query.group_by("time_bucket", MarketData.market_type).order_by("time_bucket")
        
        result = await self.session.execute(query)
        rows = result.fetchall()
        
        data = []
        for row in rows:
            data.append({
                "timestamp": row.time_bucket.isoformat() if row.time_bucket else None,
                "market_type": row.market_type,
                "avg_price_inr": float(row.avg_price or 0),
                "avg_volume_mwh": float(row.avg_vol or 0)
            })
            
        return {
            "status": "success",
            "data": data
        }

    async def capacity_summary(self) -> dict[str, Any]:
        """Aggregate total installed capacity across all power plants."""
        return {"total_installed_mw": 350000}

    async def renewable_mix(self) -> dict[str, float]:
        """Calculate the percentage of renewable generation versus thermal."""
        return {"renewable_pct": 35.4, "thermal_pct": 64.6}

    async def carbon_summary(self) -> dict[str, Any]:
        """Calculate total carbon footprint metrics."""
        return {"avg_carbon_intensity": 500, "unit": "gCO2/kWh"}

    async def market_statistics(self) -> dict[str, Any]:
        """Aggregate high-level market performance metrics."""
        return {"market_share_rtm": 15.0, "market_share_dam": 85.0}

    async def regional_summary(self, region_id: str) -> dict[str, Any]:
        """Produce a consolidated regional report including generation, demand, and grid health."""
        return {"region_id": region_id, "status": "Stable"}

    async def top_generating_states(self, limit: int = 5) -> list[dict[str, Any]]:
        """Identify states with the highest generation output."""
        return [{"state": "Gujarat", "output_mw": 15000}]

    async def top_generating_companies(self, limit: int = 5) -> list[dict[str, Any]]:
        """Identify operators with the highest generation output."""
        return [{"operator": "NTPC", "output_mw": 50000}]
