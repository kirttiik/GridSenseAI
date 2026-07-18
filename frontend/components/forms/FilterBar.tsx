import * as React from "react"
import { cn } from "@/lib/utils"
import { SearchBar } from "./SearchBar"
import { Button } from "@/components/ui/button"
import { Filter, SlidersHorizontal, RotateCcw } from "lucide-react"

export interface FilterBarProps extends React.HTMLAttributes<HTMLDivElement> {
  searchPlaceholder?: string
  searchValue?: string
  onSearchChange?: (e: React.ChangeEvent<HTMLInputElement>) => void
  onSearchClear?: () => void
  
  // Custom filter controls passed as children
  filters?: React.ReactNode
  
  onReset?: () => void
  onApply?: () => void
  
  isMobile?: boolean // If true, we might render a responsive version
}

export function FilterBar({
  searchPlaceholder = "Search...",
  searchValue,
  onSearchChange,
  onSearchClear,
  filters,
  onReset,
  onApply,
  className,
  ...props
}: FilterBarProps) {
  return (
    <div className={cn("flex flex-col md:flex-row md:items-center gap-3 w-full bg-background p-3 border rounded-lg", className)} {...props}>
      <div className="flex-1 min-w-[200px]">
        <SearchBar 
          placeholder={searchPlaceholder} 
          value={searchValue} 
          onChange={onSearchChange} 
          onClear={onSearchClear} 
        />
      </div>
      
      {filters && (
        <div className="flex items-center gap-2 overflow-x-auto pb-1 md:pb-0 scrollbar-hide">
          <div className="hidden md:flex items-center text-muted-foreground mr-1">
            <Filter className="h-4 w-4 mr-1" />
            <span className="text-xs font-medium">Filters:</span>
          </div>
          {filters}
        </div>
      )}
      
      <div className="flex items-center justify-end gap-2 mt-2 md:mt-0">
        <Button variant="outline" size="sm" onClick={onReset} className="h-9">
          <RotateCcw className="h-4 w-4 mr-2" />
          Reset
        </Button>
        <Button size="sm" onClick={onApply} className="h-9">
          <SlidersHorizontal className="h-4 w-4 mr-2" />
          Apply
        </Button>
      </div>
    </div>
  )
}
