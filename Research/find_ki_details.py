import csv
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/repos/fconline-player-search/data/details.csv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if len(row) > 10:
            # check if Korean name or English name matches or height/weight matches
            if ('기성용' in row[1] or 'Ki' in row[1]) or (row[7] == '189' and row[8] == '75' and '포항' in "".join(row)):
                print(row[0], row[1], row[3], row[4], row[13])
