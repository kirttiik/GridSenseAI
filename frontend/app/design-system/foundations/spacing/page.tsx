"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection } from "@/components/design-system/playground/ComponentPlayground"

function SpacingSwatch({ size, rem, px }: { size: string, rem: string, px: string }) {
  return (
    <div className="flex items-center space-x-4 mb-4 border-b pb-4">
      <div className="w-16 h-16 flex items-center justify-center">
         <div className="bg-primary/20 border border-primary/50 rounded-sm" style={{ width: px, height: px }} />
      </div>
      <div>
        <p className="font-semibold">{size}</p>
        <p className="text-sm text-muted-foreground font-mono">{rem} / {px}</p>
      </div>
    </div>
  )
}

export default function SpacingPage() {
  return (
    <ComponentPlayground
      title="Spacing"
      description="Design tokens for spacing and layout."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AAA",
        productionReady: true,
      }}
    >
      <PlaygroundSection title="Spacing Scale">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <SpacingSwatch size="space-1" rem="0.25rem" px="4px" />
          <SpacingSwatch size="space-2" rem="0.5rem" px="8px" />
          <SpacingSwatch size="space-3" rem="0.75rem" px="12px" />
          <SpacingSwatch size="space-4" rem="1rem" px="16px" />
          <SpacingSwatch size="space-6" rem="1.5rem" px="24px" />
          <SpacingSwatch size="space-8" rem="2rem" px="32px" />
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
