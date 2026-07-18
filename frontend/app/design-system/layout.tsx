import * as React from "react"
import { Sidebar } from "@/components/design-system/navigation/Sidebar"

export default function DesignSystemLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className="flex flex-col h-full">
      <header className="flex h-16 items-center border-b px-6 bg-background">
        <div className="font-bold text-lg">GridSense AI <span className="text-muted-foreground font-normal ml-2">Design System Playground</span></div>
      </header>
      <div className="flex flex-1 overflow-hidden">
        <Sidebar />
        <main className="flex-1 overflow-y-auto bg-background">
          {children}
        </main>
      </div>
    </div>
  )
}
