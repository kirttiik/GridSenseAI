"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection } from "@/components/design-system/playground/ComponentPlayground"

function MotionSwatch({ name, className, label }: { name: string, className: string, label: string }) {
  const [hovered, setHovered] = React.useState(false)
  return (
    <div className="flex items-center space-x-4 mb-4 border-b pb-4">
      <div 
        className={`w-16 h-16 bg-primary/20 border border-primary flex items-center justify-center cursor-pointer ${className}`}
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
        style={{ transform: hovered ? "scale(1.1)" : "scale(1)" }}
      >
        <span className="text-xs text-primary font-bold">Hover</span>
      </div>
      <div>
        <p className="font-semibold">{name}</p>
        <p className="text-sm text-muted-foreground font-mono">{label}</p>
      </div>
    </div>
  )
}

export default function MotionPage() {
  return (
    <ComponentPlayground
      title="Motion"
      description="Design tokens for transitions and animations."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AAA",
        productionReady: true,
      }}
    >
      <PlaygroundSection title="Transition Scale">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <MotionSwatch name="Fast Transition" label="transition-all duration-150" className="transition-all duration-150 ease-in-out" />
          <MotionSwatch name="Normal Transition" label="transition-all duration-300" className="transition-all duration-300 ease-in-out" />
          <MotionSwatch name="Slow Transition" label="transition-all duration-500" className="transition-all duration-500 ease-in-out" />
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
