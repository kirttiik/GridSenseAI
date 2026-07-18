import * as React from "react"
import { cn } from "@/lib/utils"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { CheckCircle2, Info, AlertTriangle, AlertCircle, X } from "lucide-react"

export type AlertBannerVariant = "success" | "info" | "warning" | "error"

export interface AlertBannerProps extends Omit<React.HTMLAttributes<HTMLDivElement>, "title"> {
  variant: AlertBannerVariant
  title?: string
  description: React.ReactNode
  dismissible?: boolean
  onDismiss?: () => void
}

const variantConfig: Record<AlertBannerVariant, { icon: React.ElementType; styles: string }> = {
  success: { icon: CheckCircle2, styles: "border-emerald-500/50 text-emerald-600 dark:border-emerald-500 [&>svg]:text-emerald-600" },
  info: { icon: Info, styles: "border-blue-500/50 text-blue-600 dark:border-blue-500 [&>svg]:text-blue-600" },
  warning: { icon: AlertTriangle, styles: "border-amber-500/50 text-amber-600 dark:border-amber-500 [&>svg]:text-amber-600" },
  error: { icon: AlertCircle, styles: "border-rose-500/50 text-rose-600 dark:border-rose-500 [&>svg]:text-rose-600" },
}

export function AlertBanner({
  variant,
  title,
  description,
  dismissible = false,
  onDismiss,
  className,
  ...props
}: AlertBannerProps) {
  const [isVisible, setIsVisible] = React.useState(true)
  const config = variantConfig[variant]
  const Icon = config.icon

  if (!isVisible) return null

  const handleDismiss = () => {
    setIsVisible(false)
    if (onDismiss) onDismiss()
  }

  return (
    <Alert className={cn("relative", config.styles, className)} {...props}>
      <Icon className="h-4 w-4" />
      {title && <AlertTitle>{title}</AlertTitle>}
      <AlertDescription className="mt-1">
        {description}
      </AlertDescription>
      {dismissible && (
        <button
          onClick={handleDismiss}
          className="absolute right-2 top-2 rounded-md p-1 hover:bg-black/5 dark:hover:bg-white/10 transition-colors"
          aria-label="Dismiss alert"
        >
          <X className="h-4 w-4 opacity-70" />
        </button>
      )}
    </Alert>
  )
}
