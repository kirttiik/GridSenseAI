"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection } from "@/components/design-system/playground/ComponentPlayground"

function RadiusSwatch({ name, value, className }: { name: string, value: string, className: string }) {
  return (
    <div className="flex items-center space-x-4 mb-4 border-b pb-4">
      <div className={`w-16 h-16 bg-primary/10 border border-primary/20 ${className}`} />
      <div>
        <p className="font-semibold">{name}</p>
        <p className="text-sm text-muted-foreground font-mono">{value}</p>
      </div>
    </div>
  )
}

export default function RadiusPage() {
  return (
    <ComponentPlayground
      title="Radius"
      description="Design tokens for border radiuses."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AAA",
        productionReady: true,
      }}
    >
      <PlaygroundSection title="Radius Scale">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <RadiusSwatch name="Small (sm)" value="calc(var(--radius) - 4px)" className="rounded-sm" />
          <RadiusSwatch name="Medium (md)" value="calc(var(--radius) - 2px)" className="rounded-md" />
          <RadiusSwatch name="Base" value="var(--radius)" className="rounded-lg" />
          <RadiusSwatch name="Large (lg)" value="calc(var(--radius) + 2px)" className="rounded-xl" />
          <RadiusSwatch name="Full" value="9999px" className="rounded-full" />
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
