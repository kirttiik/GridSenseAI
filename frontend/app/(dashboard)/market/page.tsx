"use client"

import * as React from "react"
import { PageHeader } from "@/components/layouts/PageHeader"
import { SectionHeader } from "@/components/layouts/SectionHeader"
import { KPICard } from "@/components/composites/KPICard"
import { StatisticRow } from "@/components/composites/StatisticRow"
import { LineChart } from "@/components/charts/ChartWrappers"
import { DataTable } from "@/components/composites/DataTable"
import { LineChart as LineChartIcon, Coins, IndianRupee, TrendingUp, Loader2, AlertCircle } from "lucide-react"
import { useMarket } from "@/hooks/useApi"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"

const columns = [
  { accessorKey: "date", header: "Date / Time" },
  { accessorKey: "damAvg", header: "DAM (₹/kWh)" },
  { accessorKey: "rtmAvg", header: "RTM (₹/kWh)" },
  { accessorKey: "volume", header: "Cleared Volume" },
]

export default function MarketPage() {
  const { data: marketResp, isLoading: isMarketLoading, isError: isMarketError } = useMarket()

  if (isMarketLoading) {
    return (
      <div className="flex flex-col items-center justify-center h-96 space-y-4">
        <Loader2 className="h-8 w-8 animate-spin text-primary" />
        <p className="text-muted-foreground">Loading market prices...</p>
      </div>
    )
  }

  if (isMarketError) {
    return (
      <Alert variant="destructive" className="mt-8">
        <AlertCircle className="h-4 w-4" />
        <AlertTitle>Error</AlertTitle>
        <AlertDescription>
          Failed to load market data. Ensure the backend server is running.
        </AlertDescription>
      </Alert>
    )
  }

  const rawData = marketResp?.data || []

  // Pivot data for LineChart (group by timestamp)
  const groupedByTime = rawData.reduce((acc: any, curr: any) => {
    const timeStr = new Date(curr.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    if (!acc[timeStr]) acc[timeStr] = { time: timeStr, DAM: null, RTM: null, dateFull: curr.timestamp }
    if (curr.market_type === 'DAM') {
      acc[timeStr].DAM = curr.price_inr
    } else {
      acc[timeStr].RTM = curr.price_inr
    }
    return acc
  }, {})

  const priceData = Object.values(groupedByTime).slice(0, 10).reverse() as any[]

  // Prepare table data
  const historicalPrices = priceData.map((d: any, idx: number) => ({
    id: idx.toString(),
    date: new Date(d.dateFull).toLocaleString(),
    damAvg: d.DAM?.toFixed(2) || "--",
    rtmAvg: d.RTM?.toFixed(2) || "--",
    volume: "N/A"
  }))

  const latestDam = priceData.length > 0 ? priceData[priceData.length - 1].DAM : 0
  const latestRtm = priceData.length > 0 ? priceData[priceData.length - 1].RTM : 0
  
  const damPeak = priceData.length > 0 ? Math.max(...priceData.map(d => d.DAM || 0)) : 0
  const rtmPeak = priceData.length > 0 ? Math.max(...priceData.map(d => d.RTM || 0)) : 0

  const lastSyncString = rawData.length > 0 ? new Date(rawData[0].timestamp).toLocaleString() : "Never"

  return (
    <div className="flex flex-col gap-8">
      <PageHeader
        title="Market Prices"
        subtitle="Day-Ahead Market (DAM) and Real-Time Market (RTM) analytics"
        lastUpdated={lastSyncString}
      />

      <section>
        <SectionHeader title="Market Summary" />
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mt-4">
          <KPICard
            title="DAM Average Price"
            value={latestDam ? latestDam.toFixed(2) : "0.00"}
            unit="₹/kWh"
            icon={<IndianRupee />}
            trend="neutral"
            trendValue=""
            comparison="Latest"
          />
          <KPICard
            title="RTM Average Price"
            value={latestRtm ? latestRtm.toFixed(2) : "0.00"}
            unit="₹/kWh"
            icon={<TrendingUp />}
            trend="neutral"
            trendValue=""
            comparison="Latest"
            variant="warning"
          />
          <KPICard
            title="Total Cleared Volume"
            value="--"
            unit="MU"
            icon={<Coins />}
            trend="neutral"
            trendValue=""
            comparison="Not available"
            variant="success"
          />
          <KPICard
            title="Market Volatility Index"
            value="Nominal"
            icon={<LineChartIcon />}
            trend="neutral"
            trendValue=""
            comparison="Stable"
            variant="success"
          />
        </div>
      </section>

      <section className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <SectionHeader title="Intraday Price Trend (₹/kWh)" />
          <div className="mt-4 border rounded-xl p-4 bg-card h-80 flex flex-col justify-center">
            {priceData.length > 0 ? (
                <LineChart
                  data={priceData}
                  xAxisKey="time"
                  series={[
                    { key: "DAM", color: "hsl(var(--chart-1))" },
                    { key: "RTM", color: "hsl(var(--chart-5))" }
                  ]}
                />
            ) : (
                <p className="text-center text-muted-foreground">No market price data available.</p>
            )}
          </div>
        </div>
        <div>
          <SectionHeader title="Key Statistics" />
          <div className="mt-4">
             {priceData.length > 0 ? (
                <StatisticRow items={[
                  { label: "DAM Peak Price", value: `₹${damPeak.toFixed(2)}` },
                  { label: "RTM Peak Price", value: `₹${rtmPeak.toFixed(2)}` },
                ]} className="flex-col divide-y sm:divide-y sm:divide-x-0" />
             ) : (
                <div className="p-8 border border-dashed rounded-lg text-center text-muted-foreground">
                    No statistics available.
                </div>
             )}
          </div>
        </div>
      </section>

      <section>
        <SectionHeader title="Recent Prices" />
        <div className="mt-4">
          {historicalPrices.length > 0 ? (
              <DataTable 
                columns={columns} 
                data={historicalPrices} 
                searchKey="date"
              />
          ) : (
              <div className="border border-dashed rounded-lg p-8 text-center text-muted-foreground">
                  No historical data available.
              </div>
          )}
        </div>
      </section>
    </div>
  )
}
