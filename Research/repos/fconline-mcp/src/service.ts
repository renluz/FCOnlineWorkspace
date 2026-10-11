import type {
  ApiMatchInfo,
  ApiMatchPlayer,
  ApiMatchShootDetail,
  MatchDetailResponse,
  MatchIdRecord,
  MaxDivisionResponseItem,
  RankerStatsResponseItem,
  TradeRecord,
  UserBasicResponse,
  UserResponse
} from "./types/api.js";
import type { AppConfig } from "./config.js";
import type { MatchHistoryItem, MetadataKind, RankerPlayerInput } from "./types/domain.js";
import { buildRecentMatchInsights, buildResponseMeta, controllerToLabel, matchEndTypeToLabel, summarizeMatchHistory } from "./nexon/formatters.js";
import { FcOnlineError } from "./nexon/errors.js";
import { NexonMetadataService } from "./nexon/metadata.js";
import {
  asArray,
  coerceBoolean,
  coerceNumber,
  coerceString,
  computeRate,
  createDualTimestamp,
  decodeGoalTime,
  extractPidFromSpid,
  normalizePid
} from "./nexon/normalizers.js";
import { NexonClient } from "./nexon/client.js";

export class FcOnlineService {
  constructor(
    private readonly client: Pick<
      NexonClient,
      | "getUserByNickname"
      | "getUserBasic"
      | "getUserMaxDivision"
      | "getUserMatches"
      | "getUserTrade"
      | "getMatches"
      | "getMatchDetail"
      | "getRankerStats"
      | "checkImageExists"
    >,
    private readonly metadata: NexonMetadataService,
    private readonly config: Pick<AppConfig, "imageBaseUrl">
  ) {}

  async resolveUserByNickname(nickname: string) {
    const resolved = await this.client.getUserByNickname(nickname);
    return {
      ok: true,
      query: { nickname },
      user: this.normalizeUserResponse(resolved),
      meta: buildResponseMeta()
    };
  }

  async getUserBasic(ouid: string) {
    const basic = await this.client.getUserBasic(ouid);
    return {
      ok: true,
      query: { ouid },
      user: this.normalizeUserBasic(basic),
      meta: buildResponseMeta()
    };
  }

  async getUserMaxDivision(ouid: string) {
    const [basic, maxDivisions] = await Promise.all([
      this.client.getUserBasic(ouid),
      this.client.getUserMaxDivision(ouid)
    ]);

    const entries = await Promise.all(maxDivisions.map((item) => this.mapMaxDivision(item)));

    return {
      ok: true,
      query: { ouid },
      user: this.normalizeUserBasic(basic),
      maxDivisions: entries,
      meta: buildResponseMeta()
    };
  }

  async getUserMatches(params: {
    ouid: string;
    matchType: string | number;
    offset?: number;
    limit?: number;
  }) {
    const resolvedMatchType = await this.metadata.resolveMatchType(params.matchType);
    const records = await this.client.getUserMatches({
      ouid: params.ouid,
      matchtype: resolvedMatchType.code,
      offset: params.offset,
      limit: params.limit
    });

    return {
      ok: true,
      query: {
        ouid: params.ouid,
        matchTypeInput: params.matchType,
        resolvedMatchType,
        offset: params.offset ?? 0,
        limit: params.limit ?? 20
      },
      matchIds: this.normalizeMatchIdRecords(records),
      meta: buildResponseMeta()
    };
  }

  async getUserTrade(params: {
    tradetype: "buy" | "sell";
    offset?: number;
    limit?: number;
  }) {
    const records = await this.client.getUserTrade(params);
    const trades = await Promise.all(records.map((record) => this.mapTrade(record)));

    return {
      ok: true,
      query: {
        tradetype: params.tradetype,
        offset: params.offset ?? 0,
        limit: params.limit ?? 20
      },
      restriction: {
        isSelfOnly: true,
        message: "user/trade ???얜챷苑??API ????????癰귣챷???椰꾧퀡??疫꿸퀡以됵쭕?鈺곌퀬???????됰뮸??덈뼄. ?袁⑹벥 ouid 鈺곌퀬???袁㏓럡嚥??????롢늺 ????몃빍??"
      },
      trades,
      meta: buildResponseMeta()
    };
  }

