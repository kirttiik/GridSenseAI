import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"
import { ThemePreview } from "@/components/design-system/previews/ThemePreview"
import { Section, Panel } from "@/components/layouts/Section"

export default function PanelsPage() {
  return (
    <ComponentPlayground
      title="Sections & Panels"
      description="Structural blocks for grouping related content within a page."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <div className="w-full">
        <Section title="Asset Overview" description="Key statistics for the current region.">
          <Panel className="p-6">
            <div className="h-24 flex items-center justify-center text-muted-foreground bg-muted/20 border border-dashed rounded-md">
              Widget Content Goes Here
            </div>
          </Panel>
        </Section>
      </div>

      <PlaygroundSection title="Theme Support">
        <ThemePreview>
          <div className="w-full">
            <Panel className="p-6 h-32 flex items-center justify-center">
              Panel in Theme Context
            </Panel>
          </div>
        </ThemePreview>
      </PlaygroundSection>

      <PlaygroundSection title="Documentation" description="Usage and Accessibility notes.">
        <div className="prose prose-sm max-w-none text-muted-foreground mt-4">
          <h3>When to use</h3>
          <p>Use <code>Section</code> to break up long pages into logical segments with a standard heading. Inside a Section, use <code>Panel</code> to wrap individual widgets, tables, or charts with proper elevation and borders.</p>
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
