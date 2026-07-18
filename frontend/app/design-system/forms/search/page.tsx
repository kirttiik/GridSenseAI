"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"
import { ThemePreview } from "@/components/design-system/previews/ThemePreview"
import { SearchBox } from "@/components/ui/search-box"

export default function SearchBoxPage() {
  const [value, setValue] = React.useState("")

  return (
    <ComponentPlayground
      title="Search Box"
      description="Input component specifically designed for search queries with built-in clear functionality."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <div className="max-w-md mx-auto w-full">
        <SearchBox 
          placeholder="Search for assets..." 
          value={value} 
          onChange={(e) => setValue(e.target.value)} 
          onClear={() => setValue("")}
        />
      </div>

      <PlaygroundSection title="Theme Support">
        <ThemePreview>
          <div className="max-w-md">
            <SearchBox placeholder="Search (Theme Aware)..." value="Active search" readOnly />
          </div>
        </ThemePreview>
      </PlaygroundSection>

      <PlaygroundSection title="Documentation" description="Usage and Accessibility notes.">
        <div className="prose prose-sm max-w-none text-muted-foreground mt-4">
          <h3>When to use</h3>
          <p>Use the SearchBox on list views, tables, and map layers to allow users to quickly filter items.</p>
          <h3>Props</h3>
          <ul>
            <li><code>onClear?: () =&gt; void</code> - Custom handler when the &apos;X&apos; button is clicked. If not provided, it attempts to simulate a change event with an empty string.</li>
          </ul>
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
