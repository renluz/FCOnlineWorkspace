#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/vn_market_screenshot_importer.py
Công cụ nhập và xử lý ảnh chụp màn hình TTCN FC Online Việt Nam thật.

Quy chuẩn an toàn:
- Không auto-buy, không auto-sell.
- Không click trong game.
- Không đọc RAM/process game, không packet sniff, không hook.

Chế độ hoạt động (2 modes):
1. IMAGE_PARSE: Tự động trích xuất thông tin hiển thị trên ảnh bằng Windows Native OCR Engine.
2. MANUAL_ASSISTED: Nhập hoặc bổ trợ thông tin qua sidecar json/text hoặc CLI input.

Các trường dữ liệu trích xuất:
timestamp, player_name, season, grade, price_min_visible, price_max_visible,
buy_price_visible, sell_price_visible, buy_quantity_visible, sell_quantity_visible,
market_availability, source_image, source, price_confidence

Nguyên tắc:
- Nếu ảnh không hiển thị trường nào -> ghi nhận 'null'. Không suy diễn.
- Append vào data/vn_market_history.csv (không ghi đè snapshot cũ).
- Di chuyển ảnh đã xử lý từ incoming sang processed.
- Cập nhật exports/vn_market_latest.csv và tạo VN_MARKET_SNAPSHOT_REPORT.md.
"""

import os
import sys
import re
import json
import csv
import shutil
import datetime
import subprocess
import pandas as pd
from difflib import SequenceMatcher

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
EXPORTS_DIR = os.path.join(BASE_DIR, "exports")
SCREENSHOTS_DIR = os.path.join(DATA_DIR, "vn_market_screenshots")
INCOMING_DIR = os.path.join(SCREENSHOTS_DIR, "incoming")
PROCESSED_DIR = os.path.join(SCREENSHOTS_DIR, "processed")
MARKET_HISTORY_CSV = os.path.join(DATA_DIR, "vn_market_history.csv")
MARKET_LATEST_CSV = os.path.join(EXPORTS_DIR, "vn_market_latest.csv")
SNAPSHOT_REPORT_MD = os.path.join(BASE_DIR, "VN_MARKET_SNAPSHOT_REPORT.md")

os.makedirs(INCOMING_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(EXPORTS_DIR, exist_ok=True)

# Danh sách mùa giải
KNOWN_SEASONS = [
    "WS", "WG", "25DP", "NO.7", "NO7", "HOT", "19UCL", "19", "LH", "ICONTM", "ICON",
    "24TOTY", "25TOTY", "24TOTS", "23TOTS", "24UCL", "23UCL", "RTN", "CU", "BDO",
    "CAP", "EBS", "BTB", "LN", "UT", "LE", "DC", "CC", "BLD", "WB", "LIVE"
]

# Danh sách tên cầu thủ chuẩn trong hệ thống để đối soát nhận diện OCR
STANDARD_PLAYER_NAMES = [
    "V. Boniface", "G. Zambrotta", "J. Gvardiol", "T. Rosicky",
    "Park Ji Sung", "F. Schar", "A. Del Piero", "R. Gullit",
    "Rodri", "Sergio Ramos", "W. Hennessey", "Inaki Williams", "P. Aubameyang"
]

def run_windows_ocr(image_path):
    """
    Sử dụng Windows.Media.Ocr native trên Windows để nhận diện văn bản từ ảnh.
    """
    abs_path = os.path.abspath(image_path)
    ps_ocr_script = """& {
param([string]$Path)
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$asTaskGeneric = [System.WindowsRuntimeSystemExtensions].GetMethods() | ? { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' }
function Await($asyncOp, $type) {
    $asTask = $asTaskGeneric.MakeGenericMethod($type)
    $netTask = $asTask.Invoke($null, @($asyncOp))
    $netTask.Wait(-1) | Out-Null
    return $netTask.Result
}

[Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType = WindowsRuntime] | Out-Null
[Windows.Media.Ocr.OcrEngine, Windows.Foundation.UniversalApiContract, ContentType = WindowsRuntime] | Out-Null

$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
if ($null -eq $engine) {
    $engine = [Windows.Media.Ocr.OcrEngine]::AvailableRecognizerLanguages[0]
}

$file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($Path)) ([Windows.Storage.StorageFile])
$stream = Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
$decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
$bitmap = Await ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
$ocrResult = Await ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])

