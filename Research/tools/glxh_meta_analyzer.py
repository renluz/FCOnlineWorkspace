# tools/glxh_meta_analyzer.py
import os
import sys
import json
import numpy as np
import pandas as pd

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORTS_DIR = os.path.join(BASE_DIR, "exports")
DATA_DIR = os.path.join(BASE_DIR, "data")
DETAILS_CSV = os.path.join(BASE_DIR, "repos", "fconline-player-search", "data", "details.csv")

def calculate_meta_metrics(df_ranker):
    """
    Tính các metric mô tả thực nghiệm từ dữ liệu NEXON Open API matchtype=52.
    TUYỆT ĐỐI không gọi là 'best player score'.
    Các metric:
    - usage_index: Tỷ lệ xuất hiện tương đối (matchCount / max(matchCount))
    - goal_per_appearance: status.goal
    - assist_per_appearance: status.assist
    - shot_efficiency: goal / shoot (null nếu shoot == 0)
    - defensive_action_index: block + tackle
    """
    df = df_ranker.copy()
    
    # Check fields
    max_matches = df['RAW_NEXON_matchCount'].max() if 'RAW_NEXON_matchCount' in df and len(df) > 0 else 1
    if pd.isna(max_matches) or max_matches == 0:
        max_matches = 1
        
    df['CALC_usage_index'] = df['RAW_NEXON_matchCount'] / max_matches if 'RAW_NEXON_matchCount' in df else None
    df['CALC_goal_per_appearance'] = df['RAW_NEXON_goal'] if 'RAW_NEXON_goal' in df else None
    df['CALC_assist_per_appearance'] = df['RAW_NEXON_assist'] if 'RAW_NEXON_assist' in df else None
    
    # shot_efficiency = goal / shoot (null nếu shoot = 0)
    if 'RAW_NEXON_goal' in df and 'RAW_NEXON_shoot' in df:
        df['CALC_shot_efficiency'] = np.where(
            df['RAW_NEXON_shoot'].fillna(0) > 0,
            df['RAW_NEXON_goal'] / df['RAW_NEXON_shoot'],
            None
        )
    else:
        df['CALC_shot_efficiency'] = None
        
    # defensive_action_index = block + tackle
    if 'RAW_NEXON_block' in df and 'RAW_NEXON_tackle' in df:
        df['CALC_defensive_action_index'] = df['RAW_NEXON_block'].fillna(0) + df['RAW_NEXON_tackle'].fillna(0)
    else:
        df['CALC_defensive_action_index'] = None
        
    return df

def join_with_database(df_ranker):
    """
    Ghép dữ liệu ranker thật với details.csv theo spId (player_code)
    Tách rõ tiền tố:
    - RAW_NEXON_*
    - DATABASE_*
    """
    if not os.path.exists(DETAILS_CSV):
        print(f"Cảnh báo: Không tìm thấy {DETAILS_CSV}")
        return df_ranker
        
    db_df = pd.read_csv(DETAILS_CSV, encoding='utf-8-sig')
    db_df['player_code'] = db_df['player_code'].astype(str)
    
    # Chuẩn bị bảng ranker
    df = df_ranker.copy()
    df['join_key'] = df['spId'].astype(str)
    
    # Đổi tên các cột từ ranker thành tiền tố RAW_NEXON_ nếu chưa có
    rename_raw = {}
    for col in df.columns:
        if col not in ['spId', 'join_key'] and not col.startswith('RAW_NEXON_') and not col.startswith('CALC_'):
            rename_raw[col] = f"RAW_NEXON_{col}"
    df = df.rename(columns=rename_raw)
    
    # Đổi tên các cột từ database thành tiền tố DATABASE_
    db_cols_keep = [
        'player_code', 'player_name', 'season', 'position', 'ovr', 'salary',
        'height', 'weight', 'left_foot', 'right_foot',
        'strength', 'stamina', 'finishing', 'positioning', 'shot_power',
        'long_shots', 'interceptions', 'marking', 'standing_tackle', 'heading',
        'traits', 'team_colors'
    ]
    db_sub = db_df[[c for c in db_cols_keep if c in db_df.columns]].copy()
    rename_db = {c: f"DATABASE_{c}" for c in db_sub.columns if c != 'player_code'}
    rename_db['player_code'] = 'join_key'
    db_sub = db_sub.rename(columns=rename_db)
    
    merged = pd.merge(df, db_sub, on='join_key', how='left')
    merged = merged.drop(columns=['join_key'], errors='ignore')
    return merged

