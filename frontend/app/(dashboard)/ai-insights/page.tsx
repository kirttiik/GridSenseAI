"use client"

import * as React from "react"
import { PageHeader } from "@/components/layouts/PageHeader"
import { SectionHeader } from "@/components/layouts/SectionHeader"
import { AIInsightCard } from "@/components/composites/AIInsightCard"
import { KPICard } from "@/components/composites/KPICard"
import { AlertBanner } from "@/components/feedback/AlertBanner"
import { Brain, Zap, Leaf, ShieldCheck, Loader2, AlertCircle } from "lucide-react"
import { useInsights } from "@/hooks/useApi"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"

export default function AIInsightsPage() {
  const { data: insightsResp, isLoading: isInsightsLoading, isError: isInsightsError } = useInsights()

  if (isInsightsLoading) {
    return (
      <div className="flex flex-col items-center justify-center h-96 space-y-4">
        <Loader2 className="h-8 w-8 animate-spin text-primary" />
        <p className="text-muted-foreground">Loading AI Insights...</p>
      </div>
    )
  }

  if (isInsightsError) {
    return (
      <Alert variant="destructive" className="mt-8">
        <AlertCircle className="h-4 w-4" />
        <AlertTitle>Error</AlertTitle>
        <AlertDescription>
          Failed to load insights data. Ensure the backend server is running.
        </AlertDescription>
      </Alert>
    )
  }

  const rawData = insightsResp?.data || []
  
  // Categorize randomly or arbitrarily for MVP since there's no specific 'category' field
  const operationalInsights = rawData.filter((_, i) => i % 2 === 0)
  const marketInsights = rawData.filter((_, i) => i % 2 !== 0)

  const lastSyncString = rawData.length > 0 ? new Date(rawData[0].timestamp).toLocaleString() : "Never"

  return (
    <div className="flex flex-col gap-8">
      <PageHeader
        title="AI Insights & Forecasting"
        subtitle="Machine learning predictions for load, generation, and market trends"
        lastUpdated={lastSyncString}
      />

      <section>
        <AlertBanner
          variant="info"
          title="Model Update"
          description="The AI forecasting models were re-trained recently with the latest weather and grid topology data. Accuracy metrics have improved."
          dismissible
        />
      </section>

      <section>
        <SectionHeader title="Forecast Summary" />
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mt-4">
          <KPICard
            title="Forecast Accuracy (24h)"
            value="94.8"
            unit="%"
            icon={<Brain />}
            trend="up"
            trendValue="+1.2%"
            comparison="vs last week"
            variant="success"
          />
          <KPICard
            title="Predicted Peak Load"
            value="2650"
            unit="MW"
            icon={<Zap />}
            trend="neutral"
            trendValue=""
            comparison="Expected at 14:00"
            variant="warning"
          />
          <KPICard
            title="Total Insights"
            value={rawData.length.toString()}
            unit="records"
            icon={<Leaf />}
            trend="neutral"
            trendValue=""
            comparison="Database count"
            variant="success"
          />
          <KPICard
            title="Grid Vulnerability Score"
            value="Low"
            icon={<ShieldCheck />}
            trend="neutral"
            trendValue="Stable"
            comparison="Next 12 hours"
            variant="success"
          />
        </div>
      </section>

      <section className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div>
          <SectionHeader title="Operational Recommendations" />
          <div className="mt-4 flex flex-col gap-4">
            {operationalInsights.length > 0 ? (
                operationalInsights.map((insight: any, idx: number) => (
                    <AIInsightCard
                        key={idx}
                        title={insight.title}
                        summary={insight.summary}
                        severity={insight.severity as any || "info"}
                        confidence={insight.confidence}
                        recommendation={insight.recommendation || ""}
                        timestamp={new Date(insight.timestamp).toLocaleTimeString()}
                    />
                ))
            ) : (
                <div className="border border-dashed rounded-lg p-8 text-center text-muted-foreground">
                    No operational recommendations available.
                </div>
            )}
          </div>
        </div>

        <div>
          <SectionHeader title="Market Predictions" />
          <div className="mt-4 flex flex-col gap-4">
             {marketInsights.length > 0 ? (
                marketInsights.map((insight: any, idx: number) => (
                    <AIInsightCard
                        key={idx}
                        title={insight.title}
                        summary={insight.summary}
                        severity={insight.severity as any || "info"}
                        confidence={insight.confidence}
                        recommendation={insight.recommendation || ""}
                        timestamp={new Date(insight.timestamp).toLocaleTimeString()}
                    />
                ))
             ) : (
                <div className="border border-dashed rounded-lg p-8 text-center text-muted-foreground">
                    No market predictions available.
                </div>
             )}
          </div>
        </div>
      </section>
    </div>
  )
}