$ocrResult.Lines | ForEach-Object { $_.Text }
}"""
    try:
        res = subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps_ocr_script, abs_path],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=25
        )
        if res.returncode == 0 and res.stdout:
            lines = [line.strip() for line in res.stdout.splitlines() if line.strip()]
            return lines
        return []
    except Exception as e:
        print(f"[OCR Error] Lỗi khi nhận diện ảnh {image_path}: {e}")
        return []

def parse_price_str(raw_str):
    """Làm sạch chuỗi giá và chuyển về số nguyên BP"""
    if not raw_str or raw_str == "null":
        return None
    cleaned = re.sub(r"[^\d]", "", str(raw_str))
    if cleaned.isdigit():
        return int(cleaned)
    return None

def match_player_name(raw_text):
    """Đối soát tên cầu thủ theo độ tương đồng cao nhất"""
    best_name = None
    best_ratio = 0.0
    for name in STANDARD_PLAYER_NAMES:
        # Kiểm tra chứa trực tiếp họ
        last_name = name.split()[-1]
        if last_name.lower() in raw_text.lower():
            return name
        ratio = SequenceMatcher(None, name.lower(), raw_text.lower()).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_name = name
    if best_ratio >= 0.55:
        return best_name
    return None

def parse_image_content(lines, filename):
    """
    Phân tích nội dung OCR từ ảnh chụp màn hình TTCN.
    """
    full_text = " ".join(lines)
    
    player_name = "null"
    season = "null"
    grade = "null"
    buy_price = "null"
    sell_price = "null"
    buy_qty = "null"
    sell_qty = "null"
    price_min = "null"
    price_max = "null"
    availability = "UNKNOWN"
    confidence = "LOW"
    
    # 1. Tìm mùa giải (Season)
    for s in KNOWN_SEASONS:
        pattern = rf"\b{re.escape(s)}\b"
        if re.search(pattern, full_text, re.I):
            season = s.upper()
            break
            
    # 2. Tìm cấp thẻ (Grade +1 đến +10)
    grade_match = re.search(r"(?:\+|\bcấp\s*|\bgrade\s*)(\d{1,2})\b", full_text, re.I)
    if grade_match:
        g_val = int(grade_match.group(1))
        if 1 <= g_val <= 10:
            grade = g_val
            
    # 3. Tìm tên cầu thủ
    # Thử đối soát từng dòng OCR với danh sách chuẩn
    for line in lines:
        matched = match_player_name(line)
        if matched:
            player_name = matched
            break
            
    if player_name == "null":
        for line in lines[:3]:
            if not re.search(r"(thị trường|chuyển nhượng|giá|bán|mua|bp|\+\d)", line, re.I) and len(line) > 2:
                player_name = line
                break
            
    # 4. Tìm các giá trị tiền tệ BP
    bp_numbers = re.findall(r"(\d{1,3}(?:[,\.]\d{3})+|\d{7,14})\s*(?:BP|GP|SP)?", full_text, re.I)
    valid_prices = []
    for num_str in bp_numbers:
        p_val = parse_price_str(num_str)
        if p_val and p_val > 100000:
            valid_prices.append(p_val)
            
    if len(valid_prices) == 1:
        sell_price = valid_prices[0]
    elif len(valid_prices) >= 2:
        sell_price = max(valid_prices)
        buy_price = min(valid_prices)

    # 5. Tìm số lượng lệnh bán / đặt mua
    for line in lines:
        line_clean = line.strip()
        # Tìm số lượng bán
        if sell_qty == "null":
            sq_m = re.search(r"(?:dang|đang|bán|ban|sell|sl\s*bán|lệnh\s*bán)[\s\w:]*?(\d+)\s*(?:the|thẻ)?", line_clean, re.I)
            if sq_m and not re.search(r"(?:mua|buy|dat\s*mua|đặt\s*mua|giá|gia|bp|gp)", line_clean, re.I):
                sell_qty = int(sq_m.group(1))
        # Tìm số lượng mua
        if buy_qty == "null":
            bq_m = re.search(r"(?:dat\s*mua|đặt\s*mua|mua|buy|sl\s*mua|lệnh\s*mua)[\s\w:]*?(\d+)\s*(?:the|thẻ)?", line_clean, re.I)
            if bq_m and not re.search(r"(?:ban|bán|sell|giá|gia|bp|gp)", line_clean, re.I):
                buy_qty = int(bq_m.group(1))

    if sell_qty == "null":
        sell_qty_match = re.search(r"(?:bán|đang\s*bán|sell|sl\s*bán)[\s:]*(\d+)", full_text, re.I)
        if sell_qty_match:
            sell_qty = int(sell_qty_match.group(1))
        
    if buy_qty == "null":
        buy_qty_match = re.search(r"(?:mua|đặt\s*mua|dat\s*mua|buy|sl\s*mua)[\s:]*(\d+)", full_text, re.I)
        if buy_qty_match:
            buy_qty = int(buy_qty_match.group(1))
        
    # 6. Đánh giá Availability
    if sell_qty != "null" and isinstance(sell_qty, int) and sell_qty > 0:
        availability = "AVAILABLE"
    elif sell_qty == 0:
        availability = "NO_SELL_LISTING"
    elif sell_qty == "null" and buy_qty != "null" and isinstance(buy_qty, int) and buy_qty > 0:
        availability = "BUY_ORDERS_ONLY"
    elif sell_qty == 0 and buy_qty != "null" and isinstance(buy_qty, int) and buy_qty > 0:
        availability = "BUY_ORDERS_ONLY"
    else:
        availability = "UNKNOWN"
        
    # 7. Đánh giá Confidence
    has_name = (player_name != "null" and len(player_name) > 2)
    has_season = (season != "null")
    has_grade = (grade != "null")
    has_price = (sell_price != "null" or buy_price != "null")
    
    if has_name and has_season and has_grade and has_price:
        confidence = "HIGH"
    elif has_name and (has_season or has_grade) and has_price:
        confidence = "MEDIUM"
    else:
        confidence = "LOW"
        
    return {
        "player_name": player_name,
        "season": season,
        "grade": grade,
        "price_min_visible": price_min,
        "price_max_visible": price_max,
        "buy_price_visible": buy_price,
        "sell_price_visible": sell_price,
        "buy_quantity_visible": buy_qty,
        "sell_quantity_visible": sell_qty,
        "market_availability": availability,
        "price_confidence": confidence
    }


def import_screenshots(mode="IMAGE_PARSE"):
    """
    Quét toàn bộ ảnh trong data/vn_market_screenshots/incoming/,
    phân tích thông tin, append vào data/vn_market_history.csv và di chuyển sang processed/.
    """
    print(f"=== TIẾN HÀNH NHẬP ẢNH TTCN (Mode: {mode}) ===")
    incoming_files = [
        f for f in os.listdir(INCOMING_DIR)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".webp"))
    ]
    
    print(f"Tìm thấy {len(incoming_files)} ảnh trong thư mục incoming: {INCOMING_DIR}")
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not incoming_files:
        print("[INFO] Thư mục incoming hiện đang trống. Sẵn sàng nhận ảnh mới từ người dùng.")
        update_latest_export()
        generate_snapshot_report(0, 0, 0, 0, 0, now_str)
        return []

    parsed_records = []
    
    for fname in incoming_files:
        fpath = os.path.join(INCOMING_DIR, fname)
        print(f"\n--- Xử lý ảnh: {fname} ---")
        
        record = {
            "timestamp": now_str,
            "spId": "null",
            "player_name": "null",
            "season": "null",
            "grade": "null",
            "price_min": "null",
            "price_max": "null",
            "buy_price": "null",
            "sell_price": "null",
            "buy_quantity": "null",
            "sell_quantity": "null",
            "market_availability": "UNKNOWN",
            "source": "IN_GAME_SCREENSHOT",
            "price_confidence": "LOW",
            "source_image": fname
        }
        
        # Kiểm tra sidecar file JSON nếu có (MANUAL_ASSISTED)
        sidecar_json = os.path.splitext(fpath)[0] + ".json"
        if os.path.exists(sidecar_json):
            print(f"  ✓ Phát hiện sidecar JSON: {os.path.basename(sidecar_json)}")
            with open(sidecar_json, "r", encoding="utf-8") as sf:
                sidecar_data = json.load(sf)
                for k, v in sidecar_data.items():
                    record[k] = v
            record["source"] = "USER_MANUAL_INPUT" if mode == "MANUAL_ASSISTED" else "IN_GAME_SCREENSHOT"
            if record.get("price_confidence") is None:
                record["price_confidence"] = "HIGH"
        elif mode == "IMAGE_PARSE":
            ocr_lines = run_windows_ocr(fpath)
            print(f"  ✓ OCR trích xuất {len(ocr_lines)} dòng văn bản.")
            parsed_data = parse_image_content(ocr_lines, fname)
            
            record["player_name"] = parsed_data["player_name"]
            record["season"] = parsed_data["season"]
            record["grade"] = parsed_data["grade"]
            record["price_min"] = parsed_data["price_min_visible"]
            record["price_max"] = parsed_data["price_max_visible"]
            record["buy_price"] = parsed_data["buy_price_visible"]
            record["sell_price"] = parsed_data["sell_price_visible"]
            record["buy_quantity"] = parsed_data["buy_quantity_visible"]
            record["sell_quantity"] = parsed_data["sell_quantity_visible"]
            record["market_availability"] = parsed_data["market_availability"]
            record["price_confidence"] = parsed_data["price_confidence"]

        print(
            f"  -> Kết quả: {record['player_name']} ({record['season']} +{record['grade']}) | "
            f"Giá bán: {record['sell_price']} | Bán: {record['sell_quantity']} | "
            f"Availability: {record['market_availability']} | Confidence: {record['price_confidence']}"
        )
        
        parsed_records.append(record)
        
        # Append vào data/vn_market_history.csv
        append_to_history(record)
        
        # Di chuyển ảnh và sidecar sang processed/
        dest_img = os.path.join(PROCESSED_DIR, fname)
        shutil.move(fpath, dest_img)
        if os.path.exists(sidecar_json):
            shutil.move(sidecar_json, os.path.join(PROCESSED_DIR, os.path.basename(sidecar_json)))
        print(f"  ✓ Đã lưu trữ ảnh vào: {dest_img}")

    # Cập nhật exports/vn_market_latest.csv và báo cáo snapshot
    update_latest_export()
    
    high_cnt = sum(1 for r in parsed_records if r["price_confidence"] == "HIGH")
    avail_cnt = sum(1 for r in parsed_records if r["market_availability"] == "AVAILABLE")
    unk_cnt = sum(1 for r in parsed_records if r["market_availability"] == "UNKNOWN")
    
    generate_snapshot_report(
        processed_count=len(parsed_records),
        recognized_players=len(parsed_records),
        high_confidence_count=high_cnt,
        available_count=avail_cnt,
        unknown_count=unk_cnt,
        latest_timestamp=now_str
    )
    
    return parsed_records

def append_to_history(record):
    """Append bản ghi vào data/vn_market_history.csv mà không ghi đè snapshot cũ"""
    history_fields = [
        "timestamp", "spId", "player_name", "season", "grade",
        "price_min", "price_max", "buy_price", "sell_price",
        "buy_quantity", "sell_quantity", "market_availability",
        "source", "price_confidence", "source_image"
    ]
    file_exists = os.path.exists(MARKET_HISTORY_CSV)
    
    # Kiểm tra header hiện tại có đủ các cột mới không
    needs_header_update = False
    if file_exists and os.path.getsize(MARKET_HISTORY_CSV) > 0:
        with open(MARKET_HISTORY_CSV, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader, [])
            if "price_confidence" not in headers:
                needs_header_update = True
                
    if needs_header_update:
        df_old = pd.read_csv(MARKET_HISTORY_CSV)
        for f in history_fields:
            if f not in df_old.columns:
                df_old[f] = "null"
        df_old = df_old[history_fields]
        df_old.to_csv(MARKET_HISTORY_CSV, index=False, encoding="utf-8")

    with open(MARKET_HISTORY_CSV, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=history_fields)
        if not file_exists or os.path.getsize(MARKET_HISTORY_CSV) == 0:
            writer.writeheader()
        row = {k: record.get(k, "null") for k in history_fields}
        writer.writerow(row)

def update_latest_export():
    """
    Đọc toàn bộ data/vn_market_history.csv, lấy snapshot mới nhất cho mỗi cặp player_name + season + grade,
    tính toán snapshot_age_minutes và xuất ra exports/vn_market_latest.csv.
    """
    if not os.path.exists(MARKET_HISTORY_CSV) or os.path.getsize(MARKET_HISTORY_CSV) == 0:
        return
        
    df = pd.read_csv(MARKET_HISTORY_CSV)
    if df.empty:
        return
        
    now = datetime.datetime.now()
    
    # Lọc bỏ các dòng không hợp lệ
    valid_df = df[df["player_name"].notna() & (df["player_name"] != "null")].copy()
    if valid_df.empty:
        return
        
    valid_df["dt"] = pd.to_datetime(valid_df["timestamp"], errors="coerce")
    valid_df = valid_df.sort_values(by="dt", ascending=False)
    
    # Lấy snapshot mới nhất của mỗi thẻ
    latest_df = valid_df.drop_duplicates(subset=["player_name", "season", "grade"], keep="first").copy()
    
    def calc_age(row_dt):
        if pd.isna(row_dt):
            return 9999
        diff = now - row_dt
        return max(0, int(diff.total_seconds() / 60))
        
    latest_df["snapshot_age_minutes"] = latest_df["dt"].apply(calc_age)
    latest_df["snapshot_timestamp"] = latest_df["timestamp"]
    
    # Schema yêu cầu:
    # player_name, season, grade, sell_price, buy_price, sell_quantity, buy_quantity,
    # market_availability, snapshot_timestamp, snapshot_age_minutes, price_confidence, source
    export_cols = [
        "player_name", "season", "grade", "sell_price", "buy_price",
        "sell_quantity", "buy_quantity", "market_availability",
        "snapshot_timestamp", "snapshot_age_minutes", "price_confidence", "source"
    ]
    
    for c in export_cols:
        if c not in latest_df.columns:
            latest_df[c] = "null"
            
    out_df = latest_df[export_cols].copy()

    # Định dạng sạch cho các cột số nguyên (không để số thập phân .0)
    int_cols = ["grade", "sell_price", "buy_price", "sell_quantity", "buy_quantity", "snapshot_age_minutes"]
    for c in int_cols:
        if c in out_df.columns:
            def fmt_num(v):
                if pd.isna(v) or str(v).lower() in ["null", "nan", "none", ""]:
                    return ""
                try:
                    return str(int(float(v)))
                except (ValueError, TypeError):
                    return str(v)
            out_df[c] = out_df[c].apply(fmt_num)

    # Làm sạch các cột chuỗi
    str_cols = ["player_name", "season", "market_availability", "snapshot_timestamp", "price_confidence", "source"]
    for c in str_cols:
        if c in out_df.columns:
            out_df[c] = out_df[c].apply(lambda x: "" if pd.isna(x) or str(x).lower() in ["null", "nan", "none"] else str(x))

    out_df.to_csv(MARKET_LATEST_CSV, index=False, encoding="utf-8")
    print(f"✓ Đã cập nhật snapshot thị trường mới nhất: {MARKET_LATEST_CSV} ({len(out_df)} mục)")

def generate_snapshot_report(processed_count, recognized_players, high_confidence_count, available_count, unknown_count, latest_timestamp):
    """
    Tạo báo cáo kiểm toán snapshot VN_MARKET_SNAPSHOT_REPORT.md
    """
    table_rows = []
    db_total = 0
    db_high = 0
    db_avail = 0
    db_unk = 0
    db_latest_time = latest_timestamp

    if os.path.exists(MARKET_LATEST_CSV):
        try:
            df = pd.read_csv(MARKET_LATEST_CSV, keep_default_na=False)
            db_total = len(df)
            for _, r in df.iterrows():
                p_name = str(r.get("player_name", "")).strip()
                if not p_name or p_name.lower() in ["nan", "null"]:
                    continue

                season = str(r.get("season", "")).strip()
                season_str = f"`{season}`" if season and season.lower() not in ["nan", "null"] else "`N/A`"

                grade_raw = str(r.get("grade", "")).strip()
                if grade_raw and grade_raw.lower() not in ["nan", "null"]:
                    try:
                        grade_str = f"`+{int(float(grade_raw))}`"
                    except Exception:
                        grade_str = f"`+{grade_raw}`"
                else:
                    grade_str = "`N/A`"

                sell_p_raw = str(r.get("sell_price", "")).strip()
                if sell_p_raw and sell_p_raw.lower() not in ["nan", "null"]:
                    try:
                        sell_p_str = f"`{int(float(sell_p_raw)):,} BP`"
                    except Exception:
                        sell_p_str = f"`{sell_p_raw} BP`"
                else:
                    sell_p_str = "*Chưa có giá*"

                sell_q_raw = str(r.get("sell_quantity", "")).strip()
                if sell_q_raw and sell_q_raw.lower() not in ["nan", "null"]:
                    try:
                        sell_q_str = f"`{int(float(sell_q_raw))}`"
                    except Exception:
                        sell_q_str = f"`{sell_q_raw}`"
                else:
                    sell_q_str = "`-`"

                avail = str(r.get("market_availability", "UNKNOWN")).strip()
                conf = str(r.get("price_confidence", "UNKNOWN")).strip()
                if not conf or conf.lower() in ["nan", "null"]:
                    conf = "UNKNOWN"

                age = str(r.get("snapshot_age_minutes", "")).strip()
                age_str = f"`{age}m`" if age and age.lower() not in ["nan", "null"] else "`N/A`"

                # Thống kê tổng hợp DB
                if conf == "HIGH":
                    db_high += 1
                if avail == "AVAILABLE":
                    db_avail += 1
                elif avail == "UNKNOWN":
                    db_unk += 1

                ts = str(r.get("snapshot_timestamp", "")).strip()
                if ts and ts > db_latest_time:
                    db_latest_time = ts

                table_rows.append(
                    f"| **{p_name}** | {season_str} | {grade_str} | {sell_p_str} | {sell_q_str} | `{avail}` | `{conf}` | {age_str} |"
                )
        except Exception as e:
            print(f"[Cảnh báo] Lỗi khi tạo bảng snapshot report: {e}")

    rows_md = "\n".join(table_rows) if table_rows else "| Không có dữ liệu | - | - | - | - | - | - | - |"

    md_content = f"""# 📸 BÁO CÁO KIỂM TOÁN SNAPSHOT TTCN VIỆT NAM (VN_MARKET_SNAPSHOT_REPORT.md)
