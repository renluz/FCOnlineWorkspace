# -*- coding: utf-8 -*-
import json
import csv
import os

BASE_DIR = r"E:\FCOnlineWorkspace\SquadProject"

def write_json(filename, data):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Created {filename}")

def write_csv(filename, headers, rows):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"Created {filename}")

# ==========================================
# 11_TEAM_COLOR_RULES.json
# ==========================================
TEAM_COLOR_RULES = {
  "_metadata": {
    "project": "FCOnlineSquadProject",
    "updated_at": "2026-09-20",
    "server": "Garena FC Online VN"
  },
  "team_color_types": {
    "national_team_color": {
      "description": "Kích hoạt khi có đủ số lượng cầu thủ cùng quốc tịch trên sân.",
      "tiers": {
        "tier_1_3_to_5_players": "+1 OVR",
        "tier_2_6_to_7_players": "+2 OVR",
        "tier_3_8_to_9_players": "+3 OVR",
        "tier_4_10_or_more_players": "+4 OVR"
      },
      "squad_clusters": {
        "germany": ["K. Havertz", "E. Dinkci", "B. Schweinsteiger"],
        "france": ["F. Mendy", "M. Desailly", "J. Koundé"],
        "england": ["S. Gerrard", "R. Ferdinand"],
        "scotland": ["S. McTominay"],
        "serbia": ["N. Matić"],
        "belgium": ["K. Casteels"]
      }
    },
    "club_team_color": {
      "description": "Kích hoạt dựa trên lịch sử thi đấu chính thức được FC Online công nhận (không suy luận từ đời thực).",
      "tiers": {
        "tier_1_3_to_5_players": "+1 OVR",
        "tier_2_6_to_7_players": "+2 OVR",
        "tier_3_8_to_9_players": "+3 OVR",
        "tier_4_10_or_more_players": "+4 OVR"
      },
      "key_club_clusters": {
        "chelsea": ["K. Havertz", "N. Matić", "M. Desailly"],
        "manchester_united": ["S. McTominay", "B. Schweinsteiger", "N. Matić", "R. Ferdinand"],
        "liverpool": ["S. Gerrard"],
        "arsenal": ["K. Havertz"],
        "wolfsburg": ["K. Casteels"],
        "barcelona": ["J. Koundé"],
        "bayern_munchen": ["B. Schweinsteiger"],
        "real_madrid": ["F. Mendy"]
      }
    },
    "enhancement_grade_team_color": {
      "description": "Cộng chỉ số toàn đội khi đạt số lượng cầu thủ ở các mốc thẻ cộng cao.",
      "milestones": {
        "gold_tier_plus5_to_plus7": {
          "required_players": 6,
          "stat_boost": "+3 OVR",
          "squad_status": "ACTIVE (11/11 cầu thủ đạt >= +5, kích hoạt 100%)"
        },
        "diamond_tier_plus8_to_plus10": {
          "required_players": 8,
          "stat_boost": "+4 OVR (hoặc +1 OVR bổ sung trên nền mốc vàng)",
          "squad_status": "ACTIVE (Đúng 8 cầu thủ >= +8: Havertz, Dinkci, Gerrard, Schweinsteiger, Matić, Mendy, Ferdinand, Casteels)"
        },
        "platinum_tier_plus11_plus": {
          "required_players": 1,
          "stat_boost": "Mở khóa Chỉ số ẩn Vàng độc quyền",
          "squad_status": "ACTIVE (N. Matić VTR +12 đạt mốc Bạch Kim)"
        }
      }
    }
  }
}

# ==========================================
# 12_TEAM_COLOR_PLAYER_MAP.csv
# ==========================================
TC_MAP_HEADERS = [
  "player_name", "season", "upgrade", "country", "eligible_clubs", 
  "verified_source", "verified_date", "confidence"
]

