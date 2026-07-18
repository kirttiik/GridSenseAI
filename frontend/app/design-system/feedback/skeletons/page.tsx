import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"
import { ThemePreview } from "@/components/design-system/previews/ThemePreview"
import { Skeleton } from "@/components/ui/skeleton"

export default function SkeletonsPage() {
  return (
    <ComponentPlayground
      title="Skeletons"
      description="Placeholders used to indicate loading state while preserving layout."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <div className="flex items-center space-x-4">
        <Skeleton className="h-12 w-12 rounded-full" />
        <div className="space-y-2">
          <Skeleton className="h-4 w-[250px]" />
          <Skeleton className="h-4 w-[200px]" />
        </div>
      </div>

      <PlaygroundSection title="Variants">
        <div className="space-y-6 w-full max-w-md">
          <div className="space-y-2">
            <p className="text-sm font-medium">Text Block Skeleton</p>
            <Skeleton className="h-4 w-full" />
            <Skeleton className="h-4 w-5/6" />
            <Skeleton className="h-4 w-4/6" />
          </div>
          <div className="space-y-2">
            <p className="text-sm font-medium">Card Skeleton</p>
            <Skeleton className="h-[125px] w-full rounded-xl" />
          </div>
        </div>
      </PlaygroundSection>

      <PlaygroundSection title="Theme Support">
        <ThemePreview>
          <div className="space-y-2 w-full">
            <Skeleton className="h-4 w-[250px]" />
            <Skeleton className="h-4 w-[200px]" />
          </div>
        </ThemePreview>
      </PlaygroundSection>

      <PlaygroundSection title="Documentation" description="Usage and Accessibility notes.">
        <div className="prose prose-sm max-w-none text-muted-foreground mt-4">
          <h3>When to use</h3>
          <p>Use skeletons instead of spinners when the structure of the incoming data is known. This reduces layout shift (CLS) and creates a smoother perceived loading experience.</p>
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