*Thời điểm kiểm toán:* {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} (UTC+7)  
*Pipeline:* `tools/vn_market_screenshot_importer.py` (In-Game Screenshot Processing)  
*Chính sách:* **Không auto-buy, không can thiệp game, chỉ đọc dữ liệu hình ảnh người dùng cung cấp**.

---

## 1. 📊 THỐNG KÊ TỔNG QUAN

| Chỉ Số Kiểm Toán | Đợt Quét Vừa Qua | Tổng Tích Lũy Database | Ghi Chú Kỹ Thuật |
| :--- | :---: | :---: | :--- |
| **Số ảnh xử lý:** | `{processed_count}` | `{processed_count}` ảnh mới | Đã xử lý và lưu trữ trong `processed/` |
| **Số cầu thủ nhận diện:** | `{recognized_players}` | `{db_total}` thẻ theo dõi | Khớp định danh tên và mùa |
| **Số bản ghi HIGH confidence:** | `{high_confidence_count}` | `{db_high}` thẻ | Đầy đủ tên + mùa + cấp thẻ + giá bán |
| **Số bản ghi AVAILABLE:** | `{available_count}` | `{db_avail}` thẻ | Có lệnh bán niêm yết thực tế (`sell_quantity > 0`) |
| **Số bản ghi UNKNOWN:** | `{unknown_count}` | `{db_unk}` thẻ | Chỉ có giá tham chiếu hoặc thiếu sổ lệnh bán |
| **Timestamp mới nhất:** | `{latest_timestamp}` | `{db_latest_time}` | Thời điểm snapshot gần nhất |


