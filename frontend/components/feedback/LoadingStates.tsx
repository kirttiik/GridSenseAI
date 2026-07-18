import * as React from "react"
import { cn } from "@/lib/utils"
import { Skeleton } from "@/components/ui/skeleton"
import { Card, CardContent, CardHeader } from "@/components/ui/card"

export function SkeletonCard({ className }: { className?: string }) {
  return (
    <Card className={cn("overflow-hidden", className)}>
      <CardHeader className="pb-2">
        <Skeleton className="h-4 w-1/3" />
      </CardHeader>
      <CardContent>
        <Skeleton className="h-8 w-1/2 mb-2" />
        <Skeleton className="h-4 w-1/4" />
      </CardContent>
    </Card>
  )
}

export function SkeletonTable({ rows = 5, className }: { rows?: number; className?: string }) {
  return (
    <div className={cn("w-full rounded-md border", className)}>
      <div className="border-b p-4">
        <div className="flex gap-4">
          <Skeleton className="h-4 w-1/4" />
          <Skeleton className="h-4 w-1/4" />
          <Skeleton className="h-4 w-1/4" />
          <Skeleton className="h-4 w-1/4" />
        </div>
      </div>
      {Array.from({ length: rows }).map((_, i) => (
        <div key={i} className="p-4 border-b last:border-0">
          <div className="flex gap-4">
            <Skeleton className="h-4 w-1/4" />
            <Skeleton className="h-4 w-1/4" />
            <Skeleton className="h-4 w-1/4" />
            <Skeleton className="h-4 w-1/4" />
          </div>
        </div>
      ))}
    </div>
  )
}

export function SkeletonChart({ className }: { className?: string }) {
  return (
    <Card className={cn("flex flex-col justify-between p-6", className)}>
      <div className="space-y-2 mb-6">
        <Skeleton className="h-5 w-1/4" />
        <Skeleton className="h-4 w-1/3" />
      </div>
      <div className="flex items-end justify-between gap-2 h-48 mt-auto">
        {Array.from({ length: 7 }).map((_, i) => (
          <Skeleton key={i} className="w-full rounded-t-sm" style={{ height: `${[40, 75, 50, 90, 60, 30, 80][i]}%` }} />
        ))}
      </div>
    </Card>
  )
}

export function SkeletonMap({ className }: { className?: string }) {
  return (
    <div className={cn("relative w-full h-[400px] rounded-lg overflow-hidden border", className)}>
      <Skeleton className="absolute inset-0 h-full w-full rounded-none" />
      <div className="absolute top-4 left-4 space-y-2">
        <Skeleton className="h-10 w-10 rounded-md" />
        <Skeleton className="h-10 w-10 rounded-md" />
      </div>
      <div className="absolute bottom-8 right-8">
        <Skeleton className="h-6 w-32 rounded-full" />
      </div>
    </div>
  )
}

export function SkeletonList({ items = 3, className }: { items?: number; className?: string }) {
  return (
    <div className={cn("space-y-4", className)}>
      {Array.from({ length: items }).map((_, i) => (
        <div key={i} className="flex items-center space-x-4">
          <Skeleton className="h-12 w-12 rounded-full" />
          <div className="space-y-2 flex-1">
            <Skeleton className="h-4 w-[250px]" />
            <Skeleton className="h-4 w-[200px]" />
          </div>
        </div>
      ))}
    </div>
  )
}
