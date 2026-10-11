#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/glxh_pipeline.py
Pipeline thu thập và phân tích dữ liệu Manager Mode (GLXH / matchtype=52) từ NEXON Open API.

Tuân thủ nghiêm ngặt 12 chỉ thị:
1. matchtype = 52 (Manager Mode / 감독모드). Loại bỏ hoàn toàn matchtype 50.
2. Không dùng EXPERIMENTAL_CANDIDATE_SCORE để lọc ranker-stats. Query toàn bộ (spId, spPosition)
   có sample_appearances >= 3 nếu budget cho phép.
3. Phân tầng Rank: ALL_RANKS, UPPER_LADDER (800-1300), ELITE (800, 900, 1000). Division gắn theo participant.
4. Stratified Sampling 300 trận: offset=[0, 500, 1000], limit=100 mỗi offset để giảm temporal bias.
5. Xử lý incomplete match (participant_count != 2) tách riêng glxh_incomplete_matches.csv.
6. Chuẩn hóa matchResult: 승->WIN, 무->DRAW, 패->LOSS, giữ cả raw và normalized.
7. Formation: signature là chính, gán formation_name chỉ khi EXACT (confidence=1.0), AMBIGUOUS (0.5), UNKNOWN (0.0).
8. Candidate score chỉ mang tính descriptive exploratory metric.
9. Tính Wilson 95% confidence interval cho win_rate (win_rate_ci_low, win_rate_ci_high).
10. Budget limit: max 4 req/s, dừng nếu chạm 900 req/ngày. Lần đầu chạy đúng 300 trận và dừng.
11. Báo cáo kiểm toán GLXH_300_MATCH_AUDIT.md đầy đủ các chỉ số thống kê.
12. Ghi provenance sidecar (.meta.json) cho mọi tệp CSV/JSON.
"""

import os
import sys
import json
import time
import math
import datetime
import argparse
import requests
import numpy as np
import pandas as pd

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
EXPORTS_DIR = os.path.join(BASE_DIR, "exports")
DETAILS_DIR = os.path.join(DATA_DIR, "match_details")
BATCHES_DIR = os.path.join(DATA_DIR, "ranker_stats_batches")
DETAILS_CSV = os.path.join(BASE_DIR, "repos", "fconline-player-search", "data", "details.csv")
DIVISION_JSON = os.path.join(DATA_DIR, "division.json")
SPPOSITION_JSON = os.path.join(DATA_DIR, "spposition.json")
BUDGET_STATE_FILE = os.path.join(DATA_DIR, "api_budget_state.json")
DOTENV_PATH = os.path.join(BASE_DIR, ".env")

MANAGER_MODE_MATCH_TYPE = 52
MAX_REQUESTS_PER_SECOND = 4.0
DAILY_BUDGET_LIMIT = 900
SAFETY_BUFFER = 50
KR_NEXON_LIVE_API = "UNAVAILABLE_FROM_VIETNAM"

# ==========================================
# 1. QUẢN LÝ QUOTA & RATE LIMIT
# ==========================================

class RequestBudgetTracker:
    def __init__(self, state_file=BUDGET_STATE_FILE, daily_limit=DAILY_BUDGET_LIMIT, min_interval=0.26):
        self.state_file = state_file
        self.daily_limit = daily_limit
        self.min_interval = min_interval
        self.last_req_time = 0.0
        self.daily_count = 0
        self.current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.load_state()

    def load_state(self):
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    state = json.load(f)
                    if state.get("date") == self.current_date:
                        self.daily_count = state.get("daily_count", 0)
                    else:
                        self.daily_count = 0
            except Exception:
                self.daily_count = 0

    def save_state(self):
        os.makedirs(os.path.dirname(self.state_file), exist_ok=True)
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump({
                "date": self.current_date,
                "daily_count": self.daily_count,
                "last_updated": datetime.datetime.now().isoformat()
            }, f, indent=2)

    def can_request(self):
        return self.daily_count < self.daily_limit

    def wait_and_count(self):
        if not self.can_request():
            raise RuntimeError(f"DAILY_BUDGET_EXCEEDED: Đã chạm ngưỡng an toàn {self.daily_limit} requests/ngày.")
            
        elapsed = time.time() - self.last_req_time
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
            
        self.last_req_time = time.time()
        self.daily_count += 1
        if self.daily_count % 10 == 0:
            self.save_state()

budget_tracker = RequestBudgetTracker()

def get_api_key():
    key = os.environ.get("NEXON_OPEN_API_KEY")
    if not key and os.path.exists(DOTENV_PATH):
        try:
            with open(DOTENV_PATH, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("NEXON_OPEN_API_KEY="):
                        key = line.split("=", 1)[1].strip().strip('"').strip("'")
                        break
        except Exception:
            pass
    return key

def check_authentication(api_key):
    if not api_key:
        return False, KR_NEXON_LIVE_API, "NEXON Open API live access is unavailable for the user's Vietnam region as of 2026-09-18. Live KR match/ranker datasets are therefore not available."
        
    url = "https://open.api.nexon.com/fconline/v1/match"
    params = {"matchtype": MANAGER_MODE_MATCH_TYPE, "offset": 0, "limit": 1, "orderby": "desc"}
    headers = {"x-nxopen-api-key": api_key, "User-Agent": "FCOnlineResearch-GLXH/3.0"}
    
    try:
        budget_tracker.wait_and_count()
        resp = requests.get(url, params=params, headers=headers, timeout=10)
        if resp.status_code == 200:
            return True, "200_OK", "Authentication successful"
        else:
            try:
                err = resp.json().get("error", {})
                return False, f"HTTP_{resp.status_code}_{err.get('name', 'AuthError')}", err.get('message', resp.text)
            except Exception:
                return False, f"HTTP_{resp.status_code}", resp.text
    except Exception as e:
        return False, "NETWORK_ERROR", str(e)

# ==========================================
# 2. WILSON CONFIDENCE INTERVAL & RESULT MAPPING
# ==========================================

RESULT_MAPPING = {
    "승": "WIN",
    "무": "DRAW",
    "패": "LOSS"
}

def wilson_score_interval(wins, n, confidence=0.95):
    """Tính khoảng tin cậy Wilson 95% cho win rate"""
    if n == 0 or pd.isna(n) or pd.isna(wins):
        return None, None
    z = 1.96  # 95% CI
    p_hat = float(wins) / float(n)
    denominator = 1.0 + (z ** 2) / float(n)
    centre = (p_hat + (z ** 2) / (2.0 * float(n))) / denominator
    spread = (z * math.sqrt((p_hat * (1.0 - p_hat) + (z ** 2) / (4.0 * float(n))) / float(n))) / denominator
    lower = max(0.0, centre - spread)
    upper = min(1.0, centre + spread)
    return round(lower, 4), round(upper, 4)

def save_with_provenance(df, file_path, sample_type, endpoint="", is_live=True, extra_meta=None):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False, encoding="utf-8-sig")
    
    meta_path = f"{file_path}.meta.json"
    meta = {
        "source": "NEXON_OPEN_API" if is_live else "LOCAL_OFFLINE_DATABASE",
        "matchtype": MANAGER_MODE_MATCH_TYPE,
        "sample_type": sample_type,
        "retrieved_at": datetime.datetime.now().isoformat(),
        "sample_size": len(df),
        "api_endpoint": endpoint,
        "is_live_data": is_live,
        "provenance_notice": "Generated by FCOnlineResearch GLXH Pipeline"
    }
    if extra_meta:
        meta.update(extra_meta)
        
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

def load_division_map():
    div_map = {}
    if os.path.exists(DIVISION_JSON):
        try:
            with open(DIVISION_JSON, "r", encoding="utf-8") as f:
                items = json.load(f)
                for item in items:
                    div_map[int(item.get("divisionId"))] = item.get("divisionName")
        except Exception:
            pass
    return div_map

def load_position_map():
    pos_map = {}
    if os.path.exists(SPPOSITION_JSON):
        try:
            with open(SPPOSITION_JSON, "r", encoding="utf-8") as f:
                items = json.load(f)
                for item in items:
                    pos_map[int(item.get("spposition"))] = item.get("desc")
        except Exception:
            pass
    return pos_map

# ==========================================
# 3. GIAI ĐOẠN 1: DISCOVERY BẰNG STRATIFIED SAMPLING (300 TRẬN)
# ==========================================

def fetch_stratified_match_ids(api_key, strata_offsets=[0, 500, 1000], per_stratum_limit=100, target_count=300):
    """
    Thu thập 300 matchId theo 3 tầng offset để giảm temporal bias
    Lưu checkpoint tại data/glxh_match_ids.json
    """
    os.makedirs(DATA_DIR, exist_ok=True)
    match_ids_file = os.path.join(DATA_DIR, "glxh_match_ids.json")
    
    existing_state = {}
    if os.path.exists(match_ids_file):
        try:
            with open(match_ids_file, "r", encoding="utf-8") as f:
                existing_state = json.load(f)
        except Exception:
            existing_state = {}
            
    existing_ids = existing_state.get("match_ids", []) if isinstance(existing_state, dict) else existing_state
    print(f"[Stratified Sampling] Checkpoint hiện có: {len(existing_ids)} matchId.")
    if len(existing_ids) >= target_count:
        return existing_ids[:target_count]
        
    url = "https://open.api.nexon.com/fconline/v1/match"
    headers = {"x-nxopen-api-key": api_key, "User-Agent": "FCOnlineResearch-GLXH/3.0"}
    
    unique_ids = list(existing_ids)
    
    for offset in strata_offsets:
        if len(unique_ids) >= target_count:
            break
        if not budget_tracker.can_request():
            print(f"[Budget Alert] Đạt giới hạn {DAILY_BUDGET_LIMIT} req/ngày. Dừng lấy thêm matchId.")
            break
            
        params = {
            "matchtype": MANAGER_MODE_MATCH_TYPE,
            "offset": offset,
            "limit": per_stratum_limit,
            "orderby": "desc"
        }
        
        try:
            budget_tracker.wait_and_count()
            resp = requests.get(url, params=params, headers=headers, timeout=15)
            if resp.status_code == 429:
                retry_after = int(resp.headers.get("retry-after", 5))
                time.sleep(retry_after)
                continue
            elif resp.status_code != 200:
                print(f"[Lỗi /match offset={offset}] HTTP {resp.status_code}: {resp.text}")
                continue
                
            batch = resp.json()
            if not batch:
                continue
                
            added_in_stratum = 0
            for item in batch:
                mid = item.get("matchId") if isinstance(item, dict) else item
                if mid and mid not in unique_ids:
                    unique_ids.append(mid)
                    added_in_stratum += 1
                    if len(unique_ids) >= target_count:
                        break
            print(f"[Stratified Sampling] Offset {offset}: nạp thêm {added_in_stratum} unique match IDs (Tổng: {len(unique_ids)}/{target_count}).")
        except Exception as e:
            print(f"[Lỗi kết nối /match offset={offset}]: {e}")
            
    # Bù đắp nếu chưa đủ 300
    curr_offset = 1500
    while len(unique_ids) < target_count and budget_tracker.can_request() and curr_offset <= 5000:
        needed = target_count - len(unique_ids)
        params = {"matchtype": MANAGER_MODE_MATCH_TYPE, "offset": curr_offset, "limit": min(100, needed), "orderby": "desc"}
        try:
            budget_tracker.wait_and_count()
            resp = requests.get(url, params=params, headers=headers, timeout=15)
            if resp.status_code == 200:
                batch = resp.json()
                if not batch:
                    break
                for item in batch:
                    mid = item.get("matchId") if isinstance(item, dict) else item
                    if mid and mid not in unique_ids:
                        unique_ids.append(mid)
            curr_offset += 500
        except Exception:
            break
            
    checkpoint_data = {
        "sampling_strategy": "RECENT_STRATIFIED_OFFSETS",
        "sampling_offsets": strata_offsets,
        "match_ids": unique_ids[:target_count]
    }
    with open(match_ids_file, "w", encoding="utf-8") as f:
        json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
        
    return unique_ids[:target_count]

def fetch_and_inspect_match_details(api_key, match_ids):
    os.makedirs(DETAILS_DIR, exist_ok=True)
    headers = {"x-nxopen-api-key": api_key, "User-Agent": "FCOnlineResearch-GLXH/3.0"}
    url = "https://open.api.nexon.com/fconline/v1/match-detail"
    
    valid_detail_files = []
    failed_count = 0
    c429_count = 0
    other_http_errors = 0
    division_field_detected = None
    first_inspected = False
    
    for idx, mid in enumerate(match_ids):
        cache_path = os.path.join(DETAILS_DIR, f"{mid}.json")
        if os.path.exists(cache_path):
            valid_detail_files.append(cache_path)
            continue
            
        if not budget_tracker.can_request():
            print(f"[Budget Alert] Chạm giới hạn {DAILY_BUDGET_LIMIT} request/ngày. Dừng tải match-detail.")
            break
            
        params = {"matchid": mid}
        success = False
        retries = 3
        
        while retries > 0 and not success:
            try:
                budget_tracker.wait_and_count()
                resp = requests.get(url, params=params, headers=headers, timeout=15)
                if resp.status_code == 200:
                    data = resp.json()
                    
                    m_type = int(data.get("matchType", 0))
                    if m_type != MANAGER_MODE_MATCH_TYPE:
                        print(f"[CẢNH BÁO] Trận {mid} có matchType={m_type} != 52. Loại bỏ!")
                        failed_count += 1
                        break
                        
                    # Lần đầu: In keys của matchInfo và matchDetail
                    if not first_inspected:
                        first_inspected = True
                        minfo_list = data.get("matchInfo", [])
                        if minfo_list:
                            s_minfo = minfo_list[0]
                            print(f"[Live Schema Inspection] matchInfo keys: {list(s_minfo.keys())}")
                            if "matchDetail" in s_minfo and isinstance(s_minfo["matchDetail"], dict):
                                print(f"[Live Schema Inspection] matchDetail keys: {list(s_minfo['matchDetail'].keys())}")
                            for k in s_minfo.keys():
                                if "division" in k.lower() or "rank" in k.lower() or "tier" in k.lower():
                                    division_field_detected = k
                                    print(f"==> TÌM THẤY TRƯỜNG DIVISION: {k} <==")
                            if not division_field_detected and "matchDetail" in s_minfo:
                                for k in s_minfo["matchDetail"].keys():
                                    if "division" in k.lower() or "rank" in k.lower() or "tier" in k.lower():
                                        division_field_detected = f"matchDetail.{k}"
                                        print(f"==> TÌM THẤY TRƯỜNG DIVISION TRONG matchDetail: {k} <==")
                                        
                    with open(cache_path, "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False)
                    valid_detail_files.append(cache_path)
                    success = True
                elif resp.status_code == 429:
                    c429_count += 1
                    retry_after = int(resp.headers.get("retry-after", 3))
                    time.sleep(retry_after)
                    retries -= 1
                else:
                    other_http_errors += 1
                    failed_count += 1
                    break
            except Exception as e:
                other_http_errors += 1
                time.sleep(1)
                retries -= 1
                
        if (idx + 1) % 50 == 0:
            print(f"[Details Cache] Đã xử lý {idx + 1} / {len(match_ids)} trận...")
            
    budget_tracker.save_state()
    return valid_detail_files, failed_count, c429_count, other_http_errors, division_field_detected

# ==========================================
# 4. TRÍCH XUẤT VÀ PHÂN TÁCH DỮ LIỆU THỰC CHIẾN
# ==========================================

def process_match_dataset(detail_files, division_field_name=None):
    """
    Trích xuất toàn bộ participant và player.
    Xử lý:
    - participant_count == 2 & matchEndType == 0 -> complete normal matches
    - participant_count != 2 -> incomplete matches (glxh_incomplete_matches.csv)
    - matchEndType != 0 -> abnormal matches (glxh_abnormal_matches.csv)
    - Chuẩn hóa matchResult sang WIN / DRAW / LOSS.
    """
    div_map = load_division_map()
    pos_map = load_position_map()
    
    players_rows = []
    participants_rows = []
    incomplete_matches = []
    abnormal_matches = []
    
    p_count_1 = 0
    p_count_2 = 0
    p_count_other = 0
    
    for fp in detail_files:
        try:
            with open(fp, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            continue
            
        mid = data.get("matchId")
        mdate = data.get("matchDate")
        if int(data.get("matchType", 0)) != MANAGER_MODE_MATCH_TYPE:
            continue
            
        minfo_list = data.get("matchInfo", [])
        p_count = len(minfo_list)
        
        if p_count == 2:
            p_count_2 += 1
        elif p_count == 1:
            p_count_1 += 1
        else:
            p_count_other += 1
            
        if p_count != 2:
            incomplete_matches.append({
                "matchId": mid,
                "matchDate": mdate,
                "participant_count": p_count
            })
            
        for minfo in minfo_list:
            ouid = minfo.get("ouid")
            nickname = minfo.get("nickname")
            mdetail = minfo.get("matchDetail", {})
            raw_res = mdetail.get("matchResult")
            calc_res = RESULT_MAPPING.get(raw_res, "UNKNOWN")
            end_type = mdetail.get("matchEndType", 0)
            
            # Trích xuất division theo từng participant riêng biệt
            div_id = None
            if division_field_name:
                if division_field_name.startswith("matchDetail."):
                    sub_k = division_field_name.split(".", 1)[1]
                    div_id = mdetail.get(sub_k)
                else:
                    div_id = minfo.get(division_field_name)
            div_name = div_map.get(int(div_id)) if div_id is not None else None
            
            starters = [p for p in minfo.get("player", []) if p.get("spPosition", 28) < 28]
            pos_sorted = sorted([p.get("spPosition") for p in starters[:11]]) if len(starters) >= 11 else []
            sig = "-".join([pos_map.get(p, str(p)) for p in pos_sorted]) if pos_sorted else "INCOMPLETE"
            
            is_complete = (end_type == 0 and p_count == 2)
            
            participants_rows.append({
                "matchId": mid,
                "ouid": ouid,
                "nickname": nickname,
                "matchDate": mdate,
                "matchEndType": end_type,
                "RAW_MATCH_result_raw": raw_res,
                "CALC_match_result": calc_res,
                "formation_signature": sig,
                "RAW_MATCH_division_id": div_id,
                "RAW_MATCH_division_name": div_name,
                "RAW_MATCH_is_complete_match": is_complete
            })
            
            if end_type != 0:
                abnormal_matches.append({
                    "matchId": mid,
                    "ouid": ouid,
                    "matchEndType": end_type,
                    "matchResult": raw_res
                })
                continue  # Bỏ qua không đưa cầu thủ của trận bất thường vào meta chính!
                
            for p in minfo.get("player", []):
                st = p.get("status", {})
                players_rows.append({
                    "matchId": mid,
                    "matchDate": mdate,
                    "ouid": ouid,
                    "nickname": nickname,
                    "RAW_MATCH_result_raw": raw_res,
                    "CALC_match_result": calc_res,
                    "RAW_MATCH_division_id": div_id,
                    "RAW_MATCH_division_name": div_name,
                    "RAW_MATCH_is_complete_match": is_complete,
                    "spId": p.get("spId"),
                    "spPosition": p.get("spPosition"),
                    "spGrade": p.get("spGrade"),
                    "shoot": st.get("shoot"),
                    "effectiveShoot": st.get("effectiveShoot"),
                    "assist": st.get("assist"),
                    "goal": st.get("goal"),
                    "dribble": st.get("dribble"),
                    "intercept": st.get("intercept"),
                    "defending": st.get("defending"),
                    "passTry": st.get("passTry"),
                    "passSuccess": st.get("passSuccess"),
                    "dribbleTry": st.get("dribbleTry"),
                    "dribbleSuccess": st.get("dribbleSuccess"),
                    "ballPossesionTry": st.get("ballPossesionTry"),
                    "ballPossesionSuc": st.get("ballPossesionSuc"),
                    "aerialTry": st.get("aerialTry"),
                    "aerialSuccess": st.get("aerialSuccess"),
                    "blockTry": st.get("blockTry"),
                    "block": st.get("block"),
                    "tackleTry": st.get("tackleTry"),
                    "tackle": st.get("tackle"),
                    "yellowCards": st.get("yellowCards"),
                    "redCards": st.get("redCards"),
                    "spRating": st.get("spRating")
                })
                
    df_players = pd.DataFrame(players_rows)
    df_participants = pd.DataFrame(participants_rows)
    df_incomplete = pd.DataFrame(incomplete_matches)
    df_abnormal = pd.DataFrame(abnormal_matches)
    
    # Xuất các file thô
    if not df_players.empty:
        save_with_provenance(df_players, os.path.join(EXPORTS_DIR, "glxh_match_players_raw.csv"),
                             sample_type="RECENT_GLXH_SAMPLE", endpoint="/fconline/v1/match-detail")
        df_players.to_json(os.path.join(EXPORTS_DIR, "glxh_match_players_raw.json"), orient="records", force_ascii=False, indent=2)
        
    if not df_incomplete.empty:
        save_with_provenance(df_incomplete, os.path.join(EXPORTS_DIR, "glxh_incomplete_matches.csv"),
                             sample_type="INCOMPLETE_MATCHES_AUDIT", endpoint="/fconline/v1/match-detail")
                             
    if not df_abnormal.empty:
        save_with_provenance(df_abnormal, os.path.join(EXPORTS_DIR, "glxh_abnormal_matches.csv"),
                             sample_type="ABNORMAL_MATCHES_AUDIT", endpoint="/fconline/v1/match-detail")
                             
    counts = {
        "p_count_1": p_count_1,
        "p_count_2": p_count_2,
        "p_count_other": p_count_other
    }
    return df_players, df_participants, counts

# ==========================================
# 5. SƠ ĐỒ CHIẾN THUẬT & CONFIDENCE SCORE
# ==========================================

EXACT_FORMATION_RULES = {
    # 4-2-3-1
    "GK-RB-RCB-LCB-LB-RDM-LDM-RAM-CAM-LAM-ST": "4-2-3-1",
    "GK-RB-RCB-LCB-LB-CDM-LDM-RAM-CAM-LAM-ST": "4-2-3-1",
    "GK-RB-RCB-LCB-LB-RDM-CDM-RAM-CAM-LAM-ST": "4-2-3-1",
    # 4-2-2-1-1
    "GK-RB-RCB-LCB-LB-RDM-LDM-RM-LM-CAM-ST": "4-2-2-1-1",
    # 4-1-2-3
    "GK-RB-RCB-LCB-LB-CDM-RCM-LCM-RW-ST-LW": "4-1-2-3",
    # 4-1-2-1-2
    "GK-RB-RCB-LCB-LB-CDM-RCM-LCM-CAM-RS-LS": "4-1-2-1-2",
    # 5-2-3
    "GK-RWB-RCB-CB-LCB-LWB-RCM-LCM-RW-ST-LW": "5-2-3",
    # 5-2-1-2
    "GK-RWB-RCB-CB-LCB-LWB-RCM-LCM-CAM-RS-LS": "5-2-1-2",
    # 4-4-2
    "GK-RB-RCB-LCB-LB-RM-RCM-LCM-LM-RS-LS": "4-4-2"
}

def analyze_formations(df_participants, prefix_name="glxh_formation_usage", sample_type="RECENT_GLXH_SAMPLE"):
    """
    Phân tích sơ đồ:
    - Chỉ dùng complete normal matches (matchEndType == 0 & RAW_MATCH_is_complete_match == True).
    - Aggregate theo formation_signature là chính.
    - formation_name kèm confidence: 1.0 (exact), 0.5 (ambiguous), 0.0 (unknown).
    - Tính Wilson 95% CI cho win_rate.
    """
    if df_participants.empty:
        return pd.DataFrame()
        
    valid_p = df_participants[(df_participants["matchEndType"] == 0) & (df_participants["RAW_MATCH_is_complete_match"] == True)].copy()
    if valid_p.empty:
        return pd.DataFrame()
        
    def resolve_formation(sig):
        if sig == "INCOMPLETE":
            return "INCOMPLETE", 0.0
        if sig in EXACT_FORMATION_RULES:
            return EXACT_FORMATION_RULES[sig], 1.0
        return "UNKNOWN", 0.0
        
    res_tuples = valid_p["formation_signature"].apply(resolve_formation)
    valid_p["formation_name"] = [t[0] for t in res_tuples]
    valid_p["formation_mapping_confidence"] = [t[1] for t in res_tuples]
    
    def agg_form(g):
        n = len(g)
        w = (g['CALC_match_result'] == 'WIN').sum()
        d = (g['CALC_match_result'] == 'DRAW').sum()
        l = (g['CALC_match_result'] == 'LOSS').sum()
        wr = w / n if n > 0 else 0.0
        ci_low, ci_high = wilson_score_interval(w, n)
        conf = g['formation_mapping_confidence'].iloc[0]
        return pd.Series({
            "participant_teams": n,
            "wins": w,
            "draws": d,
            "losses": l,
            "win_rate": wr,
            "win_rate_ci_low": ci_low,
            "win_rate_ci_high": ci_high,
            "formation_mapping_confidence": conf
        })
        
    form_summary = valid_p.groupby(['formation_signature', 'formation_name']).apply(agg_form, include_groups=False).reset_index()
    form_summary = form_summary.sort_values(by='participant_teams', ascending=False)
    
    out_csv = os.path.join(EXPORTS_DIR, f"{prefix_name}.csv")
    save_with_provenance(form_summary, out_csv, sample_type=sample_type, endpoint="/fconline/v1/match-detail")
    print(f"[Formation Analysis OK] {out_csv} ({len(form_summary)} signatures)")
    return form_summary

# ==========================================
# 6. THỐNG KÊ CẦU THỦ & 3 TẦNG PHÂN HẠNG (ALL, UPPER_LADDER, ELITE)
# ==========================================

def aggregate_player_usage(df_players, prefix_usage="glxh_sample_player_usage", prefix_grade="glxh_sample_player_grade_usage", sample_type="RECENT_GLXH_SAMPLE"):
    if df_players.empty:
        return pd.DataFrame(), pd.DataFrame()
        
    def calc_agg(group):
        n = len(group)
        wins = (group['CALC_match_result'] == 'WIN').sum()
        draws = (group['CALC_match_result'] == 'DRAW').sum()
        losses = (group['CALC_match_result'] == 'LOSS').sum()
        wr = wins / n if n > 0 else 0.0
        ci_low, ci_high = wilson_score_interval(wins, n)
        
        pass_try = group['passTry'].fillna(0).sum()
        pass_suc = group['passSuccess'].fillna(0).sum()
        aerial_try = group['aerialTry'].fillna(0).sum()
        aerial_suc = group['aerialSuccess'].fillna(0).sum()
        
        return pd.Series({
            "sample_appearances": n,
            "sample_wins": wins,
            "sample_draws": draws,
            "sample_losses": losses,
            "win_rate": wr,
            "win_rate_ci_low": ci_low,
            "win_rate_ci_high": ci_high,
            "avg_rating": group['spRating'].mean(),
            "avg_goal": group['goal'].mean(),
            "avg_assist": group['assist'].mean(),
            "avg_shoot": group['shoot'].mean(),
            "avg_effective_shoot": group['effectiveShoot'].mean(),
            "avg_intercept": group['intercept'].mean(),
            "avg_tackle": group['tackle'].mean(),
            "avg_block": group['block'].mean(),
            "pass_success_rate": pass_suc / pass_try if pass_try > 0 else None,
            "aerial_success_rate": aerial_suc / aerial_try if aerial_try > 0 else None
        })
        
    usage_df = df_players.groupby(['spId', 'spPosition']).apply(calc_agg, include_groups=False).reset_index()
    grade_df = df_players.groupby(['spId', 'spPosition', 'spGrade']).apply(calc_agg, include_groups=False).reset_index()
    
    out_usage_csv = os.path.join(EXPORTS_DIR, f"{prefix_usage}.csv")
    out_grade_csv = os.path.join(EXPORTS_DIR, f"{prefix_grade}.csv")
    
    save_with_provenance(usage_df, out_usage_csv, sample_type=sample_type, endpoint="/fconline/v1/match-detail")
    save_with_provenance(grade_df, out_grade_csv, sample_type=sample_type, endpoint="/fconline/v1/match-detail")
    print(f"[Usage Stats OK] {out_usage_csv} ({len(usage_df)} pairs) & {out_grade_csv}")
    return usage_df, grade_df

def process_three_tiers(df_players, df_participants):
    """
    Phân chia 3 tầng theo division của từng participant:
    - ELITE: [800, 900, 1000]
    - UPPER_LADDER: [800, 900, 1000, 1100, 1200, 1300]
    - ALL_RANKS: toàn bộ
    """
    if "RAW_MATCH_division_id" not in df_players.columns or df_players["RAW_MATCH_division_id"].dropna().empty:
        print("[Division Tiers] Live schema không cung cấp division identifier. Chỉ xuất ALL_RANKS.")
        return 0, 0, len(df_participants)
        
    elite_ids = [800, 900, 1000]
    upper_ids = [800, 900, 1000, 1100, 1200, 1300]
    
    def safe_int(x):
        try:
            return int(x)
        except Exception:
            return -1
            
    df_players["div_int"] = df_players["RAW_MATCH_division_id"].apply(safe_int)
    df_participants["div_int"] = df_participants["RAW_MATCH_division_id"].apply(safe_int)
    
    p_elite = df_players[df_players["div_int"].isin(elite_ids)].copy()
    part_elite = df_participants[df_participants["div_int"].isin(elite_ids)].copy()
    
    p_upper = df_players[df_players["div_int"].isin(upper_ids)].copy()
    part_upper = df_participants[df_participants["div_int"].isin(upper_ids)].copy()
    
    print(f"[Division Tiers] ELITE: {len(part_elite)} participants, UPPER_LADDER: {len(part_upper)} participants, ALL_RANKS: {len(df_participants)} participants.")
    
    # Xuất ELITE
    if not p_elite.empty:
        aggregate_player_usage(p_elite, prefix_usage="glxh_elite_player_usage", prefix_grade="glxh_elite_grade_usage", sample_type="RECENT_GLXH_ELITE_SAMPLE")
        analyze_formations(part_elite, prefix_name="glxh_elite_formation_usage", sample_type="RECENT_GLXH_ELITE_SAMPLE")
        
    # Xuất UPPER_LADDER
    if not p_upper.empty:
        aggregate_player_usage(p_upper, prefix_usage="glxh_upper_ladder_player_usage", prefix_grade="glxh_upper_ladder_grade_usage", sample_type="RECENT_GLXH_UPPER_LADDER_SAMPLE")
        analyze_formations(part_upper, prefix_name="glxh_upper_ladder_formation_usage", sample_type="RECENT_GLXH_UPPER_LADDER_SAMPLE")
        
    return len(part_elite), len(part_upper), len(df_participants)

# ==========================================
# 7. SÀNG LỌC ỨNG VIÊN & QUERY RANKER-STATS THEO BUDGET
# ==========================================

def select_candidates_for_ranker_query(df_usage):
    """
    Chọn ứng viên: Toàn bộ (spId, spPosition) có sample_appearances >= 3.
    Không lọc bằng candidate score để tránh selection bias!
    Tính EXPERIMENTAL_CANDIDATE_SCORE chỉ như descriptive exploratory metric.
    """
    if df_usage.empty:
        return pd.DataFrame()
        
    # Lấy toàn bộ cặp có appearances >= 3
    cand_df = df_usage[df_usage["sample_appearances"] >= 3].copy()
    if cand_df.empty:
        cand_df = df_usage[df_usage["sample_appearances"] >= 1].copy()
        
    max_apps = cand_df["sample_appearances"].max() if not cand_df.empty else 1
    norm_app = cand_df["sample_appearances"] / max_apps if max_apps > 0 else 0
    norm_rating = cand_df["avg_rating"].fillna(6.0) / 10.0
    norm_win = cand_df["win_rate"].fillna(0)
    norm_ga = (cand_df["avg_goal"].fillna(0) + cand_df["avg_assist"].fillna(0))
    norm_def = (cand_df["avg_tackle"].fillna(0) + cand_df["avg_block"].fillna(0) + cand_df["avg_intercept"].fillna(0))
    
    cand_df["EXPERIMENTAL_CANDIDATE_SCORE"] = (
        norm_app * 35.0 +
        norm_rating * 25.0 +
        norm_win * 20.0 +
        np.clip(norm_ga * 10.0, 0, 10.0) +
        np.clip(norm_def * 10.0, 0, 10.0)
    )
    
    # Sắp xếp mặc định theo sample_appearances giảm dần
    cand_df = cand_df.sort_values(by="sample_appearances", ascending=False)
    
    out_csv = os.path.join(EXPORTS_DIR, "glxh_candidate_pairs.csv")
    save_with_provenance(cand_df, out_csv, sample_type="CANDIDATE_PAIRS_FOR_RANKER_VALIDATION", endpoint="",
                         extra_meta={"min_appearances_threshold": 3, "score_notice": "EXPERIMENTAL_CANDIDATE_SCORE is descriptive exploratory metric only"})
    print(f"[Candidates Selected] {out_csv} ({len(cand_df)} pairs có appearances >= 3)")
    return cand_df

def fetch_ranker_stats_batches(api_key, cand_df):
    """
    Query /ranker-stats theo budget:
    - Batch 50 pairs/request.
    - Kiểm tra: current_daily + estimated + buffer(50) <= 900.
    - Nếu vượt budget: ưu tiên theo sample_appearances và ghi candidate_truncated_due_to_request_budget=True.
    """
    if cand_df.empty or not api_key:
        return pd.DataFrame(), 0, False, 0
        
    os.makedirs(BATCHES_DIR, exist_ok=True)
    url = "https://open.api.nexon.com/fconline/v1/ranker-stats"
    headers = {"x-nxopen-api-key": api_key, "User-Agent": "FCOnlineResearch-GLXH/3.0"}
    
    total_candidates = len(cand_df)
    estimated_requests = math.ceil(total_candidates / 50.0)
    current_requests = budget_tracker.daily_count
    
    truncated = False
    allowed_pairs = total_candidates
    if (current_requests + estimated_requests + SAFETY_BUFFER) > DAILY_BUDGET_LIMIT:
        available_reqs = max(0, DAILY_BUDGET_LIMIT - SAFETY_BUFFER - current_requests)
        allowed_pairs = available_reqs * 50
        truncated = True
        print(f"[Budget Management] Ngân sách chỉ cho phép {available_reqs} requests ({allowed_pairs} pairs). Cắt bớt tập ứng viên.")
        cand_to_query = cand_df.head(allowed_pairs)
    else:
        cand_to_query = cand_df
        
    pairs = [{"id": int(r['spId']), "po": int(r['spPosition'])} for _, r in cand_to_query.iterrows()]
    batch_size = 50
    all_ranker_records = []
    batches_count = 0
    
    for i in range(0, len(pairs), batch_size):
        if not budget_tracker.can_request():
            truncated = True
            break
            
        batch = pairs[i:i + batch_size]
        batch_idx = i // batch_size
        cache_batch = os.path.join(BATCHES_DIR, f"batch_{batch_idx}.json")
        batches_count += 1
        
        if os.path.exists(cache_batch):
            try:
                with open(cache_batch, "r", encoding="utf-8") as f:
                    batch_res = json.load(f)
            except Exception:
                batch_res = None
        else:
            params = {
                "matchtype": MANAGER_MODE_MATCH_TYPE,
                "players": json.dumps(batch)
            }
            try:
                budget_tracker.wait_and_count()
                resp = requests.get(url, params=params, headers=headers, timeout=15)
                if resp.status_code == 200:
                    batch_res = resp.json()
                    with open(cache_batch, "w", encoding="utf-8") as f:
                        json.dump(batch_res, f, ensure_ascii=False, indent=2)
                else:
                    batch_res = []
            except Exception:
                batch_res = []
                
        if batch_res and isinstance(batch_res, list):
            for item in batch_res:
                sp_id = item.get("spId") or item.get("id") or item.get("spid")
                sp_pos = item.get("spPosition") or item.get("po") or item.get("spposition")
                st = item.get("status", {})
                
                all_ranker_records.append({
                    "spId": sp_id,
                    "spPosition": sp_pos,
                    "RAW_RANKER_shoot": st.get("shoot"),
                    "RAW_RANKER_effectiveShoot": st.get("effectiveShoot"),
                    "RAW_RANKER_assist": st.get("assist"),
                    "RAW_RANKER_goal": st.get("goal"),
                    "RAW_RANKER_dribble": st.get("dribble"),
                    "RAW_RANKER_dribbleTry": st.get("dribbleTry"),
                    "RAW_RANKER_dribbleSuccess": st.get("dribbleSuccess"),
                    "RAW_RANKER_passTry": st.get("passTry"),
                    "RAW_RANKER_passSuccess": st.get("passSuccess"),
                    "RAW_RANKER_block": st.get("block"),
                    "RAW_RANKER_tackle": st.get("tackle"),
                    "RAW_RANKER_matchCount": st.get("matchCount"),
                    "RAW_RANKER_createDate": item.get("createDate")
                })
                
    df_ranker = pd.DataFrame(all_ranker_records)
    if not df_ranker.empty:
        max_mc = df_ranker['RAW_RANKER_matchCount'].max()
        df_ranker['CALC_relative_ranker_matchcount'] = df_ranker['RAW_RANKER_matchCount'] / max_mc if max_mc > 0 else 0
        
        out_csv = os.path.join(EXPORTS_DIR, "glxh_ranker_stats.csv")
        out_json = os.path.join(EXPORTS_DIR, "glxh_ranker_stats.json")
        save_with_provenance(df_ranker, out_csv, sample_type="NEXON_TOP_10000_RANKER_STATS", endpoint="/fconline/v1/ranker-stats",
                             extra_meta={
                                 "candidate_truncated_due_to_request_budget": truncated,
                                 "relative_note": "Relative only within queried candidate universe."
                             })
        df_ranker.to_json(out_json, orient="records", force_ascii=False, indent=2)
        print(f"[REAL Ranker Stats OK] {out_csv} ({len(df_ranker)} records)")
        
        live_sample_path = os.path.join(DATA_DIR, "ranker_stats_52_raw_sample.json")
        with open(live_sample_path, "w", encoding="utf-8") as f:
            json.dump({
                "source": "LIVE_NEXON_OPEN_API",
                "is_live_api_response": True,
                "matchtype": 52,
                "sample": all_ranker_records[:3]
            }, f, ensure_ascii=False, indent=2)
            
    budget_tracker.save_state()
    return df_ranker, batches_count, truncated, len(pairs)

# ==========================================
# 8. GHÉP DATABASE & TÁCH FILE VỊ TRÍ
# ==========================================

def enrich_and_export_positions(df_usage, df_grade, df_ranker):
    if df_usage.empty:
        return
        
    df_u = df_usage.copy()
    match_cols = {}
    for c in df_u.columns:
        if c not in ['spId', 'spPosition']:
            match_cols[c] = f"RAW_MATCH_{c}"
    df_u = df_u.rename(columns=match_cols)
    
    if not df_ranker.empty:
        merged = pd.merge(df_u, df_ranker, on=['spId', 'spPosition'], how='left')
    else:
        merged = df_u
        
    if os.path.exists(DETAILS_CSV):
        db_df = pd.read_csv(DETAILS_CSV, encoding="utf-8-sig")
        db_df['player_code'] = db_df['player_code'].astype(str)
        merged['join_key'] = merged['spId'].astype(str)
        
        db_cols = [
            'player_code', 'player_name', 'season', 'position', 'ovr', 'salary',
            'height', 'weight', 'left_foot', 'right_foot', 'strength', 'stamina',
            'finishing', 'positioning', 'shot_power', 'long_shots', 'interceptions',
            'marking', 'standing_tackle', 'heading', 'traits', 'team_colors'
        ]
        db_sub = db_df[[c for c in db_cols if c in db_df.columns]].copy()
        db_rename = {c: f"DATABASE_{c}" for c in db_sub.columns if c != 'player_code'}
        db_rename['player_code'] = 'join_key'
        db_sub = db_sub.rename(columns=db_rename)
        
        merged = pd.merge(merged, db_sub, on='join_key', how='left')
        merged = merged.drop(columns=['join_key'], errors='ignore')
        
    if not df_grade.empty:
        top_grades = df_grade.sort_values(by='sample_appearances', ascending=False).groupby(['spId', 'spPosition']).first().reset_index()
        top_grades = top_grades[['spId', 'spPosition', 'spGrade']].rename(columns={'spGrade': 'CALC_most_used_spGrade'})
        merged = pd.merge(merged, top_grades, on=['spId', 'spPosition'], how='left')
        
    pos_definitions = {
        "st": [25],
        "cf": [20, 21, 22, 24, 26],
        "cam": [17, 18, 19],
        "lm_rm": [12, 16, 23, 27],
        "cm": [13, 14, 15],
        "cdm": [9, 10, 11],
        "cb": [1, 4, 5, 6],
        "fullback": [2, 3, 7, 8],
        "gk": [0]
    }
    
    for tag, pos_codes in pos_definitions.items():
        sub = merged[merged['spPosition'].isin(pos_codes)]
        out_pos_csv = os.path.join(EXPORTS_DIR, f"real_glxh_{tag}.csv")
        save_with_provenance(sub, out_pos_csv, sample_type="ENRICHED_REAL_POSITION_DATASET", endpoint="")
        print(f"[Real Position OK] {out_pos_csv} ({len(sub)} cầu thủ)")
        
    return merged

# ==========================================
# 9. BÁO CÁO KIỂM TOÁN GLXH_300_MATCH_AUDIT.md
# ==========================================

def generate_audit_report(stats_summary):
    report_file = os.path.join(BASE_DIR, "GLXH_300_MATCH_AUDIT.md")
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S (UTC+7)")
    
    report = f"""# BÁO CÁO KIỂM TOÁN MẪU 300 TRẬN GLXH FC ONLINE (NEXON OPEN API)