  async getMatches(params: {
    matchType: string | number;
    offset?: number;
    limit?: number;
    orderBy?: "asc" | "desc";
  }) {
    const resolvedMatchType = await this.metadata.resolveMatchType(params.matchType);
    const records = await this.client.getMatches({
      matchtype: String(resolvedMatchType.code),
      offset: params.offset,
      limit: params.limit,
      orderby: params.orderBy ?? "desc"
    });

    return {
      ok: true,
      query: {
        matchTypeInput: params.matchType,
        resolvedMatchType,
        offset: params.offset ?? 0,
        limit: params.limit ?? 20,
        orderBy: params.orderBy ?? "desc"
      },
      matchIds: this.normalizeMatchIdRecords(records),
      meta: buildResponseMeta()
    };
  }

  async getMatchDetail(matchId: string) {
    const detail = await this.client.getMatchDetail(matchId);
    const resolvedMatchType = await this.metadata.resolveMatchType(coerceNumber(detail.matchType, "matchType"));
    const timestamps = createDualTimestamp(detail.matchDate);
    const participants = await Promise.all(asArray(detail.matchInfo).map((participant) => this.mapParticipantCore(participant)));

    return {
      ok: true,
      query: { matchId },
      match: {
        matchId: detail.matchId,
        matchDateUtc: timestamps.utc,
        matchDateKst: timestamps.kst,
        matchType: resolvedMatchType,
        participantCount: participants.length,
        participants
      },
      meta: buildResponseMeta()
    };
  }

  async getRankerStats(params: {
    matchType: string | number;
    players: RankerPlayerInput[];
  }) {
    const resolvedMatchType = await this.metadata.resolveMatchType(params.matchType);
    const records = await this.client.getRankerStats({
      matchtype: resolvedMatchType.code,
      players: params.players
    });

    return {
      ok: true,
      query: {
        matchTypeInput: params.matchType,
        resolvedMatchType,
        players: params.players
      },
      stats: await Promise.all(records.map((record) => this.mapRankerStat(record, false))),
      meta: buildResponseMeta()
    };
  }

  async getMetadata(kind: MetadataKind, lookup?: string | number) {
    const items = await this.metadata.getMetadata(kind);
    const resolved = lookup === undefined ? undefined : await this.metadata.resolveLookup(kind, lookup);

    return {
      ok: true,
      query: { kind, lookup },
      availableKinds: ["matchtype", "spid", "seasonid", "spposition", "division", "division-volta"],
      resolved,
      items: lookup === undefined ? items : undefined,
      meta: buildResponseMeta()
    };
  }

  async getPlayerImageUrl(params: {
    imageType: "card" | "action";
    identifierType: "spid" | "pid";
    value: string | number;
    verifyExists?: boolean;
    strict?: boolean;
  }) {
    const normalizedValue = params.identifierType === "pid" ? normalizePid(params.value) : String(Number(params.value));
    const url = this.buildPlayerImageUrl(params.imageType, params.identifierType, normalizedValue);
    const exists = params.verifyExists === false ? undefined : await this.client.checkImageExists(url);

    if (exists === false && params.strict) {
      throw new FcOnlineError("IMAGE_NOT_FOUND", "?醫롫땾 ???筌왖揶쎛 鈺곕똻???? ??녿뮸??덈뼄.", {
        details: {
          imageType: params.imageType,
          identifierType: params.identifierType,
          value: params.value,
          url
        }
      });
    }

    const resolvedPlayer =
      params.identifierType === "spid" ? await this.metadata.resolveSpid(Number(normalizedValue)) : undefined;

    return {
      ok: true,
      query: params,
      image: {
        imageType: params.imageType,
        identifierType: params.identifierType,
        inputValue: params.value,
        normalizedValue,
        url,
        exists
      },
      resolvedPlayer,
      meta: buildResponseMeta()
    };
  }

  async getUserProfileSummaryByNickname(nickname: string) {
    const resolvedUser = await this.client.getUserByNickname(nickname);
    const basic = await this.client.getUserBasic(resolvedUser.ouid);
    const maxDivision = await this.client.getUserMaxDivision(resolvedUser.ouid);

    return {
      ok: true,
      query: { nickname },
      user: this.normalizeUserBasic(basic),
      maxDivisions: await Promise.all(maxDivision.map((item) => this.mapMaxDivision(item))),
      meta: buildResponseMeta()
    };
  }

