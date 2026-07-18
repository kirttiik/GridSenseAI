"use client"

import * as React from "react"
import { useRouter } from "next/navigation"
import { Search as SearchIcon } from "lucide-react"
import {
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command"

export function Search() {
  const [open, setOpen] = React.useState(false)
  const router = useRouter()

  React.useEffect(() => {
    const down = (e: KeyboardEvent) => {
      if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
        e.preventDefault()
        setOpen((open) => !open)
      }
    }

    document.addEventListener("keydown", down)
    return () => document.removeEventListener("keydown", down)
  }, [])

  const runCommand = React.useCallback((command: () => unknown) => {
    setOpen(false)
    command()
  }, [])

  return (
    <>
      <button
        onClick={() => setOpen(true)}
        className="inline-flex items-center justify-between whitespace-nowrap transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 border border-input bg-transparent shadow-sm hover:bg-accent hover:text-accent-foreground rounded-md px-3 h-9 text-sm w-full lg:w-64 mb-4 text-muted-foreground"
      >
        <span className="flex items-center">
          <SearchIcon className="mr-2 h-4 w-4" />
          Search components...
        </span>
        <kbd className="pointer-events-none inline-flex h-5 select-none items-center gap-1 rounded border bg-muted px-1.5 font-mono text-[10px] font-medium text-muted-foreground opacity-100">
          <span className="text-xs">⌘</span>K
        </kbd>
      </button>
      <CommandDialog open={open} onOpenChange={setOpen}>
        <CommandInput placeholder="Type a command or search..." />
        <CommandList>
          <CommandEmpty>No results found.</CommandEmpty>
          <CommandGroup heading="Foundations">
            <CommandItem onSelect={() => runCommand(() => router.push("/design-system/foundations/colors"))}>Colors</CommandItem>
            <CommandItem onSelect={() => runCommand(() => router.push("/design-system/foundations/typography"))}>Typography</CommandItem>
          </CommandGroup>
          <CommandGroup heading="Components">
            <CommandItem onSelect={() => runCommand(() => router.push("/design-system/primitives/buttons"))}>Buttons</CommandItem>
            <CommandItem onSelect={() => runCommand(() => router.push("/design-system/primitives/inputs"))}>Inputs</CommandItem>
            <CommandItem onSelect={() => runCommand(() => router.push("/design-system/forms/search"))}>Search Box</CommandItem>
            <CommandItem onSelect={() => runCommand(() => router.push("/design-system/forms/date-picker"))}>Date Picker</CommandItem>
            <CommandItem onSelect={() => runCommand(() => router.push("/design-system/composites/metric-cards"))}>Metric Cards</CommandItem>
          </CommandGroup>
        </CommandList>
      </CommandDialog>
    </>
  )
}