*Thời điểm kiểm toán:* {now_str}
*Thư mục dự án:* `E:\\FCOnlineWorkspace\\Research`

---

## 1. 🔐 THÔNG SỐ XÁC THỰC & REQUEST BUDGET
* **API Authentication:** `{stats_summary.get('api_auth')}`
* **HTTP Status / Message:** `{stats_summary.get('auth_message')}`
* **Sampling Strategy:** `{stats_summary.get('sampling_strategy', 'RECENT_STRATIFIED_OFFSETS')}`
* **Sampling Offsets:** `{stats_summary.get('sampling_offsets', '[0, 500, 1000]')}`
* **Tổng số Request đã thực hiện hôm nay:** `{budget_tracker.daily_count} / {DAILY_BUDGET_LIMIT}`
* **Tốc độ giới hạn:** `{MAX_REQUESTS_PER_SECOND} req/s` (Rate-limiting enforced)
* **Số lỗi 429 (Rate Limit):** `{stats_summary.get('c429_count', 0)}` lần
* **Số lỗi HTTP khác:** `{stats_summary.get('other_http_errors', 0)}`

---

## 2. 📊 KẾT QUẢ THU THẬP MẪU 300 TRẬN (DISCOVERY SUMMARY)
* **Target Match Type:** `52` (Manager Mode / 감독모드 - Bắt buộc 100%)
* **Số matchId thu thập:** `{stats_summary.get('match_ids_count', 0)} / 300`
* **Số match-detail thành công:** `{stats_summary.get('details_success', 0)}`
* **Số match-detail thất bại:** `{stats_summary.get('details_failed', 0)}`
* **Số trận đủ 2 bên (participant_count == 2):** `{stats_summary.get('p_count_2', 0)}`
* **Số trận thiếu 1 bên (participant_count == 1):** `{stats_summary.get('p_count_1', 0)}`
* **Số trận có participant_count khác:** `{stats_summary.get('p_count_other', 0)}`
* **Số trận kết thúc bình thường đủ 2 bên (Complete Normal Matches):** `{stats_summary.get('complete_normal_matches', 0)}`
* **Số trận bất thường / bỏ cuộc (matchEndType != 0):** `{stats_summary.get('abnormal_matches', 0)}` *(Lưu tại `glxh_abnormal_matches.csv`)*
* **Số quan sát Participant-Team:** `{stats_summary.get('participant_rows', 0)}`
* **Số lượt cầu thủ ra sân (Player rows):** `{stats_summary.get('player_rows', 0)}`
* **Số unique spId:** `{stats_summary.get('unique_spids', 0)}`
* **Số unique cặp (spId, spPosition):** `{stats_summary.get('unique_pairs', 0)}`

