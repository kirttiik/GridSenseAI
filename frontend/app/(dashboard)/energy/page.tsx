"use client"

import * as React from "react"
import { PageHeader } from "@/components/layouts/PageHeader"
import { SectionHeader } from "@/components/layouts/SectionHeader"
import { KPICard } from "@/components/composites/KPICard"
import { AIInsightCard } from "@/components/composites/AIInsightCard"
import { AreaChart, PieChart } from "@/components/charts/ChartWrappers"
import { DataTable } from "@/components/composites/DataTable"
import { Battery, Zap, Wind, Sun, Loader2, AlertCircle } from "lucide-react"
import { useEnergy, useInsights } from "@/hooks/useApi"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { GlobalFilter } from "@/components/analytics/GlobalFilter"
import { AnalyticsFilter, useGenerationMixAnalytics } from "@/hooks/useAnalytics"

const columns = [
  { accessorKey: "region", header: "Region" },
  { accessorKey: "total", header: "Total Gen (MW)" },
  { accessorKey: "renewable", header: "Renewable (MW)" },
  { accessorKey: "status", header: "Status" },
]

export default function EnergyPage() {
  const [filters, setFilters] = React.useState<AnalyticsFilter>({ resolution: "daily" })
  const { data: energyResp, isLoading: isEnergyLoading, isError: isEnergyError } = useEnergy()
  const { data: insightsResp, isLoading: isInsightsLoading } = useInsights()
  const { data: mixResp, isLoading: isMixLoading } = useGenerationMixAnalytics(filters)

  if (isEnergyLoading || isInsightsLoading || isMixLoading) {
    return (
      <div className="flex flex-col items-center justify-center h-96 space-y-4">
        <Loader2 className="h-8 w-8 animate-spin text-primary" />
        <p className="text-muted-foreground">Loading energy data...</p>
      </div>
    )
  }

  if (isEnergyError) {
    return (
      <Alert variant="destructive" className="mt-8">
        <AlertCircle className="h-4 w-4" />
        <AlertTitle>Error</AlertTitle>
        <AlertDescription>
          Failed to load energy data. Ensure the backend server is running.
        </AlertDescription>
      </Alert>
    )
  }

  const rawData = energyResp?.data || []
  const mixData = mixResp?.data || []
  
  // Pivot data for AreaChart (group by timestamp) - keeping historical logic for Area chart
  const groupedByTime = rawData.reduce((acc: any, curr: any) => {
    const timeStr = new Date(curr.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    if (!acc[timeStr]) acc[timeStr] = { time: timeStr, Solar: 0, Wind: 0, Thermal: 0, Hydro: 0 }
    acc[timeStr][curr.source_type] = (acc[timeStr][curr.source_type] || 0) + curr.value_mw
    return acc
  }, {})

  const generationData = Object.values(groupedByTime).slice(0, 10).reverse() as Record<string, any>[]

  // Use real analytics for pie chart
  const renewableMix = mixData.map((d: any, i: number) => ({
    name: d.source_type,
    value: d.value_mw,
    fill: `hsl(var(--chart-${(i % 5) + 1}))`
  }))

  // Pivot for Table (group by region)
  const regionTotals = rawData.reduce((acc: any, curr: any) => {
    if (!acc[curr.region]) acc[curr.region] = { id: curr.region, region: curr.region, total: 0, renewable: 0, status: 'Optimal' }
    acc[curr.region].total += curr.value_mw
    if (curr.source_type === 'Solar' || curr.source_type === 'Wind' || curr.source_type === 'Hydro') {
      acc[curr.region].renewable += curr.value_mw
    }
    return acc
  }, {})

  const regionalData = Object.values(regionTotals)

  const insightsData = insightsResp?.data || []

  // Aggregate KPIs from real analytics
  const totalGen = mixResp?.total_mw || Object.values(regionTotals).reduce((a: any, curr: any) => a + curr.total, 0)
  const totalRenewable = renewableMix.filter((r: any) => ['Solar', 'Wind', 'Hydro'].includes(r.name)).reduce((a: any, b: any) => a + b.value, 0)
  const solarGen = mixData.find((d: any) => d.source_type === 'Solar')?.value_mw || 0
  const windGen = mixData.find((d: any) => d.source_type === 'Wind')?.value_mw || 0

  const lastSyncString = rawData.length > 0 ? new Date(rawData[0].timestamp).toLocaleString() : "Never"

  return (
    <div className="flex flex-col gap-8">
      <PageHeader
        title="Energy Generation"
        subtitle="Detailed breakdown of power generation by source"
        lastUpdated={lastSyncString}
      />
      
      <GlobalFilter onFilterChange={setFilters} initialFilters={filters} />
      
      <section>
        <SectionHeader title="Generation KPIs" />
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mt-4">
          <KPICard
            title="Total Generation"
            value={totalGen.toFixed(1)}
            unit="MW"
            icon={<Zap />}
            trend="up"
            trendValue=""
            comparison="total from db"
          />
          <KPICard
            title="Renewable Total"
            value={totalRenewable.toFixed(1)}
            unit="MW"
            icon={<Battery />}
            trend="up"
            trendValue=""
            comparison="Solar/Wind/Hydro"
            variant="success"
          />
          <KPICard
            title="Solar Output"
            value={solarGen.toFixed(1)}
            unit="MW"
            icon={<Sun />}
            trend="up"
            trendValue=""
            comparison=""
            variant="success"
          />
          <KPICard
            title="Wind Output"
            value={windGen.toFixed(1)}
            unit="MW"
            icon={<Wind />}
            trend="neutral"
            trendValue=""
            comparison=""
            variant="warning"
          />
        </div>
      </section>

      <section className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <SectionHeader title="Generation Trend by Source" />
          <div className="mt-4 border rounded-xl p-4 bg-card h-80 flex flex-col justify-center">
            {generationData.length > 0 ? (
                <AreaChart
                  data={generationData}
                  xAxisKey="time"
                  series={[
                    { key: "Solar", color: "hsl(var(--chart-1))" },
                    { key: "Wind", color: "hsl(var(--chart-2))" },
                    { key: "Thermal", color: "hsl(var(--chart-4))" },
                    { key: "Hydro", color: "hsl(var(--chart-3))" }
                  ]}
                  stacked={true}
                />
            ) : (
                <p className="text-center text-muted-foreground">No generation data available.</p>
            )}
          </div>
        </div>
        <div>
          <SectionHeader title="Generation Mix" />
          <div className="mt-4 border rounded-xl p-4 bg-card h-80 flex flex-col justify-center">
            {renewableMix.length > 0 ? (
                <PieChart
                  data={renewableMix}
                  dataKey="value"
                  nameKey="name"
                  donut={true}
                />
            ) : (
                <p className="text-center text-muted-foreground">No mix data available.</p>
            )}
          </div>
        </div>
      </section>

      <section className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <SectionHeader title="Regional Generation" />
          <div className="mt-4">
             {regionalData.length > 0 ? (
                <DataTable 
                  columns={columns} 
                  data={regionalData} 
                  searchKey="region"
                />
             ) : (
                <div className="border border-dashed rounded-lg p-8 text-center text-muted-foreground">
                    No regional data available.
                </div>
             )}
          </div>
        </div>
        <div>
          <SectionHeader title="AI Recommendations" />
          <div className="mt-4 space-y-4">
            {insightsData.length > 0 ? (
                insightsData.slice(0, 2).map((insight: any, idx: number) => (
                    <AIInsightCard
                        key={idx}
                        title={insight.title}
                        summary={insight.summary}
                        severity={insight.severity as any || "info"}
                        confidence={insight.confidence}
                        recommendation={insight.recommendation || ""}
                        timestamp={new Date(insight.timestamp).toLocaleTimeString()}
                    />
                ))
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
