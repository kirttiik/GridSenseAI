"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection } from "@/components/design-system/playground/ComponentPlayground"

function ColorSwatch({ name, variable, value }: { name: string, variable: string, value: string }) {
  return (
    <div className="flex items-center space-x-4 mb-4">
      <div 
        className="w-16 h-16 rounded-md shadow-sm border" 
        style={{ backgroundColor: `hsl(var(${variable}))` }}
      />
      <div>
        <p className="font-semibold">{name}</p>
        <p className="text-sm text-muted-foreground font-mono">{variable}</p>
      </div>
    </div>
  )
}

export default function ColorsPage() {
  return (
    <ComponentPlayground
      title="Colors"
      description="Design tokens for the GridSense AI color palette."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AAA",
        productionReady: true,
      }}
    >
      <PlaygroundSection title="Primary Theme Colors">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <ColorSwatch name="Background" variable="--background" value="hsl(0 0% 100%)" />
          <ColorSwatch name="Foreground" variable="--foreground" value="hsl(222.2 47.4% 11.2%)" />
          <ColorSwatch name="Primary" variable="--primary" value="hsl(221.2 83.2% 53.3%)" />
          <ColorSwatch name="Primary Foreground" variable="--primary-foreground" value="hsl(210 40% 98%)" />
          <ColorSwatch name="Secondary" variable="--secondary" value="hsl(210 40% 96.1%)" />
          <ColorSwatch name="Secondary Foreground" variable="--secondary-foreground" value="hsl(222.2 47.4% 11.2%)" />
        </div>
      </PlaygroundSection>

      <PlaygroundSection title="Feedback & State">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <ColorSwatch name="Destructive" variable="--destructive" value="hsl(0 100% 50%)" />
          <ColorSwatch name="Destructive Foreground" variable="--destructive-foreground" value="hsl(210 40% 98%)" />
          <ColorSwatch name="Muted" variable="--muted" value="hsl(210 40% 96.1%)" />
          <ColorSwatch name="Muted Foreground" variable="--muted-foreground" value="hsl(215.4 16.3% 46.9%)" />
          <ColorSwatch name="Accent" variable="--accent" value="hsl(210 40% 96.1%)" />
          <ColorSwatch name="Accent Foreground" variable="--accent-foreground" value="hsl(222.2 47.4% 11.2%)" />
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