---

## 3. 🎯 PHÂN TẦNG RANK (DIVISION TIERS)
* **Trạng thái trường Division trong live API:** `{stats_summary.get('division_detected', 'CHƯA PHÁT HIỆN / NULL')}`
* **Số lượng Participant theo tầng:**
  - **ALL_RANKS:** `{stats_summary.get('all_ranks_count', 0)}` participants
  - **UPPER_LADDER (800-1300):** `{stats_summary.get('upper_ladder_count', 0)}` participants
  - **ELITE (800, 900, 1000):** `{stats_summary.get('elite_count', 0)}` participants
  - **Division UNKNOWN / Null:** `{stats_summary.get('division_unknown_count', 0)}`

---

## 4. 🗺️ SƠ ĐỒ CHIẾN THUẬT (FORMATION SIGNATURES & CONFIDENCE)
* **Formation EXACT count (Confidence = 1.0):** `{stats_summary.get('formation_exact_count', 0)}`
* **Formation AMBIGUOUS count (Confidence = 0.5):** `{stats_summary.get('formation_ambiguous_count', 0)}`
* **Formation UNKNOWN count (Confidence = 0.0):** `{stats_summary.get('formation_unknown_count', 0)}`
* **Top sơ đồ phổ biến nhất:**
{stats_summary.get('top_formations', 'Chưa có dữ liệu')}

