"use client"

import * as React from "react"
import Link from "next/link"
import { usePathname } from "next/navigation"
import { cn } from "@/lib/utils"
import { Search } from "./Search"

const navigation = [
  {
    title: "Foundations",
    items: [
      { title: "Colors", href: "/design-system/foundations/colors" },
      { title: "Typography", href: "/design-system/foundations/typography" },
      { title: "Spacing", href: "/design-system/foundations/spacing" },
      { title: "Radius", href: "/design-system/foundations/radius" },
      { title: "Elevation", href: "/design-system/foundations/elevation" },
      { title: "Motion", href: "/design-system/foundations/motion" },
    ],
  },
  {
    title: "Layouts",
    items: [
      { title: "Page Container", href: "/design-system/layouts/page-container" },
      { title: "Page Header", href: "/design-system/layouts/page-header" },
      { title: "Section Header", href: "/design-system/layouts/section-header" },
      { title: "Panels", href: "/design-system/layouts/panels" },
      { title: "Split Layout", href: "/design-system/layouts/split-layout" },
    ],
  },
  {
    title: "Primitives",
    items: [
      { title: "Buttons", href: "/design-system/primitives/buttons" },
      { title: "Inputs", href: "/design-system/primitives/inputs" },
      { title: "Badges", href: "/design-system/primitives/badges" },
      { title: "Status Badges", href: "/design-system/feedback/status-badges" },
    ],
  },
  {
    title: "Forms & Filtering",
    items: [
      { title: "Search Box", href: "/design-system/forms/search" },
      { title: "Search Bar", href: "/design-system/forms/search-bar" },
      { title: "Filter Bar", href: "/design-system/forms/filter-bar" },
      { title: "Multi Select", href: "/design-system/forms/multi-select" },
      { title: "Date Picker", href: "/design-system/forms/date-picker" },
    ],
  },
  {
    title: "Data Display",
    items: [
      { title: "Metric Cards", href: "/design-system/composites/metric-cards" },
      { title: "KPI Cards", href: "/design-system/composites/kpi-cards" },
      { title: "Statistic Rows", href: "/design-system/composites/statistic-rows" },
      { title: "Timelines", href: "/design-system/composites/timelines" },
      { title: "AI Insights", href: "/design-system/composites/ai-insights" },
      { title: "Data Tables", href: "/design-system/composites/data-tables" },
    ],
  },
  {
    title: "Feedback & Overlays",
    items: [
      { title: "Empty States", href: "/design-system/composites/empty-states" },
      { title: "Loading", href: "/design-system/composites/loading" },
      { title: "Skeletons", href: "/design-system/feedback/loading-states" },
      { title: "Alerts", href: "/design-system/feedback/alerts" },
      { title: "Alert Banners", href: "/design-system/feedback/alert-banners" },
      { title: "Drawers", href: "/design-system/overlays/drawers" },
      { title: "Modals", href: "/design-system/overlays/modals" },
    ],
  },
  {
    title: "Visualizations",
    items: [
      { title: "Chart Wrappers", href: "/design-system/charts/wrappers" },
      { title: "Map Containers", href: "/design-system/gis/map-containers" },
    ],
  },
  {
    title: "Resources",
    items: [
      { title: "Release Notes", href: "/design-system/release-notes" },
    ],
  },
]

export function Sidebar() {
  const pathname = usePathname()

  return (
    <div className="w-64 border-r bg-muted/30 h-[calc(100vh-theme(spacing.16))] overflow-y-auto hidden md:block">
      <div className="p-4 border-b bg-muted/10">
        <Search />
      </div>
      <div className="py-4">
        {navigation.map((group) => (
          <div key={group.title} className="pb-6">
            <h4 className="mb-1 rounded-md px-4 py-1 text-sm font-semibold">
              {group.title}
            </h4>
            <div className="grid grid-flow-row auto-rows-max text-sm">
              {group.items.map((item) => (
                <Link
                  key={item.href}
                  href={item.href}
                  className={cn(
                    "group flex w-full items-center rounded-md border border-transparent px-4 py-1.5 hover:underline",
                    pathname === item.href
                      ? "font-medium text-foreground bg-muted"
                      : "text-muted-foreground"
                  )}
                >
                  {item.title}
                </Link>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

