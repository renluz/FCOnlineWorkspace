import type { AppConfig } from "../config.js";
import type { MetadataKind, ResolvedDivision, ResolvedMatchType, ResolvedPosition, ResolvedSeason, ResolvedSpid } from "../types/domain.js";
import { FcOnlineError } from "./errors.js";
import { asArray, coerceNumber, coerceString, extractPidFromSpid, isRecord } from "./normalizers.js";
import { NexonClient } from "./client.js";

interface CacheEntry {
  expiresAt: number;
  value: unknown[];
}

export class NexonMetadataService {
  private readonly cache = new Map<MetadataKind, CacheEntry>();

  constructor(
    private readonly client: Pick<NexonClient, "getMetadata">,
    private readonly config: Pick<AppConfig, "metadataTtlMs">
  ) {}

  async getMetadata(kind: MetadataKind): Promise<unknown[]> {
    const cached = this.cache.get(kind);
    if (cached && cached.expiresAt > Date.now()) {
      return cached.value;
    }

    const raw = await this.client.getMetadata<unknown[]>(kind);
    const normalized = this.normalizeMetadata(kind, raw);
    this.cache.set(kind, {
      expiresAt: Date.now() + this.config.metadataTtlMs,
      value: normalized
    });
    return normalized;
  }

  async resolveMatchType(input: string | number): Promise<ResolvedMatchType> {
    const items = (await this.getMetadata("matchtype")) as Array<{ code: number; label: string }>;

    if (typeof input === "number" || /^\d+$/.test(String(input).trim())) {
      const code = Number(input);
      const found = items.find((item) => item.code === code);
      if (!found) {
        throw new FcOnlineError("VALIDATION_ERROR", "알 수 없는 matchType 코드입니다.", {
          details: {
            input,
            candidates: items.slice(0, 20)
          }
        });
      }

      return {
        rawInput: input,
        code: found.code,
        label: found.label
      };
    }

    const normalizedInput = String(input).trim().toLowerCase();
    const exact = items.find((item) => item.label.toLowerCase() === normalizedInput);
    if (exact) {
      return {
        rawInput: input,
        code: exact.code,
        label: exact.label
      };
    }

    const fuzzy = items.filter((item) => item.label.toLowerCase().includes(normalizedInput));
    if (fuzzy.length === 1) {
      const only = fuzzy[0]!;
      return {
        rawInput: input,
        code: only.code,
        label: only.label
      };
    }

    throw new FcOnlineError("VALIDATION_ERROR", "matchType 입력을 해석할 수 없습니다.", {
      details: {
        input,
        candidates: fuzzy.length > 1 ? fuzzy : items.slice(0, 20)
      }
    });
  }

  async resolveSpid(spid: number): Promise<ResolvedSpid | undefined> {
    const items = (await this.getMetadata("spid")) as Array<{ spid: number; name: string }>;
    const found = items.find((item) => item.spid === spid);
    if (!found) {
      return undefined;
    }

    const seasonId = Math.floor(spid / 1_000_000);
    const season = await this.resolveSeason(seasonId);

    return {
      spid,
      name: found.name,
      seasonId,
      pid: String(spid).slice(-6),
      normalizedPid: extractPidFromSpid(spid),
      season
    };
  }

  async resolveSeason(seasonId: number): Promise<ResolvedSeason | undefined> {
    const items = (await this.getMetadata("seasonid")) as ResolvedSeason[];
    return items.find((item) => item.id === seasonId);
  }

  async resolvePosition(positionCode: number): Promise<ResolvedPosition | undefined> {
    const items = (await this.getMetadata("spposition")) as ResolvedPosition[];
    return items.find((item) => item.code === positionCode);
  }

  async resolveDivision(divisionId: number, matchTypeCode?: number): Promise<ResolvedDivision> {
    const divisionItems = (await this.getMetadata("division")) as ResolvedDivision[];
    const divisionVoltaItems = (await this.getMetadata("division-volta")) as ResolvedDivision[];
    const matchType = matchTypeCode === undefined ? undefined : await this.resolveMatchType(matchTypeCode);
    const prefersVolta = matchType?.label.includes("볼타") ?? false;

    const primary = prefersVolta ? divisionVoltaItems : divisionItems;
    const secondary = prefersVolta ? divisionItems : divisionVoltaItems;

    const foundPrimary = primary.find((item) => item.id === divisionId);
    if (foundPrimary) {
      return foundPrimary;
    }

    const foundSecondary = secondary.find((item) => item.id === divisionId);
    if (foundSecondary) {
      return foundSecondary;
    }

    return {
      id: divisionId,
      label: String(divisionId),
      source: "unknown"
    };
  }

  async resolveLookup(kind: MetadataKind, lookup: string | number): Promise<unknown> {
    switch (kind) {
      case "matchtype":
        return this.resolveMatchType(lookup);
      case "spid":
        return this.resolveSpid(Number(lookup));
      case "seasonid":
        return this.resolveSeason(Number(lookup));
      case "spposition":
        return this.resolvePosition(Number(lookup));
      case "division":
      case "division-volta": {
        const items = (await this.getMetadata(kind)) as ResolvedDivision[];
        return items.find((item) => item.id === Number(lookup));
      }
      default:
        return undefined;
    }
  }

  private normalizeMetadata(kind: MetadataKind, raw: unknown[]): unknown[] {
    const items = asArray(raw);

    switch (kind) {
      case "matchtype":
        return items.map((item) => {
          const record = this.expectRecord(item, kind);
          return {
            code: coerceNumber(record.matchtype, "matchtype"),
            label: coerceString(record.desc, "desc")
          };
        });
      case "spid":
        return items.map((item) => {
          const record = this.expectRecord(item, kind);
          return {
            spid: coerceNumber(record.id, "id"),
            name: coerceString(record.name, "name")
          };
        });
      case "seasonid":
        return items.map((item) => {
          const record = this.expectRecord(item, kind);
          return {
            id: coerceNumber(record.seasonId, "seasonId"),
            className: coerceString(record.className, "className"),
            seasonImage: coerceString(record.seasonImg, "seasonImg")
          };
        });
      case "spposition":
        return items.map((item) => {
          const record = this.expectRecord(item, kind);
          return {
            code: coerceNumber(record.spposition, "spposition"),
            label: coerceString(record.desc, "desc")
          };
        });
      case "division":
        return items.map((item) => {
          const record = this.expectRecord(item, kind);
          return {
            id: coerceNumber(record.divisionId, "divisionId"),
            label: coerceString(record.divisionName, "divisionName"),
            source: "division" as const
          };
        });
      case "division-volta":
        return items.map((item) => {
          const record = this.expectRecord(item, kind);
          return {
            id: coerceNumber(record.divisionId, "divisionId"),
            label: coerceString(record.divisionName, "divisionName"),
            source: "division-volta" as const
          };
        });
      default:
        return items;
    }
  }

  private expectRecord(value: unknown, kind: MetadataKind): Record<string, unknown> {
    if (!isRecord(value)) {
      throw new FcOnlineError("VALIDATION_ERROR", `${kind} 메타데이터 항목이 객체가 아닙니다.`, {
        details: { value }
      });
    }

    return value;
  }
}