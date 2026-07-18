import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"
import { PageContainer } from "@/components/layouts/PageContainer"
import { Section, Panel } from "@/components/layouts/Section"

export default function PageContainerPage() {
  return (
    <ComponentPlayground
      title="Page Container"
      description="The root structural wrapper for a page, enforcing maximum width and padding."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <div className="border border-dashed p-4 bg-muted/20">
        <PageContainer className="border bg-background h-32 flex items-center justify-center">
          <span className="text-muted-foreground text-sm">Contained Page Content</span>
        </PageContainer>
      </div>

      <PlaygroundSection title="Documentation" description="Usage and Accessibility notes.">
        <div className="prose prose-sm max-w-none text-muted-foreground mt-4">
          <h3>When to use</h3>
          <p>Wrap the main content of every route/page in a <code>PageContainer</code> to ensure consistent horizontal margins and a centralized column on ultra-wide screens.</p>
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
