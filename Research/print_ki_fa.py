import csv
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/repos/fconline-player-search/data/details.csv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if row and row[0] == '264180283':
            for h, val in zip(header, row):
                print(f"{h}: {val}")
