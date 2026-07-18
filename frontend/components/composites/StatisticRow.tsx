import * as React from "react"
import { cn } from "@/lib/utils"

export interface StatisticItem {
  label: string
  value: string | number
}

export interface StatisticRowProps extends React.HTMLAttributes<HTMLDivElement> {
  items: StatisticItem[]
}

export function StatisticRow({ items, className, ...props }: StatisticRowProps) {
  return (
    <div
      className={cn(
        "flex flex-col sm:flex-row sm:items-center divide-y sm:divide-y-0 sm:divide-x divide-border rounded-md border",
        className
      )}
      {...props}
    >
      {items.map((item, index) => (
        <div key={index} className="flex-1 flex flex-col items-center justify-center p-4">
          <p className="text-sm text-muted-foreground">{item.label}</p>
          <p className="text-2xl font-semibold tracking-tight">{item.value}</p>
        </div>
      ))}
    </div>
  )
}
