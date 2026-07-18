"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"

export default function SearchBarPage() {
  return (
    <ComponentPlayground
      title="Search Bar"
      description="Input for searching with clear button."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <PlaygroundSection title="Preview">
        <div className="p-4 border rounded-md bg-card text-center text-muted-foreground">
          Search Bar Preview (See code for implementation details)
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
