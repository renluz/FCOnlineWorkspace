"""
Tactic Verifier Core Orchestrator
"""

import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional, Dict, Any, List

from .schemas import (
    TacticConfig,
    ValidationResult,
    ValidationSummary,
    ValidationIssue,
    ValidationSeverity
)
from .engine_validator import validate_engine_rules
from .project_validator import validate_project_rules
from .evidence_validator import validate_evidence_rules


class TacticVerifier:
    def __init__(self, allow_multi_variables: bool = False):
        self.allow_multi_variables = allow_multi_variables

    def verify_file(
        self,
        tactic_path: str | Path,
        squad_path: Optional[str | Path] = None,
        configs_path: Optional[str | Path] = None,
        baseline_path: Optional[str | Path] = None
    ) -> ValidationResult:
        t_path = Path(tactic_path)
        timestamp_str = datetime.now(timezone.utc).isoformat()

        if not t_path.exists():
            return ValidationResult(
                timestamp=timestamp_str,
                verified_file=str(t_path),
                status="FAIL",
                summary=ValidationSummary(total_rules_checked=0, passed=0, errors_count=1, warnings_count=0),
                errors=[ValidationIssue(
                    rule_id="SYS-01",
                    severity=ValidationSeverity.CRITICAL,
                    path=str(t_path),
                    message=f"File không tồn tại: {t_path}"
                )]
            )

        # 1. Load tactic JSON
        try:
            with open(t_path, "r", encoding="utf-8") as f:
                raw_tactic_data = json.load(f)
        except Exception as e:
            return ValidationResult(
                timestamp=timestamp_str,
                verified_file=str(t_path),
                status="FAIL",
                summary=ValidationSummary(total_rules_checked=0, passed=0, errors_count=1, warnings_count=0),
                errors=[ValidationIssue(
                    rule_id="SYS-02",
                    severity=ValidationSeverity.CRITICAL,
                    path=str(t_path),
                    message=f"Lỗi đọc JSON: {str(e)}"
                )]
            )

        # Parse into Pydantic schema
        try:
            config = TacticConfig(**raw_tactic_data)
        except Exception as e:
            return ValidationResult(
                timestamp=timestamp_str,
                verified_file=str(t_path),
                status="FAIL",
                summary=ValidationSummary(total_rules_checked=1, passed=0, errors_count=1, warnings_count=0),
                errors=[ValidationIssue(
                    rule_id="SCHEMA-01",
                    severity=ValidationSeverity.CRITICAL,
                    path=str(t_path),
                    message=f"Lỗi cấu trúc schema không hợp lệ: {str(e)}"
                )]
            )

        # 2. Auto-locate sibling files if not provided
        parent_dir = t_path.parent

        squad_data: Optional[Dict[str, Any]] = None
        s_path = Path(squad_path) if squad_path else parent_dir / "02_CURRENT_SQUAD.json"
        if s_path.exists():
            try:
                with open(s_path, "r", encoding="utf-8") as f:
                    squad_data = json.load(f)
            except Exception:
                pass

        configs_data: Optional[Dict[str, Any]] = None
        c_path = Path(configs_path) if configs_path else parent_dir / "04_PLAYER_CONFIGS.json"
        if c_path.exists():
            try:
                with open(c_path, "r", encoding="utf-8") as f:
                    configs_data = json.load(f)
            except Exception:
                pass

        baseline_config: Optional[TacticConfig] = None
        if baseline_path:
            b_path = Path(baseline_path)
            if b_path.exists():
                try:
                    with open(b_path, "r", encoding="utf-8") as f:
                        b_raw = json.load(f)
                        baseline_config = TacticConfig(**b_raw)
                except Exception:
                    pass

        # 3. Execute 3-Tier Validation
        all_issues: List[ValidationIssue] = []

        # Tier 1: Engine Validator
        all_issues.extend(validate_engine_rules(config))

        # Tier 2: Project Validator
        all_issues.extend(validate_project_rules(config, squad_data, configs_data))

        # Tier 3: Evidence Validator
        all_issues.extend(validate_evidence_rules(config, baseline_config, self.allow_multi_variables))

        # 4. Classify issues
        critical_and_high = [i for i in all_issues if i.severity in [ValidationSeverity.CRITICAL, ValidationSeverity.HIGH]]
        warnings = [i for i in all_issues if i.severity in [ValidationSeverity.MEDIUM, ValidationSeverity.LOW]]

        errors_count = len(critical_and_high)
        warnings_count = len(warnings)

        if errors_count > 0:
            status = "FAIL"
        elif warnings_count > 0:
            status = "WARNING"
        else:
            status = "PASS"

        total_rules = 9
        passed = max(0, total_rules - errors_count)

        return ValidationResult(
            timestamp=timestamp_str,
            verified_file=str(t_path),
            status=status,
            summary=ValidationSummary(
                total_rules_checked=total_rules,
                passed=passed,
                errors_count=errors_count,
                warnings_count=warnings_count
            ),
            errors=critical_and_high,
            warnings=warnings
        )
