export type MetadataKind =
  | "matchtype"
  | "spid"
  | "seasonid"
  | "spposition"
  | "division"
  | "division-volta";

export interface ResponseMeta {
  generatedAtUtc: string;
  generatedAtKst: string;
  dataDelayNotice: string;
}

export interface ResolvedMatchType {
  rawInput: string | number;
  code: number;
  label: string;
}

export interface ResolvedDivision {
  id: number;
  label: string;
  source: "division" | "division-volta" | "unknown";
}

export interface ResolvedSeason {
  id: number;
  className: string;
  seasonImage: string;
}

export interface ResolvedSpid {
  spid: number;
  name: string;
  seasonId: number;
  pid: string;
  normalizedPid: string;
  season?: ResolvedSeason;
}

export interface ResolvedPosition {
  code: number;
  label: string;
}

export interface MatchHistoryItem {
  matchId: string;
  matchDateUtc: string;
  matchDateKst: string;
  result: string | null;
  opponent: {
    ouid?: string;
    nickname?: string;
  } | null;
  score: {
    for: number;
    against: number;
    displayFor: number;
    displayAgainst: number;
  };
  stats: {
    possession: number;
    shots: number;
    effectiveShots: number;
    passSuccessRate: number | null;
  };
  resolved: {
    matchTypeLabel: string;
  };
}

export interface RankerPlayerInput {
  spId: number;
  spPosition: number;
}