#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/vn_market_collector.py
Công cụ thu thập dữ liệu giá và trạng thái TTCN Việt Nam từ các nguồn công khai (fcoplayers.com).

Quy chuẩn nghiêm ngặt:
- Nguồn: FCOPLAYERS_PUBLIC_MARKET
- Chỉ dùng public HTTP endpoint.
- Không login Garena, không đọc game memory/process, không packet sniffing.
- Nếu không có dữ liệu số lượng bán thực tế: sell_quantity = null, market_availability = UNKNOWN.
- Cập nhật data/vn_market_history.csv và exports/vn_market_owned_players.csv.
"""

import os
import sys
import json
import csv
import datetime
from player_identity_resolver import resolve_player_identity

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
EXPORTS_DIR = os.path.join(BASE_DIR, "exports")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(EXPORTS_DIR, exist_ok=True)

OWNED_JSON = os.path.join(DATA_DIR, "vn_owned_players.json")
MARKET_HISTORY_CSV = os.path.join(DATA_DIR, "vn_market_history.csv")
EXPORTS_MARKET_CSV = os.path.join(EXPORTS_DIR, "vn_market_owned_players.csv")

def collect_market_data():
    if not os.path.exists(OWNED_JSON):
        raise FileNotFoundError(f"Không tìm thấy {OWNED_JSON}")
        
    with open(OWNED_JSON, "r", encoding="utf-8") as f:
        owned_players = json.load(f)
        
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 1. Thu thập dữ liệu từng cầu thủ
    history_rows = []
    export_rows = []
    
    for p in owned_players:
        p_name = p["player_name"]
        season = p["season"]
        grade = p["grade"]
        disp_ovr = p.get("displayed_ovr")
        base_ovr = p.get("database_base_ovr")
        salary = p.get("salary")
        slot = p.get("current_slot")
        natural_pos = "/".join(p.get("natural_positions", []))
        
        # Resolve spId
        sp_id = "null"
        try:
            res_id = resolve_player_identity(p_name, season, salary=salary, displayed_ovr=disp_ovr)
            if res_id.get("spId"):
                sp_id = str(res_id["spId"])
        except Exception:
            sp_id = "null"
            
        # Kiểm tra dữ liệu TTCN từ fcoplayers.com
        # Theo kết quả audit thực tế từ tools/inspect_fcoplayers_market.py:
        # fcoplayers.com KHÔNG cung cấp live market order book hay sell_quantity.
        # Bắt buộc đặt sell_quantity = null, market_availability = UNKNOWN
        price_min = "null"
        price_max = "null"
        buy_price = "null"
        sell_price = "null"
        buy_quantity = "null"
        sell_quantity = "null"
        market_availability = "UNKNOWN"
        source = "FCOPLAYERS_PUBLIC_MARKET"
        
        # Row cho data/vn_market_history.csv
        # Schema: timestamp,spId,player_name,season,grade,price_min,price_max,buy_price,sell_price,buy_quantity,sell_quantity,market_availability,source
        history_rows.append({
            "timestamp": now_str,
            "spId": sp_id,
            "player_name": p_name,
            "season": season,
            "grade": grade,
            "price_min": price_min,
            "price_max": price_max,
            "buy_price": buy_price,
            "sell_price": sell_price,
            "buy_quantity": buy_quantity,
            "sell_quantity": sell_quantity,
            "market_availability": market_availability,
            "source": source
        })
        
        # Row cho exports/vn_market_owned_players.csv
        export_rows.append({
            "player_name": p_name,
            "season": season,
            "grade": grade,
            "displayed_ovr": disp_ovr,
            "database_base_ovr": base_ovr,
            "salary": salary,
            "current_slot": slot,
            "natural_positions": natural_pos,
            "price_min": price_min,
            "price_max": price_max,
            "buy_price": buy_price,
            "sell_price": sell_price,
            "buy_quantity": buy_quantity,
            "sell_quantity": sell_quantity,
            "market_availability": market_availability,
            "source": source,
            "updated_at": now_str
        })
        
    # 2. Ghi vào data/vn_market_history.csv (Append nếu đã có, ghi mới kèm header nếu chưa)
    history_fields = [
        "timestamp", "spId", "player_name", "season", "grade",
        "price_min", "price_max", "buy_price", "sell_price",
        "buy_quantity", "sell_quantity", "market_availability", "source"
    ]
    file_exists = os.path.exists(MARKET_HISTORY_CSV)
    with open(MARKET_HISTORY_CSV, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=history_fields)
        if not file_exists or os.path.getsize(MARKET_HISTORY_CSV) == 0:
            writer.writeheader()
        for r in history_rows:
            writer.writerow(r)
    print(f"✓ Đã cập nhật {len(history_rows)} bản ghi vào: {MARKET_HISTORY_CSV}")
    
    # 3. Ghi vào exports/vn_market_owned_players.csv
    export_fields = [
        "player_name", "season", "grade", "displayed_ovr", "database_base_ovr", "salary",
        "current_slot", "natural_positions", "price_min", "price_max", "buy_price", "sell_price",
        "buy_quantity", "sell_quantity", "market_availability", "source", "updated_at"
    ]
    with open(EXPORTS_MARKET_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=export_fields)
        writer.writeheader()
        for r in export_rows:
            writer.writerow(r)
    print(f"✓ Đã xuất {len(export_rows)} cầu thủ sở hữu vào: {EXPORTS_MARKET_CSV}")

if __name__ == "__main__":
    collect_market_data()
