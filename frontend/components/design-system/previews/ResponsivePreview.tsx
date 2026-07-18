"use client"

import * as React from "react"
import { Monitor, Smartphone, Tablet, Laptop } from "lucide-react"
import { Button } from "@/components/ui/button"

export function ResponsivePreview({ children }: { children: React.ReactNode }) {
  const [width, setWidth] = React.useState<"100%" | "375px" | "768px" | "1024px">("100%")

  return (
    <div className="rounded-md border bg-card w-full">
      <div className="flex flex-wrap items-center justify-between p-2 border-b bg-muted/20">
        <div className="flex space-x-1">
          <Button variant="ghost" size="sm" onClick={() => setWidth("375px")} className={width === "375px" ? "bg-muted" : ""}>
            <Smartphone className="w-4 h-4 mr-2 hidden sm:block" /> Mobile
          </Button>
          <Button variant="ghost" size="sm" onClick={() => setWidth("768px")} className={width === "768px" ? "bg-muted" : ""}>
            <Tablet className="w-4 h-4 mr-2 hidden sm:block" /> Tablet
          </Button>
          <Button variant="ghost" size="sm" onClick={() => setWidth("1024px")} className={width === "1024px" ? "bg-muted" : ""}>
            <Laptop className="w-4 h-4 mr-2 hidden sm:block" /> Laptop
          </Button>
          <Button variant="ghost" size="sm" onClick={() => setWidth("100%")} className={width === "100%" ? "bg-muted" : ""}>
            <Monitor className="w-4 h-4 mr-2 hidden sm:block" /> Desktop
          </Button>
        </div>
        <div className="text-xs text-muted-foreground pr-2 hidden sm:block">
          {width === "100%" ? "100%" : width}
        </div>
      </div>
      <div className="bg-dot-pattern bg-muted/5 flex items-center justify-center p-6 min-h-[300px] overflow-auto">
        <div
          className="transition-all duration-300 ease-in-out border border-dashed rounded-md bg-background shadow-sm flex items-center justify-center p-6 overflow-hidden"
          style={{ width: width, minHeight: "200px" }}
        >
          {children}
        </div>
      </div>
    </div>
  )
}