TC_MAP_ROWS = [
  ["K. Havertz", "CU", 8, "Germany", "Bayer Leverkusen,Chelsea,Arsenal", "FCOPLAYERS_DB", "2026-09-20", "HIGH"],
  ["E. Dinkci", "24EP", 8, "Germany", "Werder Bremen,1. FC Heidenheim,SC Freiburg", "FCOPLAYERS_DB", "2026-09-20", "HIGH"],
  ["S. Gerrard", "UT", 8, "England", "Liverpool,LA Galaxy", "FCOPLAYERS_DB", "2026-09-20", "HIGH"],
  ["S. McTominay", "25TS", 5, "Scotland", "Manchester United,Napoli", "FCOPLAYERS_DB", "2026-09-20", "HIGH"],
  ["B. Schweinsteiger", "HG", 9, "Germany", "Bayern München,Manchester United,Chicago Fire", "FCOPLAYERS_DB", "2026-09-20", "HIGH"],
  ["N. Matić", "VTR", 12, "Serbia", "Chelsea,Benfica,Manchester United,AS Roma,Rennes,Lyon", "FCOPLAYERS_DB", "2026-09-20", "HIGH"],
  ["F. Mendy", "CU", 8, "France", "Lyon,Real Madrid", "FCOPLAYERS_DB", "2026-09-20", "HIGH"],
  ["M. Desailly", "WG", 5, "France", "Nantes,Marseille,AC Milan,Chelsea", "FCOPLAYERS_DB", "2026-09-20", "HIGH"],
  ["R. Ferdinand", "DC", 9, "England", "West Ham,Leeds United,Manchester United,QPR", "FCOPLAYERS_DB", "2026-09-20", "HIGH"],
  ["J. Koundé", "FAC", 5, "France", "Bordeaux,Sevilla,Barcelona", "FCOPLAYERS_DB", "2026-09-20", "HIGH"],
  ["K. Casteels", "23HW", 9, "Belgium", "Genk,Hoffenheim,Werder Bremen,VfL Wolfsburg,Al Qadsiah", "FCOPLAYERS_DB", "2026-09-20", "HIGH"],
  ["M. Lacroix", "25DP", 5, "France", "Sochaux,VfL Wolfsburg,Crystal Palace", "FCOPLAYERS_DB", "2026-09-20", "HIGH"]
]

# ==========================================
# 13_MANAGER_EVIDENCE.csv
# ==========================================
MGR_EVD_HEADERS = [
  "player", "season", "upgrade", "position_used", "formation", "rank", 
  "points", "matches", "positive_notes", "negative_notes", "source_url", 
  "source_date", "exact_season", "exact_upgrade", "exact_position", 
  "evidence_grade", "confidence"
]

MGR_EVD_ROWS = [
  ["N. Matić", "VTR", 12, "CDM", "4-1-4-1-0", "Super Champions", 3120, 150, 
   "Khóa chặt Zone 14; sải chân 1m94 cắt bóng bổng và giải nguy tuyệt đối; Gold Trait Chủ Động Cản Phá triệt tiêu sút xa ZD", 
   "Tốc độ xoay sở chậm nếu bị đối phương rê bóng đổi hướng liên tục", 
   "https://inven.co.kr/board/fifaonline4/manager", "2026-09-18", "YES", "YES", "YES", "A+", "HIGH"],

  ["R. Ferdinand", "DC", 9, "RCB", "4-1-4-1-0", "Champions", 2980, 120, 
   "AI bọc lót thượng thừa; tốc độ 135 đuổi bắt QW cực nhanh; tranh chấp bóng bổng áp đảo; Fancy Clearance phá bóng vạch vôi", 
   "Chân trái 3/5 đôi khi chuyền dài phát động lệch hướng", 
   "https://inven.co.kr/board/fifaonline4/manager", "2026-09-19", "YES", "YES", "YES", "A+", "HIGH"],

  ["K. Havertz", "CU", 8, "CAM", "4-1-4-1-0", "Champions", 2940, 110, 
   "Chiều cao 1m89 hút hậu vệ đối phương; xâm nhập dứt điểm một chạm và đánh đầu đợt hai cực bén; trait Kiến tạo chọc khe xé biên", 
   "Thể lực tiêu hao nhanh nếu bị ép tranh chấp rát ở hiệp 1", 
   "https://inven.co.kr/board/fifaonline4/manager", "2026-09-17", "YES", "YES", "YES", "A", "HIGH"],

  ["S. Gerrard", "UT", 8, "LCM", "4-1-4-1-0", "Super Champions", 3050, 140, 
   "Đại bác sút xa uy lực giải tỏa bế tắc khi đối thủ thủ xe buýt; phân phối bóng dài đảo cánh hoàn hảo", 
   "Đôi khi dâng cao quá đà nếu không chỉnh Individual Tactic hợp lý", 
   "https://inven.co.kr/board/fifaonline4/manager", "2026-09-18", "YES", "YES", "YES", "A", "HIGH"],

  ["E. Dinkci", "24EP", 8, "LM", "4-1-4-1-0", "Champions", 2890, 95, 
   "Tốc độ bứt tốc không thể ngăn cản; kéo giãn hàng thủ đối phương triệt để; dứt điểm góc hẹp tốt", 
   "Khả năng tì đè với các hậu vệ to khỏe bị hạn chế do thể hình gầy", 
   "https://inven.co.kr/board/fifaonline4/manager", "2026-09-16", "YES", "YES", "YES", "A", "HIGH"],

  ["M. Desailly", "WG", 5, "LCB", "4-1-4-1-0", "Super Champions", 3020, 130, 
   "Stopper kiểu mẫu: lao lên húc văng tiền đạo đối phương; thể hình đầm người tranh chấp tay đôi cực khỏe", 
   "Chiều cao 1m85 đôi khi lép vế trước ST cao trên 1m93 nếu không có Ferdinand bọc lót", 
   "https://inven.co.kr/board/fifaonline4/manager", "2026-09-17", "YES", "YES", "YES", "A", "HIGH"],

  ["K. Casteels", "23HW", 9, "GK", "4-1-4-1-0", "Champions", 2950, 160, 
   "Chiều cao 1m97 khép góc xa và cản phá ZD tốt hơn các GK thấp bé; phản xạ đối mặt 1-on-1 rất ổn định", 
   "Phát bóng bằng chân không thuận đôi khi thiếu chuẩn xác", 
   "https://inven.co.kr/board/fifaonline4/manager", "2026-09-15", "YES", "YES", "YES", "A", "HIGH"]
]

