import sys
sys.stdout.reconfigure(encoding='utf-8')

repo_dir = r'E:\FCOnlineWorkspace\Research\repos\fconline-player-search'
target_file = r'E:\FCOnlineWorkspace\Research\repos\fconline-player-search\피온탐색기V2-1.py'

with open(target_file, 'r', encoding='utf-8', errors='ignore') as f:
    code = f.read()

# Check functions in 피온탐색기V2-1.py
for line in code.splitlines():
    if line.strip().startswith('def '):
        print(line.strip())
