"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection } from "@/components/design-system/playground/ComponentPlayground"

function ElevationSwatch({ name, className }: { name: string, className: string }) {
  return (
    <div className="flex items-center space-x-4 mb-4 border-b pb-4">
      <div className={`w-16 h-16 bg-card border flex items-center justify-center ${className}`}>
        <div className="w-8 h-8 bg-muted rounded-sm" />
      </div>
      <div>
        <p className="font-semibold">{name}</p>
        <p className="text-sm text-muted-foreground font-mono">{className}</p>
      </div>
    </div>
  )
}

export default function ElevationPage() {
  return (
    <ComponentPlayground
      title="Elevation"
      description="Design tokens for shadows and depth."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AAA",
        productionReady: true,
      }}
    >
      <PlaygroundSection title="Elevation Scale">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <ElevationSwatch name="Small Shadow" className="shadow-sm" />
          <ElevationSwatch name="Default Shadow" className="shadow" />
          <ElevationSwatch name="Medium Shadow" className="shadow-md" />
          <ElevationSwatch name="Large Shadow" className="shadow-lg" />
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