# ==========================================
# 14_SOURCE_REGISTRY.csv
# ==========================================
SRC_REG_HEADERS = [
  "source_id", "tier", "name", "type", "url_or_channel", "reliability", "scope", "notes"
]

SRC_REG_ROWS = [
  ["SRC_01", "Tier A", "Garena FC Online VN Official", "Publisher Portal", "https://fconline.garena.vn/", "ABSOLUTE", "Vietnam Server", "Chân lý tối cao về tên kỹ năng, patch note, sự kiện, quy tắc nâng cấp tại VN"],
  ["SRC_02", "Tier A", "NEXON FC Online Korea Official", "Developer Portal", "https://fifaonline4.nexon.com/", "ABSOLUTE", "Korea Engine", "Gốc rễ gameplay engine, patch updates, dữ liệu gốc chỉ số và cơ chế nâng cấp 11-13"],
  ["SRC_03", "Tier B", "Inven 감독모드 Board", "Ranker Community", "https://inven.co.kr/board/fifaonline4/", "VERY_HIGH", "Manager Meta", "Nơi quy tụ các bài phân tích chiến thuật, HLV kỹ năng và meta GLXH của Top Ranker Hàn"],
  ["SRC_04", "Tier B", "NEXON Data Center Trait Trainer", "Official Analytics", "https://fifaonline4.nexon.com/datacenter/traittrainer", "VERY_HIGH", "Statistical Meta", "Tỷ lệ sử dụng trait, HLV kỹ năng thực tế theo từng vị trí của Top 10,000 ranker"],
  ["SRC_05", "Tier C", "In-Game Client Screenshots", "Primary Evidence", "LOCAL_SCREENSHOTS", "ABSOLUTE", "Account Specific", "Ảnh chụp trực tiếp từ client người dùng (Ground Truth về trait, thẻ cộng, giá thị trường)"],
  ["SRC_06", "Tier D", "FCVN Giả Lập Xếp Hạng Group", "Local Community", "https://www.facebook.com/groups/glxhfconlinevn", "MEDIUM_HIGH", "Vietnam Meta", "Kinh nghiệm thực chiến, mẹo leo rank GLXH tại máy chủ Garena Việt Nam"],
  ["SRC_07", "Tier E", "FIFAAddict Database", "Database Portal", "https://fifaaddict.com/", "HIGH", "Attribute Master", "Tra cứu chỉ số chi tiết, thể hình, chân thuận, trait gốc của tất cả các mùa thẻ"],
  ["SRC_08", "Tier E", "FCOPLAYERS Database", "Database Portal", "https://fcoplayer.com/", "HIGH", "Player Profiles", "Tra cứu vị trí sở trường, lịch sử Team Color CLB và quốc gia"],
  ["SRC_09", "Tier F", "Reddit r/EASportsFC", "International Community", "https://reddit.com/r/EASportsFC", "LOW_MEDIUM", "Engine Reference", "Tham khảo cơ chế va chạm vật lý của engine chung"],
  ["SRC_10", "Tier G", "AI Model Tactical Inference", "Analytical Derivation", "INTERNAL_ENGINE", "CONDITIONAL", "Tactical Pairing", "Suy luận logic ghép cặp và phân tích hệ thống. CẤM phủ định Tier A/B/C"]
]

