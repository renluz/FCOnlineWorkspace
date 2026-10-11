#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/validate_owned_inventory.py
Bộ kiểm tra tính nhất quán và toàn vẹn của inventory cầu thủ sở hữu thực tế (OWNED_PLAYER_DATA).

Quy tắc bất biến:
- data/vn_owned_players.json là SOURCE_OF_TRUTH từ screenshot game của người dùng.
- Bất kỳ sai lệch nào về season sẽ gây lỗi: OWNED_PLAYER_SEASON_MISMATCH
- Bất kỳ sai lệch nào về grade, displayed_ovr, database_base_ovr, salary, player_name sẽ gây lỗi: OWNED_INVENTORY_VALIDATION_FAILED
- Schema bắt buộc gồm:
  player_name, season, grade, displayed_ovr, database_base_ovr, salary, current_slot, natural_positions
"""

import os
import sys
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWNED_JSON_PATH = os.path.join(BASE_DIR, "data", "vn_owned_players.json")

def load_source_of_truth():
    if not os.path.exists(OWNED_JSON_PATH):
        raise FileNotFoundError(f"SOURCE_OF_TRUTH_NOT_FOUND: Không tìm thấy {OWNED_JSON_PATH}")
    with open(OWNED_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {p["player_name"]: p for p in data}

def validate_player(player_record, source_dict=None):
    """
    Kiểm tra 1 bản ghi cầu thủ xem có khớp chính xác với SOURCE_OF_TRUTH không.
    """
    if source_dict is None:
        source_dict = load_source_of_truth()
        
    p_name = player_record.get("player_name")
    if not p_name or p_name not in source_dict:
        raise ValueError(f"OWNED_INVENTORY_VALIDATION_FAILED: Cầu thủ '{p_name}' không tồn tại trong data/vn_owned_players.json")
        
    truth = source_dict[p_name]
    
    # 1. Kiểm tra Season
    rec_season = player_record.get("season")
    if rec_season != truth["season"]:
        err_msg = (
            f"OWNED_PLAYER_SEASON_MISMATCH: Cầu thủ '{p_name}' có mùa thật là '{truth['season']}', "
            f"nhưng bản ghi lại ghi nhận '{rec_season}'. Nghiêm cấm tự động sửa mùa."
        )
        print(f"[ERROR] {err_msg}", file=sys.stderr)
        raise ValueError(err_msg)
        
    # 2. Kiểm tra Grade, Displayed OVR, Database Base OVR, Salary
    mismatches = []
    if int(player_record.get("grade", 0)) != int(truth["grade"]):
        mismatches.append(f"grade (thật: +{truth['grade']}, ghi: +{player_record.get('grade')})")
        
    rec_disp_ovr = player_record.get("displayed_ovr") or player_record.get("ovr")
    if int(rec_disp_ovr or 0) != int(truth["displayed_ovr"]):
        mismatches.append(f"displayed_ovr (thật: {truth['displayed_ovr']}, ghi: {rec_disp_ovr})")
        
    if "database_base_ovr" in player_record:
        if int(player_record.get("database_base_ovr", 0)) != int(truth["database_base_ovr"]):
            mismatches.append(f"database_base_ovr (thật: {truth['database_base_ovr']}, ghi: {player_record.get('database_base_ovr')})")
            
    if int(player_record.get("salary", 0)) != int(truth["salary"]):
        mismatches.append(f"salary (thật: {truth['salary']}, ghi: {player_record.get('salary')})")
        
    if mismatches:
        err_msg = f"OWNED_INVENTORY_VALIDATION_FAILED: Cầu thủ '{p_name}' sai lệch thông số: {', '.join(mismatches)}"
        print(f"[ERROR] {err_msg}", file=sys.stderr)
        raise ValueError(err_msg)
        
    # 3. Kiểm tra Schema vị trí
    if "current_slot" not in player_record and "position" not in player_record:
        raise ValueError(f"OWNED_INVENTORY_VALIDATION_FAILED: Thiếu trường 'current_slot' cho '{p_name}'")
    if "natural_positions" not in truth or not isinstance(truth["natural_positions"], list):
        raise ValueError(f"OWNED_INVENTORY_VALIDATION_FAILED: 'natural_positions' của '{p_name}' phải là mảng danh sách vị trí tự nhiên.")
        
    return True

def validate_squad(squad_records):
    """
    Kiểm tra toàn bộ danh sách cầu thủ trong 1 đội hình.
    """
    source_dict = load_source_of_truth()
    for idx, p in enumerate(squad_records):
        try:
            validate_player(p, source_dict)
        except Exception as e:
            print(f"[FATAL] Dừng pipeline tại vị trí cầu thủ thứ {idx + 1}: {e}", file=sys.stderr)
            raise

def self_check():
    """Tự kiểm tra tính toàn vẹn của file data/vn_owned_players.json"""
    source_dict = load_source_of_truth()
    print(f"=== KIỂM TOÁN TÍNH TOÀN VẸN INVENTORY SỞ HỮU ({len(source_dict)} CẦU THỦ) ===")
    
    # 1. Sergio Ramos phải là season 19, displayed_ovr 94, salary 18, grade 1, base OVR 94
    ramos = source_dict.get("Sergio Ramos")
    if not ramos or ramos["season"] != "19" or ramos["displayed_ovr"] != 94 or ramos["salary"] != 18 or ramos["grade"] != 1 or ramos["database_base_ovr"] != 94:
        raise ValueError("OWNED_INVENTORY_VALIDATION_FAILED: Sergio Ramos không đúng thông số chuẩn season 19, +1, displayed OVR 94, base OVR 94, salary 18")
        
    # 2. W. Hennessey phải là season HOT, displayed_ovr 96, salary 13, grade 1, base OVR 91
    hennessey = source_dict.get("W. Hennessey")
    if not hennessey or hennessey["season"] != "HOT" or hennessey["displayed_ovr"] != 96 or hennessey["salary"] != 13 or hennessey["grade"] != 1 or hennessey["database_base_ovr"] != 91:
        raise ValueError("OWNED_INVENTORY_VALIDATION_FAILED: W. Hennessey không đúng thông số chuẩn season HOT, +1, displayed OVR 96, base OVR 91, salary 13")
        
    # 3. V. Boniface phải là season WS, grade 3, displayed_ovr 119, salary 28, base OVR 117
    boniface = source_dict.get("V. Boniface")
    if not boniface or boniface["season"] != "WS" or boniface["grade"] != 3 or boniface["displayed_ovr"] != 119 or boniface["salary"] != 28 or boniface["database_base_ovr"] != 117:
        raise ValueError("OWNED_INVENTORY_VALIDATION_FAILED: V. Boniface không đúng thông số chuẩn season WS, +3, displayed OVR 119, base OVR 117, salary 28")

    # 4. G. Zambrotta phải là season WG, grade 1, displayed_ovr 119, salary 30, natural_positions ['RB', 'LB']
    zambrotta = source_dict.get("G. Zambrotta")
    if not zambrotta or zambrotta["season"] != "WG" or zambrotta["grade"] != 1 or zambrotta["displayed_ovr"] != 119 or zambrotta["salary"] != 30 or zambrotta["natural_positions"] != ["RB", "LB"]:
        raise ValueError("OWNED_INVENTORY_VALIDATION_FAILED: G. Zambrotta WG phải có natural_positions là ['RB', 'LB']")

    # 5. A. Del Piero phải là HOT, displayed_ovr 102, current_slot LW, natural_positions ['CF', 'CAM'], base OVR 97
    del_piero = source_dict.get("A. Del Piero")
    if not del_piero or del_piero["season"] != "HOT" or del_piero["displayed_ovr"] != 102 or del_piero["current_slot"] != "LW" or del_piero["database_base_ovr"] != 97 or del_piero["natural_positions"] != ["CF", "CAM"]:
        raise ValueError("OWNED_INVENTORY_VALIDATION_FAILED: A. Del Piero HOT phải có natural_positions là ['CF', 'CAM']")

    # 6. R. Gullit phải là HOT, displayed_ovr 103, current_slot LCM, natural_positions ['CM', 'LW', 'ST'], base OVR 98
    gullit = source_dict.get("R. Gullit")
    if not gullit or gullit["season"] != "HOT" or gullit["displayed_ovr"] != 103 or gullit["current_slot"] != "LCM" or gullit["database_base_ovr"] != 98 or gullit["natural_positions"] != ["CM", "LW", "ST"]:
        raise ValueError("OWNED_INVENTORY_VALIDATION_FAILED: R. Gullit HOT phải có natural_positions là ['CM', 'LW', 'ST']")

    # 7. Rodri phải là 19, displayed_ovr 95, current_slot RCM, natural_positions ['CDM', 'CM'], base OVR 92
    rodri = source_dict.get("Rodri")
    if not rodri or rodri["season"] != "19" or rodri["displayed_ovr"] != 95 or rodri["current_slot"] != "RCM" or rodri["database_base_ovr"] != 92 or rodri["natural_positions"] != ["CDM", "CM"]:
        raise ValueError("OWNED_INVENTORY_VALIDATION_FAILED: Rodri 19 phải có natural_positions là ['CDM', 'CM']")

    for name, p in source_dict.items():
        print(
            f"  ✓ {name:16} | Mùa: {p['season']:5} | Cấp: +{p['grade']} | "
            f"Disp OVR: {p['displayed_ovr']:3} | Base OVR: {p['database_base_ovr']:3} | "
            f"Lương: {p['salary']:2} | Slot: {p['current_slot']:5} | Natural: {p['natural_positions']}"
        )
        
    print("\nOWNED_INVENTORY_VALIDATION_PASSED: Toàn bộ 13 cầu thủ sở hữu đạt chuẩn 100% Source of Truth với Schema mới.")
    return True

if __name__ == "__main__":
    try:
        self_check()
    except Exception as e:
        print(f"[FATAL] Kiểm toán thất bại: {e}", file=sys.stderr)
        sys.exit(1)
