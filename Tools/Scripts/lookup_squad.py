import sys
import pandas as pd

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_csv(r'E:\FCOnlineWorkspace\Research\repos\fconline-player-search\data\details.csv')
players_to_find = [
    'Boniface', 'Lampard', 'Gonzalez', 'Wirtz', 'Zaire-Emery', 'Rodri', 
    'Gvardiol', 'Desailly', 'Schar', 'Zambrotta', 'Mailson', 
    'Thomasson', 'Beckham', 'Campbell', 'Zalazar', 'Gullit', 'Son'
]

for p in players_to_find:
    sub = df[df['player_name'].str.contains(p, case=False, na=False)]
    print(f"=== {p} (Found {len(sub)}) ===")
    for _, r in sub.head(5).iterrows():
        name = r['player_name']
        season = r['season']
        ovr = r['ovr']
        pos = r['position']
        h = r['height']
        w = r['weight']
        traits = r['traits']
        print(f"  {name} | {season} | OVR {ovr} | Pos: {pos} | {h}cm {w}kg | Traits: {traits}")
