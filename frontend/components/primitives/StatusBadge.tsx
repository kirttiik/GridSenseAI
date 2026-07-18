import * as React from "react"
import { cn } from "@/lib/utils"
import { Badge } from "@/components/ui/badge"

export type StatusType = "online" | "offline" | "warning" | "maintenance" | "healthy"

export interface StatusBadgeProps extends React.ComponentProps<typeof Badge> {
  status: StatusType
  label?: string
  showDot?: boolean
}

const statusConfig: Record<StatusType, { color: string; dotClass: string; defaultLabel: string }> = {
  online: { color: "bg-emerald-100 text-emerald-800 dark:bg-emerald-900/30 dark:text-emerald-400 hover:bg-emerald-100/80", dotClass: "bg-emerald-500", defaultLabel: "Online" },
  healthy: { color: "bg-emerald-100 text-emerald-800 dark:bg-emerald-900/30 dark:text-emerald-400 hover:bg-emerald-100/80", dotClass: "bg-emerald-500", defaultLabel: "Healthy" },
  offline: { color: "bg-rose-100 text-rose-800 dark:bg-rose-900/30 dark:text-rose-400 hover:bg-rose-100/80", dotClass: "bg-rose-500", defaultLabel: "Offline" },
  warning: { color: "bg-amber-100 text-amber-800 dark:bg-amber-900/30 dark:text-amber-400 hover:bg-amber-100/80", dotClass: "bg-amber-500", defaultLabel: "Warning" },
  maintenance: { color: "bg-blue-100 text-blue-800 dark:bg-blue-900/30 dark:text-blue-400 hover:bg-blue-100/80", dotClass: "bg-blue-500", defaultLabel: "Maintenance" },
}

export function StatusBadge({ status, label, showDot = true, className, ...props }: StatusBadgeProps) {
  const config = statusConfig[status]
  
  return (
    <Badge 
      variant="outline" 
      className={cn("border-transparent font-medium", config.color, className)} 
      {...props}
    >
      {showDot && (
        <span className={cn("mr-1.5 h-2 w-2 rounded-full inline-block", config.dotClass)} aria-hidden="true" />
      )}
      {label || config.defaultLabel}
    </Badge>
  )
}
