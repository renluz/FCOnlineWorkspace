import { FcOnlineError } from "./nexon/errors.js";

export interface AppConfig {
  apiBaseUrl: string;
  imageBaseUrl: string;
  apiKey: string;
  metadataTtlMs: number;
  httpTimeoutMs: number;
  httpRetryCount: number;
  httpRetryBaseDelayMs: number;
}

export function loadConfig(env: NodeJS.ProcessEnv = process.env): AppConfig {
  const apiKey = env.NEXON_OPEN_API_KEY?.trim();
  if (!apiKey) {
    throw new FcOnlineError("CONFIG_ERROR", "환경변수 NEXON_OPEN_API_KEY 가 필요합니다.");
  }

  return {
    apiBaseUrl: "https://open.api.nexon.com",
    imageBaseUrl: "https://fco.dn.nexoncdn.co.kr",
    apiKey,
    metadataTtlMs: parseInteger(env.FCONLINE_METADATA_TTL_MS, 15 * 60 * 1000),
    httpTimeoutMs: parseInteger(env.FCONLINE_HTTP_TIMEOUT_MS, 10_000),
    httpRetryCount: parseInteger(env.FCONLINE_HTTP_RETRY_COUNT, 2),
    httpRetryBaseDelayMs: parseInteger(env.FCONLINE_HTTP_RETRY_BASE_DELAY_MS, 500)
  };
}

function parseInteger(value: string | undefined, fallback: number): number {
  if (!value) {
    return fallback;
  }

  const parsed = Number(value);
  if (!Number.isInteger(parsed) || parsed < 0) {
    throw new FcOnlineError("CONFIG_ERROR", "정수 환경변수 값이 올바르지 않습니다.", {
      details: {
        value,
        fallback
      }
    });
  }

  return parsed;
}