import * as React from "react"
import { cn } from "@/lib/utils"

interface PageContainerProps extends React.HTMLAttributes<HTMLDivElement> {
  children: React.ReactNode
  fluid?: boolean
}

export function PageContainer({
  children,
  fluid = false,
  className,
  ...props
}: PageContainerProps) {
  return (
    <div
      className={cn(
        "mx-auto w-full space-y-8 p-4 md:p-6 lg:p-8 animate-in fade-in-50",
        fluid ? "max-w-none" : "max-w-7xl",
        className
      )}
      {...props}
    >
      {children}
    </div>
  )
}
