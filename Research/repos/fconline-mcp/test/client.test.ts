import { describe, expect, it, vi } from "vitest";
import type { AppConfig } from "../src/config.js";
import { NexonClient } from "../src/nexon/client.js";

const baseConfig: AppConfig = {
  apiBaseUrl: "https://open.api.nexon.com",
  imageBaseUrl: "https://fco.dn.nexoncdn.co.kr",
  apiKey: "dummy-key",
  metadataTtlMs: 1_000,
  httpTimeoutMs: 5_000,
  httpRetryCount: 2,
  httpRetryBaseDelayMs: 10
};

function jsonResponse(body: unknown, status: number, headers: Record<string, string> = {}) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "content-type": "application/json",
      ...headers
    }
  });
}

describe("NexonClient", () => {
  it("retries transient 429 responses on GET", async () => {
    const fetchImpl = vi
      .fn<typeof fetch>()
      .mockResolvedValueOnce(
        jsonResponse({ error: { message: "too many requests" } }, 429, {
          "retry-after": "0"
        })
      )
      .mockResolvedValueOnce(jsonResponse({ ouid: "user-1" }, 200));
    const sleep = vi.fn().mockResolvedValue(undefined);
    const client = new NexonClient(baseConfig, { fetchImpl, sleep });

    const response = await client.getUserByNickname("example");

    expect(response.ouid).toBe("user-1");
    expect(fetchImpl).toHaveBeenCalledTimes(2);
    expect(sleep).toHaveBeenCalledTimes(1);
  });
});