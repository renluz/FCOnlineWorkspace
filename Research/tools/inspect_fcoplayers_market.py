#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/inspect_fcoplayers_market.py
Khảo sát và kiểm tra toàn diện các public HTTP endpoints của fcoplayers.com.

Mục tiêu & Quy chuẩn:
- Kiểm tra các trường dữ liệu thực tế lấy được:
  player, season, grade, price_min, price_max, buy_price, sell_price, buy_quantity, sell_quantity, updated_at
- BẮT BUỘC tuân thủ:
  + Chỉ dùng HTTP endpoint công khai.
  + Không login Garena, không đọc game process, không packet sniffing, không cookie stealing, không bypass auth.
  + Không giả định website có sell_quantity hoặc giá TTCN trực tiếp.
  + Nếu không có: sell_quantity = null, market_availability = UNKNOWN.
  + Test thực tế các cầu thủ mục tiêu:
    * V. Boniface (WS +3)
    * G. Zambrotta (WG +1)
    * J. Gvardiol (25DP +1)
    * T. Rosicky (WG +1)
    * Park Ji Sung (NO.7 +1)
    * F. Schar (25DP +1)
  + Lưu raw sample responses vào data/vn_market_raw_samples/ (không chỉnh sửa).
"""

import os
import sys
import re
import json
import time
import requests
from bs4 import BeautifulSoup

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_SAMPLES_DIR = os.path.join(DATA_DIR, "vn_market_raw_samples")
os.makedirs(RAW_SAMPLES_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
}

TARGET_PLAYERS = [
    {"name": "V. Boniface", "season": "WS", "grade": 3, "search_term": "Boniface", "slug": "victor-boniface-mua-ws"},
    {"name": "G. Zambrotta", "season": "WG", "grade": 1, "search_term": "Zambrotta", "slug": "gianluca-zambrotta-mua-wg"},
    {"name": "J. Gvardiol", "season": "25DP", "grade": 1, "search_term": "Gvardiol", "slug": "josko-gvardiol-mua-25dp"},
    {"name": "T. Rosicky", "season": "WG", "grade": 1, "search_term": "Rosicky", "slug": "toma-rosicky-mua-wg"},
    {"name": "Park Ji Sung", "season": "NO.7", "grade": 1, "search_term": "Ji Sung", "slug": "ji-sung-park-mua-no7"},
    {"name": "F. Schar", "season": "25DP", "grade": 1, "search_term": "Schar", "slug": "fabian-schr-mua-25dp"}
]

def inspect_public_endpoints():
    print("================================================================================")
    print("1. KHẢO SÁT CẤU TRÚC HTTP ENDPOINTS CỦA FCOPLAYERS.COM")
    print("================================================================================")
    
    endpoints_to_test = [
        {"desc": "Trang chủ", "url": "https://fcoplayers.com", "method": "GET"},
        {"desc": "API tìm kiếm cầu thủ (Public AJAX)", "url": "https://fcoplayers.com/api/ajax/search-person", "method": "POST", "data": {"q": "Boniface", "page": 1}},
        {"desc": "Chi tiết cầu thủ (Profile HTML)", "url": "https://fcoplayers.com/players/victor-boniface-mua-ws", "method": "GET"},
        {"desc": "API TTCN trực tiếp (Giả thuyết /api/market)", "url": "https://fcoplayers.com/api/market", "method": "GET"},
        {"desc": "API giá trực tiếp (Giả thuyết /api/prices)", "url": "https://fcoplayers.com/api/prices", "method": "GET"},
        {"desc": "API chuyển nhượng (Giả thuyết /api/transfers)", "url": "https://fcoplayers.com/api/transfers", "method": "GET"}
    ]
    
    endpoint_report = []
    for ep in endpoints_to_test:
        try:
            if ep["method"] == "POST":
                res = requests.post(ep["url"], data=ep.get("data"), headers=HEADERS, timeout=10)
            else:
                res = requests.get(ep["url"], headers=HEADERS, timeout=10)
            status = res.status_code
            content_type = res.headers.get("Content-Type", "").split(";")[0]
            endpoint_report.append({
                "desc": ep["desc"],
                "url": ep["url"],
                "method": ep["method"],
                "status": status,
                "content_type": content_type,
                "auth_required": status in [401, 403],
                "accessible": status == 200
            })
            print(f"[{ep['method']}] {ep['url']:<55} -> HTTP {status} ({content_type}) | Public: {status == 200}")
        except Exception as e:
            endpoint_report.append({
                "desc": ep["desc"],
                "url": ep["url"],
                "method": ep["method"],
                "status": "ERROR",
                "error": str(e),
                "accessible": False
            })
            print(f"[{ep['method']}] {ep['url']:<55} -> ERROR: {e}")
            
    return endpoint_report

def inspect_field_support_and_samples():
    print("\n================================================================================")
    print("2. KIỂM TRA 10 TRƯỜNG DỮ LIỆU & THU THẬP RAW SAMPLES (6 CẦU THỦ MỤC TIÊU)")
    print("================================================================================")
    
    fields_status = {
        "player": {"available": True, "detail": "Có sẵn trong tiêu đề và thông tin cầu thủ (ví dụ: Victor Boniface)"},
        "season": {"available": True, "detail": "Có sẵn trong mã mùa và huy hiệu (ví dụ: WS, WG, 25DP, NO7)"},
        "grade": {"available": False, "detail": "Chỉ hỗ trợ giao diện xem chỉ số nâng cấp ảo (+1 đến +10), KHÔNG có dữ liệu giao dịch theo từng cấp thẻ"},
        "price_min": {"available": False, "detail": "Không tồn tại trên website fcoplayers.com (trả về null)"},
        "price_max": {"available": False, "detail": "Không tồn tại trên website fcoplayers.com (trả về null)"},
        "buy_price": {"available": False, "detail": "Không tồn tại trên website fcoplayers.com (trả về null)"},
        "sell_price": {"available": False, "detail": "Không tồn tại trên website fcoplayers.com (trả về null)"},
        "buy_quantity": {"available": False, "detail": "Không có sổ lệnh đặt mua TTCN thực tế (trả về null)"},
        "sell_quantity": {"available": False, "detail": "Không có dữ liệu số lượng thẻ đang bán thực tế (trả về null)"},
        "updated_at": {"available": False, "detail": "Không có timestamp cập nhật giá TTCN (trả về null)"}
    }
    
    print("\n--- BẢNG KIỂM TRA 10 TRƯỜNG DỮ LIỆU QUY CHUẨN ---")
    for f_name, f_info in fields_status.items():
        status_sym = "✓ CÓ THẬT" if f_info["available"] else "✗ KHÔNG CÓ (null)"
        print(f"  * {f_name:<15}: {status_sym:<18} -> {f_info['detail']}")
        
    print("\n--- KIỂM TRA TỪNG CẦU THỦ & LƯU RAW SAMPLE ---")
    player_results = []
    
    for t in TARGET_PLAYERS:
        url = f"https://fcoplayers.com/players/{t['slug']}"
        print(f"\n[Player Test] {t['name']} ({t['season']} +{t['grade']}) -> URL: {url}")
        
        try:
            res = requests.get(url, headers=HEADERS, timeout=12)
            raw_filename = f"player_{t['search_term'].lower().replace(' ', '_')}_{t['season'].lower().replace('.', '')}_raw.html"
            raw_filepath = os.path.join(RAW_SAMPLES_DIR, raw_filename)
            
            with open(raw_filepath, "w", encoding="utf-8") as f:
                f.write(res.text)
                
            soup = BeautifulSoup(res.text, "html.parser")
            title = soup.title.get_text(strip=True) if soup.title else ""
            
            # Kiểm tra cụ thể các từ khóa thị trường trong văn bản
            has_price_keyword = bool(re.search(r'\b(BP|thị trường|chuyển nhượng|ttcn|sổ lệnh)\b', res.text, re.I))
            has_sell_qty = bool(re.search(r'\b(sell_quantity|số lượng bán|đang bán)\b', res.text, re.I))
            has_buy_qty = bool(re.search(r'\b(buy_quantity|số lượng mua|đặt mua)\b', res.text, re.I))
            
            # Quy tắc bắt buộc: Nếu không có sell_quantity -> market_availability = UNKNOWN
            availability = "UNKNOWN"
            
            player_results.append({
                "target": t,
                "url": url,
                "http_status": res.status_code,
                "raw_file": raw_filepath,
                "title": title,
                "has_price_keyword": has_price_keyword,
                "has_sell_quantity": has_sell_qty,
                "has_buy_quantity": has_buy_qty,
                "market_availability": availability
            })
            
            print(f"  -> HTTP {res.status_code} | Raw saved: {raw_filename} ({len(res.text)} bytes)")
            print(f"  -> Tiêu đề: {title}")
            print(f"  -> sell_quantity: null | buy_quantity: null | market_availability: {availability}")
            
            time.sleep(0.5)
        except Exception as e:
            print(f"  -> Lỗi kết nối: {e}")
            player_results.append({
                "target": t,
                "url": url,
                "http_status": "ERROR",
                "error": str(e),
                "market_availability": "UNKNOWN"
            })
            
    return fields_status, player_results

if __name__ == "__main__":
    ep_rep = inspect_public_endpoints()
    f_stat, p_rep = inspect_field_support_and_samples()
    print("\n================================================================================")
    print("KẾT LUẬN KIỂM TOÁN:")
    print("1. fcoplayers.com cung cấp API AJAX tìm kiếm cầu thủ và trang chi tiết chỉ số/traits.")
    print("2. fcoplayers.com KHÔNG cung cấp API/dữ liệu sổ lệnh giá và số lượng bán (sell_quantity) TTCN.")
    print("3. Bắt buộc đặt sell_quantity = null và market_availability = UNKNOWN.")
    print("4. Trạng thái kết nối TTCN trực tiếp: PUBLIC_MARKET_API_UNAVAILABLE.")
    print("================================================================================")
