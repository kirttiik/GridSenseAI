"use client"

import * as React from "react"
import { ResponsivePreview } from "../previews/ResponsivePreview"
import { Badge } from "@/components/ui/badge"
import { cn } from "@/lib/utils"

export interface ComponentMetadata {
  version: string
  status: "Stable" | "Beta" | "Alpha" | "Deprecated"
  accessibility: "WCAG AAA" | "WCAG AA" | "Partial" | "Pending"
  productionReady: boolean
  dependencies?: string[]
}

export interface ComponentPlaygroundProps {
  title: string
  description: string
  metadata: ComponentMetadata
  children: React.ReactNode // Sections will be passed as children
}

export function ComponentPlayground({
  title,
  description,
  metadata,
  children,
}: ComponentPlaygroundProps) {
  return (
    <div className="max-w-7xl mx-auto px-6 py-12 pb-32">
      <div className="mb-12">
        <h1 className="text-4xl font-bold tracking-tight text-foreground mb-4">{title}</h1>
        <p className="text-xl text-muted-foreground max-w-3xl mb-8">{description}</p>
        
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 p-6 bg-muted/30 border rounded-lg max-w-4xl">
          <div>
            <p className="text-sm text-muted-foreground font-medium mb-1">Status</p>
            <Badge variant={metadata.status === "Stable" ? "default" : metadata.status === "Deprecated" ? "destructive" : "secondary"}>
              {metadata.status}
            </Badge>
          </div>
          <div>
            <p className="text-sm text-muted-foreground font-medium mb-1">Version</p>
            <p className="text-sm font-semibold">{metadata.version}</p>
          </div>
          <div>
            <p className="text-sm text-muted-foreground font-medium mb-1">Accessibility</p>
            <p className="text-sm font-semibold">{metadata.accessibility}</p>
          </div>
          <div>
            <p className="text-sm text-muted-foreground font-medium mb-1">Production</p>
            <div className="flex items-center">
              <div className={cn("w-2 h-2 rounded-full mr-2", metadata.productionReady ? "bg-emerald-500" : "bg-amber-500")} />
              <span className="text-sm font-semibold">{metadata.productionReady ? "Ready" : "In Progress"}</span>
            </div>
          </div>
        </div>
      </div>

      <div className="space-y-16">
        {children}
      </div>
    </div>
  )
}

export function PlaygroundSection({ 
  title, 
  description, 
  children,
  className
}: { 
  title: string
  description?: string
  children: React.ReactNode
  className?: string
}) {
  return (
    <section className={cn("space-y-6", className)}>
      <div className="border-b pb-4">
        <h2 className="text-2xl font-semibold tracking-tight">{title}</h2>
        {description && <p className="text-base text-muted-foreground mt-2">{description}</p>}
      </div>
      <div>
        {children}
      </div>
    </section>
  )
}

export function LivePreview({ children }: { children: React.ReactNode }) {
  return (
    <PlaygroundSection title="Live Preview">
      <ResponsivePreview>{children}</ResponsivePreview>
    </PlaygroundSection>
  )
}