  async getUserMatchHistoryByNickname(params: {
    nickname: string;
    matchType: string | number;
    offset?: number;
    limit?: number;
  }) {
    const resolvedMatchType = await this.metadata.resolveMatchType(params.matchType);
    const resolvedUser = await this.client.getUserByNickname(params.nickname);
    const basic = await this.client.getUserBasic(resolvedUser.ouid);
    const matchIdRecords = await this.client.getUserMatches({
      ouid: resolvedUser.ouid,
      matchtype: resolvedMatchType.code,
      offset: params.offset,
      limit: params.limit
    });

    const matchIds = this.normalizeMatchIdRecords(matchIdRecords);
    if (matchIds.length === 0) {
      throw new FcOnlineError("NO_MATCHES", "鈺곌퀬???筌띲끉?귛첎? ??곷뮸??덈뼄.", {
        details: {
          nickname: params.nickname,
          matchType: resolvedMatchType
        }
      });
    }

    const details = await Promise.all(matchIds.map((matchId) => this.client.getMatchDetail(matchId)));
    const matches = details.map((detail) => this.mapMatchHistoryItem(detail, resolvedUser.ouid, resolvedMatchType.label));
    const summary = summarizeMatchHistory(matches);

    return {
      ok: true,
      query: {
        nickname: params.nickname,
        matchTypeInput: params.matchType,
        resolvedMatchType,
        offset: params.offset ?? 0,
        limit: params.limit ?? 5
      },
      user: this.normalizeUserBasic(basic),
      summary: {
        ...summary,
        requestedCount: params.limit ?? 5,
        returnedCount: matches.length
      },
      matches,
      meta: buildResponseMeta()
    };
  }

  async summarizeUserRecentMatchesByNickname(params: {
    nickname: string;
    matchType: string | number;
    limit?: number;
  }) {
    const history = await this.getUserMatchHistoryByNickname({
      nickname: params.nickname,
      matchType: params.matchType,
      offset: 0,
      limit: params.limit ?? 5
    });

    return {
      ...history,
      recentForm: history.matches.map((match) => match.result ?? "-"),
      insights: buildRecentMatchInsights(history.matches as MatchHistoryItem[])
    };
  }

  async getMatchDetailEnriched(matchId: string) {
    const detail = await this.client.getMatchDetail(matchId);
    const resolvedMatchType = await this.metadata.resolveMatchType(coerceNumber(detail.matchType, "matchType"));
    const timestamps = createDualTimestamp(detail.matchDate);

    return {
      ok: true,
      query: { matchId },
      match: {
        matchId: detail.matchId,
        matchDateUtc: timestamps.utc,
        matchDateKst: timestamps.kst,
        matchType: resolvedMatchType,
        participantCount: asArray(detail.matchInfo).length,
        participants: await Promise.all(asArray(detail.matchInfo).map((participant) => this.mapParticipantEnriched(participant)))
      },
      meta: buildResponseMeta()
    };
  }

  async getRankerStatsEnriched(params: {
    matchType: string | number;
    players: RankerPlayerInput[];
  }) {
    const resolvedMatchType = await this.metadata.resolveMatchType(params.matchType);
    const records = await this.client.getRankerStats({
      matchtype: resolvedMatchType.code,
      players: params.players
    });

    return {
      ok: true,
      query: {
        matchTypeInput: params.matchType,
        resolvedMatchType,
        players: params.players
      },
      stats: await Promise.all(records.map((record) => this.mapRankerStat(record, true))),
      meta: buildResponseMeta()
    };
  }

  private normalizeUserResponse(user: UserResponse) {
    return {
      ouid: coerceString(user.ouid, "ouid")
    };
  }

  private normalizeUserBasic(user: UserBasicResponse) {
    return {
      ouid: coerceString(user.ouid, "ouid"),
      nickname: coerceString(user.nickname, "nickname"),
      level: coerceNumber(user.level, "level")
    };
  }

  private normalizeMatchIdRecords(records: MatchIdRecord[]): string[] {
    return asArray(records).map((record) => coerceString(record.matchId, "matchId"));
  }

  private async mapMaxDivision(item: MaxDivisionResponseItem) {
    const matchTypeCode = coerceNumber(item.matchType, "matchType");
    const divisionId = coerceNumber(item.division, "division");
    const matchType = await this.metadata.resolveMatchType(matchTypeCode);
    const division = await this.metadata.resolveDivision(divisionId, matchTypeCode);
    const achievementDate = createDualTimestamp(item.achievementDate);

    return {
      matchType,
      division,
      achievementDateUtc: achievementDate.utc,
      achievementDateKst: achievementDate.kst
    };
  }

