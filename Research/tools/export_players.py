#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
export_players.py
Công cụ lọc và xuất dữ liệu cầu thủ FC Online ra CSV/JSON.
Sử dụng dữ liệu details.csv từ repository fconline-player-search.
"""

import os
import sys
import json
import argparse
import pandas as pd
import requests
from bs4 import BeautifulSoup

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


# Đường dẫn cơ sở
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "repos", "fconline-player-search", "data")
DETAILS_CSV = os.path.join(DATA_DIR, "details.csv")
EXPORTS_DIR = os.path.join(BASE_DIR, "exports")

# Bảng tăng chỉ số theo cấp thẻ cộng (theo fconline-player-search / FC Online)
ENCHANT_DELTAS = {
    1: 0, 2: 1, 3: 2, 4: 4, 5: 6,
    6: 8, 7: 11, 8: 15, 9: 17, 10: 19
}

# Ánh xạ tên cột tiếng Hàn -> tiếng Anh chuẩn
STAT_MAP = {
    '속력': 'pace',
    '가속력': 'acceleration',
    '골 결정력': 'finishing',
    '슛 파워': 'shot_power',
    '중거리 슛': 'long_shots',
    '위치 선정': 'positioning',
    '발리슛': 'volleys',
    '페널티 킥': 'penalties',
    '짧은 패스': 'short_passing',
    '시야': 'vision',
    '크로스': 'crossing',
    '긴 패스': 'long_passing',
    '프리킥': 'free_kick',
    '커브': 'curve',
    '볼 컨트롤': 'ball_control',
    '민첩성': 'agility',
    '밸런스': 'balance',
    '반응 속도': 'reactions',
    '대인 수비': 'marking',
    '태클': 'standing_tackle',
    '가로채기': 'interceptions',
    '헤더': 'heading',
    '슬라이딩 태클': 'sliding_tackle',
    '몸싸움': 'strength',
    '스태미너': 'stamina',
    '적극성': 'aggression',
    '점프': 'jumping',
    '침착성': 'composure',
    'GK 다이빙': 'gk_diving',
    'GK 핸들링': 'gk_handling',
    'GK 킥': 'gk_kicking',
    'GK 반응속도': 'gk_reflexes',
    'GK 위치 선정': 'gk_positioning'
}

def fetch_price_online(spid, enhancement=1):
    """Tra cứu giá TTCN từ Nexon Datacenter"""
    url = 'https://fconline.nexon.com/datacenter/PlayerPriceGraph'
    headers = {'User-Agent': 'Mozilla/5.0'}
    data = {'spid': str(spid), 'n1strong': str(enhancement)}
    try:
        resp = requests.post(url, headers=headers, data=data, timeout=5)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            strong = soup.select_one('div.add_info strong')
            if strong and 'title' in strong.attrs:
                return int(strong['title'].replace(',', ''))
    except Exception:
        pass
    return None

def load_players_df():
    if not os.path.exists(DETAILS_CSV):
        raise FileNotFoundError(f"Không tìm thấy file details.csv tại: {DETAILS_CSV}")
    return pd.read_csv(DETAILS_CSV, encoding='utf-8-sig')

def filter_and_export(
    position=None,
    name=None,
    season=None,
    team_color=None,
    min_height=None,
    max_salary=None,
    min_overall=None,
    min_finishing=None,
    min_strength=None,
    min_stamina=None,
    min_interceptions=None,
    min_pace=None,
    enhancement=1,
    fetch_price=False,
    output_format="csv",
    output_filename=None
):
    df = load_players_df()
    delta = ENCHANT_DELTAS.get(enhancement, 0)
    
    # 1. Lọc theo vị trí
    if position:
        pos_list = [p.strip().upper() for p in position.split(',')]
        df = df[df['position'].str.upper().isin(pos_list)]

    # 2. Lọc theo tên
    if name:
        df = df[df['player_name'].str.contains(name, case=False, na=False)]

    # 3. Lọc theo season
    if season:
        sea_list = [s.strip().upper() for s in season.split(',')]
        df = df[df['season'].str.upper().isin(sea_list)]

    # 4. Lọc theo Team Color
    if team_color:
        df = df[df['team_colors'].str.contains(team_color, case=False, na=False)]

    # 5. Lọc theo chiều cao
    if min_height is not None:
        df = df[df['height'] >= min_height]

    # 6. Lọc theo lương
    if max_salary is not None:
        df = df[df['salary'] <= max_salary]

    # 7. Lọc theo OVR (tính cả cấp thẻ cộng)
    if min_overall is not None:
        df = df[(df['ovr'] + delta) >= min_overall]

    # 8. Lọc theo các chỉ số cá nhân (tính cả cấp thẻ cộng)
    if min_finishing is not None and '골 결정력' in df.columns:
        df = df[(df['골 결정력'] + delta) >= min_finishing]
    if min_strength is not None and '몸싸움' in df.columns:
        df = df[(df['몸싸움'] + delta) >= min_strength]
    if min_stamina is not None and '스태미너' in df.columns:
        df = df[(df['스태미너'] + delta) >= min_stamina]
    if min_interceptions is not None and '가로채기' in df.columns:
        df = df[(df['가로채기'] + delta) >= min_interceptions]
    if min_pace is not None and '속력' in df.columns:
        df = df[(df['속력'] + delta) >= min_pace]

    # Tạo bảng kết quả chuẩn hóa
    records = []
    for _, row in df.iterrows():
        spid = int(row['player_code'])
        price = fetch_price_online(spid, enhancement) if fetch_price else None
        
        rec = {
            'player_name': row.get('player_name'),
            'season': row.get('season'),
            'position': row.get('position'),
            'overall': int(row.get('ovr', 0)) + delta,
            'salary': int(row.get('salary', 0)),
            'height': int(row.get('height', 0)),
            'weight': int(row.get('weight', 0)),
            'left_foot': int(row.get('left_foot', 0)),
            'right_foot': int(row.get('right_foot', 0)),
            'enhancement': enhancement,
            'price': price,
            'pace': int(row.get('속력', 0)) + delta,
            'acceleration': int(row.get('가속력', 0)) + delta,
            'finishing': int(row.get('골 결정력', 0)) + delta,
            'shot_power': int(row.get('슛 파워', 0)) + delta,
            'long_shots': int(row.get('중거리 슛', 0)) + delta,
            'strength': int(row.get('몸싸움', 0)) + delta,
            'stamina': int(row.get('스태미너', 0)) + delta,
            'aggression': int(row.get('적극성', 0)) + delta,
            'interceptions': int(row.get('가로채기', 0)) + delta,
            'marking': int(row.get('대인 수비', 0)) + delta,
            'standing_tackle': int(row.get('태클', 0)) + delta,
            'heading': int(row.get('헤더', 0)) + delta,
            'traits': row.get('traits') if pd.notna(row.get('traits')) else None,
            'team_colors': row.get('team_colors') if pd.notna(row.get('team_colors')) else None
        }
        records.append(rec)

    res_df = pd.DataFrame(records)
    
    # Xuất file
    os.makedirs(EXPORTS_DIR, exist_ok=True)
    if not output_filename:
        tag = position.lower() if position else "filtered"
        output_filename = f"exported_players_{tag}"
        
    if output_format.lower() == 'json':
        out_path = os.path.join(EXPORTS_DIR, f"{output_filename}.json")
        res_df.to_json(out_path, orient='records', force_ascii=False, indent=2)
    else:
        out_path = os.path.join(EXPORTS_DIR, f"{output_filename}.csv")
        res_df.to_csv(out_path, index=False, encoding='utf-8-sig')

    print(f"[Export OK] Số lượng cầu thủ: {len(res_df)} -> {out_path}")
    return out_path, len(res_df)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FC Online Player Exporter")
    parser.add_argument("--position", type=str, help="Vị trí (e.g. ST, CDM, CB)")
    parser.add_argument("--name", type=str, help="Tên cầu thủ")
    parser.add_argument("--season", type=str, help="Mùa thẻ (e.g. 23UCL, BWC)")
    parser.add_argument("--team-color", type=str, help="Team Color (e.g. 레알 마드리드, 맨체스터 유나이티드)")
    parser.add_argument("--min-height", type=int, help="Chiều cao tối thiểu (cm)")
    parser.add_argument("--max-salary", type=int, help="Lương tối đa")
    parser.add_argument("--min-ovr", type=int, help="OVR tối thiểu")
    parser.add_argument("--min-finishing", type=int, help="Dứt điểm tối thiểu")
    parser.add_argument("--min-strength", type=int, help="Sức mạnh tối thiểu")
    parser.add_argument("--min-stamina", type=int, help="Thể lực tối thiểu")
    parser.add_argument("--min-interceptions", type=int, help="Cắt bóng tối thiểu")
    parser.add_argument("--min-pace", type=int, help="Tốc độ tối thiểu")
    parser.add_argument("--enhancement", type=int, default=1, help="Cấp thẻ cộng (1-10)")
    parser.add_argument("--fetch-price", action="store_true", help="Tra cứu giá TTCN online")
    parser.add_argument("--format", type=str, default="csv", choices=["csv", "json"], help="Định dạng xuất (csv/json)")
    parser.add_argument("--output", type=str, help="Tên file xuất (không kèm đuôi)")
    
    args = parser.parse_args()
    
    # Nếu không có tham số nào, chạy 2 ví dụ theo yêu cầu PHẦN 6
    if len(sys.argv) == 1:
        print("Chạy 2 truy vấn ví dụ mẫu từ đề bài:")
        # Ví dụ 1: ST, height >= 185, strength >= 115, finishing >= 115, salary <= 30
        print("\n1. Xuất ST (cao >= 185, sức mạnh >= 115, dứt điểm >= 115, lương <= 30)...")
        filter_and_export(
            position="ST",
            min_height=185,
            min_strength=115,
            min_finishing=115,
            max_salary=30,
            output_filename="example_st_glxh"
        )
        # Ví dụ 2: CDM, height >= 180, interceptions >= 115, strength >= 115, stamina >= 115
        print("\n2. Xuất CDM (cao >= 180, cắt bóng >= 115, sức mạnh >= 115, thể lực >= 115)...")
        filter_and_export(
            position="CDM",
            min_height=180,
            min_interceptions=115,
            min_strength=115,
            min_stamina=115,
            output_filename="example_cdm_glxh"
        )
    else:
        filter_and_export(
            position=args.position,
            name=args.name,
            season=args.season,
            team_color=args.team_color,
            min_height=args.min_height,
            max_salary=args.max_salary,
            min_overall=args.min_ovr,
            min_finishing=args.min_finishing,
            min_strength=args.min_strength,
            min_stamina=args.min_stamina,
            min_interceptions=args.min_interceptions,
            min_pace=args.min_pace,
            enhancement=args.enhancement,
            fetch_price=args.fetch_price,
            output_format=args.format,
            output_filename=args.output
        )
