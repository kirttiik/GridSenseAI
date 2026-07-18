"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"
import { SplitLayout } from "@/components/layouts/SplitLayout"

export default function SplitLayoutPage() {
  return (
    <ComponentPlayground
      title="Split Layout"
      description="A resizable dual-pane layout, typically used for Master-Detail views or Map-Data splits."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <div className="w-full h-[400px] border rounded-md overflow-hidden">
        <SplitLayout
          leftPanel={<div className="h-full flex items-center justify-center bg-muted/30">Left Pane (List/Map)</div>}
          rightPanel={<div className="h-full flex items-center justify-center bg-background">Right Pane (Details)</div>}
          defaultLayout={[50, 50]}
        />
      </div>

      <PlaygroundSection title="Documentation" description="Usage and Accessibility notes.">
        <div className="prose prose-sm max-w-none text-muted-foreground mt-4">
          <h3>When to use</h3>
          <p>Use when the user needs to view a list/map of items and the specific details of a selected item simultaneously.</p>
          <h3>Accessibility</h3>
          <ul>
            <li>The resizer handle is focusable and can be adjusted using the left/right arrow keys.</li>
          </ul>
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
