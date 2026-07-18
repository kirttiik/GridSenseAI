"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"
import { ThemePreview } from "@/components/design-system/previews/ThemePreview"
import { LoadingIndicator } from "@/components/composites/LoadingIndicator"

export default function LoadingPage() {
  return (
    <ComponentPlayground
      title="Loading Indicators"
      description="Visual cues used while content is being fetched."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <div className="w-full flex justify-center py-12">
        <LoadingIndicator text="Fetching grid data..." />
      </div>

      <PlaygroundSection title="Variants">
        <div className="grid gap-4 md:grid-cols-2">
          <div className="border rounded-md p-12 flex items-center justify-center">
             <LoadingIndicator text="Loading..." />
          </div>
          <div className="border rounded-md p-12 flex items-center justify-center relative bg-muted/20">
             <p className="text-sm text-muted-foreground mb-4">Background content</p>
             {/* Note: In a real implementation fullScreen would cover the whole window, 
                 we simulate it here by relying on standard flow if not position fixed, 
                 but the component uses fixed inset-0. We can't render it here without covering everything. 
                 So we'll just show the inline version without text. */}
             <div className="absolute inset-0 flex items-center justify-center bg-background/80 backdrop-blur-sm z-10">
               <LoadingIndicator text="" />
             </div>
          </div>
        </div>
      </PlaygroundSection>

      <PlaygroundSection title="Theme Support">
        <ThemePreview>
          <div className="w-full flex justify-center">
            <LoadingIndicator text="Theme loading..." />
          </div>
        </ThemePreview>
      </PlaygroundSection>

      <PlaygroundSection title="Documentation" description="Usage and Accessibility notes.">
        <div className="prose prose-sm max-w-none text-muted-foreground mt-4">
          <h3>When to use</h3>
          <p>Prefer skeleton loaders (see Skeletons) for known layouts. Use LoadingIndicators for generic data fetches, table refreshing, or full-page navigation transitions.</p>
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