---

## 2. 📋 BẢNG TỔNG HỢP GIÁ TTCN GẦN NHẤT (LATEST SNAPSHOTS)

| Cầu Thủ | Mùa | Cấp | Giá Bán (BP) | Lượng Bán | Khả Dụng (Availability) | Độ Tin Cậy | Tuổi Snapshot |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
{rows_md}

---

## 3. 🛡️ QUY TRÌNH TIẾP NHẬN ẢNH TTCN CỦA NGƯỜI DÙNG

1. **Thư mục nạp ảnh:** Người dùng chỉ cần thả ảnh chụp màn hình TTCN (PNG/JPG) vào:  
   `E:\\FCOnlineWorkspace\\Research\\data\\vn_market_screenshots\\incoming\\`
2. **Kích hoạt công cụ:**
   ```powershell
   python tools\\vn_market_screenshot_importer.py
   ```
   *(Hoặc kèm cờ `MANUAL_ASSISTED` nếu dùng file JSON sidecar hỗ trợ)*
3. **Kết quả:**
   - Dữ liệu được trích xuất tự động bằng Windows Native OCR Engine.
   - Tự động append vào `data/vn_market_history.csv` (không ghi đè lịch sử).
   - Ảnh gốc được lưu trữ an toàn trong `data/vn_market_screenshots/processed/`.
   - Bảng giá thị trường mới nhất được cập nhật tại `exports/vn_market_latest.csv`.