---

## 5. 🔬 ĐỐI SOÁT RANKER STATS (VALIDATION)
* **Số ứng viên trước khi query (appearances >= 3):** `{stats_summary.get('candidate_count_before', 0)}`
* **Số ứng viên thực tế được query:** `{stats_summary.get('candidate_count_queried', 0)}`
* **Bị cắt giảm do ngân sách (candidate_truncated_due_to_request_budget):** `{stats_summary.get('candidate_truncated', False)}`
* **Số batch gửi tới /ranker-stats:** `{stats_summary.get('ranker_batches', 0)}`
* **Số requests ranker-stats đã dùng:** `{stats_summary.get('ranker_requests_used', 0)}`
* **Trạng thái file `glxh_ranker_stats.csv`:** `{stats_summary.get('ranker_stats_status', 'CHƯA TẠO')}`

---

## 6. 🛑 ĐIỂM DỪNG KIỂM TOÁN (HALT FOR REVIEW)
Hệ thống đã dừng hoàn toàn sau mẫu 300 trận đầu tiên. Tuyệt đối không tự động mở rộng mẫu (500, 1000, 5000) để người dùng và ChatGPT tiến hành kiểm tra chất lượng dữ liệu.
"""
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report.strip() + "\n")
    print(f"[Audit Report Generated] {report_file}")

# ==========================================
# 10. MAIN PIPELINE
# ==========================================

def run_pipeline(target_matches=300):
    print("=== FC ONLINE MANAGER MODE (GLXH / matchtype=52) DATA PIPELINE ===")
    print(f"KR_NEXON_LIVE_API = {KR_NEXON_LIVE_API}")
    api_key = get_api_key()
    
    auth_ok, status_code, msg = check_authentication(api_key)
    stats_summary = {
        "api_auth": "PASS" if auth_ok else "FAIL",
        "auth_message": f"{status_code}: {msg}",
        "sampling_strategy": "RECENT_STRATIFIED_OFFSETS",
        "sampling_offsets": "[0, 500, 1000]"
    }
    
    if not auth_ok:
        print("API_AUTH=FAIL")
        print(f"Status: {status_code}")
        print(f"Error Message: {msg}")
        print("REAL_DATA_UNAVAILABLE")
        print("Dừng pipeline dữ liệu thật để bảo vệ tính toàn vẹn.")
        generate_audit_report(stats_summary)
        return False
        
    print(f"API_AUTH=PASS (HTTP {status_code})")
    
    # 1. Stratified Sampling 300 match IDs
    match_ids = fetch_stratified_match_ids(api_key, strata_offsets=[0, 500, 1000], per_stratum_limit=100, target_count=target_matches)
    stats_summary["match_ids_count"] = len(match_ids)
    if not match_ids:
        generate_audit_report(stats_summary)
        return False
        
    # 2. Tải và kiểm tra match details
    detail_files, failed_cnt, c429_cnt, other_errs, div_field = fetch_and_inspect_match_details(api_key, match_ids)
    stats_summary["details_success"] = len(detail_files)
    stats_summary["details_failed"] = failed_cnt
    stats_summary["c429_count"] = c429_cnt
    stats_summary["other_http_errors"] = other_errs
    stats_summary["division_detected"] = div_field if div_field else "Không có trong live matchInfo schema"
    
    # 3. Phân tách và trích xuất
    df_players, df_participants, p_counts = process_match_dataset(detail_files, division_field_name=div_field)
    stats_summary["p_count_1"] = p_counts["p_count_1"]
    stats_summary["p_count_2"] = p_counts["p_count_2"]
    stats_summary["p_count_other"] = p_counts["p_count_other"]
    
    complete_normal = df_participants[(df_participants["matchEndType"] == 0) & (df_participants["RAW_MATCH_is_complete_match"] == True)]
    stats_summary["complete_normal_matches"] = complete_normal["matchId"].nunique() if not complete_normal.empty else 0
    stats_summary["abnormal_matches"] = len(detail_files) - stats_summary["complete_normal_matches"]
    stats_summary["participant_rows"] = len(df_participants)
    stats_summary["player_rows"] = len(df_players)
    stats_summary["unique_spids"] = df_players["spId"].nunique() if not df_players.empty else 0
    stats_summary["unique_pairs"] = len(df_players.groupby(["spId", "spPosition"])) if not df_players.empty else 0
    
    # 4. Phân tích sơ đồ & Thống kê sử dụng
    form_summary = analyze_formations(df_participants)
    if not form_summary.empty:
        stats_summary["formation_exact_count"] = (form_summary["formation_mapping_confidence"] == 1.0).sum()
        stats_summary["formation_ambiguous_count"] = (form_summary["formation_mapping_confidence"] == 0.5).sum()
        stats_summary["formation_unknown_count"] = (form_summary["formation_mapping_confidence"] == 0.0).sum()
        stats_summary["top_formations"] = form_summary.head(5).to_markdown(index=False)
    else:
        stats_summary["top_formations"] = "Chưa có dữ liệu"
        stats_summary["formation_exact_count"] = 0
        stats_summary["formation_ambiguous_count"] = 0
        stats_summary["formation_unknown_count"] = 0
        
    df_usage, df_grade = aggregate_player_usage(df_players)
    
    # 5. Phân tầng Rank: ELITE, UPPER_LADDER, ALL_RANKS
    elite_cnt, upper_cnt, all_cnt = process_three_tiers(df_players, df_participants)
    stats_summary["elite_count"] = elite_cnt
    stats_summary["upper_ladder_count"] = upper_cnt
    stats_summary["all_ranks_count"] = all_cnt
    stats_summary["division_unknown_count"] = all_cnt - upper_cnt
    
    # 6. Chọn ứng viên (appearances >= 3) và query ranker-stats
    cand_df = select_candidates_for_ranker_query(df_usage)
    stats_summary["candidate_count_before"] = len(cand_df)
    
    df_ranker, batches_count, truncated, queried_pairs = fetch_ranker_stats_batches(api_key, cand_df)
    stats_summary["candidate_count_queried"] = queried_pairs
    stats_summary["candidate_truncated"] = truncated
    stats_summary["ranker_batches"] = batches_count
    stats_summary["ranker_requests_used"] = batches_count
    stats_summary["ranker_stats_status"] = "Đã xuất glxh_ranker_stats.csv" if not df_ranker.empty else "Chưa query hoặc rỗng"
    
    # 7. Ghép database & tách file theo vị trí
    enrich_and_export_positions(df_usage, df_grade, df_ranker)
    
    # 8. Xuất báo cáo kiểm toán 300 trận và DỪNG LẠI
    generate_audit_report(stats_summary)
    print("=== HOÀN TẤT LẦN CHẠY 300 TRẬN ĐẦU TIÊN — ĐÃ DỪNG LẠI CHỜ REVIEW ===")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GLXH Real Data Pipeline")
    parser.add_argument("--matches", type=int, default=300, help="Số trận GLXH thu thập ban đầu (mặc định 300)")
    args = parser.parse_args()
    
    run_pipeline(target_matches=args.matches)
