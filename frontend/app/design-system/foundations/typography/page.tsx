"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection } from "@/components/design-system/playground/ComponentPlayground"

function TypeSpecimen({ label, className, sample }: { label: string, className: string, sample: string }) {
  return (
    <div className="mb-8 border-b pb-4">
      <p className="text-sm text-muted-foreground font-mono mb-2">{label}</p>
      <div className={className}>{sample}</div>
    </div>
  )
}

export default function TypographyPage() {
  return (
    <ComponentPlayground
      title="Typography"
      description="Design tokens for text rendering."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AAA",
        productionReady: true,
      }}
    >
      <PlaygroundSection title="Headings">
        <TypeSpecimen label="text-4xl font-bold tracking-tight" className="text-4xl font-bold tracking-tight" sample="The quick brown fox jumps over the lazy dog" />
        <TypeSpecimen label="text-3xl font-semibold tracking-tight" className="text-3xl font-semibold tracking-tight" sample="The quick brown fox jumps over the lazy dog" />
        <TypeSpecimen label="text-2xl font-semibold tracking-tight" className="text-2xl font-semibold tracking-tight" sample="The quick brown fox jumps over the lazy dog" />
        <TypeSpecimen label="text-xl font-semibold tracking-tight" className="text-xl font-semibold tracking-tight" sample="The quick brown fox jumps over the lazy dog" />
      </PlaygroundSection>

      <PlaygroundSection title="Body & UI text">
        <TypeSpecimen label="text-base" className="text-base" sample="The quick brown fox jumps over the lazy dog" />
        <TypeSpecimen label="text-sm font-medium (UI element)" className="text-sm font-medium" sample="The quick brown fox jumps over the lazy dog" />
        <TypeSpecimen label="text-sm text-muted-foreground" className="text-sm text-muted-foreground" sample="The quick brown fox jumps over the lazy dog" />
        <TypeSpecimen label="text-xs text-muted-foreground" className="text-xs text-muted-foreground" sample="The quick brown fox jumps over the lazy dog" />
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
