"""
Moneyball CAM Evaluator — Script tính điểm định lượng độc lập và kiểm chứng dữ liệu 100%.
Tuyệt đối KHÔNG tính nhẩm hoặc gán điểm cảm tính.
"""

import json
import sys
from pathlib import Path

# Đảm bảo in unicode tiếng Việt trên Windows terminal
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Cấu hình trọng số chuẩn toán học (Tổng = 100%)
WEIGHTS = {
    # Nhóm Kết Liễu (40%)
    "finish": 0.15,
    "long_shot": 0.10,
    "shot_power": 0.05,
    "composure": 0.10,
    # Nhóm Kiến Thiết (30%)
    "short_pass": 0.10,
    "vision": 0.10,
    "positioning": 0.10,
    # Nhóm Thể Chất & Zone 14 (30%)
    "balance": 0.10,
    "strength": 0.10,
    "stamina": 0.10
}

def calculate_score(candidate: dict) -> dict:
    stats = candidate["raw_stats_base"]
    
    # 1. Base Role Score (0 - 100)
    base_role_score = sum(stats[key] * WEIGHTS[key] for key in WEIGHTS)
    
    # 2. Weak Foot Modifier
    wf = candidate["weak_foot"]
    if wf == 5:
        wf_mod = 0.0
    elif wf == 4:
        wf_mod = -4.0
    else:
        wf_mod = -10.0
        
    # 3. Salary Tax / Bonus (Mốc chuẩn = 27 của Havertz)
    salary = candidate["salary"]
    if salary == 27:
        salary_tax = 0.0
    elif salary < 27:
        salary_tax = (27 - salary) * 1.5
    else:
        salary_tax = -((salary - 27) * 2.0)
        
    # 4. System Team Color Bonus
    # Real Madrid cluster: +3.0; Cluster 3 (Đức/Anh): +2.0; Ngoại binh: 0.0
    team_color_bonus = candidate.get("team_color_bonus", 0.0)
    
    total_score = base_role_score + wf_mod + salary_tax + team_color_bonus
    
    return {
        "player_name": candidate["player_name"],
        "season": candidate["season"],
        "fc_info_id": candidate["fc_info_id"],
        "fc_info_url": candidate["fc_info_url"],
        "salary": salary,
        "weak_foot": wf,
        "base_role_score": round(base_role_score, 2),
        "wf_mod": wf_mod,
        "salary_tax": salary_tax,
        "team_color_bonus": team_color_bonus,
        "total_score": round(total_score, 2)
    }

def main():
    dataset_path = Path("E:/FCOnlineWorkspace/SquadProject/16_CAM_CANDIDATE_DATASET.json")
    if not dataset_path.exists():
        print(f"Error: Dataset {dataset_path} does not exist.")
        sys.exit(1)
        
    with open(dataset_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    candidates = data.get("candidates", [])
    results = [calculate_score(c) for c in candidates]
    results.sort(key=lambda x: x["total_score"], reverse=True)
    
    print("\n" + "="*80)
    print("BẢNG XẾP HẠNG MONEYBALL ĐỊNH LƯỢNG — XUẤT TỰ ĐỘNG TỪ PYTHON SCRIPT")
    print("="*80)
    print(f"{'Hạng':<5} | {'Cầu thủ':<20} | {'Mùa':<6} | {'Lương':<6} | {'WF':<4} | {'Base':<6} | {'WF_Mod':<7} | {'Sal_Tax':<8} | {'Color':<6} | {'TỔNG ĐIỂM':<9}")
    print("-" * 80)
    for rank, r in enumerate(results, 1):
        print(f"{rank:<5} | {r['player_name']:<20} | {r['season']:<6} | {r['salary']:<6} | {r['weak_foot']:<4} | {r['base_role_score']:<6} | {r['wf_mod']:<7} | {r['salary_tax']:<8} | {r['team_color_bonus']:<6} | {r['total_score']:<9}")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