def compare_heuristic_vs_public(df_joined):
    """
    So sánh kr_public_glxh_analyzed_players.csv với public meta
    Xuất file: exports/heuristic_vs_kr_public.csv
    Tính tương quan Pearson & Spearman nếu đủ dữ liệu
    """
    analyzed_path = os.path.join(EXPORTS_DIR, "kr_public_glxh_analyzed_players.csv")
    if not os.path.exists(analyzed_path):
        print(f"Không tìm thấy {analyzed_path}")
        return None
        
    analyzed_df = pd.read_csv(analyzed_path, encoding='utf-8-sig')
    analyzed_df['player_code'] = analyzed_df['player_code'].astype(str)
    
    # Tìm cột heuristic score tương ứng theo vị trí
    score_cols = [c for c in analyzed_df.columns if c.startswith('EXPERIMENTAL_SCORE_')]
    
    comparison_rows = []
    
    for _, row in df_joined.iterrows():
        spid = str(row.get('spId'))
        cand = analyzed_df[analyzed_df['player_code'] == spid]
        if len(cand) == 0:
            continue
        c_row = cand.iloc[0]
        
        pos = row.get('RAW_NEXON_position_label') or c_row.get('position', 'ST')
        # Tìm score phù hợp với pos
        matched_score_col = f"EXPERIMENTAL_SCORE_{pos.upper()}"
        if matched_score_col not in c_row:
            matched_score_col = 'EXPERIMENTAL_SCORE_ST'
            
        h_score = c_row.get(matched_score_col)
        usage = row.get('CALC_usage_index', row.get('RAW_NEXON_matchCount'))
        
        # Agreement flag: Cả 2 đều cao (heuristic >= 80 và usage >= 0.5) hoặc cả 2 đều thấp
        agreement = "AGREE_HIGH" if (h_score and h_score >= 80 and usage and usage >= 0.5) else \
                    "AGREE_LOW" if (h_score and h_score < 75 and usage and usage < 0.3) else "DISAGREE"
                    
        comparison_rows.append({
            "spId": spid,
            "player_name": row.get('DATABASE_player_name') or row.get('RAW_NEXON_player_name'),
            "season": row.get('DATABASE_season') or row.get('RAW_NEXON_season'),
            "position": pos,
            "heuristic_score": h_score,
            "kr_public_usage": usage,
            "kr_public_goal_per_app": row.get('CALC_goal_per_appearance'),
            "kr_public_assist_per_app": row.get('CALC_assist_per_appearance'),
            "kr_public_shot_efficiency": row.get('CALC_shot_efficiency'),
            "kr_public_defensive_action": row.get('CALC_defensive_action_index'),
            "agreement_flag": agreement
        })
        
    comp_df = pd.DataFrame(comparison_rows)
    out_csv = os.path.join(EXPORTS_DIR, "heuristic_vs_kr_public.csv")
    comp_df.to_csv(out_csv, index=False, encoding='utf-8-sig')
    print(f"[Comparison OK] Đã lưu {out_csv} ({len(comp_df)} bản ghi)")
    
    # Tính tương quan nếu >= 5 mẫu hợp lệ
    valid = comp_df.dropna(subset=['heuristic_score', 'kr_public_usage'])
    if len(valid) >= 5:
        p_corr = valid['heuristic_score'].astype(float).corr(valid['kr_public_usage'].astype(float), method='pearson')
        s_corr = valid['heuristic_score'].astype(float).corr(valid['kr_public_usage'].astype(float), method='spearman')
        print(f"Pearson Correlation: {p_corr:.4f}")
        print(f"Spearman Correlation: {s_corr:.4f}")
    else:
        print("Chưa đủ dữ liệu công khai ghép đôi để tính correlation.")
        
    return comp_df

if __name__ == "__main__":
    print("GLXH Meta Analyzer Ready.")