  private async mapTrade(record: TradeRecord) {
    const spid = coerceNumber(record.spid, "spid");
    const player = await this.metadata.resolveSpid(spid);
    const tradeDate = createDualTimestamp(record.tradeDate);

    return {
      tradeDateUtc: tradeDate.utc,
      tradeDateKst: tradeDate.kst,
      saleSn: coerceString(record.saleSn, "saleSn"),
      spid,
      grade: coerceNumber(record.grade, "grade"),
      value: coerceNumber(record.value, "value"),
      resolved: {
        playerName: player?.name,
        seasonId: player?.seasonId,
        seasonLabel: player?.season?.className
      }
    };
  }

  private async mapParticipantCore(participant: ApiMatchInfo) {
    const seasonId = coerceNumber(participant.matchDetail.seasonId, "seasonId");
    const shootGoals = coerceNumber(participant.shoot.goalTotal, "goalTotal");
    const displayGoals = coerceNumber(participant.shoot.goalTotalDisplay, "goalTotalDisplay");
    const passTry = coerceNumber(participant.pass.passTry, "passTry");
    const passSuccess = coerceNumber(participant.pass.passSuccess, "passSuccess");
    const season = await this.metadata.resolveSeason(seasonId);

    return {
      ouid: coerceString(participant.ouid, "ouid"),
      nickname: coerceString(participant.nickname, "nickname"),
      matchResult: participant.matchDetail.matchResult,
      seasonId,
      resolvedSeason: season,
      score: {
        goalTotal: shootGoals,
        goalTotalDisplay: displayGoals
      },
      stats: {
        possession: coerceNumber(participant.matchDetail.possession, "possession"),
        shots: coerceNumber(participant.shoot.shootTotal, "shootTotal"),
        effectiveShots: coerceNumber(participant.shoot.effectiveShootTotal, "effectiveShootTotal"),
        passSuccessRate: computeRate(passSuccess, passTry),
        controller: participant.matchDetail.controller,
        controllerLabel: controllerToLabel(participant.matchDetail.controller),
        matchEndType: coerceNumber(participant.matchDetail.matchEndType, "matchEndType"),
        matchEndTypeLabel: matchEndTypeToLabel(coerceNumber(participant.matchDetail.matchEndType, "matchEndType"))
      }
    };
  }