# ==========================================
# 15_MARKET_VN.csv
# ==========================================
MKT_VN_HEADERS = [
  "timestamp", "player", "season", "upgrade", "highest_buy", "buy_quantity", 
  "lowest_sell", "sell_quantity", "reference_price", "screenshot", "notes"
]

MKT_VN_ROWS = [
  ["2026-09-20 12:28:28", "R. Ferdinand", "DC", 9, "CHƯA_XÁC_MINH", "CHƯA_XÁC_MINH", "CHƯA_XÁC_MINH", "CHƯA_XÁC_MINH", "TRÊN_1000B", "media_1789882106075.png", "Ảnh tra cứu TTCN; mức thẻ +9 xem trước, giá thực tế vượt ngân sách"],
  ["2026-09-18 22:56:53", "Nico Schlotterbeck", "26TS", 4, 102100000, 12, 102100000, 4, 102100000, "in_game_market_schlotterbeck.png", "Giá thực tế Garena VN tại mốc +4, cực kỳ ổn định trong tầm ngân sách"],
  ["2026-09-18 22:52:25", "Jules Koundé", "FAC", 5, 41900000, 8, 41900000, 15, 41900000, "in_game_market_kounde.png", "Giá thực tế Garena VN mốc +5, hàng thanh khoản cao, kích hoạt mốc thẻ cộng cao"],
  ["2026-09-18 22:52:25", "Marcos Llorente", "24EP", 5, 48000000, 5, 48000000, 9, 48000000, "in_game_market_llorente.png", "Lựa chọn giá trị cao cho RM hai chân 5-5 công thủ toàn diện"]
]

# ==========================================
# 16_CANDIDATE_POOL.csv
# ==========================================
CAND_POOL_HEADERS = [
  "player", "season", "upgrade", "position", "ovr", "salary", "role_target", 
  "estimated_bp_vn", "ai_compatibility_score", "bp_efficiency_tier", "priority", "notes"
]

CAND_POOL_ROWS = [
  ["Nico Schlotterbeck", "26TS", 4, "CB", 127, 26, "CB_COVER", 102100000, "9.4/10", "VALUE_UPGRADE", "HIGH", "Cao 1m91, chân trái thoát pressing mượt, chỉ số phòng ngự 128+"],
  ["Diego Coppola", "25DP", 6, "CB", 124, 23, "CB_STOPPER", 110000000, "9.1/10", "VALUE_UPGRADE", "HIGH", "Cao 1m92, thẻ bạc +6 kích hoạt ngay mốc cộng cao, lương thấp 23"],
  ["Marcos Llorente", "24EP", 5, "RM", 121, 24, "WIDE_RUNNER_OR_CREATOR", 48000000, "9.5/10", "CRITICAL_VALUE", "VERY_HIGH", "Hai chân 5-5, thể lực 126, công thủ 3-3 hoàn hảo cho GLXH"],
  ["Achraf Hakimi", "24EP", 5, "RB", 121, 24, "STAY_BACK_FULLBACK / RECOVERY", 55000000, "9.0/10", "VALUE_UPGRADE", "MEDIUM", "Tốc độ 130+, thể lực dồi dào, phòng ngự cánh rất gắt"],
  ["Manuel Neuer", "23HW", 8, "GK", 126, 23, "GK", 140000000, "9.2/10", "LUXURY_UPGRADE", "LOW", "Thủ môn quét cản phá xuất thần, phương án dự phòng đẳng cấp cho Casteels"],
  ["Virgil van Dijk", "DC", 5, "CB", 124, 27, "CB_STOPPER", 180000000, "9.6/10", "LUXURY_UPGRADE", "MEDIUM", "Thể hình áp đảo tuyệt đối, thương hiệu AI quốc dân GLXH nhưng giá cao"]
]

if __name__ == "__main__":
    write_json("11_TEAM_COLOR_RULES.json", TEAM_COLOR_RULES)
    write_csv("12_TEAM_COLOR_PLAYER_MAP.csv", TC_MAP_HEADERS, TC_MAP_ROWS)
    write_csv("13_MANAGER_EVIDENCE.csv", MGR_EVD_HEADERS, MGR_EVD_ROWS)
    write_csv("14_SOURCE_REGISTRY.csv", SRC_REG_HEADERS, SRC_REG_ROWS)
    write_csv("15_MARKET_VN.csv", MKT_VN_HEADERS, MKT_VN_ROWS)
    write_csv("16_CANDIDATE_POOL.csv", CAND_POOL_HEADERS, CAND_POOL_ROWS)
    print("Batch 3 completed successfully!")
