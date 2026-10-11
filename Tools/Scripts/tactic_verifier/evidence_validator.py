"""
Evidence Validator (Tier 3): Validates Single Variable Discipline & Empirical Evidence Ladder
"""

from typing import List, Dict, Any, Optional
from .schemas import TacticConfig, ValidationIssue, ValidationSeverity


def calculate_tactic_differences(new_cfg: TacticConfig, old_cfg: TacticConfig) -> List[str]:
    """Calculates all distinct tactical variable differences between two configs."""
    diffs: List[str] = []

    # Team Tactic differences
    new_tt = new_cfg.team_tactic
    old_tt = old_cfg.team_tactic

    if new_tt.defense.tactic_style != old_tt.defense.tactic_style:
        diffs.append(f"defense.tactic_style ('{old_tt.defense.tactic_style}' -> '{new_tt.defense.tactic_style}')")
    if new_tt.defense.width != old_tt.defense.width:
        diffs.append(f"defense.width ({old_tt.defense.width} -> {new_tt.defense.width})")
    if new_tt.defense.depth != old_tt.defense.depth:
        diffs.append(f"defense.depth ({old_tt.defense.depth} -> {new_tt.defense.depth})")

    if new_tt.offense.build_up_style != old_tt.offense.build_up_style:
        diffs.append(f"offense.build_up_style ('{old_tt.offense.build_up_style}' -> '{new_tt.offense.build_up_style}')")
    if new_tt.offense.chance_creation_style != old_tt.offense.chance_creation_style:
        diffs.append(f"offense.chance_creation_style ('{old_tt.offense.chance_creation_style}' -> '{new_tt.offense.chance_creation_style}')")
    if new_tt.offense.attack_width != old_tt.offense.attack_width:
        diffs.append(f"offense.attack_width ({old_tt.offense.attack_width} -> {new_tt.offense.attack_width})")
    if new_tt.offense.players_in_box != old_tt.offense.players_in_box:
        diffs.append(f"offense.players_in_box ({old_tt.offense.players_in_box} -> {new_tt.offense.players_in_box})")
    if new_tt.offense.corners != old_tt.offense.corners:
        diffs.append(f"offense.corners ({old_tt.offense.corners} -> {new_tt.offense.corners})")
    if new_tt.offense.free_kicks != old_tt.offense.free_kicks:
        diffs.append(f"offense.free_kicks ({old_tt.offense.free_kicks} -> {new_tt.offense.free_kicks})")
    if new_tt.offense.tendency != old_tt.offense.tendency:
        diffs.append(f"offense.tendency ('{old_tt.offense.tendency}' -> '{new_tt.offense.tendency}')")

    # Individual tactics differences
    all_slots = set(new_cfg.individual_tactics.keys()) | set(old_cfg.individual_tactics.keys())
    for s in all_slots:
        new_indiv = new_cfg.individual_tactics.get(s)
        old_indiv = old_cfg.individual_tactics.get(s)

        if not new_indiv or not old_indiv:
            diffs.append(f"individual_tactics.{s} (slot added or removed)")
            continue

        if new_indiv.player != old_indiv.player:
            diffs.append(f"individual_tactics.{s}.player ('{old_indiv.player}' -> '{new_indiv.player}')")
        if new_indiv.code_string != old_indiv.code_string:
            diffs.append(f"individual_tactics.{s}.code_string ('{old_indiv.code_string}' -> '{new_indiv.code_string}')")

    return diffs


def validate_evidence_rules(
    config: TacticConfig,
    baseline_config: Optional[TacticConfig] = None,
    allow_multi_variables: bool = False
) -> List[ValidationIssue]:
    issues: List[ValidationIssue] = []

    # 1. EV-01: Single Variable Testing Discipline (Comparison with baseline)
    if baseline_config is not None:
        differences = calculate_tactic_differences(config, baseline_config)
        diff_count = len(differences)

        if diff_count > 1 and not allow_multi_variables:
            diff_list_str = "; ".join(differences)
            issues.append(ValidationIssue(
                rule_id="EV-01",
                severity=ValidationSeverity.CRITICAL,
                path="team_tactic",
                message=f"Vi phạm kỷ luật đơn biến (Single Variable Discipline): Phát hiện {diff_count} biến số thay đổi cùng lúc ({diff_list_str}). Mỗi chu kỳ test chỉ được đổi đúng 1 biến số."
            ))

    # 2. EV-02: Status & Evidence Ladder Tagging (Handling absent status per User Note 1)
    status = config.metadata.status

    if status is None or not status.strip():
        # User Note 1: Default to PROVISIONAL_TEST and issue a warning to remind adding status
        issues.append(ValidationIssue(
            rule_id="EV-02",
            severity=ValidationSeverity.LOW,
            path="_metadata.status",
            message="Thiếu trường '_metadata.status': Hệ thống mặc định áp dụng trạng thái 'PROVISIONAL_TEST'. Vui lòng bổ sung field 'status' vào _metadata."
        ))
        effective_status = "PROVISIONAL_TEST"
    else:
        effective_status = status.strip().upper()

    if effective_status == "LOCKED_BASELINE":
        # Check if test_id or notes indicates 50+ matches test or tier A/C ranker evidence
        notes = (config.metadata.notes or "").lower()
        test_id = (config.metadata.test_id or "").lower()

        has_screening_50 = "50" in test_id or "50" in notes or "100" in notes or "screening" in test_id
        if not has_screening_50:
            issues.append(ValidationIssue(
                rule_id="EV-02",
                severity=ValidationSeverity.MEDIUM,
                path="_metadata.status",
                message="Khóa LOCKED_BASELINE nhưng chưa ghi nhận tham chiếu mẫu thử 50+ trận trong test_id hoặc notes."
            ))

    return issues
