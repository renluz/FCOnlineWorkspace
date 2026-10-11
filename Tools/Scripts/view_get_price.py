import sys
sys.stdout.reconfigure(encoding='utf-8')

target_file = r'E:\FCOnlineWorkspace\Research\repos\fconline-player-search\피온탐색기V2-1.py'
with open(target_file, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, line in enumerate(lines[120:175]):
    print(f"{i+121}: {line.rstrip()}")
