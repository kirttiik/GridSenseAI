"use client"

import * as React from "react"
import { PageHeader } from "@/components/layouts/PageHeader"
import { SectionHeader } from "@/components/layouts/SectionHeader"
import { KPICard } from "@/components/composites/KPICard"
import { AreaChart } from "@/components/charts/ChartWrappers"
import { DataTable } from "@/components/composites/DataTable"
import { StatusBadge } from "@/components/primitives/StatusBadge"
import { Activity, Zap, ShieldAlert, AlertTriangle, Loader2, AlertCircle } from "lucide-react"
import { useGrid, useEnergy } from "@/hooks/useApi"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"

const columns = [
  { accessorKey: "region", header: "Region" },
  { accessorKey: "frequency", header: "Frequency (Hz)" },
  { accessorKey: "voltage", header: "Voltage (kV)" },
  { accessorKey: "stability", header: "Stability Index" },
  { 
    accessorKey: "status", 
    header: "Status",
    cell: ({ row }: any) => {
      const status = row.getValue("status") as any;
      return <StatusBadge status={status} />;
    }
  },
]

export default function GridPage() {
  const { data: gridResp, isLoading: isGridLoading, isError: isGridError } = useGrid()
  const { data: energyResp, isLoading: isEnergyLoading } = useEnergy()

  if (isGridLoading || isEnergyLoading) {
    return (
      <div className="flex flex-col items-center justify-center h-96 space-y-4">
        <Loader2 className="h-8 w-8 animate-spin text-primary" />
        <p className="text-muted-foreground">Loading grid status...</p>
      </div>
    )
  }

  if (isGridError) {
    return (
      <Alert variant="destructive" className="mt-8">
        <AlertCircle className="h-4 w-4" />
        <AlertTitle>Error</AlertTitle>
        <AlertDescription>
          Failed to load grid data. Ensure the backend server is running.
        </AlertDescription>
      </Alert>
    )
  }

  const gridRaw = gridResp?.data || []
  const energyRaw = energyResp?.data || []

  // Regional latest grid status
  const latestByRegion = gridRaw.reduce((acc: any, curr: any) => {
    // Since it's ordered by desc, the first time we see a region, it's the latest
    if (!acc[curr.region]) {
      let status = "healthy"
      if (curr.frequency_hz < 49.9 || curr.frequency_hz > 50.1) status = "warning"
      if (curr.frequency_hz < 49.8 || curr.frequency_hz > 50.2) status = "danger"

      acc[curr.region] = {
        id: curr.id,
        region: curr.region,
        frequency: curr.frequency_hz.toFixed(2),
        voltage: curr.voltage_kv ? curr.voltage_kv.toFixed(1) : "--",
        stability: curr.stability_index.toFixed(2),
        status: status
      }
    }
    return acc
  }, {})

  const gridStatusData = Object.values(latestByRegion)

  // Demand vs Supply
  const groupedEnergy = energyRaw.reduce((acc: any, curr: any) => {
    const timeStr = new Date(curr.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    if (!acc[timeStr]) acc[timeStr] = { time: timeStr, Demand: 0, Supply: 0 }
    
    if (curr.source_type === 'Demand') {
      acc[timeStr].Demand += curr.value_mw
    } else {
      acc[timeStr].Supply += curr.value_mw
    }
    return acc
  }, {})

  const demandSupplyData = Object.values(groupedEnergy).slice(0, 10).reverse() as Record<string, any>[]

  const overallAvgFreq = gridStatusData.length > 0 
    ? (gridStatusData.reduce((acc: number, curr: any) => acc + parseFloat(curr.frequency), 0) / gridStatusData.length).toFixed(2)
    : "50.00"

  const peakDemand = demandSupplyData.length > 0
    ? Math.max(...demandSupplyData.map((d: any) => d.Demand))
    : 0

  const avgStability = gridStatusData.length > 0
    ? (gridStatusData.reduce((acc: number, curr: any) => acc + parseFloat(curr.stability), 0) / gridStatusData.length).toFixed(1)
    : "100.0"

  const lastSyncString = gridRaw.length > 0 ? new Date(gridRaw[0].timestamp).toLocaleString() : "Never"

  return (
    <div className="flex flex-col gap-8">
      <PageHeader
        title="Grid Status"
        subtitle="Real-time monitoring of grid frequency, demand, and transmission lines"
        lastUpdated={lastSyncString}
      />

      <section>
        <SectionHeader title="Grid Health KPIs" />
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mt-4">
          <KPICard
            title="Avg Grid Frequency"
            value={overallAvgFreq.toString()}
            unit="Hz"
            icon={<Activity />}
            trend="neutral"
            trendValue=""
            comparison="Target: 50.00 Hz"
          />
          <KPICard
            title="Peak Demand (Recent)"
            value={peakDemand.toFixed(1)}
            unit="MW"
            icon={<Zap />}
            trend="neutral"
            trendValue=""
            comparison=""
            variant="warning"
          />
          <KPICard
            title="Active Outages"
            value="0"
            unit="lines"
            icon={<AlertTriangle />}
            trend="neutral"
            trendValue=""
            comparison="Mock value"
            variant="success"
          />
          <KPICard
            title="Avg Stability Index"
            value={avgStability.toString()}
            unit="%"
            icon={<ShieldAlert />}
            trend="neutral"
            trendValue=""
            comparison=""
            variant="success"
          />
        </div>
      </section>

      <section className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <SectionHeader title="Demand vs Supply" />
          <div className="mt-4 border rounded-xl p-4 bg-card h-80 flex flex-col justify-center">
            {demandSupplyData.length > 0 ? (
                <AreaChart
                  data={demandSupplyData}
                  xAxisKey="time"
                  series={[
                    { key: "Demand", color: "hsl(var(--destructive))" },
                    { key: "Supply", color: "hsl(var(--primary))" }
                  ]}
                />
            ) : (
                <p className="text-center text-muted-foreground">No demand/supply data available.</p>
            )}
          </div>
        </div>
        <div>
          <SectionHeader title="Transmission Constraints" />
          <div className="mt-4 flex flex-col gap-4">
             <div className="p-8 border border-dashed rounded-lg text-center text-muted-foreground">
                No active transmission constraints detected.
             </div>
          </div>
        </div>
      </section>

      <section>
        <SectionHeader title="Regional Grid Status" />
        <div className="mt-4">
          {gridStatusData.length > 0 ? (
              <DataTable 
                columns={columns} 
                data={gridStatusData} 
                searchKey="region"
              />
          ) : (
              <div className="border border-dashed rounded-lg p-8 text-center text-muted-foreground">
                  No regional grid data available.
              </div>
          )}
        </div>
      </section>
    </div>
  )
}
