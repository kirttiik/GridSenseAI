"use client"

import * as React from "react"
import { cn } from "@/lib/utils"
import { SkeletonChart } from "@/components/feedback/LoadingStates"
import { EmptyState } from "@/components/composites/EmptyState"
import { BarChart as BarChartIcon } from "lucide-react"
import {
  ResponsiveContainer,
  BarChart as RechartsBarChart,
  LineChart as RechartsLineChart,
  AreaChart as RechartsAreaChart,
  PieChart as RechartsPieChart,
  Bar,
  Line,
  Area,
  Pie,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  Cell,
} from "recharts"

export interface ChartBaseProps {
  data?: Record<string, unknown>[]
  isLoading?: boolean
  isEmpty?: boolean
  className?: string
  height?: number | string
  emptyMessage?: string
}

// Enterprise Chart Colors mapped to theme
const CHART_COLORS = [
  "hsl(var(--primary))",
  "hsl(210, 100%, 65%)", // lighter blue
  "hsl(190, 100%, 45%)", // cyan
  "hsl(280, 70%, 60%)",  // purple
  "hsl(150, 70%, 45%)",  // green
]

export function ChartContainer({
  isLoading,
  isEmpty,
  data,
  height = 350,
  emptyMessage = "No chart data available.",
  className,
  children,
}: ChartBaseProps & { children: React.ReactNode }) {
  if (isLoading) {
    return <SkeletonChart className={cn(`h-[${height}px]`, className)} />
  }

  if (isEmpty || !data || data.length === 0) {
    return (
      <div 
        className={cn("flex w-full items-center justify-center rounded-lg border bg-muted/20", className)} 
        style={{ height }}
      >
        <EmptyState 
          icon={BarChartIcon}
          title="No Data"
          description={emptyMessage}
          className="border-none shadow-none min-h-[200px]"
        />
      </div>
    )
  }

  return (
    <div className={cn("w-full", className)} style={{ height }}>
      <ResponsiveContainer width="100%" height="100%">
        {children as React.ReactElement}
      </ResponsiveContainer>
    </div>
  )
}

// ---------------------------------------------------------
// Bar Chart Wrapper
// ---------------------------------------------------------
export interface BarChartProps extends ChartBaseProps {
  xAxisKey: string
  series: { key: string; name?: string; color?: string }[]
  stacked?: boolean
}

export function BarChart({ data, xAxisKey, series, stacked, ...props }: BarChartProps) {
  return (
    <ChartContainer data={data} {...props}>
      <RechartsBarChart data={data} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
        <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="hsl(var(--border))" />
        <XAxis dataKey={xAxisKey} stroke="hsl(var(--muted-foreground))" fontSize={12} tickLine={false} axisLine={false} />
        <YAxis stroke="hsl(var(--muted-foreground))" fontSize={12} tickLine={false} axisLine={false} tickFormatter={(v) => `${v}`} />
        <Tooltip
          contentStyle={{ backgroundColor: "hsl(var(--popover))", borderColor: "hsl(var(--border))", borderRadius: "8px", color: "hsl(var(--popover-foreground))" }}
          itemStyle={{ color: "hsl(var(--foreground))" }}
        />
        {series.length > 1 && <Legend wrapperStyle={{ fontSize: "12px" }} />}
        {series.map((s, i) => (
          <Bar key={s.key} dataKey={s.key} name={s.name || s.key} fill={s.color || CHART_COLORS[i % CHART_COLORS.length]} stackId={stacked ? "a" : undefined} radius={stacked ? [0, 0, 0, 0] : [4, 4, 0, 0]} />
        ))}
      </RechartsBarChart>
    </ChartContainer>
  )
}

// ---------------------------------------------------------
// Line Chart Wrapper
// ---------------------------------------------------------
export interface LineChartProps extends ChartBaseProps {
  xAxisKey: string
  series: { key: string; name?: string; color?: string }[]
}

