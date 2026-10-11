import * as z from "zod/v4";
import { FcOnlineService } from "../service.js";
import { matchTypeInputSchema, positiveIntegerSchema, registerJsonTool } from "./helpers.js";

const tradeTypeSchema = z.enum(["buy", "sell"]);
const metadataKindSchema = z.enum(["matchtype", "spid", "seasonid", "spposition", "division", "division-volta"]);
const imageTypeSchema = z.enum(["card", "action"]);
const identifierTypeSchema = z.enum(["spid", "pid"]);

export function registerRawTools(service: FcOnlineService, server: Parameters<typeof registerJsonTool>[0]["server"]) {
  registerJsonTool({
    server,
    name: "resolve_user_by_nickname",
    description: "닉네임으로 FC Online 계정 식별자(ouid)를 조회합니다.",
    inputSchema: z.object({
      nickname: z.string().min(1).describe("조회할 닉네임")
    }),
    handler: ({ nickname }) => service.resolveUserByNickname(nickname)
  });

  registerJsonTool({
    server,
    name: "get_user_basic",
    description: "ouid로 유저 기본 정보(닉네임, 레벨)를 조회합니다.",
    inputSchema: z.object({
      ouid: z.string().min(1).describe("유저 ouid")
    }),
    handler: ({ ouid }) => service.getUserBasic(ouid)
  });

  registerJsonTool({
    server,
    name: "get_user_max_division",
    description: "ouid로 유저의 역대 최고 등급을 조회합니다.",
    inputSchema: z.object({
      ouid: z.string().min(1).describe("유저 ouid")
    }),
    handler: ({ ouid }) => service.getUserMaxDivision(ouid)
  });

  registerJsonTool({
    server,
    name: "get_user_matches",
    description: "ouid와 matchType으로 유저의 매치 ID 목록을 조회합니다.",
    inputSchema: z.object({
      ouid: z.string().min(1).describe("유저 ouid"),
      matchType: matchTypeInputSchema.describe("매치 종류 코드 또는 한국어 라벨"),
      offset: positiveIntegerSchema.optional(),
      limit: z.number().int().min(1).max(100).optional()
    }),
    handler: (args) => service.getUserMatches(args)
  });

  registerJsonTool({
    server,
    name: "get_user_trade",
    description: "API 키 소유자 본인의 거래 기록만 조회합니다. 임의 ouid 조회 용도로 쓰면 안 됩니다.",
    inputSchema: z.object({
      tradetype: tradeTypeSchema.describe("buy 또는 sell"),
      offset: positiveIntegerSchema.optional(),
      limit: z.number().int().min(1).max(100).optional()
    }),
    handler: (args) => service.getUserTrade(args)
  });

  registerJsonTool({
    server,
    name: "get_matches",
    description: "전체 매치 기록에서 matchType 기준 매치 ID 목록을 조회합니다.",
    inputSchema: z.object({
      matchType: matchTypeInputSchema.describe("매치 종류 코드 또는 한국어 라벨"),
      offset: positiveIntegerSchema.optional(),
      limit: z.number().int().min(1).max(100).optional(),
      orderBy: z.enum(["asc", "desc"]).optional()
    }),
    handler: (args) => service.getMatches(args)
  });

  registerJsonTool({
    server,
    name: "get_match_detail",
    description: "matchId로 매치 상세 정보를 정규화해서 조회합니다.",
    inputSchema: z.object({
      matchId: z.string().min(1).describe("매치 ID")
    }),
    handler: ({ matchId }) => service.getMatchDetail(matchId)
  });

  registerJsonTool({
    server,
    name: "get_ranker_stats",
    description: "TOP 10,000 랭커 평균 스탯을 선수/포지션 목록 기준으로 조회합니다.",
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
        .describe("선수/포지션 목록")
    }),
    handler: (args) => service.getRankerStats(args)
  });

  registerJsonTool({
    server,
    name: "get_metadata",
    description: "FC Online 메타데이터를 종류별로 조회하거나 특정 항목을 lookup 합니다.",
    inputSchema: z.object({
      kind: metadataKindSchema.describe("메타데이터 종류"),
      lookup: z.union([z.string(), z.number()]).optional().describe("특정 항목 lookup 값")
    }),
    handler: ({ kind, lookup }) => service.getMetadata(kind, lookup)
  });

  registerJsonTool({
    server,
    name: "get_player_image_url",
    description: "선수 카드 이미지 또는 액션 이미지 URL을 생성하고, 필요하면 CDN 존재 여부를 확인합니다.",
    inputSchema: z.object({
      imageType: imageTypeSchema.describe("card 또는 action"),
      identifierType: identifierTypeSchema.describe("spid 또는 pid"),
      value: z.union([z.string(), z.number()]).describe("spid 또는 pid 값"),
      verifyExists: z.boolean().optional(),
      strict: z.boolean().optional()
    }),
    handler: (args) => service.getPlayerImageUrl(args)
  });
}