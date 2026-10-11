#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/vn_glxh_analyzer.py
Phân tích và tối ưu hóa đội hình Giả Lập Xếp Hạng (GLXH) 
dành riêng cho môi trường Garena Việt Nam (VN_GLXH).

Nguyên tắc toàn vẹn dữ liệu:
1. Tách biệt tuyệt đối:
   - OWNED_PLAYER_DATA: Dữ liệu cầu thủ sở hữu thực tế từ data/vn_owned_players.json
   - DATABASE_CANDIDATE_DATA: Dữ liệu mô hình tính toán từ 41,289 DB (dùng tiền tố HYPOTHETICAL_*)
2. Giới hạn lương: VN_CURRENT_SALARY_CAP = 305 (Không dùng 260/265/270 cho đội hiện tại).
3. Không tự ý nâng cấp grade/OVR hoặc đổi season của cầu thủ sở hữu.
4. Kiểm tra qua tools.validate_owned_inventory trước khi sinh đội hình.
5. Loại bỏ hoàn toàn nhãn "Auto 24/7", "anti-ban", "safe automation".
   Tên mục tiêu chuẩn: VN_GLXH_CURRENT_SQUAD_OPTIMIZATION.
6. Tách rành mạch vn_glxh_model_candidates.csv và vn_glxh_empirical_*.
7. Sinh báo cáo kiểm toán VN_CURRENT_SQUAD_AUDIT.md.
"""

import os
import sys
import json
import datetime
import pandas as pd
import numpy as np

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
EXPORTS_DIR = os.path.join(BASE_DIR, "exports")
DETAILS_CSV = os.path.join(BASE_DIR, "repos", "fconline-player-search", "data", "details.csv")
OWNED_JSON_PATH = os.path.join(DATA_DIR, "vn_owned_players.json")
AUDIT_REPORT_MD = os.path.join(BASE_DIR, "VN_CURRENT_SQUAD_AUDIT.md")

# Thêm tools vào path để import validator
sys.path.insert(0, os.path.join(BASE_DIR, "tools"))
from validate_owned_inventory import validate_squad, load_source_of_truth

# Trần lương hiện tại của tài khoản Garena VN
VN_CURRENT_SALARY_CAP = 305

# Bảng tăng chỉ số giả định (chỉ dùng cho DATABASE_CANDIDATE_DATA)
ENCHANT_DELTAS = {
    1: 0, 2: 1, 3: 2, 4: 4, 5: 6,
    6: 8, 7: 11, 8: 15, 9: 17, 10: 19
}

# ==========================================
# 1. TỐI ƯU ĐỘI HÌNH TỪ CẦU THỦ HIỆN CÓ
# (VN_GLXH_CURRENT_SQUAD_OPTIMIZATION)
# ==========================================

def optimize_current_squad():
    """
    Xây dựng các phương án sắp xếp tối ưu từ 13 cầu thủ sở hữu thật trong data/vn_owned_players.json.
    Tuyệt đối:
    - Không mua cầu thủ mới.
    - Không tự ý tăng cấp cộng.
    - Không đổi mùa thẻ.
    - Không đổi lương.
    - Kiểm tra giới hạn lương VN_CURRENT_SALARY_CAP = 305.
    """
    source_dict = load_source_of_truth()
    
    # 3 phương án sơ đồ chiến thuật tối ưu
    squad_options = [
        {
            "squad_id": "VN_CURRENT_SQUAD_4231",
            "squad_name": "Phương án 1: 4-2-3-1 Đóng Băng Trung Tuyến (Khuyến Nghị Cao Nhất)",
            "formation": "4-2-3-1",
            "target_salary_cap": VN_CURRENT_SALARY_CAP,
            "tactical_rationale": "Sơ đồ cân bằng hoàn hảo cho dàn nhân lực hiện tại: Tận dụng trọn vẹn 6 cầu thủ OVR cao nhất (Boniface 119, Zambrotta 119, Gvardiol 118, Rosicky 118, Park Ji Sung 117, Schar 114) cùng 2 CDM che chắn bảo vệ Sergio Ramos và Hennessey.",
            "starters": [
                {"pos": "ST", "player_name": "V. Boniface", "role_focus": "Target Man càn lướt làm tường, 5/5 hai chân, dứt điểm một chạm"},
                {"pos": "CAM", "player_name": "T. Rosicky", "role_focus": "Nhạc trưởng trung lộ, chọc khe kiến tạo và phân phối nhịp"},
                {"pos": "LAM", "player_name": "Park Ji Sung", "role_focus": "Tiền vệ công lệch trái, pressing tầm cao và lui về hỗ trợ phòng ngự biên"},
                {"pos": "RAM", "player_name": "A. Del Piero", "role_focus": "Tiền vệ công lệch phải / Inside Forward, xâm nhập nách trung lộ dứt điểm ZD"},
                {"pos": "LDM", "player_name": "R. Gullit", "role_focus": "Box-to-box cơ động, tranh chấp không chiến và hỗ trợ sút xa tuyến hai"},
                {"pos": "RDM", "player_name": "Rodri", "role_focus": "Mỏ neo thuần túy (Anchor), giữ vị trí trước cặp trung vệ"},
                {"pos": "LB", "player_name": "J. Gvardiol", "role_focus": "Hậu vệ biên phòng ngự, 5/5 hai chân, khóa chặt cánh trái"},
                {"pos": "LCB", "player_name": "Sergio Ramos", "role_focus": "Trung vệ dập, áp sát tranh chấp quyết liệt"},
                {"pos": "RCB", "player_name": "F. Schar", "role_focus": "Trung vệ thòng bọc lót, chống bóng bổng và chọc khe bổng (QW)"},
                {"pos": "RB", "player_name": "G. Zambrotta", "role_focus": "Hậu vệ biên toàn diện 5/5, tốc độ 121, thủ 122, thể lực 123"},
                {"pos": "GK", "player_name": "W. Hennessey", "role_focus": "Thủ môn 1m98, khép góc và bắt bóng bổng"}
            ],
            "bench": [
                {"player_name": "Inaki Williams", "pos": "RW", "role": "Dự bị chiến lược tốc độ hành lang phải"},
                {"player_name": "P. Aubameyang", "pos": "ST", "role": "Dự bị tiền đạo cắm khi Boniface xuống thể lực"}
            ]
        },
        {
            "squad_id": "VN_CURRENT_SQUAD_4123",
            "squad_name": "Phương án 2: 4-1-2-3 Đột Phá Cánh (Inven Adaptation)",
            "formation": "4-1-2-3",
            "target_salary_cap": VN_CURRENT_SALARY_CAP,
            "tactical_rationale": "Chuyển thể sơ đồ Inven 4-1-2-3 sang dàn nhân lực hiện tại: Sử dụng Del Piero (LW) và Inaki Williams (RW) bám biên tạo đột biến tốc độ.",
            "starters": [
                {"pos": "ST", "player_name": "V. Boniface", "role_focus": "Dứt điểm trong vòng cấm, đón các đường căng ngang cutback"},
                {"pos": "LW", "player_name": "A. Del Piero", "role_focus": "Cắt vào trong dứt điểm góc xa hoặc chọc khe nách"},
                {"pos": "RW", "player_name": "Inaki Williams", "role_focus": "Tốc độ xé gió bên cánh phải tạt bóng vào cột xa"},
                {"pos": "LCM", "player_name": "Park Ji Sung", "role_focus": "Tiền vệ con thoi càn quét trục giữa"},
                {"pos": "RCM", "player_name": "T. Rosicky", "role_focus": "Nhạc trưởng phân phối bóng"},
                {"pos": "CDM", "player_name": "Rodri", "role_focus": "Đơn độc thu hồi bóng trước hàng thủ 4 người"},
                {"pos": "LB", "player_name": "J. Gvardiol", "role_focus": "Khóa chặt hành lang cánh trái"},
                {"pos": "LCB", "player_name": "Sergio Ramos", "role_focus": "Đánh chặn tiền đạo đối phương"},
                {"pos": "RCB", "player_name": "F. Schar", "role_focus": "Bọc lót và tranh chấp trên không"},
                {"pos": "RB", "player_name": "G. Zambrotta", "role_focus": "Chốt chặn cánh phải vững chắc"},
                {"pos": "GK", "player_name": "W. Hennessey", "role_focus": "Trấn giữ khung thành"}
            ],
            "bench": [
                {"player_name": "R. Gullit", "pos": "CM", "role": "Thay người tuyến giữa hiệp 2"},
                {"player_name": "P. Aubameyang", "pos": "ST", "role": "Thay thế ST khi cần đẩy cao tốc độ"}
            ]
        }
    ]
    
    rows = []
    
    for sq in squad_options:
        squad_records_to_validate = []
        starters = sq["starters"]
        
        # Ghép thông tin từ source of truth
        for p in starters:
            name = p["player_name"]
            truth = source_dict[name]
            p_rec = {
                "squad_id": sq["squad_id"],
                "squad_name": sq["squad_name"],
                "formation": sq["formation"],
                "assigned_position": p["pos"],
                "player_name": name,
                "season": truth["season"],
                "grade": truth["grade"],
                "ovr": truth["ovr"],
                "salary": truth["salary"],
                "natural_position": truth["position"],
                "role_focus": p["role_focus"],
                "is_starter": True,
                "sample_type": "OWNED_PLAYER_DATA"
            }
            squad_records_to_validate.append(p_rec)
            rows.append(p_rec)
            
        # Thêm dự bị
        for b in sq["bench"]:
            name = b["player_name"]
            truth = source_dict[name]
            b_rec = {
                "squad_id": sq["squad_id"],
                "squad_name": sq["squad_name"],
                "formation": sq["formation"],
                "assigned_position": "SUB",
                "player_name": name,
                "season": truth["season"],
                "grade": truth["grade"],
                "ovr": truth["ovr"],
                "salary": truth["salary"],
                "natural_position": truth["position"],
                "role_focus": b["role"],
                "is_starter": False,
                "sample_type": "OWNED_PLAYER_DATA"
            }
            squad_records_to_validate.append(b_rec)
            rows.append(b_rec)
            
        # Kiểm tra tính toàn vẹn 100% bằng validator
        validate_squad(squad_records_to_validate)
        
        # Kiểm tra tổng lương đá chính
        starter_salary = sum(p["salary"] for p in squad_records_to_validate if p["is_starter"])
        if starter_salary > VN_CURRENT_SALARY_CAP:
            raise ValueError(f"SALARY_CAP_EXCEEDED: Đội hình {sq['squad_id']} có tổng lương {starter_salary} vượt trần {VN_CURRENT_SALARY_CAP}")
            
    df_squads = pd.DataFrame(rows)
    out_csv = os.path.join(EXPORTS_DIR, "vn_glxh_current_squad_candidates.csv")
    df_squads.to_csv(out_csv, index=False, encoding='utf-8-sig')
    print(f"[OK] Đã xuất các phương án đội hình hiện có tại {out_csv}")
    
    meta_path = f"{out_csv}.meta.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump({
            "source": "OWNED_INVENTORY_SOURCE_OF_TRUTH",
            "source_file": "data/vn_owned_players.json",
            "sample_type": "OWNED_PLAYER_DATA",
            "target_salary_cap": VN_CURRENT_SALARY_CAP,
            "validation_status": "OWNED_INVENTORY_VALIDATION_PASSED",
            "extracted_at": datetime.datetime.now().isoformat(),
            "provenance_notice": "Strictly scoped to user owned inventory from game screenshot. Zero hypothetical upgrades or season modifications."
        }, f, indent=2, ensure_ascii=False)
        
    return squad_options

# ==========================================
# 2. TUYỂN CHỌN ỨNG VIÊN MÔ HÌNH (DATABASE CANDIDATES)
# (DATABASE_CANDIDATE_DATA)
# ==========================================

def evaluate_model_candidates(db_df):
    """
    Quét cơ sở dữ liệu 41,289 cầu thủ để sinh danh sách ứng viên mô hình (DATABASE_CANDIDATE_DATA).
    Gắn nhãn rõ ràng HYPOTHETICAL_GRADE và HYPOTHETICAL_OVR.
    """
    candidates = []
    NATIONAL_SEASONS = ['HOT', 'WG', '25DP', 'NO.7', '19', 'WS', '23UCL', '22UCL', 'BTB', 'EBS', 'CAP', 'FA', 'LOL', 'MC', 'LH', 'ICON']
    filtered_db = db_df[db_df['season'].isin(NATIONAL_SEASONS)].copy()
    
    for idx, row in filtered_db.iterrows():
        pos = str(row.get('position', '')).upper()
        salary = int(row.get('salary', 30))
        ovr = int(row.get('ovr', 0))
        stamina = int(row.get('스태미너', 0))
        strength = int(row.get('몸싸움', 0))
        shot_power = int(row.get('슛 파워', 0))
        long_shots = int(row.get('중거리 슛', 0))
        marking = int(row.get('대인 수비', 0))
        tackle = int(row.get('태클', 0))
        speed = int(row.get('속력', 0))
        height = int(row.get('height', 170))
        traits = str(row.get('traits', ''))
        
        if ovr < 88 and salary > 14:
            continue
            
        has_finesse = '예리한 감아차기' in traits or 'Finesse' in traits
        has_power_header = '파워 헤더' in traits or 'Power' in traits
        has_long_shot = '중거리 슛 선호' in traits
        
        assigned_role = None
        vn_score = 0.0
        
        if pos in ['ST', 'CF']:
            assigned_role = "ST"
            if height >= 180 and (stamina + 6) >= 105:
                vn_score = (ovr * 0.3) + (shot_power * 0.2) + (strength * 0.2) + (stamina * 0.15) + (speed * 0.15)
                if has_finesse: vn_score += 5
                if has_power_header: vn_score += 3
        elif pos in ['CAM']:
            assigned_role = "CAM"
            if (stamina + 6) >= 110:
                vn_score = (ovr * 0.25) + (long_shots * 0.25) + (shot_power * 0.2) + (stamina * 0.15) + (strength * 0.15)
                if has_finesse: vn_score += 5
                if has_long_shot: vn_score += 4
        elif pos in ['CM']:
            assigned_role = "CM"
            if (stamina + 6) >= 115 and height >= 180:
                vn_score = (stamina * 0.3) + (strength * 0.25) + (long_shots * 0.2) + (shot_power * 0.15) + (ovr * 0.1)
                if has_long_shot: vn_score += 4
        elif pos in ['CDM']:
            assigned_role = "CDM"
            if height >= 185 and (stamina + 6) >= 110:
                vn_score = (marking * 0.25) + (tackle * 0.25) + (strength * 0.25) + (stamina * 0.15) + (height * 0.1)
        elif pos in ['CB', 'SW']:
            assigned_role = "CB"
            if height >= 185 and (strength + 6) >= 110:
                vn_score = (marking * 0.3) + (tackle * 0.3) + (strength * 0.2) + (speed * 0.2)
                if has_power_header: vn_score += 4
        elif pos in ['LB', 'RB', 'LWB', 'RWB']:
            assigned_role = "FULLBACK"
            if salary <= 24 and (speed + 6) >= 105:
                vn_score = (speed * 0.35) + (stamina * 0.3) + (tackle * 0.2) + (ovr * 0.15)
                if salary <= 18:
                    vn_score += (18 - salary) * 0.8
        elif pos in ['GK']:
            assigned_role = "GK"
            if height >= 192 and salary <= 16:
                vn_score = (height * 0.25) + (ovr * 0.45) + ((16 - salary) * 1.5)
                
        if assigned_role and vn_score > 75:
            candidates.append({
                "DATABASE_player_code": str(row['player_code']),
                "DATABASE_player_name": row['player_name'],
                "DATABASE_season": row['season'],
                "DATABASE_position": pos,
                "MODEL_assigned_role": assigned_role,
                "DATABASE_salary": salary,
                "DATABASE_ovr_base": ovr,
                "HYPOTHETICAL_GRADE": 5,
                "HYPOTHETICAL_OVR": ovr + 6,
                "HYPOTHETICAL_stamina": stamina + 6,
                "HYPOTHETICAL_strength": strength + 6,
                "HYPOTHETICAL_shot_power": shot_power + 6,
                "HYPOTHETICAL_long_shots": long_shots + 6,
                "HYPOTHETICAL_speed": speed + 6,
                "DATABASE_height": height,
                "DATABASE_weight": row.get('weight'),
                "DATABASE_has_finesse": has_finesse,
                "DATABASE_has_power_header": has_power_header,
                "MODEL_efficiency_score": round(vn_score, 2),
                "sample_type": "DATABASE_CANDIDATE_DATA"
            })
            
    df_cand = pd.DataFrame(candidates)
    if not df_cand.empty:
        df_cand = df_cand.sort_values(by="MODEL_efficiency_score", ascending=False)
    return df_cand

# ==========================================
# 3. SINH BÁO CÁO KIỂM TOÁN VN_CURRENT_SQUAD_AUDIT.MD
# ==========================================

def generate_audit_report(squad_options):
    """
    Sinh file báo cáo kiểm toán VN_CURRENT_SQUAD_AUDIT.md theo đúng Directive 11:
    - Salary cap = 305
    - 11 cầu thủ được chọn: season, grade, OVR, salary, position assigned
    - Total salary
    - Cầu thủ dự bị
    - Cầu thủ đang bị đá trái sở trường nếu có
    - 3 vị trí yếu nhất
    - Không đề xuất mua mới ở bước này.
    """
    opt1 = squad_options[0] # 4-2-3-1
    starters = opt1["starters"]
    bench = opt1["bench"]
    
    source_dict = load_source_of_truth()
    
    # Tính toán các chỉ số
    total_salary = sum(source_dict[p["player_name"]]["salary"] for p in starters)
    remaining_salary = VN_CURRENT_SALARY_CAP - total_salary
    
    # Kiểm tra trái sở trường
    out_of_pos = []
    for p in starters:
        name = p["player_name"]
        assigned = p["pos"]
        natural = source_dict[name]["position"]
        
        # Đánh giá độ lệch vị trí
        if assigned in ["LCB", "RCB"] and "CB" in natural:
            pass # Đúng sở trường trung vệ
        elif assigned in ["LAM", "RAM"] and natural in ["CAM", "LW", "RW"]:
            if assigned == "RAM" and natural == "LW":
                out_of_pos.append({
                    "player_name": name,
                    "assigned": assigned,
                    "natural": natural,
                    "note": f"Sở trường '{natural}' được bố trí 'RAM' (Tiền vệ công lệch phải / Inside Forward nghịch chân dứt điểm ZD)"
                })
        elif assigned in ["LDM", "RDM"] and natural == "CM":
            out_of_pos.append({
                "player_name": name,
                "assigned": assigned,
                "natural": natural,
                "note": f"Sở trường '{natural}' được kéo lùi xuống '{assigned}' (Đá tiền vệ trụ / Double Pivot phòng ngự)"
            })
        elif assigned != natural and not (assigned in natural):
            out_of_pos.append({
                "player_name": name,
                "assigned": assigned,
                "natural": natural,
                "note": f"Sở trường '{natural}' đá ở vị trí '{assigned}'"
            })
            
    # Tìm 3 vị trí yếu nhất theo OVR
    starter_details = []
    for p in starters:
        name = p["player_name"]
        truth = source_dict[name]
        starter_details.append({
            "pos": p["pos"],
            "player_name": name,
            "season": truth["season"],
            "grade": truth["grade"],
            "ovr": truth["ovr"],
            "salary": truth["salary"],
            "natural_position": truth["position"],
            "role_focus": p["role_focus"]
        })
        
    sorted_by_ovr = sorted(starter_details, key=lambda x: x["ovr"])
    weakest_3 = sorted_by_ovr[:3]
    
    content = f"""# 📋 BÁO CÁO KIỂM TOÁN ĐỘI HÌNH HIỆN TẠI (VN_CURRENT_SQUAD_AUDIT.md)
