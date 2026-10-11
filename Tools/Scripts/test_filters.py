import pandas as pd, json, sys
sys.stdout.reconfigure(encoding='utf-8')

csv_path = r'E:\FCOnlineWorkspace\Research\repos\fconline-player-search\data\details.csv'
df = pd.read_csv(csv_path)

print("Dataset shape:", df.shape)
print("Columns:", list(df.columns))

# Test filtering by player name
name_match = df[df['player_name'].str.contains('호날두|Ronaldo|손흥민', na=False, case=False)]
print("\n[Filter by Name] matches found:", len(name_match))

# Test filtering by season
season_match = df[df['season'] == '23UCL']
print("[Filter by Season (23UCL)] matches found:", len(season_match))

# Test filtering by position
pos_match = df[df['position'] == 'ST']
print("[Filter by Position (ST)] matches found:", len(pos_match))

# Test filtering by Team Color
tc_match = df[df['team_colors'].str.contains('레알 마드리드|맨체스터 유나이티드|첼시', na=False)]
print("[Filter by Team Color (Real Madrid/MU/Chelsea)] matches found:", len(tc_match))

# Test filtering by salary
sal_match = df[(df['salary'] >= 20) & (df['salary'] <= 28)]
print("[Filter by Salary (20-28)] matches found:", len(sal_match))

# Test filtering by stats (e.g. speed, finishing, strength)
# speed = 속력, finishing = 골 결정력, strength = 몸싸움
stat_match = df[(df['골 결정력'] >= 110) & (df['속력'] >= 110)]
print("[Filter by Individual Stats (Finishing>=110, Speed>=110)] matches found:", len(stat_match))
