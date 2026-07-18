import { useQuery } from '@tanstack/react-query';
import { ApiClient } from '@/lib/api-client';

// Interfaces for API Responses based on backend SuccessResponse
interface SuccessResponse<T> {
  status: string;
  data: T;
  message?: string;
}

export function useDashboard() {
  return useQuery({
    queryKey: ['dashboard', 'overview'],
    queryFn: () => ApiClient.get<SuccessResponse<unknown>>('/dashboard/overview'),
    refetchInterval: 30000, // Refetch every 30s
  });
}

export function useEnergy() {
  return useQuery({
    queryKey: ['energy', 'current'],
    queryFn: () => ApiClient.get<SuccessResponse<unknown[]>>('/energy/current'),
    refetchInterval: 60000,
  });
}

export function useGrid() {
  return useQuery({
    queryKey: ['grid', 'current'],
    queryFn: () => ApiClient.get<SuccessResponse<unknown[]>>('/grid/current'),
    refetchInterval: 15000,
  });
}

export function useMarket() {
  return useQuery({
    queryKey: ['market', 'current'],
    queryFn: () => ApiClient.get<SuccessResponse<unknown[]>>('/market/current'),
    refetchInterval: 60000,
  });
}

export function useWeather() {
  return useQuery({
    queryKey: ['weather', 'current'],
    queryFn: () => ApiClient.get<SuccessResponse<unknown[]>>('/weather/current'),
    refetchInterval: 300000, // Refetch every 5m
  });
}

export function useInsights() {
  return useQuery({
    queryKey: ['insights', 'current'],
    queryFn: () => ApiClient.get<SuccessResponse<unknown[]>>('/insights/current'),
    refetchInterval: 300000,
  });
}
