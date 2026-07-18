import * as React from "react"
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"

interface SplitLayoutProps {
  leftPanel: React.ReactNode
  rightPanel: React.ReactNode
  defaultLayout?: [number, number]
  className?: string
}

export function SplitLayout({
  leftPanel,
  rightPanel,
  defaultLayout = [30, 70],
  className,
}: SplitLayoutProps) {
  return (
    <ResizablePanelGroup
      orientation="horizontal"
      className={className}
    >
      <ResizablePanel defaultSize={defaultLayout[0]} minSize={20}>
        <div className="h-full flex flex-col p-4">{leftPanel}</div>
      </ResizablePanel>
      <ResizableHandle withHandle />
      <ResizablePanel defaultSize={defaultLayout[1]} minSize={30}>
        <div className="h-full flex flex-col p-4">{rightPanel}</div>
      </ResizablePanel>
    </ResizablePanelGroup>
  )
}
