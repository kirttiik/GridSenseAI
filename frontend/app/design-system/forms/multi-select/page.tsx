"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"
import { ThemePreview } from "@/components/design-system/previews/ThemePreview"
import { MultiSelect } from "@/components/ui/multi-select"

export default function MultiSelectPage() {
  const [selected, setSelected] = React.useState<string[]>([])
  
  const options = [
    { label: "Solar", value: "solar" },
    { label: "Wind", value: "wind" },
    { label: "Hydro", value: "hydro" },
    { label: "Nuclear", value: "nuclear" },
    { label: "Coal", value: "coal" },
  ]

  return (
    <ComponentPlayground
      title="Multi Select"
      description="Combobox allowing multiple selections with integrated search."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <div className="max-w-sm mx-auto w-full">
        <MultiSelect 
          options={options}
          selected={selected}
          onChange={setSelected}
          placeholder="Select fuel types..."
        />
      </div>

      <PlaygroundSection title="Theme Support">
        <ThemePreview>
          <div className="max-w-sm">
            <MultiSelect 
              options={options}
              selected={["solar", "wind"]}
              onChange={() => {}}
              placeholder="Select fuel types..."
            />
          </div>
        </ThemePreview>
      </PlaygroundSection>

      <PlaygroundSection title="Documentation" description="Usage and Accessibility notes.">
        <div className="prose prose-sm max-w-none text-muted-foreground mt-4">
          <h3>When to use</h3>
          <p>Use when a user needs to filter by multiple options from a predefined list (e.g., selecting multiple regions, or fuel types).</p>
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
