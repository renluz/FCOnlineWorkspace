import { describe, expect, it } from "vitest";
import { NexonMetadataService } from "../src/nexon/metadata.js";

describe("NexonMetadataService", () => {
  it("normalizes mixed string/number metadata and resolves match type", async () => {
    const client = {
      async getMetadata(kind: string) {
        switch (kind) {
          case "matchtype":
            return [
              { matchtype: "50", desc: "공식경기" },
              { matchtype: 214, desc: "볼타 공식경기" }
            ];
          case "spid":
            return [{ id: "100000051", name: "앨런 시어러" }];
          case "seasonid":
            return [{ seasonId: "100", className: "ICON", seasonImg: "https://example.com/icon.png" }];
          case "spposition":
            return [{ spposition: 18, desc: "ST" }];
          case "division":
            return [{ divisionId: "800", divisionName: "슈퍼챔피언스" }];
          case "division-volta":
            return [{ divisionId: 1100, divisionName: "월드 스타" }];
          default:
            return [];
        }
      }
    };

    const metadata = new NexonMetadataService(client as any, { metadataTtlMs: 60_000 });
    const matchType = await metadata.resolveMatchType("공식경기");
    const spid = await metadata.resolveSpid(100000051);

    expect(matchType).toEqual({ rawInput: "공식경기", code: 50, label: "공식경기" });
    expect(spid).toMatchObject({
      spid: 100000051,
      seasonId: 100,
      normalizedPid: "51"
    });
  });
});