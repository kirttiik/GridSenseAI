import { useQuery } from '@tanstack/react-query';
import { ApiClient } from '@/lib/api-client';

export interface AnalyticsFilter {
  start_date?: string | null;
  end_date?: string | null;
  state?: string | null;
  region?: string | null;
  fuel?: string | null;
  market_type?: string | null;
  resolution?: string;
}

export function useGenerationMixAnalytics(filters: AnalyticsFilter) {
  return useQuery({
    queryKey: ['analytics', 'mix', filters],
    queryFn: () => ApiClient.post<any>('/energy/analytics/mix', filters),
    refetchInterval: 60000,
  });
}

export function useGridHealthAnalytics(filters: AnalyticsFilter) {
  return useQuery({
    queryKey: ['analytics', 'health', filters],
    queryFn: () => ApiClient.post<any>('/grid/analytics/health', filters),
    refetchInterval: 60000,
  });
}

export function useMarketTrendsAnalytics(filters: AnalyticsFilter) {
  return useQuery({
    queryKey: ['analytics', 'trends', filters],
    queryFn: () => ApiClient.post<any>('/market/analytics/trends', filters),
    refetchInterval: 60000,
  });
}
