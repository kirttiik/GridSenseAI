"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"
import { ThemePreview } from "@/components/design-system/previews/ThemePreview"
import { EmptyState } from "@/components/composites/EmptyState"
import { Battery, Database } from "lucide-react"

export default function EmptyStatesPage() {
  return (
    <ComponentPlayground
      title="Empty States"
      description="Standardized fallback components for lists, tables, and dashboards with no data."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <div className="w-full">
        <EmptyState
          icon={Battery}
          title="No Storage Assets"
          description="There are currently no battery storage assets configured in this region."
          actionLabel="Add Asset"
          onAction={() => console.log("Action clicked")}
        />
      </div>

      <PlaygroundSection title="Variants">
        <div className="w-full">
          <EmptyState
            icon={Database}
            title="No Results Found"
            description="Try adjusting your filters or search terms."
            className="min-h-[250px]"
          />
        </div>
      </PlaygroundSection>

      <PlaygroundSection title="Theme Support">
        <ThemePreview>
          <div className="w-full">
            <EmptyState
              title="No Content"
              description="This widget has no content to display."
              className="min-h-[200px] bg-background"
            />
          </div>
        </ThemePreview>
      </PlaygroundSection>

      <PlaygroundSection title="Documentation" description="Usage and Accessibility notes.">
        <div className="prose prose-sm max-w-none text-muted-foreground mt-4">
          <h3>When to use</h3>
          <p>Display an Empty State whenever a user encounters a screen or widget that does not yet have data. This is better than a blank screen as it guides the user on what to do next.</p>
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
