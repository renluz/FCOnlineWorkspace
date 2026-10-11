"""
Engine Validator (Tier 1): Validates Game Client Technical Specifications
"""

import re
from typing import List
from .schemas import TacticConfig, ValidationIssue, ValidationSeverity
from .constants import (
    FORMATIONS_BASE,
    CORNERS_MAX_VALUE,
    FREE_KICKS_MAX_VALUE,
    SLIDER_MIN,
    SLIDER_MAX,
    VALID_DEFENSE_STYLES,
    VALID_BUILD_UP_STYLES,
    VALID_CHANCE_CREATION_STYLES,
    VALID_TENDENCIES,
    STANDARD_UI_CODE_GROUP_MAP,
    SLOT_TO_GROUP_MAP
)


def normalize_enum_text(text: str) -> str:
    """Helper to normalize bilingual or slash-separated text."""
    return text.strip().lower()


def is_enum_match(val: str, valid_list: List[str]) -> bool:
    """Checks if any valid option is contained or matches the value."""
    norm_val = normalize_enum_text(val)
    for opt in valid_list:
        if normalize_enum_text(opt) in norm_val or norm_val in normalize_enum_text(opt):
            return True
    return False


def validate_engine_rules(config: TacticConfig) -> List[ValidationIssue]:
    issues: List[ValidationIssue] = []

    # 1. GE-01: Formation Validity (Handling "-0" suffix)
    raw_formation = config.metadata.formation.strip()
    norm_formation = raw_formation
    if norm_formation.endswith("-0"):
        norm_formation = norm_formation[:-2]
    cleaned_formation = norm_formation.replace("-", "").replace(" ", "").replace("/", "")

    if cleaned_formation not in FORMATIONS_BASE:
        issues.append(ValidationIssue(
            rule_id="GE-01",
            severity=ValidationSeverity.CRITICAL,
            path="_metadata.formation",
            message=f"Sơ đồ thi đấu không hợp lệ: '{raw_formation}' (chuẩn hóa '{cleaned_formation}' không thuộc danh mục base formation)."
        ))

    # 2. GE-02: Team Tactic Sliders & Configurable Limits
    tt = config.team_tactic

    # Width / Depth (1-10)
    if not (SLIDER_MIN <= tt.defense.width <= SLIDER_MAX):
        issues.append(ValidationIssue(
            rule_id="GE-02",
            severity=ValidationSeverity.CRITICAL,
            path="team_tactic.defense.width",
            message=f"Cự ly phòng thủ (Rộng) {tt.defense.width} nằm ngoài phạm vi [{SLIDER_MIN}, {SLIDER_MAX}]."
        ))
    if not (SLIDER_MIN <= tt.defense.depth <= SLIDER_MAX):
        issues.append(ValidationIssue(
            rule_id="GE-02",
            severity=ValidationSeverity.CRITICAL,
            path="team_tactic.defense.depth",
            message=f"Cự ly phòng thủ (Sâu) {tt.defense.depth} nằm ngoài phạm vi [{SLIDER_MIN}, {SLIDER_MAX}]."
        ))

    # Attack Width / Players in Box (1-10)
    if not (SLIDER_MIN <= tt.offense.attack_width <= SLIDER_MAX):
        issues.append(ValidationIssue(
            rule_id="GE-02",
            severity=ValidationSeverity.CRITICAL,
            path="team_tactic.offense.attack_width",
            message=f"Cự ly tấn công (Rộng) {tt.offense.attack_width} nằm ngoài phạm vi [{SLIDER_MIN}, {SLIDER_MAX}]."
        ))
    if not (SLIDER_MIN <= tt.offense.players_in_box <= SLIDER_MAX):
        issues.append(ValidationIssue(
            rule_id="GE-02",
            severity=ValidationSeverity.CRITICAL,
            path="team_tactic.offense.players_in_box",
            message=f"Cầu thủ trong vòng cấm {tt.offense.players_in_box} nằm ngoài phạm vi [{SLIDER_MIN}, {SLIDER_MAX}]."
        ))

    # Corners / Free kicks (Configurable limits)
    if not (1 <= tt.offense.corners <= CORNERS_MAX_VALUE):
        issues.append(ValidationIssue(
            rule_id="GE-02",
            severity=ValidationSeverity.HIGH,
            path="team_tactic.offense.corners",
            message=f"Chỉ số phạt góc {tt.offense.corners} vượt giới hạn cho phép [1, {CORNERS_MAX_VALUE}]."
        ))
    if not (1 <= tt.offense.free_kicks <= FREE_KICKS_MAX_VALUE):
        issues.append(ValidationIssue(
            rule_id="GE-02",
            severity=ValidationSeverity.HIGH,
            path="team_tactic.offense.free_kicks",
            message=f"Chỉ số đá phạt {tt.offense.free_kicks} vượt giới hạn cho phép [1, {FREE_KICKS_MAX_VALUE}]."
        ))

    # 3. GE-03: Tactical Enums & Tendency
    if not is_enum_match(tt.defense.tactic_style, VALID_DEFENSE_STYLES):
        issues.append(ValidationIssue(
            rule_id="GE-03",
            severity=ValidationSeverity.HIGH,
            path="team_tactic.defense.tactic_style",
            message=f"Phong cách phòng thủ không hợp lệ: '{tt.defense.tactic_style}'."
        ))

    if not is_enum_match(tt.offense.build_up_style, VALID_BUILD_UP_STYLES):
        issues.append(ValidationIssue(
            rule_id="GE-03",
            severity=ValidationSeverity.HIGH,
            path="team_tactic.offense.build_up_style",
            message=f"Lối chơi xây dựng tấn công không hợp lệ: '{tt.offense.build_up_style}'."
        ))

    if not is_enum_match(tt.offense.chance_creation_style, VALID_CHANCE_CREATION_STYLES):
        issues.append(ValidationIssue(
            rule_id="GE-03",
            severity=ValidationSeverity.HIGH,
            path="team_tactic.offense.chance_creation_style",
            message=f"Lối chơi tạo cơ hội không hợp lệ: '{tt.offense.chance_creation_style}'."
        ))

    if not is_enum_match(tt.offense.tendency, VALID_TENDENCIES):
        issues.append(ValidationIssue(
            rule_id="GE-03",
            severity=ValidationSeverity.HIGH,
            path="team_tactic.offense.tendency",
            message=f"Xu hướng tấn công (tendency) không hợp lệ: '{tt.offense.tendency}'."
        ))

    # 4. GE-04: Position Code & GK Instruction Mapping
    code_group_map = config.ui_code_group_map or STANDARD_UI_CODE_GROUP_MAP

    for slot, indiv in config.individual_tactics.items():
        group_key = SLOT_TO_GROUP_MAP.get(slot, slot)
        allowed_prefixes = code_group_map.get(group_key, [])

        if slot == "GK":
            # GK special check
            gk_keys = list(indiv.settings.keys()) if indiv.settings else []
            for k in gk_keys:
                if k not in ["GK_CROSS", "GK_SWEEPER"]:
                    issues.append(ValidationIssue(
                        rule_id="GE-04",
                        severity=ValidationSeverity.HIGH,
                        path=f"individual_tactics.GK.settings.{k}",
                        message=f"Chỉ thị thủ môn không hợp lệ: '{k}'. GK chỉ chấp nhận GK_CROSS và GK_SWEEPER."
                    ))
            continue

        # Extract codes from code_string
        if indiv.code_string:
            tokens = [t.strip() for t in indiv.code_string.split("/") if t.strip()]
            for token in tokens:
                # Token may be like "CC2", "DS1", "IN2", "AS"
                match = re.match(r"^([A-Z]{2})", token)
                if match:
                    prefix = match.group(1)
                    if prefix not in allowed_prefixes:
                        issues.append(ValidationIssue(
                            rule_id="GE-04",
                            severity=ValidationSeverity.HIGH,
                            path=f"individual_tactics.{slot}.code_string",
                            message=f"Mã chỉ thị '{prefix}' (từ '{token}') không thuộc nhóm vị trí {slot} ({group_key}: {allowed_prefixes})."
                        ))

    return issues
