"""
Project Validator (Tier 2): Validates FCOnlineWorkspace Business & Meta Rules
"""

import unicodedata
from typing import List, Dict, Any, Optional
from .schemas import TacticConfig, ValidationIssue, ValidationSeverity


def _normalize_skill(s: Any) -> str:
    if not isinstance(s, str):
        return ""
    return unicodedata.normalize("NFC", " ".join(s.strip().split()).lower())


def validate_project_rules(
    config: TacticConfig,
    squad_data: Optional[Dict[str, Any]] = None,
    configs_data: Optional[Dict[str, Any]] = None
) -> List[ValidationIssue]:
    issues: List[ValidationIssue] = []

    # 1. PR-01: Cross-file Exact Card Triplet
    if squad_data and "starting_xi" in squad_data:
        squad_starters = squad_data["starting_xi"]
        slot_map: Dict[str, Dict[str, Any]] = {}
        exact_card_set = set()

        for player in squad_starters:
            slot = player.get("slot")
            p_name = player.get("player_name", "").strip()
            season = player.get("season", "").strip()
            grade = player.get("grade", "")
            exact_str = f"{p_name} {season} +{grade}".strip()

            slot_map[slot] = {
                "player_name": p_name,
                "season": season,
                "grade": grade,
                "exact_str": exact_str
            }
            exact_card_set.add(exact_str)

        # A. Check individual_tactics
        for slot, indiv in config.individual_tactics.items():
            tactic_player = indiv.player.strip()

            # Detect ambiguous grade notation with "/" (e.g., "+9 / +10")
            if "/" in tactic_player or "\\\\" in tactic_player:
                issues.append(ValidationIssue(
                    rule_id="PR-01",
                    severity=ValidationSeverity.CRITICAL,
                    path=f"individual_tactics.{slot}.player",
                    message=f"Vi phạm Exact Card: Giá trị '{tactic_player}' mập mờ mức cộng (chứa ký tự phân tách '/'). Bắt buộc ghi chính xác mức thẻ."
                ))
                continue

            # Check exact match with starting_xi slot
            if slot in slot_map:
                expected_card = slot_map[slot]["exact_str"]
                if tactic_player != expected_card:
                    issues.append(ValidationIssue(
                        rule_id="PR-01",
                        severity=ValidationSeverity.CRITICAL,
                        path=f"individual_tactics.{slot}.player",
                        message=f"Lệch thẻ đội hình tại {slot}: Tactic ghi '{tactic_player}' nhưng 02_CURRENT_SQUAD.json xác nhận là '{expected_card}'."
                    ))

        # B. Check set_pieces_and_roles
        if config.set_pieces_and_roles:
            sp = config.set_pieces_and_roles
            roles_to_check = {
                "captain": sp.captain,
                "penalty": sp.penalty,
                "left_corner": sp.left_corner,
                "right_corner": sp.right_corner,
                "left_free_kick": sp.left_free_kick,
                "right_free_kick": sp.right_free_kick,
                "long_free_kick": sp.long_free_kick,
            }
            for role_name, player_str in roles_to_check.items():
                if not player_str:
                    continue
                cleaned_role_player = player_str.strip()
                if "/" in cleaned_role_player:
                    issues.append(ValidationIssue(
                        rule_id="PR-01",
                        severity=ValidationSeverity.CRITICAL,
                        path=f"set_pieces_and_roles.{role_name}",
                        message=f"Vi phạm Exact Card tại {role_name}: Giá trị '{cleaned_role_player}' mập mờ mức cộng."
                    ))
                elif cleaned_role_player not in exact_card_set:
                    issues.append(ValidationIssue(
                        rule_id="PR-01",
                        severity=ValidationSeverity.CRITICAL,
                        path=f"set_pieces_and_roles.{role_name}",
                        message=f"Cầu thủ đảm nhiệm {role_name} ('{cleaned_role_player}') không tồn tại trong danh sách xuất phát 02_CURRENT_SQUAD.json."
                    ))

    # 2. PR-02: Stopper & Cover Complementarity
    cb_slots = [slot for slot in config.individual_tactics.keys() if "CB" in slot]
    if len(cb_slots) == 2:
        stoppers = []
        covers = []
        for slot in cb_slots:
            slot_data = config.individual_tactics[slot]
            text_context = " ".join([
                slot_data.defensive_role or "",
                slot_data.role or "",
                slot_data.tactical_logic or ""
            ]).lower()

            is_stopper = "stopper" in text_context or "dập" in text_context
            is_cover = "cover" in text_context or "bọc lót" in text_context

            if is_stopper:
                stoppers.append(slot)
            if is_cover:
                covers.append(slot)

        if len(stoppers) == 2 and len(covers) == 0:
            issues.append(ValidationIssue(
                rule_id="PR-02",
                severity=ValidationSeverity.CRITICAL,
                path="individual_tactics.CB",
                message="Lỗi hàng thủ: Cả 2 CB đều mang vai trò Stopper (dập), gây nguy cơ hổng lưng cực lớn."
            ))
        elif len(covers) == 2 and len(stoppers) == 0:
            issues.append(ValidationIssue(
                rule_id="PR-02",
                severity=ValidationSeverity.CRITICAL,
                path="individual_tactics.CB",
                message="Lỗi hàng thủ: Cả 2 CB đều mang vai trò Cover (bọc lót), thiếu trung vệ dập áp sát chủ động."
            ))

    # 3. PR-03: Cross-file Anti-Overlap Coach Skills
    if configs_data and "players" in configs_data and isinstance(configs_data["players"], list):
        for p in configs_data["players"]:
            if not isinstance(p, dict):
                continue
            card_spec = p.get("card_spec", {})
            p_name = card_spec.get("player_name", "Unknown")
            slots = p.get("slots")
            if not isinstance(slots, dict):
                continue

            p8 = slots.get("plus8_skill_coach")
            if not isinstance(p8, dict):
                continue

            status = str(p8.get("status", "")).upper()
            if "PENDING" in status:
                # Graceful skip for players awaiting coach verification (e.g. Mendy, Carvajal)
                continue

            add_skill_raw = p8.get("additional_plus8_skill")
            if not add_skill_raw or not isinstance(add_skill_raw, str) or not add_skill_raw.strip():
                continue

            tc = p8.get("training_coach")
            if not isinstance(tc, dict):
                # Courtois or unassigned training coach
                continue

            training_skills_raw = tc.get("skills", [])
            if not isinstance(training_skills_raw, list):
                continue

            norm_add_skill = _normalize_skill(add_skill_raw)
            for skill_item in training_skills_raw:
                if isinstance(skill_item, str) and norm_add_skill == _normalize_skill(skill_item):
                    issues.append(ValidationIssue(
                        rule_id="PR-03",
                        severity=ValidationSeverity.CRITICAL,
                        path=f"04_PLAYER_CONFIGS.players.{p_name}.slots.plus8_skill_coach",
                        message=(
                            f"Vi phạm luật Nexon Anti-Overlap tại {p_name}: Kỹ năng bổ sung +8 "
                            f"'{add_skill_raw.strip()}' bị trùng lặp với kỹ năng của HLV Tập luyện ('{skill_item.strip()}')."
                        )
                    ))

    # 4. PR-04: Role & Position Conflict Guard
    for slot, indiv in config.individual_tactics.items():
        code_str = (indiv.code_string or "").upper()

        # A. CM must not have AS1
        if slot in ["CM", "LCM", "RCM"] and "AS1" in code_str:
            issues.append(ValidationIssue(
                rule_id="PR-04",
                severity=ValidationSeverity.CRITICAL,
                path=f"individual_tactics.{slot}.code_string",
                message=f"Xung đột vai trò tại {slot}: Cấm cài AS1 (Ở lại phía sau) cho tiền vệ giữ nhịp (bài học Bellingham)."
            ))

        # B. Single Pivot CDM must not have PF1
        if slot in ["CDM"] and "PF1" in code_str:
            issues.append(ValidationIssue(
                rule_id="PR-04",
                severity=ValidationSeverity.HIGH,
                path=f"individual_tactics.{slot}.code_string",
                message=f"Xung đột vai trò tại {slot}: Cấm thả rông PF1 (Di chuyển tự do) cho mỏ neo duy nhất bảo vệ Zone 14."
            ))

    # C. Zero-ST Wing Penetration Check
    formation_str = config.metadata.formation or ""
    formation_style = config.metadata.formation_style or ""
    is_zero_st = formation_str.endswith("-0") or "zero-st" in formation_style.lower()

    if is_zero_st:
        wing_slots = [slot for slot in config.individual_tactics.keys() if slot in ["LM", "RM", "LW", "RW"]]
        has_penetration = False
        for ws in wing_slots:
            w_code = (config.individual_tactics[ws].code_string or "").upper()
            if "CC2" in w_code or "SC1" in w_code:
                has_penetration = True
                break
        if wing_slots and not has_penetration:
            issues.append(ValidationIssue(
                rule_id="PR-04",
                severity=ValidationSeverity.HIGH,
                path="individual_tactics.Wings",
                message="Thiếu mũi nhọn trong sơ đồ Zero-ST: Ít nhất 1 tiền vệ cánh (LM/RM) phải cài lệnh CC2 (Cắt vào trong) hoặc SC1 (Xâm nhập box)."
            ))

    # 5. PR-05: Warning Bẫy Thể Lực (Re-introduced per User Note 2)
    depth = config.team_tactic.defense.depth
    def_style = config.team_tactic.defense.tactic_style.lower()

    is_continuous_pressure = (
        "liên tục" in def_style or
        "constant pressure" in def_style or
        "continuous pressure" in def_style or
        "mất bóng" in def_style
    )

    if depth >= 8 or is_continuous_pressure:
        issues.append(ValidationIssue(
            rule_id="PR-05",
            severity=ValidationSeverity.MEDIUM,
            path="team_tactic.defense",
            message=f"Cảnh báo bẫy thể lực: Depth = {depth} hoặc Phong cách '{def_style}' có nguy cơ cao làm kiệt quệ thể lực toàn đội từ phút 70+ (bài học xương máu Gegenpressing)."
        ))

    return issues
