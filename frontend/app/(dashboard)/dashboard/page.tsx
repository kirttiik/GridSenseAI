"use client"

import * as React from "react"
import { PageHeader } from "@/components/layouts/PageHeader"
import { SectionHeader } from "@/components/layouts/SectionHeader"
import { KPICard } from "@/components/composites/KPICard"
import { AIInsightCard } from "@/components/composites/AIInsightCard"
import { BarChart, LineChart } from "@/components/charts/ChartWrappers"
import { Battery, Cloud, Zap, Activity, AlertCircle, Loader2 } from "lucide-react"
import { useDashboard, useEnergy, useMarket, useWeather, useInsights } from "@/hooks/useApi"
import { GlobalFilter } from "@/components/analytics/GlobalFilter"
import { AnalyticsFilter, useGenerationMixAnalytics, useMarketTrendsAnalytics } from "@/hooks/useAnalytics"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
export default function DashboardPage() {
  const [filters, setFilters] = React.useState<AnalyticsFilter>({ resolution: "daily" })
  const { data: dashboardResp, isLoading: isDashboardLoading, isError: isDashboardError } = useDashboard()
  
  // Analytics queries
  const { data: mixResp, isLoading: isMixLoading } = useGenerationMixAnalytics(filters)
  const { data: trendResp, isLoading: isTrendLoading } = useMarketTrendsAnalytics(filters)

  const { data: energyResp, isLoading: isEnergyLoading } = useEnergy()
  const { data: marketResp, isLoading: isMarketLoading } = useMarket()
  const { data: weatherResp, isLoading: isWeatherLoading } = useWeather()
  const { data: insightsResp, isLoading: isInsightsLoading } = useInsights()

  if (isDashboardLoading) {
    return (
      <div className="flex flex-col items-center justify-center h-96 space-y-4">
        <Loader2 className="h-8 w-8 animate-spin text-primary" />
        <p className="text-muted-foreground">Loading dashboard data...</p>
      </div>
    )
  }

  if (isDashboardError) {
    return (
      <Alert variant="destructive" className="mt-8">
        <AlertCircle className="h-4 w-4" />
        <AlertTitle>Error</AlertTitle>
        <AlertDescription>
          Failed to load dashboard data. Ensure the backend server is running and the database is reachable.
        </AlertDescription>
      </Alert>
    )
  }

  const overview = dashboardResp?.data
  
  // Transform Analytics data for charts
  const mixDataList = mixResp?.data || []
  const generationData = mixDataList.map((d: any) => ({
        name: d.source_type,
        value: d.value_mw
      }))

  const trendDataList = trendResp?.data || []
  const marketData = trendDataList.map((d: any) => ({
        name: new Date(d.timestamp).toLocaleDateString(),
        value: d.avg_price_inr
      }))

  const latestWeather = weatherResp?.data?.[0] || null
  const latestInsight = insightsResp?.data?.[0] || null

  const lastSyncString = overview?.last_sync_time 
    ? new Date(overview.last_sync_time).toLocaleString()
    : "Never"

  return (
    <div className="flex flex-col gap-8">
      <PageHeader
        title="Home Dashboard"
        subtitle="Overview of GridSense AI Operations"
        lastUpdated={lastSyncString}
      />
      
      <GlobalFilter onFilterChange={setFilters} initialFilters={filters} />

      <section>
        <SectionHeader title="Grid Overview" description="Key performance indicators across the grid." />
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mt-4">
          <KPICard
            title="Total Generation Records"
            value={overview?.total_energy_records?.toString() || "0"}
            unit="Rows"
            icon={<Zap />}
            trend="up"
            trendValue="+1"
            comparison="total in database"
          />
          <KPICard
            title="Latest Energy Value"
            value={overview?.latest_energy_info?.value_mw?.toString() || "0"}
            unit="MW"
            icon={<Battery />}
            trend="neutral"
            trendValue=""
            comparison={overview?.latest_energy_info?.source_type || "N/A"}
            variant="success"
          />
          <KPICard
            title="Latest Market Price"
            value={overview?.latest_market_info?.price_inr?.toString() || "0"}
            unit="INR"
            icon={<Activity />}
            trend="neutral"
            trendValue=""
            comparison={overview?.latest_market_info?.market_type || "N/A"}
          />
          <KPICard
            title="Grid Frequency"
            value={overview?.latest_grid_status?.frequency_hz?.toString() || "0"}
            unit="Hz"
            icon={<Activity />}
            trend={overview?.latest_grid_status?.frequency_hz >= 50.0 ? "up" : "down"}
            trendValue=""
            comparison="Target: 50.00 Hz"
            variant={overview?.latest_grid_status?.frequency_hz >= 49.9 && overview?.latest_grid_status?.frequency_hz <= 50.1 ? "success" : "warning"}
          />
        </div>
      </section>

      <section className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div>
          <SectionHeader title="Generation Trend" />
          <div className="mt-4 border rounded-xl p-4 bg-card h-80 flex flex-col justify-center">
            {generationData.length > 0 ? (
              <LineChart
                data={generationData}
                xAxisKey="name"
                series={[{ key: "value", name: "Generation (MW)", color: "hsl(var(--primary))" }]}
              />
            ) : (
              <p className="text-center text-muted-foreground">No generation data available.</p>
            )}
          </div>
        </div>
        <div>
          <SectionHeader title="Market Price Trend" />
          <div className="mt-4 border rounded-xl p-4 bg-card h-80 flex flex-col justify-center">
             {marketData.length > 0 ? (
                <BarChart
                  data={marketData}
                  xAxisKey="name"
                  series={[{ key: "value", name: "Price (INR)", color: "hsl(var(--chart-2))" }]}
                />
             ) : (
                <p className="text-center text-muted-foreground">No market data available.</p>
             )}
          </div>
        </div>
      </section>

      <section className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <SectionHeader title="Weather Summary" />
          <div className="grid grid-cols-2 gap-4 mt-4">
            <KPICard title="Temperature" value={latestWeather?.temperature_c?.toString() || "--"} unit="°C" icon={<Cloud />} />
            <KPICard title="Solar Irradiance" value={latestWeather?.solar_irradiance_wm2?.toString() || "--"} unit="W/m²" icon={<Cloud />} />
            <KPICard title="Wind Speed" value={latestWeather?.wind_speed_ms?.toString() || "--"} unit="m/s" icon={<Cloud />} />
            <KPICard title="Humidity" value={latestWeather?.humidity_pct?.toString() || "--"} unit="%" icon={<Cloud />} />
          </div>
        </div>
        <div>
          <SectionHeader title="Latest AI Insight" />
          <div className="mt-4">
            {latestInsight ? (
                <AIInsightCard
                  title={latestInsight.title}
                  summary={latestInsight.summary}
                  severity={latestInsight.severity as any || "info"}
                  confidence={latestInsight.confidence}
                  recommendation={latestInsight.recommendation || ""}
                  timestamp={new Date(latestInsight.timestamp).toLocaleTimeString()}
                />
            ) : (
                <div className="border border-dashed rounded-lg p-8 text-center text-muted-foreground">
                    No AI insights currently available.
                </div>
            )}
          </div>
        </div>
      </section>
    </div>
  )
}
