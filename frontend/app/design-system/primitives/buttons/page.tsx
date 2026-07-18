import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"
import { ThemePreview } from "@/components/design-system/previews/ThemePreview"
import { Button } from "@/components/ui/button"

export default function ButtonsPage() {
  return (
    <ComponentPlayground
      title="Buttons"
      description="Interactive elements that communicate actions users can take."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AAA",
        productionReady: true,
        dependencies: ["@/components/ui/button"]
      }}
    >
      <LivePreview>
        <Button>Primary Action</Button>
      </LivePreview>

      <PlaygroundSection title="Variants">
        <div className="flex flex-wrap gap-4">
          <Button variant="default">Default</Button>
          <Button variant="secondary">Secondary</Button>
          <Button variant="destructive">Destructive</Button>
          <Button variant="outline">Outline</Button>
          <Button variant="ghost">Ghost</Button>
          <Button variant="link">Link</Button>
        </div>
      </PlaygroundSection>

      <PlaygroundSection title="Sizes">
        <div className="flex flex-wrap items-center gap-4">
          <Button size="sm">Small</Button>
          <Button size="default">Default</Button>
          <Button size="lg">Large</Button>
          <Button size="icon" aria-label="Icon only">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="lucide lucide-plus"><path d="M5 12h14"/><path d="M12 5v14"/></svg>
          </Button>
        </div>
      </PlaygroundSection>

      <PlaygroundSection title="States">
        <div className="flex flex-wrap gap-4">
          <Button>Normal</Button>
          <Button disabled>Disabled</Button>
        </div>
      </PlaygroundSection>

      <PlaygroundSection title="Theme Support">
        <ThemePreview>
          <div className="flex flex-wrap gap-4">
            <Button variant="default">Primary</Button>
            <Button variant="secondary">Secondary</Button>
            <Button variant="outline">Outline</Button>
          </div>
        </ThemePreview>
      </PlaygroundSection>

      <PlaygroundSection title="Documentation" description="Usage and Accessibility notes.">
        <div className="prose prose-sm max-w-none text-muted-foreground mt-4">
          <h3>Accessibility</h3>
          <ul>
            <li>Buttons must have discernible text. If an icon-only button is used, provide an <code>aria-label</code>.</li>
            <li>Keyboard navigation is supported (Tab to focus, Space/Enter to activate).</li>
          </ul>
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
