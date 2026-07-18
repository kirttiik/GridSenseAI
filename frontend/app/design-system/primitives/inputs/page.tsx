import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"
import { ThemePreview } from "@/components/design-system/previews/ThemePreview"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"

export default function InputsPage() {
  return (
    <ComponentPlayground
      title="Inputs & Textareas"
      description="Form controls for user text input."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <div className="flex flex-col gap-4 w-full max-w-sm mx-auto">
        <div className="space-y-2 w-full">
          <Label htmlFor="email">Email</Label>
          <Input type="email" id="email" placeholder="Email address" />
        </div>
      </div>

      <PlaygroundSection title="Variants">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-2xl">
          <div className="space-y-2">
            <Label htmlFor="default">Default Input</Label>
            <Input id="default" placeholder="Default placeholder" />
          </div>
          <div className="space-y-2">
            <Label htmlFor="file">File Input</Label>
            <Input id="file" type="file" />
          </div>
          <div className="space-y-2">
            <Label htmlFor="disabled">Disabled Input</Label>
            <Input id="disabled" disabled placeholder="Disabled state" />
          </div>
          <div className="space-y-2">
            <Label htmlFor="textarea">Textarea</Label>
            <Textarea id="textarea" placeholder="Enter longer text..." />
          </div>
        </div>
      </PlaygroundSection>

      <PlaygroundSection title="Theme Support">
        <ThemePreview>
          <div className="space-y-2 max-w-xs">
            <Label>Example Input</Label>
            <Input placeholder="Theme aware input" />
          </div>
        </ThemePreview>
      </PlaygroundSection>

      <PlaygroundSection title="Documentation" description="Usage and Accessibility notes.">
        <div className="prose prose-sm max-w-none text-muted-foreground mt-4">
          <h3>When to use</h3>
          <p>Use inputs for standard data entry. Use Textarea for multi-line inputs.</p>
          <h3>Accessibility</h3>
          <ul>
            <li>Always associate an `Input` with a `Label` using the `id` and `htmlFor` props.</li>
            <li>Use appropriate `type` attributes (email, tel, url, number) to ensure correct virtual keyboards on mobile devices.</li>
          </ul>
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
