// src/lib/api-client.ts (frontend)
// Centralized API Client

const BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "https://gridsenseai-63wk.onrender.com/api/v1";

export class ApiClient {
  static async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    const url = `${BASE_URL}${endpoint}`;
    
    // Default headers
    const headers = new Headers(options.headers);
    headers.set("Content-Type", "application/json");

    // We can add auth token interception here from zustand or cookies
    
    const config: RequestInit = {
      ...options,
      headers,
    };

    const response = await fetch(url, config);
    if (!response.ok) {
      const errorData = await response.json().catch(() => null);
      throw new Error(errorData?.detail || "An error occurred");
    }

    // Attempt to return JSON, otherwise return null
    return response.json().catch(() => null) as Promise<T>;
  }

  static get<T>(endpoint: string, options?: RequestInit) {
    return this.request<T>(endpoint, { ...options, method: "GET" });
  }

  static post<T>(endpoint: string, data?: unknown, options?: RequestInit) {
    return this.request<T>(endpoint, {
      ...options,
      method: "POST",
      body: JSON.stringify(data),
    });
  }

  static put<T>(endpoint: string, data?: unknown, options?: RequestInit) {
    return this.request<T>(endpoint, {
      ...options,
      method: "PUT",
      body: JSON.stringify(data),
    });
  }

  static delete<T>(endpoint: string, options?: RequestInit) {
    return this.request<T>(endpoint, { ...options, method: "DELETE" });
  }
}
