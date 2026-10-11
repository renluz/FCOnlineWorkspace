#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/vn_market_candidate_scanner.py
Công cụ rà soát tính khả thi trên TTCN Việt Nam cho các cầu thủ ứng viên (Candidates).

Quy tắc bất biến:
- Chỉ sử dụng snapshot có price_confidence in ["HIGH", "MEDIUM"].
- Ưu tiên snapshot mới nhất (latest snapshot).
- Không dùng snapshot quá 24h (1440 phút) nếu muốn quyết định mua ngay.
- Thêm cột snapshot_age_minutes.
- Tuyệt đối không giả định thẻ có sẵn trên thị trường nếu chưa chứng minh được sell_quantity > 0.
- Nếu không có sổ lệnh thực tế: market_availability = UNKNOWN.
"""

import os
import sys
import json
import csv
import datetime
import pandas as pd

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
EXPORTS_DIR = os.path.join(BASE_DIR, "exports")
MARKET_LATEST_CSV = os.path.join(EXPORTS_DIR, "vn_market_latest.csv")
MARKET_HISTORY_CSV = os.path.join(DATA_DIR, "vn_market_history.csv")
CANDIDATE_SCAN_CSV = os.path.join(EXPORTS_DIR, "vn_market_candidate_scan.csv")
OWNED_PLAYERS_JSON = os.path.join(DATA_DIR, "vn_owned_players.json")

def load_latest_market_snapshots():
    """
    Nạp dữ liệu snapshot TTCN mới nhất từ exports/vn_market_latest.csv hoặc data/vn_market_history.csv.
    Trả về dict tra cứu theo (clean_name, clean_season, grade_int).
    """
    now = datetime.datetime.now()
    snapshot_map = {}

    if os.path.exists(MARKET_LATEST_CSV) and os.path.getsize(MARKET_LATEST_CSV) > 0:
        try:
            df = pd.read_csv(MARKET_LATEST_CSV)
            for _, row in df.iterrows():
                p_name = str(row.get("player_name", "")).strip()
                season = str(row.get("season", "")).strip().upper()
                grade_raw = row.get("grade", "")
                if not p_name or p_name.lower() == "null":
                    continue
                try:
                    grade_int = int(float(grade_raw))
                except (ValueError, TypeError):
                    grade_int = 1

                key = (p_name.lower(), season, grade_int)
                snapshot_map[key] = row.to_dict()
            if snapshot_map:
                print(f"✓ Đã nạp {len(snapshot_map)} snapshot mới nhất từ {MARKET_LATEST_CSV}")
                return snapshot_map
        except Exception as e:
            print(f"[Cảnh báo] Không thể đọc {MARKET_LATEST_CSV}: {e}")

    # Fallback đọc từ data/vn_market_history.csv
    if os.path.exists(MARKET_HISTORY_CSV) and os.path.getsize(MARKET_HISTORY_CSV) > 0:
        try:
            df_hist = pd.read_csv(MARKET_HISTORY_CSV)
            df_hist["dt"] = pd.to_datetime(df_hist["timestamp"], errors="coerce")
            df_hist = df_hist.sort_values(by="dt", ascending=False)
            for _, row in df_hist.iterrows():
                p_name = str(row.get("player_name", "")).strip()
                season = str(row.get("season", "")).strip().upper()
                grade_raw = row.get("grade", "")
                if not p_name or p_name.lower() == "null":
                    continue
                try:
                    grade_int = int(float(grade_raw))
                except (ValueError, TypeError):
                    grade_int = 1

                key = (p_name.lower(), season, grade_int)
                if key not in snapshot_map:
                    rec = row.to_dict()
                    diff = now - row["dt"] if pd.notna(row["dt"]) else datetime.timedelta(days=999)
                    rec["snapshot_age_minutes"] = max(0, int(diff.total_seconds() / 60))
                    rec["snapshot_timestamp"] = row.get("timestamp", "")
                    snapshot_map[key] = rec
            print(f"✓ Đã nạp {len(snapshot_map)} snapshot từ lịch sử {MARKET_HISTORY_CSV}")
        except Exception as e:
            print(f"[Cảnh báo] Không thể đọc history: {e}")

    return snapshot_map

def scan_market_candidates(candidate_list=None):
    """
    Rà soát tính khả thi trên TTCN Việt Nam cho các ứng viên.
    Áp dụng bộ lọc độ tin cậy [HIGH, MEDIUM] và thời hạn 24h (1440 phút).
    """
    print("=== RÀ SOÁT TÍNH KHẢ THI TTCN VIỆT NAM (VN_MARKET_CANDIDATE_SCANNER) ===")
    
    snapshot_map = load_latest_market_snapshots()
    
    if candidate_list is None:
        # Tự động nạp ứng viên từ các nguồn có sẵn
        candidate_list = []
        candidates_csv = os.path.join(EXPORTS_DIR, "vn_glxh_current_squad_candidates.csv")
        if os.path.exists(candidates_csv):
            try:
                candidate_list = pd.read_csv(candidates_csv).to_dict("records")
                print(f"✓ Nạp {len(candidate_list)} ứng viên từ {candidates_csv}")
            except Exception:
                pass
                
        if not candidate_list and os.path.exists(OWNED_PLAYERS_JSON):
            with open(OWNED_PLAYERS_JSON, "r", encoding="utf-8") as f:
                candidate_list = json.load(f)
                print(f"✓ Nạp {len(candidate_list)} cầu thủ từ {OWNED_PLAYERS_JSON}")

    if not candidate_list:
        print("[LỖI] Không có danh sách ứng viên để rà soát.")
        return []

    scan_results = []
    
    for c in candidate_list:
        p_name = str(c.get("player_name", "")).strip()
        season = str(c.get("season", "")).strip().upper()
        grade_raw = c.get("grade", 1)
        try:
            grade_int = int(float(grade_raw))
        except (ValueError, TypeError):
            grade_int = 1

        key = (p_name.lower(), season, grade_int)
        snapshot = snapshot_map.get(key)
        
        # Nếu không khớp exact name, thử đối soát tên họ
        if not snapshot:
            for s_key, s_data in snapshot_map.items():
                if s_key[1] == season and s_key[2] == grade_int:
                    # So sánh họ
                    if p_name.split()[-1].lower() in s_key[0]:
                        snapshot = s_data
                        break

        # Khởi tạo giá trị mặc định
        sell_price = ""
        buy_price = ""
        sell_qty = ""
        buy_qty = ""
        availability = "UNKNOWN"
        confidence = "UNKNOWN"
        snapshot_time = ""
        snapshot_age = ""
        is_viable = False
        market_flag = "NO_SNAPSHOT_FOUND"
        note = "Chưa có ảnh chụp màn hình hoặc dữ liệu TTCN VN cho thẻ này."

        if snapshot:
            sell_price = snapshot.get("sell_price", "")
            buy_price = snapshot.get("buy_price", "")
            sell_qty = snapshot.get("sell_quantity", "")
            buy_qty = snapshot.get("buy_quantity", "")
            availability = str(snapshot.get("market_availability", "UNKNOWN")).strip().upper()
            confidence = str(snapshot.get("price_confidence", "LOW")).strip().upper()
            snapshot_time = str(snapshot.get("snapshot_timestamp", "")).strip()
            
            # Tính tuổi snapshot
            try:
                snapshot_age = int(float(snapshot.get("snapshot_age_minutes", 9999)))
            except (ValueError, TypeError):
                snapshot_age = 9999

            # 1. Kiểm tra Độ tin cậy (Confidence)
            if confidence not in ["HIGH", "MEDIUM"]:
                is_viable = False
                market_flag = "LOW_CONFIDENCE_REJECTED"
                note = f"Độ tin cậy giá là {confidence} (không đảm bảo chính xác mùa/cấp thẻ). Không dùng để ra quyết định mua."

            # 2. Kiểm tra Tuổi snapshot (Quá 24 giờ = 1440 phút)
            elif snapshot_age > 1440:
                is_viable = False
                market_flag = "SNAPSHOT_EXPIRED_OVER_24H"
                note = f"Snapshot đã quá 24 giờ ({snapshot_age} phút trước). Cần chụp ảnh mới để xác nhận thẻ còn trên TTCN."

            # 3. Kiểm tra Tính khả dụng (Availability)
            elif availability == "AVAILABLE":
                # sell_qty > 0
                is_viable = True
                market_flag = "VERIFIED_AVAILABLE"
                note = f"Đã xác minh có hàng bán thực tế ({sell_qty} thẻ) trong vòng 24 giờ qua ({snapshot_age} phút trước)."

            elif availability == "BUY_ORDERS_ONLY":
                is_viable = False
                market_flag = "BUY_ORDERS_ONLY"
                note = f"Thị trường chỉ có lệnh đặt mua ({buy_qty} thẻ), không có ai niêm yết bán."

            elif availability == "NO_SELL_LISTING":
                is_viable = False
                market_flag = "NO_SELL_LISTING"
                note = "Thị trường hiện không có người bán (0 thẻ bán)."

            else:
                is_viable = False
                market_flag = "UNKNOWN"
                note = "Chưa có dữ liệu sổ lệnh bán thực tế từ TTCN Garena VN; cần xác minh qua screenshot in-game."

        assessment = {
            "player_name": p_name,
            "season": season,
            "grade": grade_int,
            "sell_price": sell_price,
            "buy_price": buy_price,
            "sell_quantity": sell_qty,
            "buy_quantity": buy_qty,
            "market_availability": availability,
            "price_confidence": confidence,
            "snapshot_timestamp": snapshot_time,
            "snapshot_age_minutes": snapshot_age,
            "is_purchase_viable": is_viable,
            "market_status_flag": market_flag,
            "note": note
        }
        scan_results.append(assessment)

    # Xuất file kết quả quét
    out_df = pd.DataFrame(scan_results)
    out_df.to_csv(CANDIDATE_SCAN_CSV, index=False, encoding="utf-8")
    print(f"✓ Đã lưu kết quả rà soát TTCN: {CANDIDATE_SCAN_CSV} ({len(out_df)} mục)")

    # Báo cáo tóm tắt
    print("\n" + "="*85)
    print(f"{'CẦU THỦ':<16} {'MÙA':<6} {'CẤP':<4} {'TIN CẬY':<8} {'TUỔI (m)':<9} {'KHẢ DỤNG':<16} {'KHẢ THI MUA?':<12}")
    print("="*85)
    for r in scan_results:
        viable_str = "✓ CÓ THỂ MUA" if r["is_purchase_viable"] else "✗ KHÔNG MUA"
        age_str = f"{r['snapshot_age_minutes']}m" if r['snapshot_age_minutes'] != "" else "N/A"
        print(
            f"{r['player_name']:<16} {r['season']:<6} +{r['grade']:<3} "
            f"{r['price_confidence']:<8} {age_str:<9} {r['market_availability']:<16} {viable_str:<12}"
        )
    print("="*85 + "\n")

    return scan_results

if __name__ == "__main__":
    scan_market_candidates()

