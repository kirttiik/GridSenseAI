import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"
import { ThemePreview } from "@/components/design-system/previews/ThemePreview"
import { MetricCard } from "@/components/composites/MetricCard"
import { Zap, Activity, AlertTriangle } from "lucide-react"

export default function MetricCardsPage() {
  return (
    <ComponentPlayground
      title="Metric Cards"
      description="Standardized cards displaying a Label, Large Numeric Value, trend indicator, and optional icon."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <div className="grid gap-4 md:grid-cols-2">
        <MetricCard
          title="Total Generation"
          value="4,521 MW"
          icon={Zap}
          trend="up"
          trendValue="+12%"
          description="vs last hour"
        />
      </div>

      <PlaygroundSection title="Variants">
        <div className="grid gap-4 md:grid-cols-3">
          <MetricCard
            title="System Frequency"
            value="49.98 Hz"
            icon={Activity}
            trend="down"
            trendValue="-0.02 Hz"
            description="Stable"
          />
          <MetricCard
            title="Grid Anomalies"
            value="3"
            icon={AlertTriangle}
            className="border-destructive/50"
            description="Requires attention"
          />
          <MetricCard
            title="Active Markets"
            value="14"
            description="Operating normally"
          />
        </div>
      </PlaygroundSection>

      <PlaygroundSection title="Theme Support">
        <ThemePreview>
          <div className="w-full">
            <MetricCard
              title="Demand Forecast"
              value="5,100 MW"
              trend="up"
              trendValue="+4%"
            />
          </div>
        </ThemePreview>
      </PlaygroundSection>

      <PlaygroundSection title="Documentation" description="Usage and Accessibility notes.">
        <div className="prose prose-sm max-w-none text-muted-foreground mt-4">
          <h3>When to use</h3>
          <p>Use MetricCards at the top of workspaces or dashboards to highlight Key Performance Indicators (KPIs).</p>
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