export function LineChart({ data, xAxisKey, series, ...props }: LineChartProps) {
  return (
    <ChartContainer data={data} {...props}>
      <RechartsLineChart data={data} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
        <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="hsl(var(--border))" />
        <XAxis dataKey={xAxisKey} stroke="hsl(var(--muted-foreground))" fontSize={12} tickLine={false} axisLine={false} />
        <YAxis stroke="hsl(var(--muted-foreground))" fontSize={12} tickLine={false} axisLine={false} />
        <Tooltip
          contentStyle={{ backgroundColor: "hsl(var(--popover))", borderColor: "hsl(var(--border))", borderRadius: "8px" }}
        />
        {series.length > 1 && <Legend wrapperStyle={{ fontSize: "12px" }} />}
        {series.map((s, i) => (
          <Line type="monotone" key={s.key} dataKey={s.key} name={s.name || s.key} stroke={s.color || CHART_COLORS[i % CHART_COLORS.length]} strokeWidth={2} dot={{ r: 4 }} activeDot={{ r: 6 }} />
        ))}
      </RechartsLineChart>
    </ChartContainer>
  )
}

// ---------------------------------------------------------
// Area Chart Wrapper
// ---------------------------------------------------------
export interface AreaChartProps extends ChartBaseProps {
  xAxisKey: string
  series: { key: string; name?: string; color?: string }[]
  stacked?: boolean
}

export function AreaChart({ data, xAxisKey, series, stacked, ...props }: AreaChartProps) {
  return (
    <ChartContainer data={data} {...props}>
      <RechartsAreaChart data={data} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
        <defs>
          {series.map((s, i) => (
            <linearGradient key={`color-${s.key}`} id={`color-${s.key}`} x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor={s.color || CHART_COLORS[i % CHART_COLORS.length]} stopOpacity={0.3}/>
              <stop offset="95%" stopColor={s.color || CHART_COLORS[i % CHART_COLORS.length]} stopOpacity={0}/>
            </linearGradient>
          ))}
        </defs>
        <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="hsl(var(--border))" />
        <XAxis dataKey={xAxisKey} stroke="hsl(var(--muted-foreground))" fontSize={12} tickLine={false} axisLine={false} />
        <YAxis stroke="hsl(var(--muted-foreground))" fontSize={12} tickLine={false} axisLine={false} />
        <Tooltip
          contentStyle={{ backgroundColor: "hsl(var(--popover))", borderColor: "hsl(var(--border))", borderRadius: "8px" }}
        />
        {series.length > 1 && <Legend wrapperStyle={{ fontSize: "12px" }} />}
        {series.map((s, i) => (
          <Area 
            type="monotone" 
            key={s.key} 
            dataKey={s.key} 
            name={s.name || s.key} 
            stroke={s.color || CHART_COLORS[i % CHART_COLORS.length]} 
            fillOpacity={1} 
            fill={`url(#color-${s.key})`} 
            stackId={stacked ? "a" : undefined}
          />
        ))}
      </RechartsAreaChart>
    </ChartContainer>
  )
}

// ---------------------------------------------------------
// Pie/Donut Chart Wrapper
// ---------------------------------------------------------
export interface PieChartProps extends ChartBaseProps {
  dataKey: string
  nameKey: string
  donut?: boolean
}

export function PieChart({ data, dataKey, nameKey, donut, ...props }: PieChartProps) {
  return (
    <ChartContainer data={data} {...props}>
      <RechartsPieChart>
        <Tooltip
          contentStyle={{ backgroundColor: "hsl(var(--popover))", borderColor: "hsl(var(--border))", borderRadius: "8px" }}
        />
        <Legend wrapperStyle={{ fontSize: "12px" }} />
        <Pie
          data={data}
          cx="50%"
          cy="50%"
          innerRadius={donut ? "60%" : 0}
          outerRadius="80%"
          paddingAngle={donut ? 2 : 0}
          dataKey={dataKey}
          nameKey={nameKey}
          stroke="hsl(var(--background))"
        >
          {data?.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={CHART_COLORS[index % CHART_COLORS.length]} />
          ))}
        </Pie>
      </RechartsPieChart>
    </ChartContainer>
  )
}
