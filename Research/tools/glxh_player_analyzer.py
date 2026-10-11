#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
glxh_player_analyzer.py
Script phân tích và chấm điểm metric cho cầu thủ phục vụ nghiên cứu Giả Lập Xếp Hạng (GLXH).

LƯU Ý QUAN TRỌNG:
Script này KHÔNG tự khẳng định cầu thủ nào "hay nhất".
Các điểm số tổng hợp đều được đánh dấu là EXPERIMENTAL_SCORE để ChatGPT
và người dùng có thể tự điều chỉnh trọng số dựa trên dữ liệu thực tế.
"""

import os
import sys
import json
import argparse
import pandas as pd

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORTS_DIR = os.path.join(BASE_DIR, "exports")
DATA_DIR = os.path.join(BASE_DIR, "repos", "fconline-player-search", "data")
DETAILS_CSV = os.path.join(DATA_DIR, "details.csv")
RANKER_CSV = os.path.join(EXPORTS_DIR, "glxh_ranker_stats.csv")

def load_data():
    if not os.path.exists(DETAILS_CSV):
        raise FileNotFoundError(f"Không tìm thấy file: {DETAILS_CSV}")
    
    df_players = pd.read_csv(DETAILS_CSV, encoding='utf-8-sig')
    
    df_ranker = None
    if os.path.exists(RANKER_CSV):
        try:
            df_ranker = pd.read_csv(RANKER_CSV, encoding='utf-8-sig')
        except Exception:
            pass
            
    return df_players, df_ranker

def calculate_position_metrics(row, ranker_info=None):
    """
    Tính toán các chỉ số thành phần theo từng vị trí chuyên biệt cho GLXH.
    Tất cả điểm số tổng hợp đều là EXPERIMENTAL_SCORE.
    """
    pos = str(row.get('position', '')).upper()
    
    # Chỉ số cơ bản
    height = float(row.get('height', 0))
    weight = float(row.get('weight', 0))
    salary = float(row.get('salary', 0))
    left_foot = float(row.get('left_foot', 0))
    right_foot = float(row.get('right_foot', 0))
    weak_foot = min(left_foot, right_foot)
    
    # Chỉ số ingame (tiếng Hàn trong details.csv)
    pace = float(row.get('속력', 0))
    finishing = float(row.get('골 결정력', 0))
    shot_power = float(row.get('슛 파워', 0))
    long_shots = float(row.get('중거리 슛', 0))
    positioning = float(row.get('위치 선정', 0))
    short_passing = float(row.get('짧은 패스', 0))
    long_passing = float(row.get('긴 패스', 0))
    marking = float(row.get('대인 수비', 0))
    standing_tackle = float(row.get('태클', 0))
    interceptions = float(row.get('가로채기', 0))
    heading = float(row.get('헤더', 0))
    strength = float(row.get('몸싸움', 0))
    stamina = float(row.get('스태미너', 0))
    aggression = float(row.get('적극성', 0))
    
    # GK stats
    gk_diving = float(row.get('GK 다이빙', 0))
    gk_handling = float(row.get('GK 핸들링', 0))
    gk_kicking = float(row.get('GK 킥', 0))
    gk_reflexes = float(row.get('GK 반응속도', 0))
    gk_positioning = float(row.get('GK 위치 선정', 0))
    
    # Ranker stats nếu có
    ranker_usage = ranker_info.get('matchCount') if ranker_info else None
    goals_per_match = ranker_info.get('goal') if ranker_info else None
    assists_per_match = ranker_info.get('assist') if ranker_info else None
    
    metrics = {
        "spId": row.get('player_code'),
        "player_name": row.get('player_name'),
        "season": row.get('season'),
        "position": pos,
        "overall": row.get('ovr'),
        "salary": salary,
        "height": height,
        "weight": weight,
        "weak_foot": weak_foot,
        "ranker_usage": ranker_usage,
        "goals_per_match": goals_per_match,
        "assists_per_match": assists_per_match,
        "traits": row.get('traits'),
        "team_colors": row.get('team_colors')
    }
    
    # Tính EXPERIMENTAL_SCORE theo từng nhóm vị trí
    if pos in ['ST', 'CF', 'LS', 'RS']:
        # Nhóm tiền đạo ST: Ưu tiên Dứt điểm, Chọn vị trí, Lực sút, Thể hình, Sức mạnh, Đánh đầu, Chân phụ
        metrics.update({
            "metric_finishing": finishing,
            "metric_positioning": positioning,
            "metric_shot_power": shot_power,
            "metric_strength": strength,
            "metric_heading": heading,
            "metric_aggression": aggression,
            "metric_pace": pace,
            # Điểm thử nghiệm ST (Finishing 25%, Positioning 20%, Shot Power 15%, Strength 15%, Heading 15%, Weak Foot bonus 10%)
            "EXPERIMENTAL_SCORE_ST": round(
                (finishing * 0.25) +
                (positioning * 0.20) +
                (shot_power * 0.15) +
                (strength * 0.15) +
                (heading * 0.15) +
                (weak_foot * 2.0),
                2
            )
        })
    elif pos in ['CDM', 'LDM', 'RDM']:
        # Nhóm tiền vệ phòng ngự CDM: Cắt bóng, Tranh chấp, Thể lực, Kèm người, Chiều cao
        metrics.update({
            "metric_interceptions": interceptions,
            "metric_aggression": aggression,
            "metric_strength": strength,
            "metric_stamina": stamina,
            "metric_marking": marking,
            "metric_standing_tackle": standing_tackle,
            "metric_short_passing": short_passing,
            # Điểm thử nghiệm CDM (Interceptions 25%, Tackle 20%, Strength 20%, Stamina 20%, Marking 15%)
            "EXPERIMENTAL_SCORE_CDM": round(
                (interceptions * 0.25) +
                (standing_tackle * 0.20) +
                (strength * 0.20) +
                (stamina * 0.20) +
                (marking * 0.15),
                2
            )
        })
    elif pos in ['CB', 'LCB', 'RCB', 'SW']:
        # Nhóm trung vệ CB: Chiều cao, Thể hình, Sức mạnh, Quyết đoán, Cắt bóng, Kèm người, Tắc bóng, Đánh đầu, Tốc độ
        metrics.update({
            "metric_strength": strength,
            "metric_aggression": aggression,
            "metric_interceptions": interceptions,
            "metric_marking": marking,
            "metric_standing_tackle": standing_tackle,
            "metric_heading": heading,
            "metric_pace": pace,
            # Điểm thử nghiệm CB (Marking 20%, Tackle 20%, Interceptions 20%, Heading 15%, Strength 15%, Pace 10%)
            "EXPERIMENTAL_SCORE_CB": round(
                (marking * 0.20) +
                (standing_tackle * 0.20) +
                (interceptions * 0.20) +
                (heading * 0.15) +
                (strength * 0.15) +
                (pace * 0.10),
                2
            )
        })
    elif pos == 'GK':
        # Nhóm thủ môn GK: Chiều cao, Đổ người, Bắt bóng, Phản xạ, Chọn vị trí
        metrics.update({
            "metric_gk_diving": gk_diving,
            "metric_gk_handling": gk_handling,
            "metric_gk_reflexes": gk_reflexes,
            "metric_gk_positioning": gk_positioning,
            # Điểm thử nghiệm GK (Reflexes 30%, Diving 25%, Positioning 25%, Handling 20% + Height bonus)
            "EXPERIMENTAL_SCORE_GK": round(
                (gk_reflexes * 0.30) +
                (gk_diving * 0.25) +
                (gk_positioning * 0.25) +
                (gk_handling * 0.20) +
                (max(0, height - 185) * 0.5),
                2
            )
        })
    elif pos in ['CAM', 'LAM', 'RAM', 'CM', 'LCM', 'RCM']:
        # Nhóm tiền vệ tấn công & trung tâm: Sút xa, Chuyền ngắn, Tầm nhìn, Rê bóng, Thể lực
        metrics.update({
            "metric_long_shots": long_shots,
            "metric_shot_power": shot_power,
            "metric_short_passing": short_passing,
            "metric_long_passing": long_passing,
            "metric_stamina": stamina,
            "EXPERIMENTAL_SCORE_MID": round(
                (long_shots * 0.30) +
                (shot_power * 0.20) +
                (short_passing * 0.25) +
                (long_passing * 0.15) +
                (stamina * 0.10),
                2
            )
        })
        
    return metrics

def run_analysis(team_color=None, min_ovr=100, max_salary=None, top_n=200):
    df_players, df_ranker = load_data()
    print(f"Tổng số cầu thủ nạp từ database: {len(df_players)}")
    
    # Lọc sơ bộ
    filtered = df_players[df_players['ovr'] >= min_ovr]
    if max_salary:
        filtered = filtered[filtered['salary'] <= max_salary]
    if team_color:
        filtered = filtered[filtered['team_colors'].str.contains(team_color, case=False, na=False)]
        
    print(f"Số lượng sau lọc (OVR >= {min_ovr}): {len(filtered)}")
    
    # Map ranker info nếu có
    ranker_dict = {}
    if df_ranker is not None and not df_ranker.empty:
        for _, rk in df_ranker.iterrows():
            sp_id = str(rk.get('spId'))
            ranker_dict[sp_id] = {
                "matchCount": rk.get('matchCount'),
                "goal": rk.get('goal'),
                "assist": rk.get('assist')
            }

    results = []
    for _, row in filtered.iterrows():
        sp_id = str(row.get('player_code'))
        rk_info = ranker_dict.get(sp_id)
        metric_rec = calculate_position_metrics(row, rk_info)
        results.append(metric_rec)

    res_df = pd.DataFrame(results)
    
    # Xuất file kết quả phân tích
    os.makedirs(EXPORTS_DIR, exist_ok=True)
    out_csv = os.path.join(EXPORTS_DIR, "glxh_analyzed_players.csv")
    out_json = os.path.join(EXPORTS_DIR, "glxh_analyzed_players.json")
    
    res_df.to_csv(out_csv, index=False, encoding='utf-8-sig')
    res_df.to_json(out_json, orient='records', force_ascii=False, indent=2)
    
    print(f"[Analysis OK] Xuất {len(res_df)} cầu thủ -> {out_csv}")
    return out_csv, out_json

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GLXH Player Metric Analyzer")
    parser.add_argument("--team-color", type=str, help="Lọc theo Team Color (e.g. 레알 마드리드)")
    parser.add_argument("--min-ovr", type=int, default=100, help="OVR tối thiểu (mặc định 100)")
    parser.add_argument("--max-salary", type=int, help="Lương tối đa")
    args = parser.parse_args()
    
    run_analysis(team_color=args.team_color, min_ovr=args.min_ovr, max_salary=args.max_salary)
