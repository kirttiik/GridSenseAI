"use client"

import * as React from "react"
import { ComponentPlayground, PlaygroundSection, LivePreview } from "@/components/design-system/playground/ComponentPlayground"
import { ThemePreview } from "@/components/design-system/previews/ThemePreview"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { AlertTriangle, Info, CheckCircle, XCircle } from "lucide-react"

export default function AlertsPage() {
  return (
    <ComponentPlayground
      title="Alerts & Toasts"
      description="Feedback messages to communicate state or action results to the user."
      metadata={{
        version: "1.0.0",
        status: "Stable",
        accessibility: "WCAG AA",
        productionReady: true,
      }}
    >
      <div className="flex flex-col gap-4 w-full">
        <Alert>
          <Info className="h-4 w-4" />
          <AlertTitle>Information</AlertTitle>
          <AlertDescription>
            This is a standard informational alert used to provide context.
          </AlertDescription>
        </Alert>
      </div>

      <PlaygroundSection title="Variants">
        <div className="flex flex-col gap-4 w-full">
          <Alert variant="destructive">
            <AlertTriangle className="h-4 w-4" />
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>
              Failed to connect to the Grid API. Please check your network connection.
            </AlertDescription>
          </Alert>
        </div>
      </PlaygroundSection>

      <PlaygroundSection title="Theme Support">
        <ThemePreview>
          <div className="w-full">
            <Alert>
              <Info className="h-4 w-4" />
              <AlertTitle>Theme Aware</AlertTitle>
              <AlertDescription>
                This alert matches the current theme automatically.
              </AlertDescription>
            </Alert>
          </div>
        </ThemePreview>
      </PlaygroundSection>

      <PlaygroundSection title="Documentation" description="Usage and Accessibility notes.">
        <div className="prose prose-sm max-w-none text-muted-foreground mt-4">
          <h3>When to use</h3>
          <p>Use inline Alerts for persistent feedback (e.g., &quot;Your account is missing information&quot;). Use Toasts (Sonner) for ephemeral, action-based feedback (e.g., &quot;Asset saved successfully&quot;).</p>
        </div>
      </PlaygroundSection>
    </ComponentPlayground>
  )
}
