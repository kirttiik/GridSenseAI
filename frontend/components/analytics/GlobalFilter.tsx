"use client";

import React, { useState } from 'react';
import { AnalyticsFilter } from '@/hooks/useAnalytics';

interface GlobalFilterProps {
  onFilterChange: (filters: AnalyticsFilter) => void;
  initialFilters?: AnalyticsFilter;
}

export function GlobalFilter({ onFilterChange, initialFilters = {} }: GlobalFilterProps) {
  const [filters, setFilters] = useState<AnalyticsFilter>({
    resolution: "daily",
    ...initialFilters
  });

  const handleChange = (e: React.ChangeEvent<HTMLSelectElement | HTMLInputElement>) => {
    const { name, value } = e.target;
    const newFilters = { ...filters, [name]: value || null };
    setFilters(newFilters);
    onFilterChange(newFilters);
  };

  return (
    <div className="flex flex-wrap gap-4 p-4 bg-[var(--surface-color)] rounded-xl border border-[var(--border-color)] mb-6 shadow-sm items-center">
      <div className="text-sm font-semibold text-[var(--text-secondary)] mr-2 uppercase tracking-wider">
        Global Filters
      </div>
      
      <div className="flex flex-col">
        <label className="text-xs text-[var(--text-secondary)] mb-1">Region</label>
        <select 
          name="region" 
          value={filters.region || ""} 
          onChange={handleChange}
          className="bg-[var(--background-color)] border border-[var(--border-color)] rounded-lg px-3 py-1.5 text-sm outline-none focus:border-[var(--primary-color)] transition-colors"
        >
          <option value="">All Regions</option>
          <option value="NORTH">North</option>
          <option value="SOUTH">South</option>
          <option value="EAST">East</option>
          <option value="WEST">West</option>
          <option value="NORTHEAST">North-East</option>
        </select>
      </div>

      <div className="flex flex-col">
        <label className="text-xs text-[var(--text-secondary)] mb-1">Resolution</label>
        <select 
          name="resolution" 
          value={filters.resolution || "daily"} 
          onChange={handleChange}
          className="bg-[var(--background-color)] border border-[var(--border-color)] rounded-lg px-3 py-1.5 text-sm outline-none focus:border-[var(--primary-color)] transition-colors"
        >
          <option value="hourly">Hourly</option>
          <option value="daily">Daily</option>
          <option value="monthly">Monthly</option>
        </select>
      </div>
      
      <div className="flex flex-col">
        <label className="text-xs text-[var(--text-secondary)] mb-1">Fuel Type (Optional)</label>
        <select 
          name="fuel" 
          value={filters.fuel || ""} 
          onChange={handleChange}
          className="bg-[var(--background-color)] border border-[var(--border-color)] rounded-lg px-3 py-1.5 text-sm outline-none focus:border-[var(--primary-color)] transition-colors"
        >
          <option value="">All Sources</option>
          <option value="Solar">Solar</option>
          <option value="Wind">Wind</option>
          <option value="Thermal">Thermal</option>
          <option value="Hydro">Hydro</option>
          <option value="Nuclear">Nuclear</option>
        </select>
      </div>
      
      <div className="flex flex-col">
        <label className="text-xs text-[var(--text-secondary)] mb-1">Market Type</label>
        <select 
          name="market_type" 
          value={filters.market_type || ""} 
          onChange={handleChange}
          className="bg-[var(--background-color)] border border-[var(--border-color)] rounded-lg px-3 py-1.5 text-sm outline-none focus:border-[var(--primary-color)] transition-colors"
        >
          <option value="">All Markets</option>
          <option value="DAM">Day Ahead (DAM)</option>
          <option value="RTM">Real Time (RTM)</option>
        </select>
      </div>
      
    </div>
  );
}
