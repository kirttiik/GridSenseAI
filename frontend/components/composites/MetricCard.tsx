import * as React from "react"
import { LucideIcon, ArrowUpRight, ArrowDownRight } from "lucide-react"

import { cn } from "@/lib/utils"
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

interface MetricCardProps {
  title: string
  value: string | number
  icon?: LucideIcon
  trend?: "up" | "down" | "neutral"
  trendValue?: string
  description?: string
  className?: string
}

export function MetricCard({
  title,
  value,
  icon: Icon,
  trend,
  trendValue,
  description,
  className,
}: MetricCardProps) {
  return (
    <Card className={cn("overflow-hidden", className)}>
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium">
          {title}
        </CardTitle>
        {Icon && <Icon className="h-4 w-4 text-muted-foreground" aria-hidden="true" />}
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">{value}</div>
        {(trendValue || description) && (
          <p className="text-xs text-muted-foreground mt-1 flex items-center">
            {trend === "up" && (
              <ArrowUpRight className="mr-1 h-3 w-3 text-emerald-500" aria-hidden="true" />
            )}
            {trend === "down" && (
              <ArrowDownRight className="mr-1 h-3 w-3 text-red-500" aria-hidden="true" />
            )}
            {trendValue && (
              <span
                className={cn("mr-1 font-medium", {
                  "text-emerald-500": trend === "up",
                  "text-red-500": trend === "down",
                })}
              >
                {trendValue}
              </span>
            )}
            {description && <span>{description}</span>}
          </p>
        )}
      </CardContent>
    </Card>
  )
}
