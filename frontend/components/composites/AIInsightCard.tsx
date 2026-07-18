import * as React from "react"
import { cn } from "@/lib/utils"
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { AlertTriangle, Info, CheckCircle2, AlertCircle, Sparkles } from "lucide-react"

export type InsightSeverity = "info" | "low" | "medium" | "high" | "critical"

export interface AIInsightCardProps extends Omit<React.HTMLAttributes<HTMLDivElement>, "title"> {
  title: string
  summary: string
  severity?: InsightSeverity
  confidence?: number // 0-100
  recommendation?: string
  timestamp?: string
}

const severityConfig = {
  info: { icon: Info, color: "text-blue-500", bg: "bg-blue-500/10 border-blue-500/20" },
  low: { icon: CheckCircle2, color: "text-emerald-500", bg: "bg-emerald-500/10 border-emerald-500/20" },
  medium: { icon: AlertTriangle, color: "text-amber-500", bg: "bg-amber-500/10 border-amber-500/20" },
  high: { icon: AlertCircle, color: "text-orange-500", bg: "bg-orange-500/10 border-orange-500/20" },
  critical: { icon: AlertCircle, color: "text-rose-500", bg: "bg-rose-500/10 border-rose-500/20" },
}

export function AIInsightCard({
  title,
  summary,
  severity = "info",
  confidence,
  recommendation,
  timestamp,
  className,
  ...props
}: AIInsightCardProps) {
  const config = severityConfig[severity]
  const Icon = config.icon

  return (
    <Card className={cn("overflow-hidden border-l-4", config.bg, className)} {...props}>
      <CardHeader className="pb-3 flex flex-row items-start justify-between gap-4 space-y-0">
        <div className="flex items-center gap-2">
          <Sparkles className="h-4 w-4 text-indigo-500" />
          <CardTitle className="text-sm font-semibold">{title}</CardTitle>
        </div>
        {timestamp && (
          <span className="text-xs text-muted-foreground whitespace-nowrap">{timestamp}</span>
        )}
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="flex gap-3">
          <Icon className={cn("h-5 w-5 mt-0.5 shrink-0", config.color)} />
          <div className="space-y-1">
            <p className="text-sm text-foreground leading-relaxed">{summary}</p>
          </div>
        </div>
        
        {recommendation && (
          <div className="rounded-md bg-background/50 p-3 mt-2 border">
            <p className="text-xs font-semibold uppercase tracking-wider text-muted-foreground mb-1">Recommendation</p>
            <p className="text-sm text-foreground">{recommendation}</p>
          </div>
        )}
      </CardContent>
      {confidence !== undefined && (
        <CardFooter className="pt-0 pb-4">
          <div className="flex items-center gap-2 text-xs text-muted-foreground w-full">
            <span>AI Confidence: {confidence}%</span>
            <div className="h-1.5 flex-1 bg-muted rounded-full overflow-hidden">
              <div 
                className={cn("h-full rounded-full", confidence >= 80 ? "bg-emerald-500" : confidence >= 50 ? "bg-amber-500" : "bg-rose-500")} 
                style={{ width: `${confidence}%` }} 
              />
            </div>
          </div>
        </CardFooter>
      )}
    </Card>
  )
}
