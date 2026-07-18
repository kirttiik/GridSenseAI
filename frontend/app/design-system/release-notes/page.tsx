"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection } from "@/components/design-system/playground/ComponentPlayground"
import { Badge } from "@/components/ui/badge"

export default function ReleaseNotesPage() {
  return (
    <ComponentPlayground
      title="Release Notes"
      description="Track the evolution of the GridSense AI Design System."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <PlaygroundSection title="Current Version: 1.0.0">
        <div className="prose prose-sm max-w-none text-muted-foreground">
          <h3>Overview</h3>
          <p>
            The initial release of the internal Design System Portal. This release focuses on the core primitives, custom forms, and high-level composite components needed for Sprint 7 implementation.
          </p>

          <h3>Recently Added Components</h3>
          <ul>
            <li><strong>Foundations:</strong> Colors, Typography, Spacing, Radius, Elevation, Motion.</li>
            <li><strong>Primitives:</strong> Button, Input, Badge.</li>
            <li><strong>Forms:</strong> SearchBox, MultiSelect, DatePicker.</li>
            <li><strong>Composites:</strong> MetricCard, EmptyState, LoadingIndicator.</li>
            <li><strong>Layouts:</strong> PageContainer, Panel, SplitLayout.</li>
            <li><strong>Feedback:</strong> Alert, Skeleton.</li>
          </ul>

          <h3>Recently Updated Components</h3>
          <p>None yet. This is the first release.</p>

          <h3>Deprecated Components</h3>
          <p>None yet.</p>
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
