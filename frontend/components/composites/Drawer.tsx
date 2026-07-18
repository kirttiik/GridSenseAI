import * as React from "react"
import { cn } from "@/lib/utils"
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
  SheetFooter,
  SheetClose,
} from "@/components/ui/sheet"
import { Button } from "@/components/ui/button"

export type DrawerSize = "sm" | "default" | "md" | "lg" | "xl" | "full"
export type DrawerSide = "top" | "right" | "bottom" | "left"

export interface DrawerProps {
  trigger?: React.ReactNode
  title?: React.ReactNode
  description?: React.ReactNode
  children: React.ReactNode
  footer?: React.ReactNode
  side?: DrawerSide
  size?: DrawerSize
  open?: boolean
  onOpenChange?: (open: boolean) => void
  showCloseButton?: boolean
}

const sizeConfig: Record<DrawerSize, string> = {
  sm: "sm:max-w-sm",
  default: "sm:max-w-md",
  md: "sm:max-w-lg",
  lg: "sm:max-w-xl",
  xl: "sm:max-w-2xl",
  full: "sm:max-w-full",
}

export function Drawer({
  trigger,
  title,
  description,
  children,
  footer,
  side = "right",
  size = "default",
  open,
  onOpenChange,
  showCloseButton = true,
}: DrawerProps) {
  return (
    <Sheet open={open} onOpenChange={onOpenChange}>
      {trigger && <SheetTrigger>{trigger}</SheetTrigger>}
      <SheetContent side={side} className={cn("flex flex-col h-full overflow-hidden", sizeConfig[size])}>
        {(title || description) && (
          <SheetHeader className="pb-4 border-b">
            {title && <SheetTitle>{title}</SheetTitle>}
            {description && <SheetDescription>{description}</SheetDescription>}
          </SheetHeader>
        )}
        
        <div className="flex-1 overflow-y-auto py-4">
          {children}
        </div>
        
        {footer && (
          <SheetFooter className="pt-4 border-t mt-auto">
            {footer}
            {showCloseButton && !footer && (
              <SheetClose>
                <Button type="button" variant="outline">
                  Close
                </Button>
              </SheetClose>
            )}
          </SheetFooter>
        )}
      </SheetContent>
    </Sheet>
  )
}
