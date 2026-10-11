import { createDualTimestamp, sum } from "./normalizers.js";
import type { MatchHistoryItem, ResponseMeta } from "../types/domain.js";

export const DATA_DELAY_NOTICE = "FC Online OpenAPI 데이터는 최신 시점 대비 약 2시간 지연될 수 있습니다.";

export function buildResponseMeta(now: Date = new Date()): ResponseMeta {
  const utc = now.toISOString();
  const kst = createDualTimestamp(utc).kst;

  return {
    generatedAtUtc: utc,
    generatedAtKst: kst,
    dataDelayNotice: DATA_DELAY_NOTICE
  };
}

export function controllerToLabel(controller: string): string {
  switch (controller) {
    case "keyboard":
      return "키보드";
    case "pad":
      return "패드";
    case "etc":
      return "기타";
    default:
      return controller;
  }
}

export function matchEndTypeToLabel(matchEndType: number): string {
  switch (matchEndType) {
    case 0:
      return "정상 종료";
    case 1:
      return "몰수승";
    case 2:
      return "몰수패";
    default:
      return "알 수 없음";
  }
}

export function summarizeMatchHistory(matches: MatchHistoryItem[]) {
  const wins = matches.filter((match) => match.result === "승").length;
  const draws = matches.filter((match) => match.result === "무").length;
  const losses = matches.filter((match) => match.result === "패").length;
  const goalsFor = sum(matches.map((match) => match.score.for));
  const goalsAgainst = sum(matches.map((match) => match.score.against));

  return {
    requestedCount: matches.length,
    returnedCount: matches.length,
    wins,
    draws,
    losses,
    goalsFor,
    goalsAgainst
  };
}

export function buildRecentMatchInsights(matches: MatchHistoryItem[]): string[] {
  if (matches.length === 0) {
    return ["조회된 최근 경기가 없습니다."];
  }

  const summary = summarizeMatchHistory(matches);
  const averagePossession = average(matches.map((match) => match.stats.possession));
  const averageShots = average(matches.map((match) => match.stats.shots));
  const averagePassSuccessRate = average(matches.map((match) => match.stats.passSuccessRate).filter((value): value is number => value !== null));
  const recentForm = matches.map((match) => match.result ?? "-").join(" ");
  const possessionAndShotsInsight =
    averagePossession === null || averageShots === null
      ? "점유율/슈팅 평균을 계산할 수 있는 데이터가 부족합니다."
      : `경기당 평균 점유율은 ${averagePossession.toFixed(1)}%, 평균 슈팅은 ${averageShots.toFixed(1)}회입니다.`;

  return [
    `최근 ${matches.length}경기 전적은 ${summary.wins}승 ${summary.draws}무 ${summary.losses}패입니다.`,
    `최근 폼은 ${recentForm} 입니다.`,
    possessionAndShotsInsight,
    averagePassSuccessRate === null
      ? "패스 성공률 평균을 계산할 수 있는 데이터가 없습니다."
      : `평균 패스 성공률은 ${(averagePassSuccessRate * 100).toFixed(1)}%입니다.`
  ];
}

function average(numbers: number[]): number | null {
  if (numbers.length === 0) {
    return null;
  }

  return numbers.reduce((accumulator, value) => accumulator + value, 0) / numbers.length;
}