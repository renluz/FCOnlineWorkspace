import { describe, expect, it } from "vitest";
import { decodeGoalTime } from "../src/nexon/normalizers.js";

describe("decodeGoalTime", () => {
  it("decodes second half goal times using the documented bucket rule", () => {
    const secondHalfOffset = 2 ** 24;
    const decoded = decodeGoalTime(secondHalfOffset + 120);

    expect(decoded.periodLabel).toBe("후반");
    expect(decoded.totalSeconds).toBe(45 * 60 + 120);
    expect(decoded.minute).toBe(47);
    expect(decoded.second).toBe(0);
  });
});