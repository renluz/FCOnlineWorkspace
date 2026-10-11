import csv
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/repos/fconline-player-search/data/details.csv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if any('184484' in col for col in row):
            for h, val in zip(header, row):
                if val:
                    print(f"{h}: {val}")
            print("="*40)
