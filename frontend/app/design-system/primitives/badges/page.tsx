import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"
import { ThemePreview } from "@/components/design-system/previews/ThemePreview"
import { Badge } from "@/components/ui/badge"

export default function BadgesPage() {
  return (
    <ComponentPlayground
      title="Badges"
      description="Small status descriptors for UI elements."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <div className="flex flex-wrap gap-4 items-center justify-center">
        <Badge>Active</Badge>
        <Badge variant="secondary">Draft</Badge>
        <Badge variant="outline">Offline</Badge>
        <Badge variant="destructive">Critical</Badge>
      </div>

      <PlaygroundSection title="Variants">
        <div className="flex flex-wrap gap-4 items-center">
          <Badge variant="default">Default</Badge>
          <Badge variant="secondary">Secondary</Badge>
          <Badge variant="outline">Outline</Badge>
          <Badge variant="destructive">Destructive</Badge>
        </div>
      </PlaygroundSection>

      <PlaygroundSection title="Theme Support">
        <ThemePreview>
          <div className="flex flex-wrap gap-4 items-center">
            <Badge>Primary</Badge>
            <Badge variant="secondary">Secondary</Badge>
            <Badge variant="outline">Outline</Badge>
            <Badge variant="destructive">Destructive</Badge>
          </div>
        </ThemePreview>
      </PlaygroundSection>

      <PlaygroundSection title="Documentation" description="Usage and Accessibility notes.">
        <div className="prose prose-sm max-w-none text-muted-foreground mt-4">
          <h3>When to use</h3>
          <p>Use badges to highlight the status of an item (e.g., active, warning, draft) or to denote categories.</p>
          <h3>When Not to Use</h3>
          <p>Do not use Badges for interactive filters. For interactive selections, use <code>Toggle</code> or <code>Checkbox</code>.</p>
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
