import * as React from "react"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { FileSearch, Database, AlertCircle, Clock } from "lucide-react"

export type EmptyStateVariant = "no-data" | "no-results" | "error" | "coming-soon" | "custom"

export interface EmptyStateProps extends Omit<React.HTMLAttributes<HTMLDivElement>, "title"> {
  variant?: EmptyStateVariant
  title?: string
  description?: string
  icon?: React.ElementType
  actionLabel?: string
  onAction?: () => void
}

const variantConfig: Record<EmptyStateVariant, { title: string; description: string; icon: React.ElementType }> = {
  "no-data": { title: "No Data Available", description: "There is currently no data to display in this section.", icon: Database },
  "no-results": { title: "No Results Found", description: "Try adjusting your filters or search terms.", icon: FileSearch },
  "error": { title: "Something went wrong", description: "An error occurred while loading this content.", icon: AlertCircle },
  "coming-soon": { title: "Coming Soon", description: "This feature is currently under development.", icon: Clock },
  "custom": { title: "", description: "", icon: Database },
}

export function EmptyState({
  variant = "no-data",
  title,
  description,
  icon,
  actionLabel,
  onAction,
  className,
  ...props
}: EmptyStateProps) {
  const config = variantConfig[variant]
  const Icon = icon || config.icon
  const displayTitle = title || config.title
  const displayDescription = description || config.description

  return (
    <div
      className={cn(
        "flex min-h-[300px] w-full flex-col items-center justify-center rounded-md border border-dashed p-8 text-center animate-in fade-in-50",
        className
      )}
      {...props}
    >
      <div className="flex h-20 w-20 items-center justify-center rounded-full bg-muted/50 mb-4">
        <Icon className="h-10 w-10 text-muted-foreground" />
      </div>
      
      <h3 className="mt-4 text-lg font-semibold">{displayTitle}</h3>
      
      <p className="mt-2 mb-6 text-sm text-muted-foreground max-w-sm">
        {displayDescription}
      </p>
      
      {actionLabel && onAction && (
        <Button onClick={onAction} variant={variant === "error" ? "destructive" : "default"}>
          {actionLabel}
        </Button>
      )}
    </div>
  )
}
