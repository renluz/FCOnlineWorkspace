"""
Pydantic Schemas for Tactic Verifier and 03_CURRENT_TACTICS.json
"""

from typing import Dict, List, Optional, Any
from enum import Enum
from pydantic import BaseModel, Field


class ValidationSeverity(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class ValidationIssue(BaseModel):
    rule_id: str
    severity: ValidationSeverity
    path: str
    message: str


class ValidationSummary(BaseModel):
    total_rules_checked: int = 0
    passed: int = 0
    errors_count: int = 0
    warnings_count: int = 0


class ValidationResult(BaseModel):
    timestamp: str
    verified_file: str
    status: str  # "PASS" | "FAIL" | "WARNING"
    summary: ValidationSummary
    errors: List[ValidationIssue] = Field(default_factory=list)
    warnings: List[ValidationIssue] = Field(default_factory=list)


# --- 03_CURRENT_TACTICS.json Ground Truth Schemas ---

class TacticMetadata(BaseModel):
    project: Optional[str] = None
    updated_at: Optional[str] = None
    preset_name: Optional[str] = None
    test_id: Optional[str] = None
    formation: str
    formation_style: Optional[str] = None
    manager: Optional[str] = None
    schema_standard: Optional[str] = None
    notes: Optional[str] = None
    status: Optional[str] = None  # Note 1: Defaults to None if absent


class TeamTacticDefense(BaseModel):
    tactic_style: str
    width: int
    depth: int
    notes: Optional[str] = None


class TeamTacticOffense(BaseModel):
    build_up_style: str
    chance_creation_style: str
    attack_width: int
    players_in_box: int
    corners: int
    free_kicks: int
    tendency: str
    notes: Optional[str] = None


class TeamTactic(BaseModel):
    defense: TeamTacticDefense
    offense: TeamTacticOffense


class IndividualTacticSlot(BaseModel):
    player: str
    workrate: Optional[str] = None
    code_string: Optional[str] = None
    role: Optional[str] = None
    defensive_role: Optional[str] = None
    settings: Optional[Dict[str, Any]] = None
    tactical_logic: Optional[str] = None
    verification: Optional[str] = None
    notes: Optional[str] = None


class SetPiecesAndRoles(BaseModel):
    captain: Optional[str] = None
    penalty: Optional[str] = None
    left_corner: Optional[str] = None
    right_corner: Optional[str] = None
    left_free_kick: Optional[str] = None
    right_free_kick: Optional[str] = None
    long_free_kick: Optional[str] = None
    verification: Optional[str] = None
    notes: Optional[str] = None


class TacticConfig(BaseModel):
    metadata: TacticMetadata = Field(..., alias="_metadata")
    ui_code_group_map: Optional[Dict[str, List[str]]] = None
    team_tactic: TeamTactic
    set_pieces_and_roles: Optional[SetPiecesAndRoles] = None
    individual_tactics: Dict[str, IndividualTacticSlot]

    model_config = {"populate_by_name": True}
