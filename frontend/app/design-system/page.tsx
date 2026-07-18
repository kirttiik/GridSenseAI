import { PageContainer } from "@/components/layouts/PageContainer"
import { EmptyState } from "@/components/composites/EmptyState"
import { Component } from "lucide-react"

export default function DesignSystemIndex() {
  return (
    <PageContainer>
      <EmptyState
        icon={Component}
        title="GridSense AI Design System Playground"
        description="Select a component from the sidebar to view its interactive documentation, states, and responsive previews."
      />
    </PageContainer>
  )
}