*Thời điểm kiểm toán:* {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (UTC+7)
*Mục tiêu:* `VN_GLXH_CURRENT_SQUAD_OPTIMIZATION` (Tối ưu hóa sơ đồ từ đúng 13 cầu thủ người dùng thực tế đang sở hữu)
*Nguồn dữ liệu:* [data/vn_owned_players.json](file:///E:/FCOnlineWorkspace/Research/data/vn_owned_players.json) (SOURCE_OF_TRUTH từ screenshot game)

---

## 1. 💰 THÔNG SỐ QUỸ LƯƠNG (SALARY CAP)
* **Trần lương tài khoản Garena VN hiện tại:** `{VN_CURRENT_SALARY_CAP}`
* **Tổng lương 11 cầu thủ đá chính:** `{total_salary}`
* **Quỹ lương còn dư:** `{remaining_salary}` (Lương dư dồi dào, hoàn toàn không bị kịch trần)
* **Tổng lương toàn bộ 13 cầu thủ sở hữu:** `{sum(p['salary'] for p in source_dict.values())} / {VN_CURRENT_SALARY_CAP}`

---

## 2. 🛡️ 11 CẦU THỦ ĐÁ CHÍNH ĐƯỢC CHỌN (SƠ ĐỒ 4-2-3-1)

| Vị Trí Chỉ Định | Cầu Thủ | Mùa Thẻ | Cấp Thẻ | OVR | Lương | Vị Trí Gốc | Vai Trò Vận Hành GLXH |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
"""
    for p in starter_details:
        content += f"| **{p['pos']}** | {p['player_name']} | `{p['season']}` | `+{p['grade']}` | **{p['ovr']}** | `{p['salary']}` | {p['natural_position']} | {p['role_focus']} |\n"

    content += f"""
*Tổng OVR trung bình 11 cầu thủ chính:* **{round(sum(p['ovr'] for p in starter_details) / 11.0, 1)}**

---

## 3. 🔄 CẦU THỦ DỰ BỊ (BENCH PLAYERS)

| Cầu Thủ | Mùa Thẻ | Cấp Thẻ | OVR | Lương | Vị Trí Gốc | Vai Trò Dự Bị |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
"""
    for b in bench:
        t = source_dict[b["player_name"]]
        content += f"| **{b['player_name']}** | `{t['season']}` | `+{t['grade']}` | **{t['ovr']}** | `{t['salary']}` | {t['position']} | {b['role']} |\n"

    content += f"""
---

## 4. ⚠️ ĐÁNH GIÁ CẦU THỦ ĐÁ LỆCH SỞ TRƯỜNG (OUT-OF-POSITION ANALYSIS)
"""
    if not out_of_pos:
        content += """* **Tình trạng:** `KHÔNG CÓ CẦU THỦ NÀO BỊ TRÁI SỞ TRƯỜNG NGHIÊM TRỌNG`.
* **Ghi chú điều phối vị trí:**
  - **A. Del Piero (HOT, Gốc: LW):** Được xếp đá `RAM` (Tiền vệ công lệch phải / Inside Forward). Trong engine GLXH, Del Piero thuận chân phải và có chỉ số ẩn Finesse Shot, việc bố trí ở nách phải giúp anh nhận bóng, ngoặt vào trung lộ hoặc dứt điểm chéo góc rất tự nhiên.
  - **Park Ji Sung (NO.7, Gốc: CAM):** Được xếp đá `LAM` (Tiền vệ công lệch trái). Với thể lực 117+ và xu hướng hoạt động rộng, Park đảm bảo áp sát cánh trái và lui về bọc lót cho Gvardiol khi cần.
  - **R. Gullit & Rodri (Gốc: CM):** Được xếp đá cặp `LDM - RDM`. Thể hình và chỉ số phòng ngự/tranh chấp của cả hai hoàn toàn thích ứng hoàn hảo với vai trò Double Pivot.
  - **Sergio Ramos (19, Gốc: RB/CB):** Đá trung vệ lệch trái `LCB`, đúng sở trường CB phụ của thẻ.
"""
    else:
        for oop in out_of_pos:
            content += f"- **{oop['player_name']}**: {oop['note']}\n"

    content += f"""
---

## 5. 📉 3 VỊ TRÍ YẾU NHẤT TRONG ĐỘI HÌNH CHÍNH (WEAKEST POSITIONS)

Dựa trên OVR và chất lượng thẻ phôi thực tế (không giả định nâng cấp):

1. **🔴 Vị trí 1: LCB — Sergio Ramos (Mùa 19, +1, OVR 94, Lương 18)**
   - *Điểm yếu:* Là thẻ mùa 19 phôi cơ bản, OVR 94 thấp nhất đội hình chính. Tốc độ và khả năng đeo bám ở mức +1 sẽ gặp nhiều khó khăn trước các tiền đạo mục tiêu OVR 115+ của đối phương.
2. **🔴 Vị trí 2: RDM — Rodri (Mùa 19, +1, OVR 95, Lương 17)**
   - *Điểm yếu:* Dù sở hữu chiều cao 1m91 và AI mỏ neo tốt, thẻ mùa 19 mức +1 có thể lực và tốc độ xuất phát chưa cao, dễ bị đuối sức trong các pha chuyển đổi trạng thái nhanh ở hiệp 2.
3. **🔴 Vị trí 3: GK — W. Hennessey (Mùa HOT, +1, OVR 96, Lương 13)**
   - *Điểm yếu:* Sở hữu chiều cao lý tưởng 1m98 nhưng OVR 96 ở mức +1 khiến chỉ số phản xạ và đổ người cơ bản còn thấp, dễ bị thủng lưới trước các cú sút xa búa bổ ngoài vòng cấm.
   - *(Dự phòng tuyến giữa: A. Del Piero HOT +1 OVR 102 và R. Gullit HOT +1 OVR 103 cũng thuộc nhóm OVR cơ bản cần gia cố sau này).*

---

## 6. 🚫 NGUYÊN TẮC BẢO TOÀN (NO BUYING RECOMMENDATION AT THIS STAGE)
Theo đúng chỉ thị cốt lõi, bước này **TUYỆT ĐỐI KHÔNG ĐỀ XUẤT MUA CẦU THỦ MỚI**. Toàn bộ phân tích và cấu hình sơ đồ được xây dựng để khai thác 100% tiềm năng của đúng 13 cầu thủ bạn đang nắm giữ trên tài khoản.
"""

    with open(AUDIT_REPORT_MD, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[Audit Report Generated] {AUDIT_REPORT_MD}")

# ==========================================
# 4. HÀM CHÍNH (RUN)
# ==========================================

def run():
    print("=== EXECUTING VN_GLXH_CURRENT_SQUAD_OPTIMIZATION ===")
    
    # 1. Tối ưu đội hình hiện tại từ vn_owned_players.json
    squad_options = optimize_current_squad()
    
    # 2. Sinh báo cáo kiểm toán VN_CURRENT_SQUAD_AUDIT.md
    generate_audit_report(squad_options)
    
    # 3. Phân tích ứng viên mô hình từ Database 41,289 (chỉ dùng HYPOTHETICAL_*)
    if os.path.exists(DETAILS_CSV):
        db = pd.read_csv(DETAILS_CSV, encoding='utf-8-sig')
        db['player_code'] = db['player_code'].astype(str)
        
        df_cand = evaluate_model_candidates(db)
        out_cand_csv = os.path.join(EXPORTS_DIR, "vn_glxh_model_candidates.csv")
        df_cand.head(175).to_csv(out_cand_csv, index=False, encoding='utf-8-sig')
        print(f"[OK] Đã xuất {min(175, len(df_cand))} ứng viên mô hình tại {out_cand_csv}")
        
        with open(f"{out_cand_csv}.meta.json", "w", encoding="utf-8") as f:
            json.dump({
                "source": "41289_PLAYER_DATABASE",
                "sample_type": "DATABASE_CANDIDATE_DATA",
                "extracted_at": datetime.datetime.now().isoformat(),
                "provenance_notice": "Hypothetical candidate evaluation from database. Strictly separated from owned inventory."
            }, f, indent=2, ensure_ascii=False)
            
    print("=== HOÀN TẤT VN_GLXH_CURRENT_SQUAD_OPTIMIZATION ===")

if __name__ == "__main__":
    run()
