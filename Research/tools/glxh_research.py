#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
glxh_research.py
Công cụ thu thập và trích xuất dữ liệu ranker stats phục vụ nghiên cứu Giả Lập Xếp Hạng (Manager Mode / 감독모드).

Chỉ thu thập matchType = 52 (감독모드 - Manager Mode / GLXH).
Tuyệt đối KHÔNG thu thập matchType = 50 (1v1 rank tay).
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.parse
import pandas as pd

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
EXPORTS_DIR = os.path.join(BASE_DIR, "exports")
DETAILS_CSV = os.path.join(BASE_DIR, "repos", "fconline-player-search", "data", "details.csv")

MANAGER_MODE_MATCH_TYPE = 52  # 감독모드 (Manager Mode / Giả Lập Xếp Hạng)

def load_metadata():
    """Tải metadata đã lưu cục bộ"""
    metadata = {}
    for kind in ['matchtype', 'spposition', 'seasonid', 'division']:
        path = os.path.join(DATA_DIR, f"{kind}.json")
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                metadata[kind] = json.load(f)
        else:
            metadata[kind] = []
    return metadata

def get_position_map():
    metadata = load_metadata()
    pos_map = {}
    for item in metadata.get('spposition', []):
        pos_map[int(item.get('spposition'))] = item.get('desc')
    return pos_map

def get_season_map():
    metadata = load_metadata()
    sea_map = {}
    for item in metadata.get('seasonid', []):
        sea_map[int(item.get('seasonId'))] = item.get('className')
    return sea_map

def fetch_ranker_stats_api(api_key, players_list):
    """
    Gọi Nexon OpenAPI endpoint:
    GET /fconline/v1/ranker-stats?matchtype=52&players=[{"id":spid,"po":pos},...]
    """
    url = "https://open.api.nexon.com/fconline/v1/ranker-stats"
    players_param = json.dumps([{"id": p["spId"], "po": p["spPosition"]} for p in players_list])
    query = urllib.parse.urlencode({
        "matchtype": MANAGER_MODE_MATCH_TYPE,
        "players": players_param
    })
    full_url = f"{url}?{query}"
    
    req = urllib.request.Request(full_url, headers={
        "x-nxopen-api-key": api_key,
        "User-Agent": "FCOnlineResearch-GLXH/1.0"
    })
    
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode('utf-8'))

def build_candidate_players_from_local():
    """
    Trích xuất danh sách cầu thủ tiêu biểu từ details.csv cục bộ
    để phục vụ nghiên cứu ranker stats theo vị trí.
    """
    if not os.path.exists(DETAILS_CSV):
        return []
    
    df = pd.read_csv(DETAILS_CSV, encoding='utf-8-sig')
    pos_map = get_position_map()
    rev_pos_map = {v.upper(): k for k, v in pos_map.items()}
    
    candidates = []
    positions_to_sample = ['ST', 'CF', 'CAM', 'CM', 'CDM', 'CB', 'LB', 'RB', 'GK']
    
    for pos in positions_to_sample:
        sub = df[df['position'].str.upper() == pos].sort_values(by='ovr', ascending=False).head(15)
        po_code = rev_pos_map.get(pos, 25)
        for _, row in sub.iterrows():
            spid = int(row['player_code'])
            candidates.append({
                "spId": spid,
                "spPosition": po_code,
                "player_name": row['player_name'],
                "season": row['season'],
                "position_label": pos,
                "salary": int(row['salary']),
                "overall": int(row['ovr']),
                "height": int(row['height']),
                "weight": int(row['weight']),
                "traits": row['traits'],
                "team_colors": row['team_colors']
            })
    return candidates

