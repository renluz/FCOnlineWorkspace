"""
Constants and Configurable Rules for Tactic Verifier
"""

# Base Formations recognized by FC Online / FIFA engine
FORMATIONS_BASE = {
    "4231", "4141", "4123", "433", "442", "4222", "4312", "4132", "41212",
    "4213", "4321", "4411", "451", "424", "42211",
    "343", "3412", "3232", "32212", "31213", "3142", "352",
    "541", "532", "523", "5212", "51211", "5221"
}

# Configurable Limits (Configurable by region/client)
CORNERS_MAX_VALUE: int = 5       # Client Garena VN standard (5 ticks)
FREE_KICKS_MAX_VALUE: int = 5    # Client Garena VN standard (5 ticks)
SLIDER_MIN: int = 1
SLIDER_MAX: int = 10

# Valid Tactical Enums (normalized matching handles "Tiếng Việt / English")
VALID_DEFENSE_STYLES = [
    "Lùi sâu", "Drop Back",
    "Cân bằng", "Balanced",
    "Gây áp lực khi đỡ bóng hỏng", "Press After Heavy Touch",
    "Gây áp lực sau khi mất bóng", "Áp lực ngay khi mất bóng", "Press After Possession Loss",
    "Áp lực liên tục", "Cùng nhau gây áp lực", "Constant Pressure", "Continuous Pressure"
]

VALID_BUILD_UP_STYLES = [
    "Xây dựng chậm", "Slow Build Up",
    "Cân bằng", "Balanced",
    "Chuyền dài", "Long Ball",
    "Chuyển trạng thái nhanh", "Xây dựng nhanh", "Fast Build Up"
]

VALID_CHANCE_CREATION_STYLES = [
    "Cân bằng", "Balanced",
    "Chuyền dài", "Long Ball",
    "Chuyền mạo hiểm", "Direct Passing",
    "Kiến tạo cơ hội", "Forward Runs"
]

VALID_TENDENCIES = [
    "Cân bằng / Chung", "Cân bằng", "Balanced",
    "Tấn công", "Attacking",
    "Tổng tấn công", "All Out Attack",
    "Phòng thủ", "Defensive"
]

# Standard UI Code Group Mapping (Positional prefix constraints)
STANDARD_UI_CODE_GROUP_MAP = {
    "LM_RM": ["CC", "DS", "IN", "SC", "SR"],
    "LW_RW": ["CC", "DS", "IN", "SC", "SR"],
    "CAM": ["CC", "DS", "IN", "PF", "SC"],
    "CM": ["AS", "DP", "IN", "PF", "SC"],
    "CDM": ["AS", "DP", "DB", "IN"],
    "LB_RB": ["AR", "IN", "SR"],
    "LWB_RWB": ["AR", "IN", "SR"],
    "CB": ["AS", "IN"],
    "GK": ["GK_CROSS", "GK_SWEEPER"]
}

# Mapping position slot to its group key
# Trong sơ đồ 4-1-2-3-0, LAM và RAM là tiền vệ cánh tấn công mang chỉ thị nhóm LM_RM (CC, DS, IN, SC, SR)
SLOT_TO_GROUP_MAP = {
    "LM": "LM_RM", "RM": "LM_RM",
    "LW": "LW_RW", "RW": "LW_RW",
    "CAM": "CAM", "LAM": "LM_RM", "RAM": "LM_RM",
    "CM": "CM", "LCM": "CM", "RCM": "CM",
    "CDM": "CDM", "LDM": "CDM", "RDM": "CDM",
    "LB": "LB_RB", "RB": "LB_RB",
    "LWB": "LWB_RWB", "RWB": "LWB_RWB",
    "CB": "CB", "LCB": "CB", "RCB": "CB",
    "GK": "GK"
}
