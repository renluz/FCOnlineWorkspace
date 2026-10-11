import { setTimeout as delay } from "node:timers/promises";
import type {
  MatchDetailResponse,
  MatchIdRecord,
  MaxDivisionResponseItem,
  RankerStatsResponseItem,
  TradeRecord,
  UserBasicResponse,
  UserResponse
} from "../types/api.js";
import type { MetadataKind, RankerPlayerInput } from "../types/domain.js";
import type { AppConfig } from "../config.js";
import { FcOnlineError } from "./errors.js";

interface RequestOptions {
  query?: Record<string, string | number | undefined>;
  requiresAuth?: boolean;
  baseUrl?: string;
  method?: "GET" | "HEAD";
}

export class NexonClient {
  private readonly fetchImpl: typeof fetch;
  private readonly sleep: (ms: number) => Promise<unknown>;

  constructor(
    private readonly config: AppConfig,
    options: {
      fetchImpl?: typeof fetch;
      sleep?: (ms: number) => Promise<unknown>;
    } = {}
  ) {
    this.fetchImpl = options.fetchImpl ?? globalThis.fetch.bind(globalThis);
    this.sleep = options.sleep ?? delay;
  }

  async getUserByNickname(nickname: string): Promise<UserResponse> {
    return this.requestJson<UserResponse>("/fconline/v1/id", {
      query: { nickname },
      requiresAuth: true
    });
  }

  async getUserBasic(ouid: string): Promise<UserBasicResponse> {
    return this.requestJson<UserBasicResponse>("/fconline/v1/user/basic", {
      query: { ouid },
      requiresAuth: true
    });
  }

  async getUserMaxDivision(ouid: string): Promise<MaxDivisionResponseItem[]> {
    return this.requestJson<MaxDivisionResponseItem[]>("/fconline/v1/user/maxdivision", {
      query: { ouid },
      requiresAuth: true
    });
  }

  async getUserMatches(params: {
    ouid: string;
    matchtype: string | number;
    offset?: number;
    limit?: number;
  }): Promise<MatchIdRecord[]> {
    return this.requestJson<MatchIdRecord[]>("/fconline/v1/user/match", {
      query: params,
      requiresAuth: true
    });
  }

  async getUserTrade(params: {
    tradetype: string;
    offset?: number;
    limit?: number;
  }): Promise<TradeRecord[]> {
    return this.requestJson<TradeRecord[]>("/fconline/v1/user/trade", {
      query: params,
      requiresAuth: true
    });
  }

  async getMatches(params: {
    matchtype: string | number;
    offset?: number;
    limit?: number;
    orderby?: string;
  }): Promise<MatchIdRecord[]> {
    return this.requestJson<MatchIdRecord[]>("/fconline/v1/match", {
      query: params,
      requiresAuth: true
    });
  }

  async getMatchDetail(matchid: string): Promise<MatchDetailResponse> {
    return this.requestJson<MatchDetailResponse>("/fconline/v1/match-detail", {
      query: { matchid },
      requiresAuth: true
    });
  }

  async getRankerStats(params: {
    matchtype: string | number;
    players: RankerPlayerInput[];
  }): Promise<RankerStatsResponseItem[]> {
    return this.requestJson<RankerStatsResponseItem[]>("/fconline/v1/ranker-stats", {
      query: {
        matchtype: params.matchtype,
        players: JSON.stringify(params.players.map((player) => ({ id: player.spId, po: player.spPosition })))
      },
      requiresAuth: true
    });
  }

  async getMetadata<T>(kind: MetadataKind): Promise<T> {
    return this.requestJson<T>(`/static/fconline/meta/${kind}.json`, {
      requiresAuth: false
    });
  }

  async checkImageExists(url: string): Promise<boolean> {
    const headResponse = await this.requestRaw(url, {
      requiresAuth: false,
      baseUrl: "",
      method: "HEAD"
    });

    if (headResponse.status === 200) {
      return true;
    }

    if (headResponse.status === 404) {
      return false;
    }

    if (headResponse.status === 405) {
      const getResponse = await this.requestRaw(url, {
        requiresAuth: false,
        baseUrl: "",
        method: "GET"
      });
      if (getResponse.status === 200) {
        return true;
      }
      if (getResponse.status === 404) {
        return false;
      }
      throw await this.createHttpError(getResponse, url);
    }

    throw await this.createHttpError(headResponse, url);
  }

