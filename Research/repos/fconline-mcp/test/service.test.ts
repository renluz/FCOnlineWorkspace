import { describe, expect, it } from "vitest";
import { NexonMetadataService } from "../src/nexon/metadata.js";
import { FcOnlineService } from "../src/service.js";

describe("FcOnlineService", () => {
  it("summarizes match history even when opponent participant data is missing", async () => {
    const apiClient = {
      async getUserByNickname() {
        return { ouid: "user-1" };
      },
      async getUserBasic() {
        return { ouid: "user-1", nickname: "example", level: 123 };
      },
      async getUserMatches() {
        return [{ matchId: "match-1" }];
      },
      async getMatchDetail() {
        return {
          matchId: "match-1",
          matchDate: "2026-03-06T01:23:45",
          matchType: 50,
          matchInfo: [
            {
              ouid: "user-1",
              nickname: "example",
              matchDetail: {
                seasonId: 100,
                matchResult: "승",
                matchEndType: 0,
                systemPause: 0,
                foul: 0,
                injury: 0,
                redCards: 0,
                yellowCards: 0,
                dribble: 10,
                cornerKick: 1,
                possession: 54,
                OffsideCount: 0,
                averageRating: 1.2,
                controller: "keyboard"
              },
              shoot: {
                shootTotal: 8,
                effectiveShootTotal: 5,
                shootOutScore: 0,
                goalTotal: 2,
                goalTotalDisplay: 2,
                ownGoal: 0,
                shootHeading: 0,
                goalHeading: 0,
                shootFreekick: 0,
                goalFreekick: 0,
                shootInPenalty: 8,
                goalInPenalty: 2,
                shootOutPenalty: 0,
                goalOutPenalty: 0,
                shootPenaltyKick: 0,
                goalPenaltyKick: 0,
                shootDetail: []
              },
              pass: {
                passTry: 100,
                passSuccess: 89,
                shortPassTry: 60,
                shortPassSuccess: 55,
                longPassTry: 10,
                longPassSuccess: 9,
                bouncingLobPassTry: 0,
                bouncingLobPassSuccess: 0,
                drivenGroundPassTry: 15,
                drivenGroundPassSuccess: 14,
                throughPassTry: 10,
                throughPassSuccess: 9,
                lobbedThroughPassTry: 5,
                lobbedThroughPassSuccess: 2
              },
              defence: {
                blockTry: 3,
                blockSuccess: 1,
                tackleTry: 4,
                tackleSuccess: 2
              },
              player: []
            }
          ]
        };
      },
      async getUserMaxDivision() {
        return [];
      },
      async getUserTrade() {
        return [];
      },
      async getMatches() {
        return [];
      },
      async getRankerStats() {
        return [];
      },
      async checkImageExists() {
        return true;
      }
    };

    const metadataClient = {
      async getMetadata(kind: string) {
        switch (kind) {
          case "matchtype":
            return [{ matchtype: 50, desc: "공식경기" }];
          case "seasonid":
            return [{ seasonId: 100, className: "ICON", seasonImg: "https://example.com/icon.png" }];
          case "spid":
          case "spposition":
          case "division":
          case "division-volta":
          default:
            return [];
        }
      }
    };

    const metadata = new NexonMetadataService(metadataClient as any, { metadataTtlMs: 60_000 });
    const service = new FcOnlineService(apiClient as any, metadata, {
      imageBaseUrl: "https://fco.dn.nexoncdn.co.kr"
    });

    const response = await service.getUserMatchHistoryByNickname({
      nickname: "example",
      matchType: "공식경기",
      limit: 1
    });

    expect(response.summary.wins).toBe(1);
    expect(response.summary.goalsAgainst).toBe(0);
    expect(response.matches[0]?.opponent).toBeNull();
    expect(response.matches[0]?.score.for).toBe(2);
  });

  it("normalizes pid image paths by removing leading zeros", async () => {
    const apiClient = {
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
        return [];
      },
      async checkImageExists() {
        return true;
      }
    };

    const metadata = new NexonMetadataService({ getMetadata: async () => [] } as any, { metadataTtlMs: 60_000 });
    const service = new FcOnlineService(apiClient as any, metadata, {
      imageBaseUrl: "https://fco.dn.nexoncdn.co.kr"
    });

    const response = await service.getPlayerImageUrl({
      imageType: "card",
      identifierType: "pid",
      value: "000401",
      verifyExists: false
    });

    expect(response.image.normalizedValue).toBe("401");
    expect(response.image.url.endsWith("/players/p401.png")).toBe(true);
  });
});