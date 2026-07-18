"use client"

import * as React from "react"
import { PageHeader } from "@/components/layouts/PageHeader"
import { SectionHeader } from "@/components/layouts/SectionHeader"
import { Card, CardContent } from "@/components/ui/card"
import { Separator } from "@/components/ui/separator"
import { Layers, Database, Code, Shield, Network, BrainCircuit } from "lucide-react"

export default function AboutPage() {
  return (
    <div className="flex flex-col gap-8 max-w-4xl mx-auto">
      <PageHeader
        title="About GridSense AI"
        subtitle="Enterprise Energy Intelligence Platform"
      />

      <section>
        <SectionHeader title="Project Overview" />
        <Card className="mt-4">
          <CardContent className="pt-6 text-muted-foreground space-y-4">
            <p>
              GridSense AI is a next-generation Energy Intelligence Platform designed to monitor, forecast, and optimize the Indian Power Grid. 
              By combining real-time SCADA data, meteorological inputs, and market economics, the platform provides actionable insights for Grid Operators and Energy Traders.
            </p>
            <p>
              This portfolio project demonstrates modern software engineering practices, clean architecture, and enterprise-grade design systems.
            </p>
          </CardContent>
        </Card>
      </section>

      <section>
        <SectionHeader title="Core Objectives" />
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
          <div className="p-4 border rounded-xl bg-card">
            <h4 className="font-semibold mb-2 flex items-center gap-2 text-primary">
              <BrainCircuit className="h-5 w-5" /> AI-Driven Insights
            </h4>
            <p className="text-sm text-muted-foreground">Leveraging machine learning to predict demand spikes, renewable generation drop-offs, and market price volatility.</p>
          </div>
          <div className="p-4 border rounded-xl bg-card">
            <h4 className="font-semibold mb-2 flex items-center gap-2 text-primary">
              <Network className="h-5 w-5" /> Grid Resilience
            </h4>
            <p className="text-sm text-muted-foreground">Monitoring transmission constraints and frequency deviations to maintain grid stability and prevent blackouts.</p>
          </div>
        </div>
      </section>

      <section>
        <SectionHeader title="Technology Stack" />
        <div className="mt-4 border rounded-xl bg-card overflow-hidden">
          <div className="grid grid-cols-1 md:grid-cols-3 divide-y md:divide-y-0 md:divide-x">
            <div className="p-6">
              <h4 className="font-semibold flex items-center gap-2 mb-4">
                <Code className="h-5 w-5 text-muted-foreground" /> Frontend
              </h4>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li className="flex items-center gap-2"><span>•</span> Next.js 15 (App Router)</li>
                <li className="flex items-center gap-2"><span>•</span> React 19</li>
                <li className="flex items-center gap-2"><span>•</span> TypeScript</li>
                <li className="flex items-center gap-2"><span>•</span> Tailwind CSS v4</li>
                <li className="flex items-center gap-2"><span>•</span> shadcn/ui & base-ui</li>
                <li className="flex items-center gap-2"><span>•</span> TanStack Query & Table</li>
              </ul>
            </div>
            
            <div className="p-6">
              <h4 className="font-semibold flex items-center gap-2 mb-4">
                <Layers className="h-5 w-5 text-muted-foreground" /> Architecture
              </h4>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li className="flex items-center gap-2"><span>•</span> Feature-Sliced Design (FSD)</li>
                <li className="flex items-center gap-2"><span>•</span> Custom Design System</li>
                <li className="flex items-center gap-2"><span>•</span> Token-driven theming</li>
                <li className="flex items-center gap-2"><span>•</span> Component Playgrounds</li>
                <li className="flex items-center gap-2"><span>•</span> Strict accessibility (WCAG)</li>
              </ul>
            </div>

            <div className="p-6">
              <h4 className="font-semibold flex items-center gap-2 mb-4">
                <Database className="h-5 w-5 text-muted-foreground" /> Backend (Planned)
              </h4>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li className="flex items-center gap-2"><span>•</span> FastAPI (Python)</li>
                <li className="flex items-center gap-2"><span>•</span> PostgreSQL</li>
                <li className="flex items-center gap-2"><span>•</span> TimescaleDB for time-series</li>
                <li className="flex items-center gap-2"><span>•</span> Redis caching</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <section>
        <SectionHeader title="Data Sources & Credits" />
        <Card className="mt-4">
          <CardContent className="pt-6 text-sm text-muted-foreground space-y-3">
            <p><strong>Energy Data:</strong> Simulated based on typical profiles from the Indian Power Grid and Energy Atlas.</p>
            <p><strong>Meteorological Data:</strong> Mocked representations inspired by NASA POWER (Prediction of Worldwide Energy Resources).</p>
            <Separator className="my-2" />
            <p className="flex items-center gap-2">
              <Shield className="h-4 w-4" /> 
              Designed and built as a demonstration of enterprise frontend engineering and domain-driven design.
            </p>
          </CardContent>
        </Card>
      </section>
    </div>
  )
}
