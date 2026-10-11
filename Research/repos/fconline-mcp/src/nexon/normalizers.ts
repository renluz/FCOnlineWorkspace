import { FcOnlineError } from "./errors.js";

const KST_FORMATTER = new Intl.DateTimeFormat("sv-SE", {
  timeZone: "Asia/Seoul",
  year: "numeric",
  month: "2-digit",
  day: "2-digit",
  hour: "2-digit",
  minute: "2-digit",
  second: "2-digit",
  hour12: false
});

const GOAL_TIME_SEGMENT = 2 ** 24;

export function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

export function asArray<T>(value: T[] | undefined | null): T[] {
  return Array.isArray(value) ? value : [];
}

export function coerceString(value: unknown, fieldName: string): string {
  if (typeof value === "string") {
    return value;
  }

  if (typeof value === "number" || typeof value === "bigint") {
    return String(value);
  }

  throw new FcOnlineError("VALIDATION_ERROR", `${fieldName} 값이 문자열이 아닙니다.`, {
    details: {
      fieldName,
      receivedType: typeof value
    }
  });
}

export function coerceNumber(value: unknown, fieldName: string): number {
  if (typeof value === "number" && Number.isFinite(value)) {
    return value;
  }

  if (typeof value === "string" && value.trim().length > 0) {
    const parsed = Number(value);
    if (Number.isFinite(parsed)) {
      return parsed;
    }
  }

  throw new FcOnlineError("VALIDATION_ERROR", `${fieldName} 값이 숫자가 아닙니다.`, {
    details: {
      fieldName,
      receivedValue: value
    }
  });
}

export function coerceOptionalNumber(value: unknown): number | undefined {
  if (value === undefined || value === null || value === "") {
    return undefined;
  }

  return coerceNumber(value, "optionalNumber");
}

export function coerceBoolean(value: unknown, fieldName: string): boolean {
  if (typeof value === "boolean") {
    return value;
  }

  if (typeof value === "number") {
    return value !== 0;
  }

  if (typeof value === "string") {
    const normalized = value.trim().toLowerCase();
    if (["true", "1", "yes", "y"].includes(normalized)) {
      return true;
    }

    if (["false", "0", "no", "n"].includes(normalized)) {
      return false;
    }
  }

  throw new FcOnlineError("VALIDATION_ERROR", `${fieldName} 값이 불리언이 아닙니다.`, {
    details: {
      fieldName,
      receivedValue: value
    }
  });
}

export function normalizePid(value: string | number): string {
  const digits = String(value).replace(/\D/g, "");
  const stripped = digits.replace(/^0+/, "");
  return stripped.length > 0 ? stripped : "0";
}

export function extractPidFromSpid(spid: string | number): string {
  const digits = String(spid).replace(/\D/g, "");
  const pid = digits.slice(-6);
  return normalizePid(pid);
}

export function toUtcIsoString(value: string): string {
  const trimmed = value.trim();
  const candidate = trimmed.endsWith("Z") ? trimmed : `${trimmed}Z`;
  const date = new Date(candidate);

  if (Number.isNaN(date.getTime())) {
    throw new FcOnlineError("VALIDATION_ERROR", "UTC 시간 문자열을 파싱할 수 없습니다.", {
      details: { value }
    });
  }

  return date.toISOString();
}

export function toKstIsoString(value: string | Date): string {
  const date = typeof value === "string" ? new Date(toUtcIsoString(value)) : value;
  if (Number.isNaN(date.getTime())) {
    throw new FcOnlineError("VALIDATION_ERROR", "KST 시간 문자열을 파싱할 수 없습니다.", {
      details: { value }
    });
  }

  const parts = Object.fromEntries(
    KST_FORMATTER.formatToParts(date)
      .filter((part) => part.type !== "literal")
      .map((part) => [part.type, part.value])
  );

  return `${parts.year}-${parts.month}-${parts.day}T${parts.hour}:${parts.minute}:${parts.second}+09:00`;
}

export function createDualTimestamp(value: string): { utc: string; kst: string } {
  const utc = toUtcIsoString(value);
  return {
    utc,
    kst: toKstIsoString(utc)
  };
}

export function computeRate(success: number, attempts: number): number | null {
  if (attempts <= 0) {
    return null;
  }

  return Number((success / attempts).toFixed(4));
}

export function decodeGoalTime(goalTime: number) {
  const bucket = Math.floor(goalTime / GOAL_TIME_SEGMENT);
  const remainder = goalTime % GOAL_TIME_SEGMENT;

  const periodMap = [
    { label: "전반", baseSeconds: 0 },
    { label: "후반", baseSeconds: 45 * 60 },
    { label: "연장 전반", baseSeconds: 90 * 60 },
    { label: "연장 후반", baseSeconds: 105 * 60 },
    { label: "승부차기", baseSeconds: 120 * 60 }
  ] as const;

  const period = periodMap[bucket] ?? {
    label: "알 수 없음",
    baseSeconds: bucket * 45 * 60
  };

  const totalSeconds = period.baseSeconds + remainder;
  const minute = Math.floor(totalSeconds / 60);
  const second = totalSeconds % 60;

  return {
    raw: goalTime,
    periodIndex: bucket,
    periodLabel: period.label,
    totalSeconds,
    minute,
    second,
    display: `${minute}' ${String(second).padStart(2, "0")}"`
  };
}

export function sum(numbers: number[]): number {
  return numbers.reduce((accumulator, value) => accumulator + value, 0);
}