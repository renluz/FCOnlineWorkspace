import re

with open('e:/FCOnlineWorkspace/Research/epl_index.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Look for dynamic imports or .js files
js_files = re.findall(r'["\']([^"\']+\.js)["\']', content)
print("JS files mentioned in index.js:")
print(set(js_files))

# Look for import(
dyn_imports = re.findall(r'import\s*\([^)]+\)', content)
print("Dynamic imports:", dyn_imports)
