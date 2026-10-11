export type NumericLike = number | string;
export type BooleanLike = boolean | number | string;

export interface UserResponse {
  ouid: string;
}

export interface UserBasicResponse {
  ouid: string;
  nickname: string;
  level: NumericLike;
}

export interface MaxDivisionResponseItem {
  matchType: NumericLike;
  division: NumericLike;
  achievementDate: string;
}

export interface MatchIdRecord {
  matchId: string;
}

export interface TradeRecord {
  tradeDate: string;
  saleSn: string;
  spid: NumericLike;
  grade: NumericLike;
  value: NumericLike;
}

export interface ApiMatchShootDetail {
  goalTime: NumericLike;
  x: NumericLike;
  y: NumericLike;
  type: NumericLike;
  result: NumericLike;
  spId: NumericLike;
  spGrade: NumericLike;
  spLevel: NumericLike;
  spIdType: BooleanLike;
  assist: BooleanLike;
  assistSpId?: NumericLike;
  assistSpI?: NumericLike;
  assistX?: NumericLike;
  assistY?: NumericLike;
  hitPost: BooleanLike;
  inPenalty: BooleanLike;
}

export interface ApiMatchShoot {
  shootTotal: NumericLike;
  effectiveShootTotal: NumericLike;
  shootOutScore: NumericLike;
  goalTotal: NumericLike;
  goalTotalDisplay: NumericLike;
  ownGoal: NumericLike;
  shootHeading: NumericLike;
  goalHeading: NumericLike;
  shootFreekick: NumericLike;
  goalFreekick: NumericLike;
  shootInPenalty: NumericLike;
  goalInPenalty: NumericLike;
  shootOutPenalty: NumericLike;
  goalOutPenalty: NumericLike;
  shootPenaltyKick: NumericLike;
  goalPenaltyKick: NumericLike;
  shootDetail?: ApiMatchShootDetail[];
}

export interface ApiMatchPass {
  passTry: NumericLike;
  passSuccess: NumericLike;
  shortPassTry: NumericLike;
  shortPassSuccess: NumericLike;
  longPassTry: NumericLike;
  longPassSuccess: NumericLike;
  bouncingLobPassTry: NumericLike;
  bouncingLobPassSuccess: NumericLike;
  drivenGroundPassTry: NumericLike;
  drivenGroundPassSuccess: NumericLike;
  throughPassTry: NumericLike;
  throughPassSuccess: NumericLike;
  lobbedThroughPassTry: NumericLike;
  lobbedThroughPassSuccess: NumericLike;
}

export interface ApiMatchDefence {
  blockTry: NumericLike;
  blockSuccess: NumericLike;
  tackleTry: NumericLike;
  tackleSuccess: NumericLike;
}

export interface ApiPlayerStatus {
  shoot: NumericLike;
  effectiveShoot: NumericLike;
  assist: NumericLike;
  goal: NumericLike;
  dribble: NumericLike;
  intercept: NumericLike;
  defending: NumericLike;
  passTry: NumericLike;
  passSuccess: NumericLike;
  dribbleTry: NumericLike;
  dribbleSuccess: NumericLike;
  ballPossesionTry: NumericLike;
  ballPossesionSuc: NumericLike;
  aerialTry: NumericLike;
  aerialSuccess: NumericLike;
  blockTry: NumericLike;
  block: NumericLike;
  tackleTry: NumericLike;
  tackle: NumericLike;
  yellowCards: NumericLike;
  redCards: NumericLike;
  spRating: NumericLike;
}

export interface ApiMatchPlayer {
  spId: NumericLike;
  spPosition: NumericLike;
  spGrade: NumericLike;
  status?: ApiPlayerStatus;
}

export interface ApiMatchInfo {
  ouid: string;
  nickname: string;
  matchDetail: {
    seasonId: NumericLike;
    matchResult: string;
    matchEndType: NumericLike;
    systemPause: NumericLike;
    foul: NumericLike;
    injury: NumericLike;
    redCards: NumericLike;
    yellowCards: NumericLike;
    dribble: NumericLike;
    cornerKick: NumericLike;
    possession: NumericLike;
    OffsideCount: NumericLike;
    averageRating: NumericLike;
    controller: string;
  };
  shoot: ApiMatchShoot;
  pass: ApiMatchPass;
  defence: ApiMatchDefence;
  player?: ApiMatchPlayer[];
}

export interface MatchDetailResponse {
  matchId: string;
  matchDate: string;
  matchType: NumericLike;
  matchInfo?: ApiMatchInfo[];
}

export interface RankerStatsResponseItem {
  spId?: NumericLike;
  spid?: NumericLike;
  id?: NumericLike;
  spPosition?: NumericLike;
  spposition?: NumericLike;
  po?: NumericLike;
  status: {
    shoot: NumericLike;
    effectiveShoot: NumericLike;
    assist: NumericLike;
    goal: NumericLike;
    dribble: NumericLike;
    dribbleTry: NumericLike;
    dribbleSuccess: NumericLike;
    passTry: NumericLike;
    passSuccess: NumericLike;
    block: NumericLike;
    tackle: NumericLike;
    matchCount: NumericLike;
  };
  createDate: string;
}