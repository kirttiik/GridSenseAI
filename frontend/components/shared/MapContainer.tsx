import * as React from "react"
import { cn } from "@/lib/utils"
import { SkeletonMap } from "@/components/feedback/LoadingStates"
import { EmptyState } from "@/components/composites/EmptyState"
import { Map as MapIcon } from "lucide-react"

export interface MapContainerProps extends React.HTMLAttributes<HTMLDivElement> {
  isLoading?: boolean
  isEmpty?: boolean
  emptyMessage?: string
  children?: React.ReactNode
}

export function MapContainer({
  isLoading,
  isEmpty,
  emptyMessage = "No map data available for this region.",
  children,
  className,
  ...props
}: MapContainerProps) {
  if (isLoading) {
    return <SkeletonMap className={className} />
  }

  if (isEmpty) {
    return (
      <div className={cn("flex min-h-[400px] w-full items-center justify-center rounded-lg border bg-muted/20", className)}>
        <EmptyState 
          icon={MapIcon}
          title="Map Data Unavailable"
          description={emptyMessage}
          className="border-none shadow-none"
        />
      </div>
    )
  }

  return (
    <div className={cn("relative w-full h-[400px] rounded-lg overflow-hidden border bg-muted/20", className)} {...props}>
      {children || (
        <div className="absolute inset-0 flex items-center justify-center text-muted-foreground">
          Map Layer Placeholder
        </div>
      )}
    </div>
  )
}