def collect_and_export_glxh_data(api_key=None, sample_limit=50):
    os.makedirs(EXPORTS_DIR, exist_ok=True)
    pos_map = get_position_map()
    season_map = get_season_map()
    
    candidates = build_candidate_players_from_local()
    print(f"Tổng số ứng viên nghiên cứu GLXH từ database: {len(candidates)}")
    
    real_results = []
    api_success = False

    if api_key:
        print(f"Đang kết nối NEXON OpenAPI với matchType={MANAGER_MODE_MATCH_TYPE} (Manager Mode)...")
        batch_size = 50
        try:
            for i in range(0, min(len(candidates), sample_limit), batch_size):
                batch = candidates[i:i + batch_size]
                api_res = fetch_ranker_stats_api(api_key, batch)
                if isinstance(api_res, list) and len(api_res) > 0:
                    api_success = True
                    for item in api_res:
                        sp_id = item.get('spId') or item.get('id')
                        sp_pos = item.get('spPosition') or item.get('po')
                        status = item.get('status', {})
                        create_date = item.get('createDate')
                        
                        cand = next((c for c in batch if c['spId'] == sp_id and c['spPosition'] == sp_pos), None)
                        season_id = int(sp_id) // 1_000_000 if sp_id else None
                        season_label = season_map.get(season_id, cand.get('season') if cand else None)
                        
                        record = {
                            "spId": sp_id,
                            "player_name": cand.get('player_name') if cand else None,
                            "season": season_label,
                            "spPosition": sp_pos,
                            "position_label": pos_map.get(sp_pos, cand.get('position_label') if cand else "UNKNOWN"),
                            "source_matchtype": MANAGER_MODE_MATCH_TYPE,
                            "source_matchtype_desc": "감독모드 (Manager Mode / GLXH)",
                            "shoot": status.get('shoot'),
                            "effectiveShoot": status.get('effectiveShoot'),
                            "assist": status.get('assist'),
                            "goal": status.get('goal'),
                            "dribble": status.get('dribble'),
                            "dribbleTry": status.get('dribbleTry'),
                            "dribbleSuccess": status.get('dribbleSuccess'),
                            "passTry": status.get('passTry'),
                            "passSuccess": status.get('passSuccess'),
                            "block": status.get('block'),
                            "tackle": status.get('tackle'),
                            "matchCount": status.get('matchCount'),
                            "createDate": create_date,
                            "overall": cand.get('overall') if cand else None,
                            "salary": cand.get('salary') if cand else None,
                            "height": cand.get('height') if cand else None,
                            "weight": cand.get('weight') if cand else None,
                            "traits": cand.get('traits') if cand else None,
                            "team_colors": cand.get('team_colors') if cand else None
                        }
                        real_results.append(record)
        except Exception as e:
            print(f"Lỗi khi gọi API ranker-stats: {e}")
            api_success = False

    if api_success and real_results:
        # Xuất file ranker thật
        json_path = os.path.join(EXPORTS_DIR, "glxh_ranker_stats.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(real_results, f, ensure_ascii=False, indent=2)
        print(f"[Export REAL Ranker JSON OK] {json_path}")
        
        df_real = pd.DataFrame(real_results)
        csv_path = os.path.join(EXPORTS_DIR, "glxh_ranker_stats.csv")
        df_real.to_csv(csv_path, index=False, encoding='utf-8-sig')
        print(f"[Export REAL Ranker CSV OK] {csv_path} ({len(df_real)} dòng)")
        return csv_path, json_path
    else:
        # Báo REAL_RANKER_DATA_UNAVAILABLE
        print("REAL_RANKER_DATA_UNAVAILABLE")
        print("Không tạo file glxh_ranker_stats.csv / glxh_ranker_stats.json bằng dữ liệu giả lập/offline.")
        
        # Xóa file cũ nếu có để tránh nhầm lẫn
        for f in ["glxh_ranker_stats.csv", "glxh_ranker_stats.json"]:
            fp = os.path.join(EXPORTS_DIR, f)
            if os.path.exists(fp):
                os.remove(fp)
                print(f"Đã xóa file ranker cũ: {f}")
        
        # Xuất candidate list offline sang file riêng biệt
        offline_cands = []
        for cand in candidates:
            record = {
                "spId": cand['spId'],
                "player_name": cand['player_name'],
                "season": cand['season'],
                "spPosition": cand['spPosition'],
                "position_label": cand['position_label'],
                "salary": cand['salary'],
                "overall": cand['overall'],
                "height": cand['height'],
                "weight": cand['weight'],
                "traits": cand['traits'],
                "team_colors": cand['team_colors']
            }
            offline_cands.append(record)
            
        cand_json = os.path.join(EXPORTS_DIR, "glxh_offline_candidates.json")
        with open(cand_json, 'w', encoding='utf-8') as f:
            json.dump(offline_cands, f, ensure_ascii=False, indent=2)
            
        cand_csv = os.path.join(EXPORTS_DIR, "glxh_offline_candidates.csv")
        pd.DataFrame(offline_cands).to_csv(cand_csv, index=False, encoding='utf-8-sig')
        print(f"[Offline Candidates OK] {cand_csv} & {cand_json}")
        return None, None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GLXH Research Data Collector")
    parser.add_argument("--api-key", type=str, default=os.getenv("NEXON_OPEN_API_KEY"), help="Nexon Open API Key")
    parser.add_argument("--limit", type=int, default=50, help="Giới hạn số cầu thủ truy vấn API")
    args = parser.parse_args()
    
    collect_and_export_glxh_data(api_key=args.api_key, sample_limit=args.limit)
