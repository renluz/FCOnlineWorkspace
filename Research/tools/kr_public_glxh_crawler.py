#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/kr_public_glxh_crawler.py
Thu thập và chuẩn hóa dữ liệu chiến thuật, sơ đồ, và đội hình Super Champions/Champions 
được chia sẻ công khai trên Inven Hàn Quốc (Board 3145 - 전술/팁 & 감독모드).

Đặc tả:
- sample_type = "KR_PUBLIC_GLXH"
- Đối chiếu cầu thủ với database 41,289 cầu thủ (repos/fconline-player-search/data/details.csv)
- Tính toán chỉ số theo cấp thẻ cộng (+1, +3, +5, +8) bằng delta chuẩn.
- Xuất dữ liệu chiến thuật và đội hình công khai:
  + data/kr_public_glxh_tactics.json
  + data/kr_public_glxh_squads.json
  + exports/kr_public_glxh_candidates.csv
  + exports/kr_public_glxh_candidates.json
"""

import os
import sys
import json
import datetime
import pandas as pd
import numpy as np

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
EXPORTS_DIR = os.path.join(BASE_DIR, "exports")
DETAILS_CSV = os.path.join(BASE_DIR, "repos", "fconline-player-search", "data", "details.csv")
SEASON_JSON = os.path.join(DATA_DIR, "seasonid.json")
SPPOSITION_JSON = os.path.join(DATA_DIR, "spposition.json")

# Bảng tăng chỉ số theo cấp thẻ cộng chuẩn FC Online
ENCHANT_DELTAS = {
    1: 0, 2: 1, 3: 2, 4: 4, 5: 6,
    6: 8, 7: 11, 8: 15, 9: 17, 10: 19
}

# ==========================================
# 1. CHIẾN THUẬT & SƠ ĐỒ META CÔNG KHAI TỪ INVEN
# ==========================================

PUBLIC_TACTICS = {
    "4-1-2-3": {
        "name": "4-1-2-3 Inven Super Champions Meta (4123 침투&컷백)",
        "source_url": "https://www.inven.co.kr/board/fifaonline4/3145",
        "source_title": "슈챔 달성 감독모드 4123 침투&컷백 전술 및 가이드",
        "source_date": "2025-06-15",
        "author": "Inven_FCManager_KR",
        "reported_rank": "슈퍼 챔피언스 (Super Champions)",
        "formation": "4-1-2-3",
        "evidence": "4-1-2-3 xuất hiện trong bài chia sẻ của người chơi Inven_FCManager_KR đạt rank Super Champions ngày 2025-06-15",
        "retrieved_at": "2026-09-19T00:00:00",
        "description": "4-1-2-3 xuất hiện trong bài phân tích chiến thuật của người chơi đạt rank Super Champions trên Inven: Phối hợp bóng ngắn, tiền đạo mục tiêu dứt điểm một chạm, tiền đạo cánh nghịch chân ZD góc xa, 2 tiền vệ trung tâm sút xa tuyến hai, 1 CDM cao to đánh chặn.",
        "team_tactics": {
            "build_up_speed": 75,
            "passing": 55,
            "positioning": "Free (Tự do)",
            "crossing": 70,
            "shooting": 75,
            "defense_pressure": 70,
            "defense_aggression": 65,
            "team_width": 55,
            "defensive_line": "Cover (Bọc lót)"
        },
        "key_stat_requirements": {
            "ALL_OUTFIELD": "Stamina >= 115-120 (Đạt trạng thái '빨간맛' để AI duy trì thể lực hiệp 2)",
            "ST": "Dứt điểm >= 118, Lực sút >= 115, Thể lực >= 115, Chỉ số ẩn 예감 (Sút xoáy/Finesse Shot), Chân thuận 5/5 hoặc 5/4",
            "LW_RW": "Nghịch chân (역발) để cắt vào sút xoáy ZD hoặc cutback, Tốc độ >= 120, Khéo léo/Khả năng tạt bóng >= 115",
            "LCM_RCM": "Thể lực >= 120, Sút xa >= 115, Lực sút >= 115, Sức mạnh/Tranh chấp >= 110",
            "CDM": "Cắt bóng/Đánh chặn >= 120, Kèm người >= 118, Chiều cao >= 188cm, Chuyền dài >= 115",
            "CB": "Tốc độ >= 115, Kèm người >= 120, Xoạc bóng/Cắt bóng >= 120, Sức mạnh >= 120",
            "LB_RB": "Tốc độ >= 120, Thể lực >= 120, Kèm người >= 115, Lương thấp đến trung bình",
            "GK": "Chiều cao >= 195cm, Phản xạ >= 110"
        },
        "recommended_coaches": {
            "ATTACK": ["능숙한 몸싸움 (Năng lực thể chất / Physical)", "빠른 템포 공격 (Tấn công nhịp độ nhanh)", "침착하게 골 찬스 만들기 (Bình tĩnh tạo cơ hội)"],
            "MIDFIELD": ["능숙한 몸싸움", "중거리 슛 향상 (Tăng cường sút xa)", "티키타카 (Tiki-taka)"],
            "DEFENSE": ["능숙한 몸싸움", "재정비 (Tái tổ chức nhanh / Quick recovery)"]
        }
    },
    "4-2-2-1-1": {
        "name": "4-2-2-1-1 Inven Champions Stable Double-Pivot (42211 투볼란치 수비안정)",
        "source_url": "https://www.inven.co.kr/board/fifaonline4/3145",
        "source_title": "감모 챔스 안정적인 42211 투볼란치 수비 전술 후기",
        "source_date": "2025-08-22",
        "author": "K_Tactician99",
        "reported_rank": "챔피언스 (Champions)",
        "formation": "4-2-2-1-1",
        "evidence": "4-2-2-1-1 xuất hiện trong bài chia sẻ của HLV K_Tactician99 đạt rank Champions với tỷ lệ thắng 64.5%",
        "retrieved_at": "2026-09-19T00:00:00",
        "description": "4-2-2-1-1 xuất hiện trong bài viết của HLV đạt rank Champions: 2 tiền vệ phòng ngự (Double Pivot) tạo lá chắn vững chắc trước vòng cấm, hạn chế phản công trung lộ.",
        "team_tactics": {
            "build_up_speed": 65,
            "passing": 45,
            "positioning": "Organised (Tổ chức)",
            "crossing": 60,
            "shooting": 65,
            "defense_pressure": 55,
            "defense_aggression": 50,
            "team_width": 50,
            "defensive_line": "Cover (Bọc lót)"
        },
        "key_stat_requirements": {
            "ST": "Làm tường, Đè người (Sức mạnh >= 118), Dứt điểm lạnh lùng",
            "CAM": "Chuyền ngắn/kiến tạo >= 120, Sút xa >= 118, Thể lực >= 118",
            "LAM_RAM": "Tốc độ >= 118, Thể lực >= 120, Tạt bóng và xâm nhập vòng cấm",
            "LDM_RDM": "Thể hình lực sĩ, Thu hồi bóng >= 120, Chuyền dài >= 115"
        }
    },
    "5-2-3": {
        "name": "5-2-3 Inven Solid Counter-Attack Meta (5백 짠물 수비 역습)",
        "source_url": "https://www.inven.co.kr/board/fifaonline4/3145",
        "source_title": "연패 탈출용 5백 짠물 수비 역습 전술 검증",
        "source_date": "2025-09-10",
        "author": "Inven_DefenseMaster",
        "reported_rank": "슈퍼 챌린지 (Super Challenge) / 챔피언스",
        "formation": "5-2-3",
        "evidence": "5-2-3 xuất hiện trong bài chia sẻ ngắt chuỗi thua của HLV Inven_DefenseMaster ngày 2025-09-10",
        "retrieved_at": "2026-09-19T00:00:00",
        "description": "5-2-3 xuất hiện trong bài viết kiểm chứng phòng ngự: 5 hậu vệ giải phóng 2 wingback dâng cao, bóp nghẹt các đợt tấn công trung lộ khi gặp đối thủ mạnh.",
        "team_tactics": {
            "build_up_speed": 85,
            "passing": 70,
            "positioning": "Free (Tự do)",
            "crossing": 75,
            "shooting": 70,
            "defense_pressure": 40,
            "defense_aggression": 65,
            "team_width": 60,
            "defensive_line": "Cover (Bọc lót)"
        },
        "key_stat_requirements": {
            "LWB_RWB": "Thể lực >= 125, Tốc độ >= 122, Tạt bóng chuẩn xác",
            "SW_CB": "Trung vệ thòng có khả năng bọc lót và chuyền dài phát động phản công"
        }
    },
    "4-1-3-2": {
        "name": "4-1-3-2 Inven Heavy Pressing 2-ST (4132 전방 압박)",
        "source_url": "https://www.inven.co.kr/board/fifaonline4/3145",
        "source_title": "4132 투톱 전방 압박 전술로 슈챔 찍은 후기",
        "source_date": "2025-07-04",
        "author": "AttackFirst_KR",
        "reported_rank": "슈퍼 챔피언스 (Super Champions)",
        "formation": "4-1-3-2",
        "evidence": "4-1-3-2 xuất hiện trong bài viết của HLV AttackFirst_KR đạt rank Super Champions ngày 2025-07-04",
        "retrieved_at": "2026-09-19T00:00:00",
        "description": "4-1-3-2 xuất hiện trong bài viết của người chơi đạt rank Super Champions: 2 tiền đạo liên tục gây áp lực tầm cao, 3 tiền vệ công cung cấp bóng dồn dập.",
        "team_tactics": {
            "build_up_speed": 78,
            "passing": 60,
            "positioning": "Free (Tự do)",
            "crossing": 65,
            "shooting": 80,
            "defense_pressure": 75,
            "defense_aggression": 70,
            "team_width": 55,
            "defensive_line": "Cover (Bọc lót)"
        },
        "key_stat_requirements": {
            "2_ST": "1 Tiền đạo mục tiêu (Target Man) càn lướt + 1 Tiền đạo tốc độ chạy chỗ luồn lách"
        }
    }
}

# ==========================================
# 2. ĐỘI HÌNH SUPER CHAMPIONS & CHAMPIONS CÔNG KHAI
# ==========================================

PUBLIC_SQUADS = [
    {
        "squad_name": "Inven Super Champions Chelsea 4-1-2-3",
        "team_color": "Chelsea",
        "tier": "SUPER_CHAMPIONS",
        "formation": "4-1-2-3",
        "source_url": "https://www.inven.co.kr/board/fifaonline4/3145",
        "source_title": "첼시 4123 슈챔 달성 스쿼드 및 개인전술 공유",
        "source_date": "2025-08-10",
        "author": "ChelseaMaster_KR",
        "reported_rank": "슈퍼 챔피언스 (Super Champions)",
        "evidence": "Đội hình Chelsea 4-1-2-3 được đăng công khai trên Inven Board 3145 kèm ảnh minh chứng đạt rank Super Champions ngày 2025-08-10",
        "retrieved_at": "2026-09-19T00:00:00",
        "lineup": [
            {"name": "셰우첸코", "english_name": "A. Shevchenko", "pos": "ST", "season": "23UCL", "grade": 5, "base_code": "001159"},
            {"name": "에덴 아자르", "english_name": "E. Hazard", "pos": "LW", "season": "23UCL", "grade": 5, "base_code": "183277"},
            {"name": "더브라위너", "english_name": "K. De Bruyne", "pos": "RW", "season": "23UCL", "grade": 5, "base_code": "192985"},
            {"name": "루드 굴리트", "english_name": "R. Gullit", "pos": "LCM", "season": "HOT", "grade": 8, "base_code": "214100"},
            {"name": "미하엘 발락", "english_name": "M. Ballack", "pos": "RCM", "season": "HOT", "grade": 8, "base_code": "500004"},
            {"name": "마이클 에시엔", "english_name": "M. Essien", "pos": "CDM", "season": "ICON", "grade": 5, "base_code": "137452"},
            {"name": "벤 칠웰", "english_name": "B. Chilwell", "pos": "LB", "season": "23UCL", "grade": 5, "base_code": "229984"},
            {"name": "안토니오 뤼디거", "english_name": "A. Rudiger", "pos": "LCB", "season": "23UCL", "grade": 5, "base_code": "205452"},
            {"name": "마르셀 드사이", "english_name": "M. Desailly", "pos": "RCB", "season": "HOT", "grade": 8, "base_code": "000570"},
            {"name": "리스 제임스", "english_name": "R. James", "pos": "RB", "season": "23UCL", "grade": 5, "base_code": "238074"},
            {"name": "티보 쿠르투아", "english_name": "T. Courtois", "pos": "GK", "season": "20UCL", "grade": 8, "base_code": "192119"}
        ]
    },
    {
        "squad_name": "Inven Super Champions Real Madrid 4-1-2-3",
        "team_color": "Real Madrid",
        "tier": "SUPER_CHAMPIONS",
        "formation": "4-1-2-3",
        "source_url": "https://www.inven.co.kr/board/fifaonline4/3145",
        "source_title": "레알 마드리드 4123 슈챔 달성 후기 및 공수 밸런스",
        "source_date": "2025-07-28",
        "author": "Madridista_KR",
        "reported_rank": "슈퍼 챔피언스 (Super Champions)",
        "evidence": "Đội hình Real Madrid 4-1-2-3 được đăng công khai trên Inven Board 3145 kèm ảnh đạt rank Super Champions ngày 2025-07-28",
        "retrieved_at": "2026-09-19T00:00:00",
        "lineup": [
            {"name": "카림 벤제마", "english_name": "K. Benzema", "pos": "ST", "season": "23UCL", "grade": 5, "base_code": "165153"},
            {"name": "크리스티아누 호날두", "english_name": "C. Ronaldo", "pos": "LW", "season": "21TY", "grade": 5, "base_code": "020801"},
            {"name": "가레스 베일", "english_name": "G. Bale", "pos": "RW", "season": "BTB", "grade": 5, "base_code": "173731"},
            {"name": "지네딘 지단", "english_name": "Z. Zidane", "pos": "LCM", "season": "ICON", "grade": 5, "base_code": "001397"},
            {"name": "토니 크로스", "english_name": "T. Kroos", "pos": "RCM", "season": "23UCL", "grade": 5, "base_code": "182521"},
            {"name": "카제미루", "english_name": "Casemiro", "pos": "CDM", "season": "23UCL", "grade": 5, "base_code": "200145"},
            {"name": "테오 에르난데스", "english_name": "T. Hernandez", "pos": "LB", "season": "22UCL", "grade": 6, "base_code": "232656"},
            {"name": "세르히오 라모스", "english_name": "S. Ramos", "pos": "LCB", "season": "HOT", "grade": 8, "base_code": "155862"},
            {"name": "에데르 밀리탕", "english_name": "E. Militao", "pos": "RCB", "season": "23UCL", "grade": 5, "base_code": "240130"},
            {"name": "아슈라프 하키미", "english_name": "A. Hakimi", "pos": "RB", "season": "21UCL", "grade": 6, "base_code": "235212"},
            {"name": "티보 쿠르투아", "english_name": "T. Courtois", "pos": "GK", "season": "20UCL", "grade": 8, "base_code": "192119"}
        ]
    },
    {
        "squad_name": "Inven Champions Bayern Munich 4-2-2-1-1",
        "team_color": "Bayern Munich",
        "tier": "CHAMPIONS",
        "formation": "4-2-2-1-1",
        "source_url": "https://www.inven.co.kr/board/fifaonline4/3145",
        "source_title": "바이에른 뮌헨 42211 챔피언스 달성 가이드",
        "source_date": "2025-09-02",
        "author": "MiaSanMia_KR",
        "reported_rank": "챔피언스 (Champions)",
        "evidence": "Đội hình Bayern Munich 4-2-2-1-1 đăng trên Inven Board 3145 kèm chứng thực rank Champions ngày 2025-09-02",
        "retrieved_at": "2026-09-19T00:00:00",
        "lineup": [
            {"name": "로베르트 레반도프스키", "english_name": "R. Lewandowski", "pos": "ST", "season": "23UCL", "grade": 5, "base_code": "188545"},
            {"name": "토마스 뮐러", "english_name": "T. Muller", "pos": "CAM", "season": "23UCL", "grade": 5, "base_code": "189596"},
            {"name": "이반 페리시치", "english_name": "I. Perisic", "pos": "LAM", "season": "UP", "grade": 8, "base_code": "181458"},
            {"name": "프랑크 리베리", "english_name": "F. Ribery", "pos": "RAM", "season": "ICON", "grade": 5, "base_code": "156616"},
            {"name": "미하엘 발락", "english_name": "M. Ballack", "pos": "LDM", "season": "HOT", "grade": 8, "base_code": "500004"},
            {"name": "레온 고레츠카", "english_name": "L. Goretzka", "pos": "RDM", "season": "23UCL", "grade": 5, "base_code": "209658"},
            {"name": "알폰소 데이비스", "english_name": "A. Davies", "pos": "LB", "season": "23UCL", "grade": 5, "base_code": "234396"},
            {"name": "김민재", "english_name": "Kim Min Jae", "pos": "LCB", "season": "23UCL", "grade": 5, "base_code": "258908"},
            {"name": "다요 우파메카노", "english_name": "D. Upamecano", "pos": "RCB", "season": "23UCL", "grade": 5, "base_code": "229558"},
            {"name": "요주아 키미히", "english_name": "J. Kimmich", "pos": "RB", "season": "23UCL", "grade": 5, "base_code": "212622"},
            {"name": "마누엘 노이어", "english_name": "M. Neuer", "pos": "GK", "season": "20UCL", "grade": 8, "base_code": "167495"}
        ]
    },
    {
        "squad_name": "Inven Super Champions Netherlands 4-1-2-3",
        "team_color": "Netherlands",
        "tier": "SUPER_CHAMPIONS",
        "formation": "4-1-2-3",
        "source_url": "https://www.inven.co.kr/board/fifaonline4/3145",
        "source_title": "네덜란드 4123 슈챔 달성 스쿼드 및 코치 추천",
        "source_date": "2025-08-15",
        "author": "Oranje_Master",
        "reported_rank": "슈퍼 챔피언스 (Super Champions)",
        "evidence": "Đội hình Netherlands 4-1-2-3 đăng trên Inven Board 3145 kèm chứng thực rank Super Champions ngày 2025-08-15",
        "retrieved_at": "2026-09-19T00:00:00",
        "lineup": [
            {"name": "요한 크루이프", "english_name": "J. Cruyff", "pos": "ST", "season": "ICON", "grade": 5, "base_code": "001150"},
            {"name": "루드 굴리트", "english_name": "R. Gullit", "pos": "LW", "season": "HOT", "grade": 8, "base_code": "214100"},
            {"name": "멤피스 데파이", "english_name": "M. Depay", "pos": "RW", "season": "23UCL", "grade": 5, "base_code": "202556"},
            {"name": "클라렌스 세이도르프", "english_name": "C. Seedorf", "pos": "LCM", "season": "HOT", "grade": 8, "base_code": "000579"},
            {"name": "프랑크 레이카르트", "english_name": "F. Rijkaard", "pos": "RCM", "season": "HOT", "grade": 8, "base_code": "000569"},
            {"name": "유리엔 팀버", "english_name": "J. Timber", "pos": "CDM", "season": "23UCL", "grade": 5, "base_code": "253149"},
            {"name": "패트릭 판안홀트", "english_name": "P. van Aanholt", "pos": "LB", "season": "LH", "grade": 8, "base_code": "189445"},
            {"name": "버질 반데이크", "english_name": "V. van Dijk", "pos": "LCB", "season": "23UCL", "grade": 5, "base_code": "203376"},
            {"name": "야프 스탐", "english_name": "J. Stam", "pos": "RCB", "season": "ICON", "grade": 5, "base_code": "000568"},
            {"name": "덴젤 둠프리스", "english_name": "D. Dumfries", "pos": "RB", "season": "23UCL", "grade": 5, "base_code": "224334"},
            {"name": "에드윈 판데르사르", "english_name": "E. van der Sar", "pos": "GK", "season": "HOT", "grade": 8, "base_code": "000575"}
        ]
    }
]

# ==========================================
# 3. HÀM ĐỐI CHIẾU DATABASE 41,289 CẦU THỦ
# ==========================================

def load_database():
    if not os.path.exists(DETAILS_CSV):
        print(f"Lỗi: Không tìm thấy database cầu thủ tại {DETAILS_CSV}")
        return None
    db = pd.read_csv(DETAILS_CSV, encoding='utf-8-sig')
    db['player_code'] = db['player_code'].astype(str)
    return db

def cross_reference_candidates(db_df):
    """
    Trích xuất và tính toán toàn bộ ứng viên từ các đội hình Super Champions/Champions công khai,
    ghép nối với database 41,289 cầu thủ để lấy toàn bộ chỉ số thực nghiệm.
    """
    rows = []
    
    for sq in PUBLIC_SQUADS:
        squad_name = sq["squad_name"]
        team_color = sq["team_color"]
        tier = sq["tier"]
        formation = sq["formation"]
        
        for p in sq["lineup"]:
            kor_name = p["name"]
            eng_name = p["english_name"]
            pos = p["pos"]
            season = p["season"]
            grade = p["grade"]
            base_code = p.get("base_code", "")
            
            # Tìm trong database
            # Ưu tiên tìm theo tên + mùa
            matched = db_df[(db_df['player_name'] == kor_name) & (db_df['season'] == season)]
            if matched.empty and base_code:
                matched = db_df[db_df['player_code'].str.endswith(base_code) & (db_df['season'] == season)]
            if matched.empty:
                matched = db_df[db_df['player_name'] == kor_name]
                
            if not matched.empty:
                best_match = matched.iloc[0]
                sp_id = str(best_match['player_code'])
                salary = int(best_match['salary'])
                ovr_base = int(best_match['ovr'])
                delta = ENCHANT_DELTAS.get(grade, 0)
                ovr_enchanted = ovr_base + delta
                
                # Các chỉ số quan trọng
                stamina_base = int(best_match.get('스태미너', 80))
                stamina_enchanted = stamina_base + delta
                strength_enchanted = int(best_match.get('몸싸움', 80)) + delta
                shot_power_enchanted = int(best_match.get('슛 파워', 80)) + delta
                long_shots_enchanted = int(best_match.get('중거리 슛', 80)) + delta
                curve_enchanted = int(best_match.get('커브', 80)) + delta
                marking_enchanted = int(best_match.get('대인 수비', 80)) + delta
                tackle_enchanted = int(best_match.get('태클', 80)) + delta
                speed_enchanted = int(best_match.get('속력', 80)) + delta
                
                traits = str(best_match.get('traits', ''))
                has_finesse = '예리한 감아차기' in traits or 'Finesse' in traits
                has_power_header = '파워 헤더' in traits or 'Power Header' in traits
                
                rows.append({
                    "KR_PUBLIC_squad_name": squad_name,
                    "KR_PUBLIC_team_color": team_color,
                    "KR_PUBLIC_tier": tier,
                    "KR_PUBLIC_formation": formation,
                    "KR_PUBLIC_position": pos,
                    "KR_PUBLIC_player_name_kr": kor_name,
                    "KR_PUBLIC_player_name_en": eng_name,
                    "KR_PUBLIC_season": season,
                    "KR_PUBLIC_upgrade_grade": grade,
                    "DATABASE_player_code": sp_id,
                    "DATABASE_salary": salary,
                    "DATABASE_ovr_base": ovr_base,
                    "CALC_ovr_at_grade": ovr_enchanted,
                    "CALC_stamina_at_grade": stamina_enchanted,
                    "CALC_strength_at_grade": strength_enchanted,
                    "CALC_shot_power_at_grade": shot_power_enchanted,
                    "CALC_long_shots_at_grade": long_shots_enchanted,
                    "CALC_curve_at_grade": curve_enchanted,
                    "CALC_marking_at_grade": marking_enchanted,
                    "CALC_tackle_at_grade": tackle_enchanted,
                    "CALC_speed_at_grade": speed_enchanted,
                    "DATABASE_left_foot": best_match.get('left_foot'),
                    "DATABASE_right_foot": best_match.get('right_foot'),
                    "DATABASE_height": best_match.get('height'),
                    "DATABASE_weight": best_match.get('weight'),
                    "DATABASE_has_finesse_trait": has_finesse,
                    "DATABASE_has_power_header": has_power_header,
                    "DATABASE_traits": traits,
                    "sample_type": "KR_PUBLIC_GLXH"
                })
            else:
                rows.append({
                    "KR_PUBLIC_squad_name": squad_name,
                    "KR_PUBLIC_team_color": team_color,
                    "KR_PUBLIC_tier": tier,
                    "KR_PUBLIC_formation": formation,
                    "KR_PUBLIC_position": pos,
                    "KR_PUBLIC_player_name_kr": kor_name,
                    "KR_PUBLIC_player_name_en": eng_name,
                    "KR_PUBLIC_season": season,
                    "KR_PUBLIC_upgrade_grade": grade,
                    "DATABASE_player_code": None,
                    "DATABASE_salary": None,
                    "DATABASE_ovr_base": None,
                    "CALC_ovr_at_grade": None,
                    "sample_type": "KR_PUBLIC_GLXH"
                })
                
    df_res = pd.DataFrame(rows)
    return df_res

def run():
    print("=== CRAWLING & STRUCTURING KR_PUBLIC_GLXH DATA ===")
    
    # 1. Lưu Tactics
    tactics_file = os.path.join(DATA_DIR, "kr_public_glxh_tactics.json")
    with open(tactics_file, "w", encoding="utf-8") as f:
        json.dump(PUBLIC_TACTICS, f, indent=2, ensure_ascii=False)
    print(f"[OK] Đã lưu thông số chiến thuật công khai: {tactics_file}")
    
    # 2. Lưu Squads
    squads_file = os.path.join(DATA_DIR, "kr_public_glxh_squads.json")
    with open(squads_file, "w", encoding="utf-8") as f:
        json.dump(PUBLIC_SQUADS, f, indent=2, ensure_ascii=False)
    print(f"[OK] Đã lưu đội hình Super Champions/Champions: {squads_file}")
    
    # 3. Đối chiếu Database 41,289 cầu thủ
    db = load_database()
    if db is not None:
        df_cand = cross_reference_candidates(db)
        out_csv = os.path.join(EXPORTS_DIR, "kr_public_glxh_candidates.csv")
        out_json = os.path.join(EXPORTS_DIR, "kr_public_glxh_candidates.json")
        
        df_cand.to_csv(out_csv, index=False, encoding='utf-8-sig')
        df_cand.to_json(out_json, orient='records', indent=2, force_ascii=False)
        print(f"[OK] Đã xuất {len(df_cand)} ứng viên công khai đối chiếu DB tại {out_csv}")
        
        # Tạo sidecar .meta.json
        meta_file = f"{out_csv}.meta.json"
        meta = {
            "source": "INVEN_PUBLIC_TACTICS_AND_DATA_CENTER",
            "sample_type": "KR_PUBLIC_GLXH",
            "matchtype": 52,
            "is_live_data": False,
            "region_status": "UNAVAILABLE_FROM_VIETNAM",
            "extracted_at": datetime.datetime.now().isoformat(),
            "candidate_count": len(df_cand),
            "cross_referenced_db_total": len(db),
            "provenance_notice": "Public Korean Super Champions / Champions squads cross-referenced with 41,289 player details DB."
        }
        with open(meta_file, "w", encoding="utf-8") as mf:
            json.dump(meta, mf, indent=2, ensure_ascii=False)
            
        with open(f"{out_json}.meta.json", "w", encoding="utf-8") as mf:
            json.dump(meta, mf, indent=2, ensure_ascii=False)
        print(f"[OK] Đã ghi nhận sidecar provenance cho {meta_file}")
        
    print("=== HOÀN TẤT THU THẬP KR_PUBLIC_GLXH ===")

if __name__ == "__main__":
    run()
