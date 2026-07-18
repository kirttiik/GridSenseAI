import * as React from "react"
import { cn } from "@/lib/utils"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Skeleton } from "@/components/ui/skeleton"
import { AlertCircle, TrendingDown, TrendingUp, Minus } from "lucide-react"

export type KPICardVariant = "default" | "success" | "warning" | "danger" | "neutral"

export interface KPICardProps extends Omit<React.HTMLAttributes<HTMLDivElement>, "title"> {
  title: string
  value?: string | number
  unit?: string
  icon?: React.ReactNode
  trend?: "up" | "down" | "neutral"
  trendValue?: string
  comparison?: string
  variant?: KPICardVariant
  isLoading?: boolean
  isEmpty?: boolean
}

const variantStyles: Record<KPICardVariant, { icon: string; trendUp: string; trendDown: string; trendNeutral: string }> = {
  default: { icon: "text-muted-foreground", trendUp: "text-emerald-500", trendDown: "text-rose-500", trendNeutral: "text-muted-foreground" },
  success: { icon: "text-emerald-500", trendUp: "text-emerald-600", trendDown: "text-emerald-400", trendNeutral: "text-emerald-500" },
  warning: { icon: "text-amber-500", trendUp: "text-amber-600", trendDown: "text-amber-400", trendNeutral: "text-amber-500" },
  danger: { icon: "text-rose-500", trendUp: "text-rose-600", trendDown: "text-rose-400", trendNeutral: "text-rose-500" },
  neutral: { icon: "text-muted-foreground", trendUp: "text-muted-foreground", trendDown: "text-muted-foreground", trendNeutral: "text-muted-foreground" },
}

export function KPICard({
  title,
  value,
  unit,
  icon,
  trend,
  trendValue,
  comparison,
  variant = "default",
  isLoading = false,
  isEmpty = false,
  className,
  ...props
}: KPICardProps) {
  const styles = variantStyles[variant]

  return (
    <Card className={cn("overflow-hidden", className)} {...props}>
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium">{title}</CardTitle>
        {icon && (
          <div className={cn("h-4 w-4", styles.icon)}>
            {icon}
          </div>
        )}
      </CardHeader>
      <CardContent>
        {isLoading ? (
          <div className="space-y-2">
            <Skeleton className="h-8 w-24" />
            <Skeleton className="h-4 w-32" />
          </div>
        ) : isEmpty ? (
          <div className="flex flex-col items-center justify-center py-4 text-muted-foreground">
            <AlertCircle className="h-6 w-6 mb-2" />
            <p className="text-sm">No data available</p>
          </div>
        ) : (
          <>
            <div className="flex items-baseline gap-1">
              <div className="text-2xl font-bold">{value}</div>
              {unit && <div className="text-sm text-muted-foreground">{unit}</div>}
            </div>
            
            {(trend || comparison) && (
              <div className="mt-1 flex items-center text-xs">
                {trend === "up" && <TrendingUp className={cn("mr-1 h-3 w-3", styles.trendUp)} />}
                {trend === "down" && <TrendingDown className={cn("mr-1 h-3 w-3", styles.trendDown)} />}
                {trend === "neutral" && <Minus className={cn("mr-1 h-3 w-3", styles.trendNeutral)} />}
                
                {trendValue && (
                  <span
                    className={cn(
                      "font-medium mr-1",
                      trend === "up" && styles.trendUp,
                      trend === "down" && styles.trendDown,
                      trend === "neutral" && styles.trendNeutral
                    )}
                  >
                    {trendValue}
                  </span>
                )}
                
                {comparison && (
                  <span className="text-muted-foreground">{comparison}</span>
                )}
              </div>
            )}
          </>
        )}
      </CardContent>
    </Card>
  )
}
