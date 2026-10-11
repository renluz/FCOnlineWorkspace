import csv
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/repos/fconline-player-search/data/codes.csv', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        if '기성용' in line or 'Ki' in line or 'Sung Yueng' in line:
            print(line.strip())
