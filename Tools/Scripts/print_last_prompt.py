import json
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
path = r"C:\Users\PhucVu\.gemini\antigravity\brain\bb318d08-30a5-4a17-b499-6d2d5f6b0de5\.system_generated\logs\transcript.jsonl"
prompts = []
with open(path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        if data.get("source") == "USER_EXPLICIT":
            prompts.append(data.get("content"))
if prompts:
    print("LAST USER PROMPT:\n" + prompts[-1])
