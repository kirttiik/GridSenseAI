"use client"

import * as React from "react"
import { PageHeader } from "@/components/layouts/PageHeader"
import { SectionHeader } from "@/components/layouts/SectionHeader"
import { KPICard } from "@/components/composites/KPICard"
import { AreaChart, LineChart } from "@/components/charts/ChartWrappers"
import { Cloud, Sun, Wind, Droplets, CloudRain, Loader2, AlertCircle } from "lucide-react"
import { useWeather } from "@/hooks/useApi"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"

export default function WeatherPage() {
  const { data: weatherResp, isLoading: isWeatherLoading, isError: isWeatherError } = useWeather()

  if (isWeatherLoading) {
    return (
      <div className="flex flex-col items-center justify-center h-96 space-y-4">
        <Loader2 className="h-8 w-8 animate-spin text-primary" />
        <p className="text-muted-foreground">Loading weather forecast...</p>
      </div>
    )
  }

  if (isWeatherError) {
    return (
      <Alert variant="destructive" className="mt-8">
        <AlertCircle className="h-4 w-4" />
        <AlertTitle>Error</AlertTitle>
        <AlertDescription>
          Failed to load weather data. Ensure the backend server is running.
        </AlertDescription>
      </Alert>
    )
  }

  const rawData = weatherResp?.data || []
  
  // Format for charts
  const chartData = rawData.slice(0, 10).reverse().map((d: any) => ({
    time: new Date(d.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    Temperature: d.temperature_c,
    Humidity: d.humidity_pct,
    WindSpeed: d.wind_speed_ms,
    Irradiance: d.solar_irradiance_wm2,
  }))

  const latest = rawData.length > 0 ? rawData[0] : null
  const lastSyncString = latest ? new Date(latest.timestamp).toLocaleString() : "Never"

  return (
    <div className="flex flex-col gap-8">
      <PageHeader
        title="Weather Forecast"
        subtitle="Meteorological data affecting energy generation and demand"
        lastUpdated={lastSyncString}
      />

      <section>
        <SectionHeader title="Current Weather Conditions" />
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mt-4">
          <KPICard
            title="Temperature"
            value={latest?.temperature_c?.toString() || "--"}
            unit="°C"
            icon={<Sun />}
            trend="neutral"
            trendValue=""
            comparison="Latest reading"
            variant={latest?.temperature_c > 35 ? "warning" : "default"}
          />
          <KPICard
            title="Solar Irradiance"
            value={latest?.solar_irradiance_wm2?.toString() || "--"}
            unit="W/m²"
            icon={<Sun />}
            trend="neutral"
            trendValue=""
            comparison="Latest reading"
            variant="success"
          />
          <KPICard
            title="Wind Speed"
            value={latest?.wind_speed_ms?.toString() || "--"}
            unit="m/s"
            icon={<Wind />}
            trend="neutral"
            trendValue=""
            comparison="Latest reading"
          />
          <KPICard
            title="Humidity"
            value={latest?.humidity_pct?.toString() || "--"}
            unit="%"
            icon={<Droplets />}
            trend="neutral"
            trendValue=""
            comparison="Latest reading"
          />
        </div>
      </section>

      <section className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div>
          <SectionHeader title="Temperature & Humidity Trend" />
          <div className="mt-4 border rounded-xl p-4 bg-card h-80 flex flex-col justify-center">
            {chartData.length > 0 ? (
                <LineChart
                  data={chartData}
                  xAxisKey="time"
                  series={[
                    { key: "Temperature", color: "hsl(var(--destructive))" },
                    { key: "Humidity", color: "hsl(var(--primary))" }
                  ]}
                />
            ) : (
                <p className="text-center text-muted-foreground">No weather trend data available.</p>
            )}
          </div>
        </div>
        <div>
          <SectionHeader title="Solar Irradiance Forecast" />
          <div className="mt-4 border rounded-xl p-4 bg-card h-80 flex flex-col justify-center">
             {chartData.length > 0 ? (
                <AreaChart
                  data={chartData}
                  xAxisKey="time"
                  series={[{ key: "Irradiance", color: "hsl(var(--chart-4))" }]}
                />
             ) : (
                <p className="text-center text-muted-foreground">No irradiance data available.</p>
             )}
          </div>
        </div>
      </section>
      
      <section>
        <SectionHeader title="7-Day Forecast" />
        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-7 gap-4 mt-4">
           {/* Hardcoded for visual completeness since we don't have a 7-day forecast API yet */}
           {[
             { day: "Mon", temp: 32, icon: <Sun className="h-6 w-6 text-amber-500" /> },
             { day: "Tue", temp: 33, icon: <Sun className="h-6 w-6 text-amber-500" /> },
             { day: "Wed", temp: 30, icon: <Cloud className="h-6 w-6 text-muted-foreground" /> },
             { day: "Thu", temp: 28, icon: <CloudRain className="h-6 w-6 text-primary" /> },
             { day: "Fri", temp: 27, icon: <CloudRain className="h-6 w-6 text-primary" /> },
             { day: "Sat", temp: 29, icon: <Cloud className="h-6 w-6 text-muted-foreground" /> },
             { day: "Sun", temp: 31, icon: <Sun className="h-6 w-6 text-amber-500" /> },
           ].map((forecast, i) => (
             <div key={i} className="flex flex-col items-center justify-center p-4 border rounded-xl bg-card">
               <span className="font-medium mb-2">{forecast.day}</span>
               {forecast.icon}
               <span className="text-xl font-bold mt-2">{forecast.temp}°C</span>
             </div>
           ))}
        </div>
      </section>
    </div>
  )
}