  private async requestJson<T>(path: string, options: RequestOptions): Promise<T> {
    const response = await this.requestRaw(path, options);

    if (!response.ok) {
      throw await this.createHttpError(response, this.buildUrl(path, options).toString());
    }

    const text = await response.text();
    if (!text) {
      return undefined as T;
    }

    return JSON.parse(text) as T;
  }

  private async requestRaw(path: string, options: RequestOptions): Promise<Response> {
    const url = this.buildUrl(path, options);
    const method = options.method ?? "GET";
    const retryLimit = method === "GET" ? this.config.httpRetryCount : 0;

    for (let attempt = 0; attempt <= retryLimit; attempt += 1) {
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), this.config.httpTimeoutMs);

      try {
        const response = await this.fetchImpl(url, {
          method,
          headers: this.buildHeaders(options.requiresAuth ?? false),
          signal: controller.signal
        });

        clearTimeout(timeout);

        if (response.ok || !this.isTransientStatus(response.status) || attempt === retryLimit) {
          return response;
        }

        const retryAfterSeconds = this.parseRetryAfter(response.headers.get("retry-after"));
        await this.sleep(this.getRetryDelayMs(attempt, retryAfterSeconds));
      } catch (error) {
        clearTimeout(timeout);

        const isAbortError = error instanceof DOMException && error.name === "AbortError";
        if ((isAbortError || error instanceof TypeError) && attempt < retryLimit) {
          await this.sleep(this.getRetryDelayMs(attempt));
          continue;
        }

        if (error instanceof FcOnlineError) {
          throw error;
        }

        throw new FcOnlineError("UPSTREAM_ERROR", "Nexon API 요청에 실패했습니다.", {
          details: { url: url.toString(), method },
          cause: error
        });
      }
    }

    throw new FcOnlineError("UPSTREAM_ERROR", "재시도 한도를 초과했습니다.", {
      details: { url: url.toString(), method }
    });
  }

  private buildUrl(path: string, options: RequestOptions): URL {
    const baseUrl = options.baseUrl ?? this.config.apiBaseUrl;
    const url = path.startsWith("http") ? new URL(path) : new URL(path, baseUrl);

    for (const [key, value] of Object.entries(options.query ?? {})) {
      if (value !== undefined) {
        url.searchParams.set(key, String(value));
      }
    }

    return url;
  }

  private buildHeaders(requiresAuth: boolean): Headers {
    const headers = new Headers();
    if (requiresAuth) {
      headers.set("x-nxopen-api-key", this.config.apiKey);
    }

    return headers;
  }

  private async createHttpError(response: Response, url: string): Promise<FcOnlineError> {
    const text = await response.text();
    const message = this.extractErrorMessage(text) ?? `Nexon API 요청이 실패했습니다. (${response.status})`;
    const retryAfterSeconds = this.parseRetryAfter(response.headers.get("retry-after"));

    if (response.status === 429) {
      return new FcOnlineError("RATE_LIMITED", message, {
        status: response.status,
        retryAfterSeconds,
        details: { url }
      });
    }

    if (response.status === 404) {
      return new FcOnlineError("NOT_FOUND", message, {
        status: response.status,
        details: { url }
      });
    }

    return new FcOnlineError("UPSTREAM_ERROR", message, {
      status: response.status,
      details: { url }
    });
  }

  private extractErrorMessage(text: string): string | undefined {
    if (!text) {
      return undefined;
    }

    try {
      const parsed = JSON.parse(text) as {
        error?: {
          message?: string;
        };
      };
      return parsed.error?.message ?? text;
    } catch {
      return text;
    }
  }

  private isTransientStatus(status: number): boolean {
    return status === 429 || status === 500 || status === 502 || status === 503 || status === 504;
  }

  private parseRetryAfter(value: string | null): number | undefined {
    if (!value) {
      return undefined;
    }

    const numeric = Number(value);
    return Number.isFinite(numeric) ? numeric : undefined;
  }

  private getRetryDelayMs(attempt: number, retryAfterSeconds?: number): number {
    if (retryAfterSeconds !== undefined) {
      return retryAfterSeconds * 1000;
    }

    return this.config.httpRetryBaseDelayMs * 2 ** attempt;
  }
}