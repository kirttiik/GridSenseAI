"use client"

import * as React from "react"
import { Moon, Sun } from "lucide-react"
import { Badge } from "@/components/ui/badge"

export function ThemePreview({ children }: { children: React.ReactNode }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 w-full">
      <div className="rounded-md border p-6 bg-white text-slate-950 light">
        <div className="mb-4 flex items-center justify-between">
          <Badge variant="outline" className="bg-slate-100 text-slate-900 border-slate-200">
            <Sun className="w-3 h-3 mr-1" /> Light Theme
          </Badge>
        </div>
        {children}
      </div>
      <div className="rounded-md border p-6 bg-slate-950 text-slate-50 dark">
        <div className="mb-4 flex items-center justify-between">
          <Badge variant="outline" className="bg-slate-800 text-slate-300 border-slate-700">
            <Moon className="w-3 h-3 mr-1" /> Dark Theme
          </Badge>
        </div>
        {children}
      </div>
    </div>
  )
}