  private async mapParticipantEnriched(participant: ApiMatchInfo) {
    const base = await this.mapParticipantCore(participant);
    const seasonId = coerceNumber(participant.matchDetail.seasonId, "seasonId");
    const passTry = coerceNumber(participant.pass.passTry, "passTry");
    const passSuccess = coerceNumber(participant.pass.passSuccess, "passSuccess");

    return {
      ...base,
      matchDetail: {
        seasonId,
        seasonLabel: base.resolvedSeason?.className,
        matchResult: participant.matchDetail.matchResult,
        matchEndType: coerceNumber(participant.matchDetail.matchEndType, "matchEndType"),
        matchEndTypeLabel: matchEndTypeToLabel(coerceNumber(participant.matchDetail.matchEndType, "matchEndType")),
        systemPause: coerceNumber(participant.matchDetail.systemPause, "systemPause"),
        foul: coerceNumber(participant.matchDetail.foul, "foul"),
        injury: coerceNumber(participant.matchDetail.injury, "injury"),
        redCards: coerceNumber(participant.matchDetail.redCards, "redCards"),
        yellowCards: coerceNumber(participant.matchDetail.yellowCards, "yellowCards"),
        dribble: coerceNumber(participant.matchDetail.dribble, "dribble"),
        cornerKick: coerceNumber(participant.matchDetail.cornerKick, "cornerKick"),
        possession: coerceNumber(participant.matchDetail.possession, "possession"),
        offsideCount: coerceNumber(participant.matchDetail.OffsideCount, "OffsideCount"),
        averageRating: coerceNumber(participant.matchDetail.averageRating, "averageRating"),
        controller: participant.matchDetail.controller,
        controllerLabel: controllerToLabel(participant.matchDetail.controller)
      },
      shoot: {
        shootTotal: coerceNumber(participant.shoot.shootTotal, "shootTotal"),
        effectiveShootTotal: coerceNumber(participant.shoot.effectiveShootTotal, "effectiveShootTotal"),
        shootOutScore: coerceNumber(participant.shoot.shootOutScore, "shootOutScore"),
        goalTotal: coerceNumber(participant.shoot.goalTotal, "goalTotal"),
        goalTotalDisplay: coerceNumber(participant.shoot.goalTotalDisplay, "goalTotalDisplay"),
        ownGoal: coerceNumber(participant.shoot.ownGoal, "ownGoal"),
        shootHeading: coerceNumber(participant.shoot.shootHeading, "shootHeading"),
        goalHeading: coerceNumber(participant.shoot.goalHeading, "goalHeading"),
        shootFreekick: coerceNumber(participant.shoot.shootFreekick, "shootFreekick"),
        goalFreekick: coerceNumber(participant.shoot.goalFreekick, "goalFreekick"),
        shootInPenalty: coerceNumber(participant.shoot.shootInPenalty, "shootInPenalty"),
        goalInPenalty: coerceNumber(participant.shoot.goalInPenalty, "goalInPenalty"),
        shootOutPenalty: coerceNumber(participant.shoot.shootOutPenalty, "shootOutPenalty"),
        goalOutPenalty: coerceNumber(participant.shoot.goalOutPenalty, "goalOutPenalty"),
        shootPenaltyKick: coerceNumber(participant.shoot.shootPenaltyKick, "shootPenaltyKick"),
        goalPenaltyKick: coerceNumber(participant.shoot.goalPenaltyKick, "goalPenaltyKick"),
        shootDetail: await Promise.all(asArray(participant.shoot.shootDetail).map((detail) => this.mapShootDetail(detail)))
      },
      pass: {
        passTry,
        passSuccess,
        passSuccessRate: computeRate(passSuccess, passTry),
        shortPassTry: coerceNumber(participant.pass.shortPassTry, "shortPassTry"),
        shortPassSuccess: coerceNumber(participant.pass.shortPassSuccess, "shortPassSuccess"),
        longPassTry: coerceNumber(participant.pass.longPassTry, "longPassTry"),
        longPassSuccess: coerceNumber(participant.pass.longPassSuccess, "longPassSuccess"),
        bouncingLobPassTry: coerceNumber(participant.pass.bouncingLobPassTry, "bouncingLobPassTry"),
        bouncingLobPassSuccess: coerceNumber(participant.pass.bouncingLobPassSuccess, "bouncingLobPassSuccess"),
        drivenGroundPassTry: coerceNumber(participant.pass.drivenGroundPassTry, "drivenGroundPassTry"),
        drivenGroundPassSuccess: coerceNumber(participant.pass.drivenGroundPassSuccess, "drivenGroundPassSuccess"),
        throughPassTry: coerceNumber(participant.pass.throughPassTry, "throughPassTry"),
        throughPassSuccess: coerceNumber(participant.pass.throughPassSuccess, "throughPassSuccess"),
        lobbedThroughPassTry: coerceNumber(participant.pass.lobbedThroughPassTry, "lobbedThroughPassTry"),
        lobbedThroughPassSuccess: coerceNumber(participant.pass.lobbedThroughPassSuccess, "lobbedThroughPassSuccess")
      },
      defence: {
        blockTry: coerceNumber(participant.defence.blockTry, "blockTry"),
        blockSuccess: coerceNumber(participant.defence.blockSuccess, "blockSuccess"),
        tackleTry: coerceNumber(participant.defence.tackleTry, "tackleTry"),
        tackleSuccess: coerceNumber(participant.defence.tackleSuccess, "tackleSuccess")
      },
      players: await Promise.all(asArray(participant.player).map((player) => this.mapPlayer(player)))
    };
  }

