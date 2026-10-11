import sys
import json
import os
import pandas as pd

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
details_path = os.path.join(BASE_DIR, 'repos', 'fconline-player-search', 'data', 'details.csv')
df = pd.read_csv(details_path)

names = {
    'Boniface': ['보니페이스', '보니파체', '보니파이스', '보니'],
    'Zambrotta': ['잠브로타'],
    'Gvardiol': ['그바르디올'],
    'Rosicky': ['로시츠키'],
    'Park Ji Sung': ['박지성'],
    'Schar': ['셰어', '샤르']
}

for eng, k_list in names.items():
    found = df[df['player_name'].apply(lambda x: any(k in str(x) for k in k_list))]
    seasons = found['season'].unique().tolist()
    print(f"{eng}: {len(found)} rows. Seasons: {seasons[:10]}")
    # check if target seasons in found
    for target_s in ['WS', 'WG', '25DP', 'NO.7', 'NO7']:
        m = found[found['season'] == target_s]
        if not m.empty:
            print(f"  -> FOUND {target_s}: {m[['player_code', 'player_name', 'season', 'salary', 'ovr', 'position']].to_dict('records')}")
