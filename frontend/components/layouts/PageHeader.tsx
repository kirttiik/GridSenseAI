import * as React from "react"
import { cn } from "@/lib/utils"

export interface PageHeaderProps extends Omit<React.HTMLAttributes<HTMLDivElement>, "title"> {
  title: React.ReactNode
  subtitle?: React.ReactNode
  breadcrumb?: React.ReactNode
  actions?: React.ReactNode
  status?: React.ReactNode
  lastUpdated?: string
}

export function PageHeader({
  title,
  subtitle,
  breadcrumb,
  actions,
  status,
  lastUpdated,
  className,
  ...props
}: PageHeaderProps) {
  return (
    <div className={cn("flex flex-col space-y-4 pb-6 border-b", className)} {...props}>
      {breadcrumb && (
        <div className="text-sm text-muted-foreground">
          {breadcrumb}
        </div>
      )}
      
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div className="space-y-1">
          <div className="flex items-center gap-3">
            <h1 className="text-3xl font-bold tracking-tight">{title}</h1>
            {status && <div>{status}</div>}
          </div>
          {subtitle && (
            <p className="text-lg text-muted-foreground">{subtitle}</p>
          )}
          {lastUpdated && (
            <p className="text-sm text-muted-foreground">Last updated: {lastUpdated}</p>
          )}
        </div>
        
        {actions && (
          <div className="flex items-center gap-2">
            {actions}
          </div>
        )}
      </div>
    </div>
  )
}
