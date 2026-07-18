import * as React from "react"
import { cn } from "@/lib/utils"
import { Search, X, Loader2 } from "lucide-react"
import { Input } from "@/components/ui/input"

export interface SearchBarProps extends React.InputHTMLAttributes<HTMLInputElement> {
  onClear?: () => void
  isLoading?: boolean
  shortcut?: string
}

export const SearchBar = React.forwardRef<HTMLInputElement, SearchBarProps>(
  ({ className, onClear, isLoading, shortcut, value, onChange, ...props }, ref) => {
    return (
      <div className={cn("relative flex items-center w-full", className)}>
        <Search className="absolute left-3 h-4 w-4 text-muted-foreground" />
        <Input
          ref={ref}
          value={value}
          onChange={onChange}
          className={cn(
            "pl-9 pr-12 w-full", 
            shortcut && !value ? "pr-16" : ""
          )}
          {...props}
        />
        
        <div className="absolute right-3 flex items-center gap-1.5">
          {isLoading ? (
            <Loader2 className="h-4 w-4 animate-spin text-muted-foreground" />
          ) : (
            <>
              {value && onClear && (
                <button
                  type="button"
                  onClick={onClear}
                  className="h-5 w-5 rounded-sm hover:bg-muted flex items-center justify-center text-muted-foreground hover:text-foreground focus:outline-none focus:ring-2 focus:ring-ring"
                >
                  <X className="h-3.5 w-3.5" />
                  <span className="sr-only">Clear search</span>
                </button>
              )}
              {shortcut && !value && (
                <kbd className="pointer-events-none inline-flex h-5 select-none items-center gap-1 rounded border bg-muted px-1.5 font-mono text-[10px] font-medium text-muted-foreground opacity-100">
                  {shortcut}
                </kbd>
              )}
            </>
          )}
        </div>
      </div>
    )
  }
)

SearchBar.displayName = "SearchBar"