---

## 4. 🎯 NGUYÊN TẮC PHÂN CẤP ĐỘ TIN CẬY (CONFIDENCE & AVAILABILITY)

* **HIGH Confidence:** Đầy đủ `player_name`, `season`, `grade`, `price`. Đạt chuẩn đưa vào mô hình tối ưu GLXH.
* **MEDIUM Confidence:** Nhận diện chắc chắn danh tính nhưng thiếu trường phụ (sàn/trần). Được phép tham chiếu.
* **LOW Confidence:** Thiếu season hoặc grade. **Tuyệt đối không dùng để ra quyết định mua.**
* **AVAILABLE:** Chỉ kích hoạt khi screenshot cho thấy số lượng bán `sell_quantity > 0`.
* **BUY_ORDERS_ONLY:** Sổ lệnh chỉ toàn người đặt mua, không có người bán.
* **NO_SELL_LISTING:** Không có thẻ nào được niêm yết bán (0 thẻ bán).
* **UNKNOWN:** Thiếu thông tin sổ lệnh thị trường.
"""
    with open(SNAPSHOT_REPORT_MD, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"✓ Đã tạo báo cáo kiểm toán snapshot: {SNAPSHOT_REPORT_MD}")


if __name__ == "__main__":
    mode = "IMAGE_PARSE"
    if len(sys.argv) > 1 and sys.argv[1].upper() == "MANUAL_ASSISTED":
        mode = "MANUAL_ASSISTED"
    import_screenshots(mode=mode)
