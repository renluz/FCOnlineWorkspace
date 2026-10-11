# create_sample_raw.py
import json
import os

sample_data = {
  "_description": "Raw response schema from NEXON Open API /fconline/v1/ranker-stats with matchtype=52 (Manager Mode)",
  "_endpoint": "GET https://open.api.nexon.com/fconline/v1/ranker-stats?matchtype=52&players=[{\"id\":<spId>,\"po\":<spPosition>}]",
  "_headers_required": ["x-nxopen-api-key"],
  "sample_response": [
    {
      "spId": 100000051,
      "spPosition": 25,
      "status": {
        "shoot": 3.2,
        "effectiveShoot": 1.7,
        "assist": 0.4,
        "goal": 1.1,
        "dribble": 140.5,
        "dribbleTry": 7.5,
        "dribbleSuccess": 5.6,
        "passTry": 18.2,
        "passSuccess": 14.3,
        "block": 0.2,
        "tackle": 0.4,
        "matchCount": 20
      },
      "createDate": "2026-03-06T01:23:45"
    }
  ],
  "fields_analysis": {
    "present_in_api": [
      "spId (or id / spid)",
      "spPosition (or po / spposition)",
      "status.shoot",
      "status.effectiveShoot",
      "status.assist",
      "status.goal",
      "status.dribble",
      "status.dribbleTry",
      "status.dribbleSuccess",
      "status.passTry",
      "status.passSuccess",
      "status.block",
      "status.tackle",
      "status.matchCount",
      "createDate"
    ],
    "absent_from_api": [
      "enhancement_level (spGrade) - Not provided in ranker-stats",
      "interceptions - Not provided in ranker-stats",
      "spRating (rating) - Only available in match-detail, not in ranker-stats",
      "win/draw/loss context - Only available in match-detail or user/match"
    ]
  }
}

target_file = r"E:\FCOnlineWorkspace\Research\data\ranker_stats_52_raw_sample.json"
with open(target_file, "w", encoding="utf-8") as f:
    json.dump(sample_data, f, ensure_ascii=False, indent=2)

print("Created", target_file)
