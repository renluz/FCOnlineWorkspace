import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/epl_index.js', 'r', encoding='utf-8') as f:
    content = f.read()

# find all calls on qe
qe_calls = re.findall(r'qe\.(?:get|post|put|delete)\([^)]*\)', content)
print("qe calls count:", len(qe_calls))
for q in set(qe_calls):
    print(q)
