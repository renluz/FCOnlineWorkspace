import { describe, expect, it } from "vitest";
import { NexonMetadataService } from "../src/nexon/metadata.js";
import { FcOnlineService } from "../src/service.js";

describe("FcOnlineService ranker stats parsing", () => {
  it("accepts lowercase spid fields from raw ranker responses", async () => {
    const apiClient = createApiClient([
      {
        spid: 205331,
        spPosition: 18,
        status: createStatus(),
        createDate: "2026-03-06T01:23:45"
      }
    ]);

    const metadata = createMetadataService({
      matchtype: [{ matchtype: 50, desc: "Official" }],
      spposition: [{ spposition: 18, desc: "ST" }],
      spid: [{ id: 205331, name: "Cristiano Ronaldo" }],
      seasonid: [],
      division: [],
      "division-volta": []
    });

    const service = new FcOnlineService(apiClient as any, metadata, {
      imageBaseUrl: "https://fco.dn.nexoncdn.co.kr"
    });

    const response = await service.getRankerStatsEnriched({
      matchType: 50,
      players: [{ spId: 205331, spPosition: 18 }]
    });

    expect(response.stats).toHaveLength(1);
    expect(response.stats[0]?.spId).toBe(205331);
    expect(response.stats[0]?.resolved?.playerName).toBe("Cristiano Ronaldo");
    expect(response.stats[0]?.resolved?.positionLabel).toBe("ST");
  });

  it("also accepts id and po aliases if upstream echoes request-style keys", async () => {
    const apiClient = createApiClient([
      {
        id: 289020801,
        po: 25,
        status: createStatus(),
        createDate: "2026-03-06T01:23:45"
      }
    ]);

    const metadata = createMetadataService({
      matchtype: [{ matchtype: 50, desc: "Official" }],
      spposition: [{ spposition: 25, desc: "ST" }],
      spid: [{ id: 289020801, name: "CC Cristiano Ronaldo" }],
      seasonid: [{ seasonId: 289, className: "CC", seasonImg: "https://example.com/cc.png" }],
      division: [],
      "division-volta": []
    });

    const service = new FcOnlineService(apiClient as any, metadata, {
      imageBaseUrl: "https://fco.dn.nexoncdn.co.kr"
    });

    const response = await service.getRankerStatsEnriched({
      matchType: 50,
      players: [{ spId: 289020801, spPosition: 25 }]
    });

    expect(response.stats[0]?.spId).toBe(289020801);
    expect(response.stats[0]?.spPosition).toBe(25);
    expect(response.stats[0]?.resolved?.playerName).toBe("CC Cristiano Ronaldo");
    expect(response.stats[0]?.resolved?.seasonLabel).toBe("CC");
  });
});

function createApiClient(rankerStats: unknown[]) {
  return {
    async getUserByNickname() {
      return { ouid: "unused" };
    },
    async getUserBasic() {
      return { ouid: "unused", nickname: "unused", level: 1 };
    },
    async getUserMaxDivision() {
      return [];
    },
    async getUserMatches() {
      return [];
    },
    async getUserTrade() {
      return [];
    },
    async getMatches() {
      return [];
    },
    async getMatchDetail() {
      throw new Error("unused");
    },
    async getRankerStats() {
      return rankerStats;
    },
    async checkImageExists() {
      return true;
    }
  };
}

function createMetadataService(data: Record<string, unknown[]>) {
  return new NexonMetadataService(
    {
      async getMetadata(kind: string) {
        return data[kind] ?? [];
      }
    } as any,
    { metadataTtlMs: 60_000 }
  );
}

function createStatus() {
  return {
    shoot: 3.2,
    effectiveShoot: 1.7,
    assist: 0.4,
    goal: 1.1,
    dribble: 140.5,
    dribbleTry: 7.5,
    dribbleSuccess: 5.6,
    passTry: 18.2,
    passSuccess: 14.3,
    block: 0.2,
    tackle: 0.4,
    matchCount: 20
  };
}