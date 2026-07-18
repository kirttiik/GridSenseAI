"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"

export default function KPICardPage() {
  return (
    <ComponentPlayground
      title="KPI Cards"
      description="Key Performance Indicator display card."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <PlaygroundSection title="Preview">
        <div className="p-4 border rounded-md bg-card text-center text-muted-foreground">
          KPI Cards Preview (See code for implementation details)
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
