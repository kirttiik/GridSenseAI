import * as React from "react"
import { cn } from "@/lib/utils"
import { Skeleton } from "@/components/ui/skeleton"

interface LoadingIndicatorProps {
  className?: string
  text?: string
  fullScreen?: boolean
}

export function LoadingIndicator({
  className,
  text = "Loading data...",
  fullScreen = false,
}: LoadingIndicatorProps) {
  if (fullScreen) {
    return (
      <div className="fixed inset-0 z-50 flex items-center justify-center bg-background/80 backdrop-blur-sm">
        <div className="flex flex-col items-center gap-4">
          <div className="h-8 w-8 animate-spin rounded-full border-4 border-primary border-t-transparent" />
          <p className="text-sm text-muted-foreground animate-pulse">{text}</p>
        </div>
      </div>
    )
  }

  return (
    <div className={cn("flex flex-col items-center justify-center p-8", className)}>
      <div className="flex space-x-2">
        <Skeleton className="h-3 w-3 rounded-full" />
        <Skeleton className="h-3 w-3 rounded-full delay-75" />
        <Skeleton className="h-3 w-3 rounded-full delay-150" />
      </div>
      {text && <p className="mt-4 text-sm text-muted-foreground">{text}</p>}
    </div>
  )
}
