import * as React from "react"
import { cn } from "@/lib/utils"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
  DialogFooter,
  DialogClose,
} from "@/components/ui/dialog"
import { Button } from "@/components/ui/button"

export type ModalVariant = "default" | "confirmation" | "information" | "destructive"

export interface ModalProps {
  trigger?: React.ReactNode
  title?: React.ReactNode
  description?: React.ReactNode
  children?: React.ReactNode
  variant?: ModalVariant
  open?: boolean
  onOpenChange?: (open: boolean) => void
  
  // For confirmation/destructive variants
  onConfirm?: () => void
  confirmText?: string
  cancelText?: string
  isConfirmLoading?: boolean
  
  className?: string
}

export function Modal({
  trigger,
  title,
  description,
  children,
  variant = "default",
  open,
  onOpenChange,
  onConfirm,
  confirmText = "Confirm",
  cancelText = "Cancel",
  isConfirmLoading = false,
  className,
}: ModalProps) {
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      {trigger && <DialogTrigger>{trigger}</DialogTrigger>}
      <DialogContent className={cn("sm:max-w-[500px]", className)}>
        {(title || description) && (
          <DialogHeader>
            {title && <DialogTitle>{title}</DialogTitle>}
            {description && <DialogDescription>{description}</DialogDescription>}
          </DialogHeader>
        )}
        
        {children && (
          <div className="py-4">
            {children}
          </div>
        )}
        
        {variant !== "default" && (
          <DialogFooter className="sm:justify-end gap-2 mt-4 pt-4 border-t">
            {variant === "information" ? (
              <DialogClose>
                <Button type="button" variant="default">
                  OK
                </Button>
              </DialogClose>
            ) : (
              <>
                <DialogClose>
                  <Button type="button" variant="outline">
                    {cancelText}
                  </Button>
                </DialogClose>
                <Button 
                  type="button" 
                  variant={variant === "destructive" ? "destructive" : "default"}
                  onClick={onConfirm}
                  disabled={isConfirmLoading}
                >
                  {isConfirmLoading ? "Loading..." : confirmText}
                </Button>
              </>
            )}
          </DialogFooter>
        )}
      </DialogContent>
    </Dialog>
  )
}
