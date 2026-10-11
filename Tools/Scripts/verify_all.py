# -*- coding: utf-8 -*-
import json
import os
import csv

base = r"E:\FCOnlineWorkspace\SquadProject"

# 1. Check 11_TEAM_COLOR_RULES.json
with open(os.path.join(base, "11_TEAM_COLOR_RULES.json"), encoding="utf-8") as f:
    tc = json.load(f)
assert tc["team_color_types"]["enhancement_grade_team_color"]["milestones"]["silver_gold_tier_plus5_to_plus7"]["thresholds"]["tier_2_6_to_11_players"] == "+2 OVR"
assert tc["team_color_types"]["enhancement_grade_team_color"]["milestones"]["golden_tier_plus8_to_plus10"]["thresholds"]["tier_2_6_to_11_players"] == "+3 OVR"
assert tc["team_color_types"]["enhancement_grade_team_color"]["milestones"]["platinum_tier_plus11_to_plus13"]["thresholds"]["tier_1_5_players"] == "+4 OVR"
assert tc["team_color_types"]["enhancement_grade_team_color"]["milestones"]["platinum_tier_plus11_to_plus13"]["thresholds"]["tier_2_8_players"] == "+5 OVR"
assert "+4 OVR" not in tc["team_color_types"]["national_team_color"]["tiers"]["tier_4_10_to_11_players"]
assert "+4 OVR" not in tc["team_color_types"]["club_team_color"]["tiers"]["tier_4_10_to_11_players"]
print("Check 1: 11_TEAM_COLOR_RULES.json PASSED")

# 2. Check 02_CURRENT_SQUAD.json
with open(os.path.join(base, "02_CURRENT_SQUAD.json"), encoding="utf-8") as f:
    sq = json.load(f)
for p in sq["starting_xi"]:
    assert "Kim Cương" not in p.get("tier", ""), f"Found Kim Cuong in {p}"
assert "Kim Cương" not in sq["tier_summary"]["team_color_upgrade_status"]
print("Check 2: 02_CURRENT_SQUAD.json PASSED")

# 3. Check PROJECT_STATUS.md
with open(os.path.join(base, "PROJECT_STATUS.md"), encoding="utf-8") as f:
    ps = f.read()
assert "baseline 100%" not in ps.lower() and "chuẩn mực 100%" not in ps.lower()
assert "CORE_BASELINE_ESTABLISHED / PARTIAL_VERIFICATION_REMAINS" in ps
print("Check 3: PROJECT_STATUS.md PASSED")

# 4. Check Provenance & Source IDs
with open(os.path.join(base, "14_SOURCE_REGISTRY.csv"), encoding="utf-8") as f:
    valid_sources = {row["source_id"] for row in csv.DictReader(f)}

for fname, key in [("07_NORMAL_TRAITS_VI.json", "traits"), ("08_SKILL_COACHES_VI.json", "skill_coaches"), ("09_GOLD_TRAITS_VI.json", "gold_traits")]:
    with open(os.path.join(base, fname), encoding="utf-8") as f:
        data = json.load(f)[key]
    for item in data:
        for k, v in item.items():
            if k.endswith("_confidence") and "HIGH" in str(v):
                field_prefix = k.replace("_confidence", "")
                source_id_field = f"{field_prefix}_source_ids"
                srcs = item.get(source_id_field) or item.get("source_ids")
                assert srcs, f"{fname} item {item.get('id')} field {k} has HIGH confidence but no source_ids!"
                for s in srcs:
                    assert s in valid_sources, f"Unknown source_id {s} in {fname}"
print("Check 4: Provenance and Source IDs PASSED")

# 5. Check FINAL_CONSISTENCY_AUDIT.md and 21_AUDIT_LOG.md
assert os.path.exists(os.path.join(base, "FINAL_CONSISTENCY_AUDIT.md"))
with open(os.path.join(base, "FINAL_CONSISTENCY_AUDIT.md"), encoding="utf-8") as f:
    fca = f.read()
assert "Lỗi đã sửa" in fca or "LĨNH VỰC" in fca or "BẢNG ĐỐI SOÁT" in fca
assert "UNRESOLVED ITEMS" in fca.upper()
print("Check 5: FINAL_CONSISTENCY_AUDIT.md PASSED")

with open(os.path.join(base, "21_AUDIT_LOG.md"), encoding="utf-8") as f:
    al = f.read()
assert "Final Consistency Audit" in al
print("Check 6: 21_AUDIT_LOG.md PASSED")

print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY!")
