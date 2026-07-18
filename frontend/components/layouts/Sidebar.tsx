import Link from "next/link";
import { LayoutDashboard, LineChart, Map, Zap, Settings, LogOut, Battery, Cloud, Brain, Info } from "lucide-react";

const navigation = [
  { name: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
  { name: "Energy", href: "/energy", icon: Battery },
  { name: "Grid", href: "/grid", icon: Zap },
  { name: "Market", href: "/market", icon: LineChart },
  { name: "Weather", href: "/weather", icon: Cloud },
  { name: "GIS", href: "/gis", icon: Map },
  { name: "AI Insights", href: "/ai-insights", icon: Brain },
  { name: "About", href: "/about", icon: Info },
];

export function Sidebar() {
  return (
    <div className="flex h-full w-64 flex-col border-r bg-sidebar text-sidebar-foreground">
      <div className="flex h-16 shrink-0 items-center px-6 font-semibold text-lg border-b">
        GridSense AI
      </div>
      <div className="flex flex-1 flex-col overflow-y-auto pt-4">
        <nav className="flex-1 space-y-1 px-3">
          {navigation.map((item) => {
            const Icon = item.icon;
            return (
              <Link
                key={item.name}
                href={item.href}
                className="group flex items-center rounded-md px-3 py-2 text-sm font-medium hover:bg-sidebar-accent hover:text-sidebar-accent-foreground"
              >
                <Icon className="mr-3 h-5 w-5 flex-shrink-0" aria-hidden="true" />
                {item.name}
              </Link>
            );
          })}
        </nav>
      </div>
      <div className="flex shrink-0 border-t p-4">
        <button className="group block w-full shrink-0">
          <div className="flex items-center hover:opacity-80 transition-opacity">
            <div>
              <LogOut className="inline-block h-5 w-5" />
            </div>
            <div className="ml-3">
              <p className="text-sm font-medium">Log out</p>
            </div>
          </div>
        </button>
      </div>
    </div>
  );
}