  private async mapPlayer(player: ApiMatchPlayer) {
    const spId = coerceNumber(player.spId, "spId");
    const spPosition = coerceNumber(player.spPosition, "spPosition");
    const resolvedPlayer = await this.metadata.resolveSpid(spId);
    const resolvedPosition = await this.metadata.resolvePosition(spPosition);

    return {
      spId,
      spPosition,
      spGrade: coerceNumber(player.spGrade, "spGrade"),
      resolved: {
        playerName: resolvedPlayer?.name,
        seasonId: resolvedPlayer?.seasonId,
        seasonLabel: resolvedPlayer?.season?.className,
        positionLabel: resolvedPosition?.label,
        imageUrls: {
          card: this.buildPlayerImageUrl("card", "spid", String(spId)),
          action: this.buildPlayerImageUrl("action", "spid", String(spId))
        }
      },
      status: player.status
        ? {
            shoot: coerceNumber(player.status.shoot, "shoot"),
            effectiveShoot: coerceNumber(player.status.effectiveShoot, "effectiveShoot"),
            assist: coerceNumber(player.status.assist, "assist"),
            goal: coerceNumber(player.status.goal, "goal"),
            dribble: coerceNumber(player.status.dribble, "dribble"),
            intercept: coerceNumber(player.status.intercept, "intercept"),
            defending: coerceNumber(player.status.defending, "defending"),
            passTry: coerceNumber(player.status.passTry, "passTry"),
            passSuccess: coerceNumber(player.status.passSuccess, "passSuccess"),
            dribbleTry: coerceNumber(player.status.dribbleTry, "dribbleTry"),
            dribbleSuccess: coerceNumber(player.status.dribbleSuccess, "dribbleSuccess"),
            ballPossesionTry: coerceNumber(player.status.ballPossesionTry, "ballPossesionTry"),
            ballPossesionSuc: coerceNumber(player.status.ballPossesionSuc, "ballPossesionSuc"),
            aerialTry: coerceNumber(player.status.aerialTry, "aerialTry"),
            aerialSuccess: coerceNumber(player.status.aerialSuccess, "aerialSuccess"),
            blockTry: coerceNumber(player.status.blockTry, "blockTry"),
            block: coerceNumber(player.status.block, "block"),
            tackleTry: coerceNumber(player.status.tackleTry, "tackleTry"),
            tackle: coerceNumber(player.status.tackle, "tackle"),
            yellowCards: coerceNumber(player.status.yellowCards, "yellowCards"),
            redCards: coerceNumber(player.status.redCards, "redCards"),
            spRating: coerceNumber(player.status.spRating, "spRating")
          }
        : undefined
    };
  }

  private async mapShootDetail(detail: ApiMatchShootDetail) {
    const shooterSpId = coerceNumber(detail.spId, "spId");
    const assistSpIdValue = detail.assistSpId ?? detail.assistSpI;
    const assistSpId = assistSpIdValue === undefined ? undefined : coerceNumber(assistSpIdValue, "assistSpId");
    const shooter = await this.metadata.resolveSpid(shooterSpId);
    const assister = assistSpId !== undefined && assistSpId >= 0 ? await this.metadata.resolveSpid(assistSpId) : undefined;

    return {
      goalTime: decodeGoalTime(coerceNumber(detail.goalTime, "goalTime")),
      x: coerceNumber(detail.x, "x"),
      y: coerceNumber(detail.y, "y"),
      type: coerceNumber(detail.type, "type"),
      result: coerceNumber(detail.result, "result"),
      spId: shooterSpId,
      spGrade: coerceNumber(detail.spGrade, "spGrade"),
      spLevel: coerceNumber(detail.spLevel, "spLevel"),
      isLoan: coerceBoolean(detail.spIdType, "spIdType"),
      assist: coerceBoolean(detail.assist, "assist"),
      assistSpId: assister?.spid,
      assistX: detail.assistX === undefined ? undefined : coerceNumber(detail.assistX, "assistX"),
      assistY: detail.assistY === undefined ? undefined : coerceNumber(detail.assistY, "assistY"),
      hitPost: coerceBoolean(detail.hitPost, "hitPost"),
      inPenalty: coerceBoolean(detail.inPenalty, "inPenalty"),
      resolved: {
        shooterName: shooter?.name,
        assistName: assister?.name
      }
    };
  }

