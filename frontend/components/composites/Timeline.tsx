import * as React from "react"
import { cn } from "@/lib/utils"

export interface TimelineItem {
  id: string | number
  title: React.ReactNode
  description?: React.ReactNode
  time?: React.ReactNode
  icon?: React.ReactNode
  status?: "default" | "success" | "warning" | "error"
}

export interface TimelineProps extends React.HTMLAttributes<HTMLDivElement> {
  items: TimelineItem[]
}

const statusColors = {
  default: "bg-muted border-border",
  success: "bg-emerald-100 border-emerald-500 text-emerald-600 dark:bg-emerald-950/50",
  warning: "bg-amber-100 border-amber-500 text-amber-600 dark:bg-amber-950/50",
  error: "bg-rose-100 border-rose-500 text-rose-600 dark:bg-rose-950/50",
}

export function Timeline({ items, className, ...props }: TimelineProps) {
  return (
    <div className={cn("space-y-4", className)} {...props}>
      {items.map((item, index) => {
        const isLast = index === items.length - 1
        const statusClass = statusColors[item.status || "default"]

        return (
          <div key={item.id} className="relative flex gap-4">
            <div className="flex flex-col items-center">
              <div
                className={cn(
                  "flex h-8 w-8 items-center justify-center rounded-full border-2",
                  statusClass,
                  !item.icon && "bg-background"
                )}
              >
                {item.icon ? (
                  <div className="h-4 w-4">{item.icon}</div>
                ) : (
                  <div className={cn("h-2 w-2 rounded-full", item.status ? `bg-${item.status}-500` : "bg-muted-foreground")} />
                )}
              </div>
              {!isLast && <div className="mt-2 w-px flex-1 bg-border" />}
            </div>
            <div className={cn("flex flex-col pb-6", isLast && "pb-0")}>
              <div className="flex items-center gap-2">
                <p className="text-sm font-semibold">{item.title}</p>
                {item.time && (
                  <span className="text-xs text-muted-foreground">{item.time}</span>
                )}
              </div>
              {item.description && (
                <div className="mt-1 text-sm text-muted-foreground">
                  {item.description}
                </div>
              )}
            </div>
          </div>
        )
      })}
    </div>
  )
}
