import * as z from "zod/v4";
import { FcOnlineService } from "../service.js";
import { matchTypeInputSchema, positiveIntegerSchema, registerJsonTool } from "./helpers.js";

export function registerCompositeTools(service: FcOnlineService, server: Parameters<typeof registerJsonTool>[0]["server"]) {
  registerJsonTool({
    server,
    name: "get_user_profile_summary_by_nickname",
    description: "닉네임 기준으로 유저 기본 정보와 역대 최고 등급을 한 번에 조회합니다.",
    inputSchema: z.object({
      nickname: z.string().min(1).describe("조회할 닉네임")
    }),
    handler: ({ nickname }) => service.getUserProfileSummaryByNickname(nickname)
  });

  registerJsonTool({
    server,
    name: "get_user_match_history_by_nickname",
    description: "닉네임 기준 최근 경기 목록을 가져오고 승무패/득실점 요약까지 함께 반환합니다.",
    inputSchema: z.object({
      nickname: z.string().min(1).describe("조회할 닉네임"),
      matchType: matchTypeInputSchema.describe("매치 종류 코드 또는 한국어 라벨"),
      offset: positiveIntegerSchema.optional(),
      limit: z.number().int().min(1).max(20).optional()
    }),
    handler: (args) => service.getUserMatchHistoryByNickname(args)
  });

  registerJsonTool({
    server,
    name: "summarize_user_recent_matches_by_nickname",
    description: "닉네임 기준 최근 경기 요약과 인사이트를 반환합니다.",
    inputSchema: z.object({
      nickname: z.string().min(1).describe("조회할 닉네임"),
      matchType: matchTypeInputSchema.describe("매치 종류 코드 또는 한국어 라벨"),
      limit: z.number().int().min(1).max(10).optional()
    }),
    handler: (args) => service.summarizeUserRecentMatchesByNickname(args)
  });

  registerJsonTool({
    server,
    name: "get_match_detail_enriched",
    description: "matchId 상세 정보에 선수명, 포지션, 시즌명, 슈팅 시간 디코드 등을 보강해서 반환합니다.",
    inputSchema: z.object({
      matchId: z.string().min(1).describe("매치 ID")
    }),
    handler: ({ matchId }) => service.getMatchDetailEnriched(matchId)
  });

  registerJsonTool({
    server,
    name: "get_ranker_stats_enriched",
    description: "랭커 평균 스탯 조회 결과에 선수명, 시즌명, 포지션명을 보강해서 반환합니다.",
    inputSchema: z.object({
      matchType: matchTypeInputSchema.describe("매치 종류 코드 또는 한국어 라벨"),
      players: z
        .array(
          z.object({
            spId: z.number().int().positive(),
            spPosition: z.number().int().min(0)
          })
        )
        .min(1)
        .max(50)
    }),
    handler: (args) => service.getRankerStatsEnriched(args)
  });
}