  private mapMatchHistoryItem(detail: MatchDetailResponse, ouid: string, matchTypeLabel: string): MatchHistoryItem {
    const timestamps = createDualTimestamp(detail.matchDate);
    const matchInfo = asArray(detail.matchInfo);
    const me = matchInfo.find((participant) => participant.ouid === ouid) ?? matchInfo[0];
    if (!me) {
      throw new FcOnlineError("NOT_FOUND", "筌띲끉????筌〓챷肉???類ｋ궖??筌≪뼚??????곷뮸??덈뼄.", {
        details: { matchId: detail.matchId, ouid }
      });
    }

    const opponent = matchInfo.find((participant) => participant.ouid !== me.ouid);
    const myGoals = coerceNumber(me.shoot.goalTotal, "goalTotal");
    const myDisplayGoals = coerceNumber(me.shoot.goalTotalDisplay, "goalTotalDisplay");
    const opponentGoals = opponent ? coerceNumber(opponent.shoot.goalTotal, "goalTotal") : 0;
    const opponentDisplayGoals = opponent ? coerceNumber(opponent.shoot.goalTotalDisplay, "goalTotalDisplay") : 0;
    const passTry = coerceNumber(me.pass.passTry, "passTry");
    const passSuccess = coerceNumber(me.pass.passSuccess, "passSuccess");

    return {
      matchId: coerceString(detail.matchId, "matchId"),
      matchDateUtc: timestamps.utc,
      matchDateKst: timestamps.kst,
      result: me.matchDetail.matchResult ?? null,
      opponent: opponent
        ? {
            ouid: opponent.ouid,
            nickname: opponent.nickname
          }
        : null,
      score: {
        for: myGoals,
        against: opponentGoals,
        displayFor: myDisplayGoals,
        displayAgainst: opponentDisplayGoals
      },
      stats: {
        possession: coerceNumber(me.matchDetail.possession, "possession"),
        shots: coerceNumber(me.shoot.shootTotal, "shootTotal"),
        effectiveShots: coerceNumber(me.shoot.effectiveShootTotal, "effectiveShootTotal"),
        passSuccessRate: computeRate(passSuccess, passTry)
      },
      resolved: {
        matchTypeLabel
      }
    };
  }

  private async mapRankerStat(record: RankerStatsResponseItem, includeResolved: boolean) {
    const spId = coerceNumber(this.getRankerStatSpId(record), "spId");
    const spPosition = coerceNumber(this.getRankerStatSpPosition(record), "spPosition");
    const createDate = createDualTimestamp(record.createDate);
    const resolvedPlayer = includeResolved ? await this.metadata.resolveSpid(spId) : undefined;
    const resolvedPosition = includeResolved ? await this.metadata.resolvePosition(spPosition) : undefined;

    return {
      spId,
      spPosition,
      status: {
        shoot: coerceNumber(record.status.shoot, "shoot"),
        effectiveShoot: coerceNumber(record.status.effectiveShoot, "effectiveShoot"),
        assist: coerceNumber(record.status.assist, "assist"),
        goal: coerceNumber(record.status.goal, "goal"),
        dribble: coerceNumber(record.status.dribble, "dribble"),
        dribbleTry: coerceNumber(record.status.dribbleTry, "dribbleTry"),
        dribbleSuccess: coerceNumber(record.status.dribbleSuccess, "dribbleSuccess"),
        passTry: coerceNumber(record.status.passTry, "passTry"),
        passSuccess: coerceNumber(record.status.passSuccess, "passSuccess"),
        passSuccessRate: computeRate(
          coerceNumber(record.status.passSuccess, "passSuccess"),
          coerceNumber(record.status.passTry, "passTry")
        ),
        block: coerceNumber(record.status.block, "block"),
        tackle: coerceNumber(record.status.tackle, "tackle"),
        matchCount: coerceNumber(record.status.matchCount, "matchCount")
      },
      createDateUtc: createDate.utc,
      createDateKst: createDate.kst,
      resolved: includeResolved
        ? {
            playerName: resolvedPlayer?.name,
            seasonId: resolvedPlayer?.seasonId,
            seasonLabel: resolvedPlayer?.season?.className,
            positionLabel: resolvedPosition?.label
          }
        : undefined
    };
  }

  private getRankerStatSpId(record: RankerStatsResponseItem) {
    return record.spId ?? record.spid ?? record.id;
  }

  private getRankerStatSpPosition(record: RankerStatsResponseItem) {
    return record.spPosition ?? record.spposition ?? record.po;
  }

  private buildPlayerImageUrl(imageType: "card" | "action", identifierType: "spid" | "pid", value: string) {
    const directory = imageType === "action" ? "playersAction" : "players";
    const normalizedValue = identifierType === "pid" ? normalizePid(value) : value;
    return `${this.config.imageBaseUrl}/live/externalAssets/common/${directory}/p${normalizedValue}.png`;
  }
}