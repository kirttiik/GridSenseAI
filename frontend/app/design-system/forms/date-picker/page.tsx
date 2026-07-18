"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"
import { ThemePreview } from "@/components/design-system/previews/ThemePreview"
import { DatePicker } from "@/components/ui/date-picker"

export default function DatePickerPage() {
  const [date, setDate] = React.useState<Date | undefined>(new Date())

  return (
    <ComponentPlayground
      title="Date Picker"
      description="A calendar popover for selecting dates."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <div className="max-w-sm mx-auto w-full">
        <DatePicker date={date} setDate={setDate} />
      </div>

      <PlaygroundSection title="Theme Support">
        <ThemePreview>
          <div className="max-w-sm">
            <DatePicker date={date} setDate={() => {}} />
          </div>
        </ThemePreview>
      </PlaygroundSection>

      <PlaygroundSection title="Documentation" description="Usage and Accessibility notes.">
        <div className="prose prose-sm max-w-none text-muted-foreground mt-4">
          <h3>When to use</h3>
          <p>Use for forms that require a specific date input, such as outage scheduling or historical data querying.</p>
          <h3>Accessibility</h3>
          <ul>
            <li>The calendar is fully keyboard navigable.</li>
            <li>Users can tab into the popover and use arrow keys to change dates.</li>
          </ul>
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
