"use client"

import * as React from "react"
import { PageHeader } from "@/components/layouts/PageHeader"
import { SectionHeader } from "@/components/layouts/SectionHeader"
import { MapContainer } from "@/components/shared/MapContainer"
import { FilterBar } from "@/components/forms/FilterBar"
import { Map as MapIcon, Zap, Battery, AlertTriangle } from "lucide-react"

export default function GISPage() {
  const [isLoading, setIsLoading] = React.useState(true)

  React.useEffect(() => {
    // Simulate loading map data
    const timer = setTimeout(() => {
      setIsLoading(false)
    }, 1500)
    return () => clearTimeout(timer)
  }, [])

  return (
    <div className="flex flex-col gap-6 h-[calc(100vh-6rem)]">
      <div className="flex-none">
        <PageHeader
          title="GIS Dashboard"
          subtitle="Geospatial visualization of Grid Infrastructure"
          lastUpdated="Just now"
          actions={
            <div className="flex items-center gap-4 text-sm text-muted-foreground bg-card px-4 py-2 rounded-md border">
              <span className="flex items-center gap-1"><Zap className="h-4 w-4 text-primary" /> Power Plants</span>
              <span className="flex items-center gap-1"><Battery className="h-4 w-4 text-success" /> Renewables</span>
              <span className="flex items-center gap-1"><AlertTriangle className="h-4 w-4 text-destructive" /> Outages</span>
            </div>
          }
        />
        
        <div className="mt-4">
          <FilterBar
            searchPlaceholder="Search locations, plants, or substations..."
          />
        </div>
      </div>

      <div className="flex-1 min-h-[500px]">
        <MapContainer 
          isLoading={isLoading} 
          className="h-full w-full rounded-xl border"
        >
           {!isLoading && (
              <div className="absolute top-4 left-4 p-4 bg-background/90 backdrop-blur-sm border rounded-lg shadow-sm z-10 w-64">
                <h3 className="font-semibold mb-2 flex items-center gap-2">
                  <MapIcon className="h-4 w-4" /> Map Layers
                </h3>
                <div className="space-y-2 text-sm">
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input type="checkbox" defaultChecked className="rounded border-input" />
                    <span>Transmission Lines (400kV+)</span>
                  </label>
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input type="checkbox" defaultChecked className="rounded border-input" />
                    <span>Substations</span>
                  </label>
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input type="checkbox" defaultChecked className="rounded border-input" />
                    <span>Thermal Power Plants</span>
                  </label>
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input type="checkbox" defaultChecked className="rounded border-input" />
                    <span>Solar Parks</span>
                  </label>
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input type="checkbox" defaultChecked className="rounded border-input" />
                    <span>Wind Farms</span>
                  </label>
                </div>
              </div>
           )}
        </MapContainer>
      </div>
    </div>
  )
}
