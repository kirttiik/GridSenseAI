import * as React from "react"
import { Search, X } from "lucide-react"

import { cn } from "@/lib/utils"
import { Input } from "@/components/ui/input"
import { IconButton } from "@/components/ui/icon-button"

export interface SearchBoxProps extends React.InputHTMLAttributes<HTMLInputElement> {
  onClear?: () => void
}

const SearchBox = React.forwardRef<HTMLInputElement, SearchBoxProps>(
  ({ className, onClear, value, onChange, ...props }, ref) => {
    const handleClear = () => {
      if (onClear) {
        onClear()
      } else if (onChange) {
        // Create a synthetic event to clear the input
        const e = {
          target: { value: "" },
          currentTarget: { value: "" }
        } as React.ChangeEvent<HTMLInputElement>
        onChange(e)
      }
    }

    return (
      <div className={cn("relative flex w-full items-center", className)}>
        <Search className="absolute left-2.5 h-4 w-4 text-muted-foreground" aria-hidden="true" />
        <Input
          type="search"
          className="pl-9 pr-9"
          ref={ref}
          value={value}
          onChange={onChange}
          {...props}
        />
        {value && value.toString().length > 0 && (
          <IconButton
            variant="ghost"
            size="sm"
            className="absolute right-1 h-7 w-7 text-muted-foreground hover:text-foreground"
            onClick={handleClear}
            aria-label="Clear search"
          >
            <X className="h-4 w-4" />
          </IconButton>
        )}
      </div>
    )
  }
)
SearchBox.displayName = "SearchBox"

export { SearchBox }
