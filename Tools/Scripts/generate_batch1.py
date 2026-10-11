# -*- coding: utf-8 -*-
import json
import csv
import os

BASE_DIR = r"E:\FCOnlineWorkspace\SquadProject"

def write_text(filename, content):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created {filename}")

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
# 00_README.md
# ==========================================
README_CONTENT = """# ⚽ FCOnlineSquadProject: Persistent Knowledge Base & Squad Decision Engine

> **Máy chủ:** Garena FC Online Việt Nam  
> **Phiên bản tri thức:** 1.0.0 (Tháng 09/2026 - Gameplay 12th / Cập nhật mùa hè 2026)  
> **Chế độ trọng tâm:** Giả Lập Xếp Hạng (GLXH / Manager Mode)  
> **Sơ đồ vận hành baseline:** `4-1-4-1-0 / Zero-ST`  
> **Vị trí lưu trữ:** `E:\\FCOnlineWorkspace\\SquadProject\\`

---

## 1. 🎯 Mục Đích Dự Án
Dự án **FCOnlineSquadProject** được xây dựng nhằm tạo ra một **Cơ sở tri thức phân tán, bền vững (Decentralized Project Memory)** phục vụ lâu dài cho AI Assistant (ChatGPT, Gemini, Claude) và huấn luyện viên:
1. **Không sửa file game:** Chỉ lưu trữ tri thức phân tích, nghiên cứu, cấu hình và lịch sử thực nghiệm.
2. **Loại bỏ hiện tượng ảo giác (Hallucination):** Dữ liệu được xác thực nghiêm ngặt theo phân cấp nguồn (Tier A đến Tier G).
3. **Chống trùng lặp & nhầm lẫn:** Phân biệt tuyệt đối theo nguyên tắc **Exact-Card** (Tên + Mùa thẻ + Mức cộng).
4. **Tối ưu hóa kinh tế (BP Efficiency):** Xây dựng chiến lược đầu tư tích lũy BP dài hạn, từ chối các nâng cấp hào nhoáng nhưng không mang lại hiệu quả AI trong GLXH.

---

## 2. 🗺️ Bản Đồ Cấu Trúc Dự Án (23 Files Core)

| Tệp tin | Định dạng | Chức năng chính |
| :--- | :---: | :--- |
| `00_README.md` | Markdown | Tổng quan kiến trúc dự án và chỉ dẫn truy xuất tri thức. |
| `01_PROJECT_RULES.md` | Markdown | Toàn bộ quy chuẩn kỹ thuật, bảo vệ dữ liệu gốc và chính sách nghiêm ngặt. |
| `02_CURRENT_SQUAD.json` | JSON | Đội hình chính thức 11 cầu thủ (Starting XI) và phân bổ cấp độ thẻ. |
| `03_CURRENT_TACTICS.json` | JSON | Thiết lập Chiến thuật đội và Chiến thuật đơn sơ đồ 4-1-4-1-0. |
| `04_PLAYER_CONFIGS.json` | JSON | Cấu hình chuyên sâu từng cầu thủ: Archetype, Trait gốc, Trait trang bị (+5, +8, +11). |
| `05_PLAYER_CARDS_MASTER.csv` | CSV | Sổ bộ danh mục toàn bộ thẻ cầu thủ master với chỉ số và thuộc tính thể hình. |
| `06_ROLE_PROFILES.json` | JSON | Đặc tả 11 vai trò chiến thuật: Nhiệm vụ, hành vi mong muốn và hành vi cấm kỵ. |
| `07_NORMAL_TRAITS_VI.json` | JSON | Bảng danh mục **23 Chỉ số ẩn thường** (Mốc +5) xác minh từ client VN. |
| `08_SKILL_COACHES_VI.json` | JSON | Bảng danh mục **41 HLV kỹ năng** (Mốc +8) xác minh từ client VN. |
| `09_GOLD_TRAITS_VI.json` | JSON | Bảng danh mục **14 Chỉ số ẩn vàng** (Mốc +11) xác minh từ client VN. |
| `10_UPGRADE_RULES.json` | JSON | Cơ chế mở khóa mốc thẻ, sơ đồ 3 slot UI và quy tắc thẻ đặc biệt. |
| `11_TEAM_COLOR_RULES.json` | JSON | Quy tắc cộng chỉ số Team Color Quốc gia, CLB và Team Color Nâng cấp. |
| `12_TEAM_COLOR_PLAYER_MAP.csv` | CSV | Bản đồ liên kết cầu thủ với các Team Color hợp lệ (Đức, Pháp, MU, Chelsea...). |
| `13_MANAGER_EVIDENCE.csv` | CSV | Kho dữ liệu thực nghiệm thi đấu GLXH được phân cấp độ tin cậy từ A+ đến E. |
| `14_SOURCE_REGISTRY.csv` | CSV | Sổ bộ phân cấp nguồn tin (Tier A đến Tier G). |
| `15_MARKET_VN.csv` | CSV | Lịch sử giá giao dịch thị trường chuyển nhượng Garena Việt Nam. |
| `16_CANDIDATE_POOL.csv` | CSV | Danh sách trinh sát cầu thủ tiềm năng / phương án dự phòng. |
| `17_DECISION_RULES.md` | Markdown | Bộ luật logic IF/THEN/PENALTY/BONUS cho mua bán và ghép cặp cầu thủ. |
| `18_MATCH_TEST_LOG.csv` | CSV | Nhật ký A/B testing hiệu năng trận đấu giả lập. |
| `19_SCREENSHOT_INDEX.csv` | CSV | Sổ mục lục định danh và trích xuất thông tin ảnh chụp màn hình client. |
| `20_PATCH_CHANGELOG.md` | Markdown | Lịch sử thay đổi cơ chế gameplay qua các bản cập nhật. |
| `21_AUDIT_LOG.md` | Markdown | Nhật ký kiểm toán tri thức và rà soát tính toàn vẹn dữ liệu. |
| `22_SYSTEM_SYNERGY.md` | Markdown | Phân tích tính liên kết hệ thống, các tam giác phối hợp và chuyển trạng thái. |
| `PROJECT_STATUS.md` | Markdown | Báo cáo kiểm toán tổng thể tình trạng hoàn thiện của dự án. |

---

## 3. 🧠 Hướng Dẫn Dành Cho AI Assistant (LLM Prompting Protocol)
Khi nhận câu hỏi từ người dùng về build đội hình hoặc mua bán cầu thủ:
1. Đọc ngay `02_CURRENT_SQUAD.json` và `04_PLAYER_CONFIGS.json` để nắm tình trạng đội hình hiện tại mà không cần hỏi lại.
2. Tra cứu `17_DECISION_RULES.md` trước khi đưa ra bất kỳ đề xuất chuyển nhượng hay ghép cặp CB/CM nào.
3. Sử dụng đúng tên tiếng Việt chính thức trong `07_NORMAL_TRAITS_VI.json`, `08_SKILL_COACHES_VI.json`, `09_GOLD_TRAITS_VI.json`.
4. Không đề xuất tiêu quá 30% quỹ BP dự trữ nếu không phải là `Critical Upgrade`.
"""

# ==========================================
# 01_PROJECT_RULES.md
# ==========================================
PROJECT_RULES_CONTENT = """# 🛡️ QUY TẮC CỐT LÕI CỦA DỰ ÁN (PROJECT DIRECTIVES)

Tài liệu này thiết lập các nguyên tắc bất biến trong việc xử lý dữ liệu, phân tích chiến thuật và ra quyết định chuyển nhượng trong FC Online Giả Lập Xếp Hạng.

---

## 1. 🛡️ AN TOÀN DỮ LIỆU & NGUYÊN TẮC KHÔNG CAN THIỆP GAME (SAFE PRACTICE)
* **Tuyệt đối không can thiệp game:** Dự án chỉ là không gian phân tích tri thức, thống kê dữ liệu và lập kế hoạch chiến thuật bên ngoài. Không tạo file lạ trong thư mục cài game, không can thiệp bộ nhớ RAM, không can thiệp client FC Online.
* **Mã hóa chuẩn UTF-8 No BOM:** Mọi file dữ liệu văn bản, JSON và CSV bắt buộc phải được lưu ở định dạng UTF-8 No BOM để tương thích hoàn toàn với các công cụ lập trình trên Windows.

---

## 2. 📇 NGUYÊN TẮC EXACT-CARD (CHÍNH SÁCH ĐỊNH DANH ĐỘC NHẤT)
Mọi dữ liệu cầu thủ trong dự án phải được phân biệt rành mạch theo bộ ba:
`[Tên cầu thủ] + [Mùa thẻ] + [Mức thẻ cộng]`

* **Không suy diễn chéo mùa (No Cross-Season Extrapolation):**
  * `R. Ferdinand DC +9` $\neq$ `R. Ferdinand DC +8` (khác nhau về mốc chỉ số ngưỡng và mở slot).
  * `R. Ferdinand DC +9` $\neq$ `R. Ferdinand WB +8` $\neq$ `R. Ferdinand ICON +5` (hoàn toàn khác biệt về AI ẩn, thể hình chi tiết và đặc tính vận hành).
  * `N. Matić VTR +12` $\neq$ `N. Matić RTN +8`.
* **Cấm gộp chung:** Không bao giờ phân tích theo kiểu "Ferdinand nói chung" hay "Matić nói chung".

---

## 3. ⚖️ PHÂN CẤP NGUỒN TRI THỨC (EVIDENCE HIERARCHY)
Khi có sự mâu thuẫn thông tin giữa các nguồn, tuân thủ nghiêm ngặt theo thứ bậc ưu tiên từ trên xuống dưới:

* **Tier A (Chân lý tối cao):** Garena FC Online VN Official / NEXON Official Patch Notes & Announcements.
* **Tier B (Thực nghiệm đỉnh cao):** Dữ liệu Top Ranker Giả Lập Xếp Hạng NEXON Hàn Quốc / Thảo luận chuyên sâu trên Inven 감독모드.
* **Tier C (Thực nghiệm trực tiếp):** Bằng chứng Exact Season + Exact Card từ các trận đấu GLXH đã kiểm chứng.
* **Tier D (Cộng đồng uy tín):** FC-Info / Group Giả Lập Xếp Hạng Garena VN / Kinh nghiệm cộng đồng GLXH Việt Nam.
* **Tier E (Cơ sở dữ liệu thống kê):** FIFAAddict / FCOPlayers (Dùng để tra cứu chỉ số nền, thể hình, trait gốc).
* **Tier F (Cộng đồng quốc tế tham khảo):** Reddit r/EASportsFC / FIFA Online subs.
* **Tier G (Suy luận logic của Model):** Suy luận logic nội tại của AI.  
  ⚠️ **LUẬT THÉP:** Tuyệt đối không dùng Tier G (suy luận mô hình) để phủ định hoặc ghi đè thông tin từ Tier A, B hoặc C.

---

## 4. 🏷️ CHUẨN MỰC BẢN ĐỊA HÓA CHỈ SỐ ẨN & KỸ NĂNG (LOCALIZATION)
* **Thứ tự ưu tiên gọi tên:**
  `Client FC Online VN thực tế` > `Trang chủ Garena VN` > `Thuật ngữ cộng đồng VN phổ biến` > `Dịch thô EN/KR`.
* **Cấm tự dịch tùy tiện:** Nếu một trait hoặc kỹ năng đã có tên hiển thị chính thức trong game (ví dụ: `Chủ Động Cản Phá`, `Siêu cản phá`, `Khả năng tắc bóng`), bắt buộc phải dùng đúng cụm từ đó.
* **Quy tắc nhãn `(Đã chọn)`:** Khi thấy nhãn này, hiểu rằng trait đó đã có sẵn trên card gốc hoặc đã được trang bị trước đó, không phải trait mới đang được chọn thêm.

---

## 5. 💰 CHÍNH SÁCH KINH TẾ & TÍCH LŨY BP DÀI HẠN (BP ECONOMY POLICY)
Huấn luyện viên có mục tiêu **tích lũy BP bền vững lâu dài**, tuyệt đối không khuyến nghị tiêu hết ngân sách mỗi khi tích lũy được vài trăm triệu hoặc vài tỷ BP.
* **Phân loại nâng cấp:**
  1. `Critical Upgrade (Nâng cấp sống còn):` Thay thế mắt xích bị thủng nghiêm trọng trong hệ thống (ví dụ: CB quá thấp bé, CDM không giữ vị trí).
  2. `Value Upgrade (Nâng cấp giá trị cao):` Nâng cấp mang lại bước nhảy vọt về AI và kích hoạt mốc thẻ/Team color với chi phí hợp lý.
  3. `Luxury Upgrade (Nâng cấp xa xỉ):` Thẻ cộng cao của các mùa quá đắt đỏ, chỉ số tăng nhẹ nhưng giá gấp 5-10 lần thẻ tiêu chuẩn $\rightarrow$ **Khuyến nghị trì hoãn**.
  4. `Team Color-only Upgrade:` Nâng cấp chỉ để lấy thêm 1 điểm chỉ số Team color $\rightarrow$ Cân nhắc kỹ chi phí/lợi ích.
* **Quy tắc ngân sách:** Luôn giữ lại ít nhất **40% – 50% quỹ BP dự phòng** sau mỗi đợt mua sắm.

---

## 6. 🔄 CHÍNH SÁCH CẬP NHẬT PATCH (PATCH ROLLOVER)
Khi FC Online ra mắt bản cập nhật Gameplay Patch mới (ví dụ Next Field mới):
* Không xóa dữ liệu và phân tích cũ.
* Đánh dấu toàn bộ dữ liệu bị ảnh hưởng bởi patch cũ bằng tag `OUTDATED_PATCH`.
* Ghi nhận sự thay đổi vào `20_PATCH_CHANGELOG.md`.
"""

# ==========================================
# 02_CURRENT_SQUAD.json
# ==========================================
CURRENT_SQUAD_DATA = {
  "_metadata": {
    "project": "FCOnlineSquadProject",
    "updated_at": "2026-09-20",
    "server": "VN_GARENA",
    "notes": "Đội hình chính thức 11 cầu thủ GLXH baseline. 8 cầu thủ đạt mốc >= +8."
  },
  "formation": "4-1-4-1-0",
  "formation_style": "zero-ST / 5 Midfielders",
  "tier_summary": {
    "diamond_tier_plus8_or_more": 8,
    "gold_silver_tier_plus5_to_plus7": 3,
    "below_plus5": 0,
    "team_color_upgrade_status": "Kích hoạt đồng thời Team Color Kim Cương (8 thẻ >= +8) và Team Color Vàng (11 thẻ >= +5)"
  },
  "starting_xi": [
    {
      "slot": "CAM",
      "player_name": "K. Havertz",
      "season": "CU",
      "grade": 8,
      "tier": "Kim Cương",
      "role_archetype": "CAM_CONNECTOR / FALSE_9",
      "status": "starter_confirmed"
    },
    {
      "slot": "LM",
      "player_name": "E. Dinkci",
      "season": "24EP",
      "grade": 8,
      "tier": "Kim Cương",
      "role_archetype": "WIDE_RUNNER",
      "status": "starter_confirmed"
    },
    {
      "slot": "LCM",
      "player_name": "S. Gerrard",
      "season": "UT",
      "grade": 8,
      "tier": "Kim Cương",
      "role_archetype": "CM_PROGRESSOR / SECOND_WAVE",
      "status": "starter_confirmed"
    },
    {
      "slot": "RCM",
      "player_name": "S. McTominay",
      "season": "25TS",
      "grade": 5,
      "tier": "Vàng / Bạc",
      "role_archetype": "BOX_TO_BOX_CM",
      "status": "starter_confirmed"
    },
    {
      "slot": "RM",
      "player_name": "B. Schweinsteiger",
      "season": "HG",
      "grade": 9,
      "tier": "Kim Cương",
      "role_archetype": "WIDE_CREATOR",
      "status": "starter_confirmed"
    },
    {
      "slot": "CDM",
      "player_name": "N. Matić",
      "season": "VTR",
      "grade": 12,
      "tier": "Bạch Kim",
      "role_archetype": "ANCHOR_CDM",
      "status": "starter_confirmed",
      "verified_gold_trait": "Chủ Động Cản Phá"
    },
    {
      "slot": "LB",
      "player_name": "F. Mendy",
      "season": "CU",
      "grade": 8,
      "tier": "Kim Cương",
      "role_archetype": "STAY_BACK_FULLBACK",
      "status": "starter_confirmed"
    },
    {
      "slot": "LCB",
      "player_name": "M. Desailly",
      "season": "WG",
      "grade": 5,
      "tier": "Vàng / Bạc",
      "role_archetype": "CB_STOPPER",
      "status": "starter_confirmed"
    },
    {
      "slot": "RCB",
      "player_name": "R. Ferdinand",
      "season": "DC",
      "grade": 9,
      "tier": "Kim Cương",
      "role_archetype": "CB_COVER",
      "status": "starter_confirmed"
    },
    {
      "slot": "RB",
      "player_name": "J. Koundé",
      "season": "FAC",
      "grade": 5,
      "tier": "Vàng / Bạc",
      "role_archetype": "STAY_BACK_FULLBACK / RECOVERY",
      "status": "starter_confirmed"
    },
    {
      "slot": "GK",
      "player_name": "K. Casteels",
      "season": "23HW",
      "grade": 9,
      "tier": "Kim Cương",
      "role_archetype": "GK",
      "status": "starter_confirmed"
    }
  ],
  "bench_and_reserves": [
    {
      "player_name": "M. Lacroix",
      "season": "25DP",
      "grade": 5,
      "role": "CB backup",
      "note": "Đã bị thay khỏi đội hình xuất phát chính, lưu trữ dạng dự bị / cựu cầu thủ"
    }
  ]
}

# ==========================================
# 03_CURRENT_TACTICS.json
# ==========================================
CURRENT_TACTICS_DATA = {
  "_metadata": {
    "project": "FCOnlineSquadProject",
    "updated_at": "2026-09-20",
    "formation": "4-1-4-1-0",
    "source": "USER_BASELINE_CONFIRMED"
  },
  "team_tactic": {
    "defense": {
      "tactic_style": "Cân bằng",
      "width": 5,
      "depth": 4,
      "notes": "Độ sâu 4 hạn chế tối đa khoảng trống sau lưng trung vệ; cự ly 5 duy trì cự ly phòng ngự tiêu chuẩn chống chọc khe bổng QW."
    },
    "offense": {
      "build_up_style": "Cân bằng",
      "chance_creation_style": "Chuyền dài",
      "attack_width": 6,
      "players_in_box": 5,
      "corners": 2,
      "free_kicks": 2,
      "tendency": "Chung",
      "notes": "Chuyền dài kích hoạt AI chạy chỗ xuyên tuyến cho 2 cánh và tiền vệ công; 5 cầu thủ tràn vào vòng cấm tận dụng các đường chuyền hai (second-wave)."
    }
  },
  "individual_tactics": {
    "CAM": {
      "slot": "CAM",
      "player": "K. Havertz CU +8",
      "attack_runs": "Tham gia tấn công khi có cơ hội / Tự do di chuyển",
      "interceptions": "Bình thường",
      "defensive_support": "Hỗ trợ phòng ngự cơ bản",
      "tactical_role": "Kết nối bóng trung lộ và xâm nhập dứt điểm bước 2"
    },
    "LM": {
      "slot": "LM",
      "player": "E. Dinkci 24EP +8",
      "chance_creation": "Bám biên",
      "support_runs": "Xâm nhập vòng cấm",
      "defensive_support": "Hỗ trợ phòng ngự khi cần",
      "interceptions": "Bình thường"
    },
    "RM": {
      "slot": "RM",
      "player": "B. Schweinsteiger HG +9",
      "chance_creation": "Cắt vào trong / Tạo cơ hội",
      "support_runs": "Chờ đón bóng ở rìa vòng cấm",
      "defensive_support": "Hỗ trợ phòng ngự tích cực",
      "interceptions": "Bình thường"
    },
    "LCM": {
      "slot": "LCM",
      "player": "S. Gerrard UT +8",
      "attack_support": "Tham gia tấn công rìa vòng cấm",
      "interceptions": "Cắt bóng chủ động",
      "cross_support": "Chờ bóng tuyến hai để sút xa",
      "tactical_role": "Trạm sút xa uy lực và điều tiết bóng"
    },
    "RCM": {
      "slot": "RCM",
      "player": "S. McTominay 25TS +5",
      "attack_support": "Tấn công cân bằng",
      "interceptions": "Áp sát quyết liệt",
      "cross_support": "Xâm nhập tranh chấp bóng hai",
      "tactical_role": "Máy quét thể lực và đè bật tuyến giữa đối phương"
    },
    "CDM": {
      "slot": "CDM",
      "player": "N. Matić VTR +12",
      "attack_support": "Ở lại phía sau khi tấn công (Stay Back)",
      "interceptions": "Cắt bóng chủ động",
      "defensive_position": "Giữ vị trí mỏ neo (Anchor)",
      "tactical_role": "Khóa chặt Zone 14, không dâng cao quá nửa sân"
    },
    "LB": {
      "slot": "LB",
      "player": "F. Mendy CU +8",
      "attack_runs": "Ở lại phía sau khi tấn công (Stay Back)",
      "interceptions": "Bình thường",
      "tactical_role": "Bịt kín hành lang cánh trái, dùng tốc độ khóa winger đối phương"
    },
    "RB": {
      "slot": "RB",
      "player": "J. Koundé FAC +5",
      "attack_runs": "Ở lại phía sau khi tấn công (Stay Back)",
      "interceptions": "Bình thường",
      "tactical_role": "Đá như một hậu vệ thứ ba (Inverted/Third CB), khóa chặt biên phải"
    },
    "LCB": {
      "slot": "LCB",
      "player": "M. Desailly WG +5",
      "interceptions": "Quyết đoán / Tắc bóng chủ động",
      "tactical_role": "Stopper: Chủ động dập bóng và đè bật tiền đạo đối phương"
    },
    "RCB": {
      "slot": "RCB",
      "player": "R. Ferdinand DC +9",
      "interceptions": "Bình thường / Bọc lót",
      "tactical_role": "Cover: Giữ cự ly, bọc lót phía sau cho Desailly, chống bóng bổng"
    },
    "GK": {
      "slot": "GK",
      "player": "K. Casteels 23HW +9",
      "crosses": "Cản phá tạt bóng",
      "sweeper": "Thủ môn quét cơ bản",
      "tactical_role": "Khép góc, tận dụng chiều cao 1m97 cản phá ZD và bóng bổng"
    }
  }
}

# ==========================================
# 04_PLAYER_CONFIGS.json
# ==========================================
PLAYER_CONFIGS_DATA = {
  "_metadata": {
    "project": "FCOnlineSquadProject",
    "updated_at": "2026-09-20",
    "notes": "Cấu hình chi tiết trang bị kỹ năng 3 mốc (+5, +8, +11) cho từng cầu thủ"
  },
  "players": [
    {
      "slot": "CAM",
      "player_name": "K. Havertz",
      "season": "CU",
      "grade": 8,
      "archetype": "CAM_CONNECTOR / FALSE_9",
      "innate_traits": ["Tinh tế", "Đánh đầu mạnh", "Bấm bóng"],
      "trait_slots": {
        "slot_1_plus8_coach": {
          "equipped": "Khả năng khéo léo",
          "status": "confirmed_applied"
        },
        "slot_2_plus11_gold": {
          "equipped": None,
          "status": "locked_requires_plus11"
        },
        "slot_3_plus5_normal": {
          "equipped": "Kiến tạo",
          "status": "confirmed_applied"
        }
      }
    },
    {
      "slot": "LM",
      "player_name": "E. Dinkci",
      "season": "24EP",
      "grade": 8,
      "archetype": "WIDE_RUNNER",
      "innate_traits": ["Ma tốc độ", "Tinh tế"],
      "trait_slots": {
        "slot_1_plus8_coach": {
          "equipped": "Bậc thầy tốc độ",
          "status": "recommended_unconfirmed"
        },
        "slot_2_plus11_gold": {
          "equipped": None,
          "status": "locked_requires_plus11"
        },
        "slot_3_plus5_normal": {
          "equipped": "Ma tốc độ",
          "status": "recommended_unconfirmed",
          "fallback": "Tạt bóng sớm"
        }
      }
    },
    {
      "slot": "LCM",
      "player_name": "S. Gerrard",
      "season": "UT",
      "grade": 8,
      "archetype": "CM_PROGRESSOR / SECOND_WAVE",
      "innate_traits": ["Sút xa", "Chuyền dài", "Lãnh đạo"],
      "trait_slots": {
        "slot_1_plus8_coach": {
          "equipped": "Cải thiện chuyền xuyên phá",
          "status": "recommended_unconfirmed",
          "fallback": "Chiến thuật chuyền trực tiếp"
        },
        "slot_2_plus11_gold": {
          "equipped": None,
          "status": "locked_requires_plus11"
        },
        "slot_3_plus5_normal": {
          "equipped": "Thánh chuyền bóng",
          "status": "recommended_unconfirmed"
        }
      }
    },
    {
      "slot": "RCM",
      "player_name": "S. McTominay",
      "season": "25TS",
      "grade": 5,
      "archetype": "BOX_TO_BOX_CM",
      "innate_traits": ["Cứng như thép", "Sút xa"],
      "trait_slots": {
        "slot_1_plus8_coach": {
          "equipped": None,
          "status": "locked_requires_plus8"
        },
        "slot_2_plus11_gold": {
          "equipped": None,
          "status": "locked_requires_plus11"
        },
        "slot_3_plus5_normal": {
          "equipped": "Thánh chuyền bóng",
          "status": "recommended_unconfirmed",
          "fallback": "Nỗ lực đến cùng"
        }
      }
    },
    {
      "slot": "RM",
      "player_name": "B. Schweinsteiger",
      "season": "HG",
      "grade": 9,
      "archetype": "WIDE_CREATOR",
      "innate_traits": ["Thánh chuyền bóng", "Sút xa", "Chuyền dài"],
      "trait_slots": {
        "slot_1_plus8_coach": {
          "equipped": "Khả năng khéo léo",
          "status": "confirmed_applied"
        },
        "slot_2_plus11_gold": {
          "equipped": None,
          "status": "locked_requires_plus11"
        },
        "slot_3_plus5_normal": {
          "equipped": "Sút xoáy",
          "status": "confirmed_applied"
        }
      }
    },
    {
      "slot": "CDM",
      "player_name": "N. Matić",
      "season": "VTR",
      "grade": 12,
      "archetype": "ANCHOR_CDM",
      "innate_traits": ["Chuyền dài", "Cứng như thép"],
      "trait_slots": {
        "slot_1_plus8_coach": {
          "equipped": "Tập trung đánh chặn",
          "status": "recommended_unconfirmed"
        },
        "slot_2_plus11_gold": {
          "equipped": "Chủ Động Cản Phá",
          "status": "confirmed_applied_client_verified",
          "description": "Bay người cản phá cú sút."
        },
        "slot_3_plus5_normal": {
          "equipped": "Thánh chuyền bóng",
          "status": "recommended_unconfirmed"
        }
      }
    },
    {
      "slot": "LB",
      "player_name": "F. Mendy",
      "season": "CU",
      "grade": 8,
      "archetype": "STAY_BACK_FULLBACK",
      "innate_traits": ["Ma tốc độ", "Tinh tế"],
      "trait_slots": {
        "slot_1_plus8_coach": {
          "equipped": "Cải thiện phòng thủ bên trái",
          "status": "recommended_unconfirmed"
        },
        "slot_2_plus11_gold": {
          "equipped": None,
          "status": "locked_requires_plus11"
        },
        "slot_3_plus5_normal": {
          "equipped": "Chuyền dài",
          "status": "recommended_unconfirmed",
          "fallback": "Tạt bóng sớm"
        }
      }
    },
    {
      "slot": "LCB",
      "player_name": "M. Desailly",
      "season": "WG",
      "grade": 5,
      "archetype": "CB_STOPPER",
      "innate_traits": ["Đánh đầu mạnh", "Cứng như thép"],
      "trait_slots": {
        "slot_1_plus8_coach": {
          "equipped": None,
          "status": "locked_requires_plus8"
        },
        "slot_2_plus11_gold": {
          "equipped": None,
          "status": "locked_requires_plus11"
        },
        "slot_3_plus5_normal": {
          "equipped": "Thánh chuyền bóng",
          "status": "confirmed_applied"
        }
      }
    },
    {
      "slot": "RCB",
      "player_name": "R. Ferdinand",
      "season": "DC",
      "grade": 9,
      "archetype": "CB_COVER",
      "innate_traits": ["Đánh đầu mạnh"],
      "trait_slots": {
        "slot_1_plus8_coach": {
          "equipped": "Khả năng tắc bóng",
          "status": "recommended_unconfirmed"
        },
        "slot_2_plus11_gold": {
          "equipped": None,
          "status": "locked_requires_plus11"
        },
        "slot_3_plus5_normal": {
          "equipped": "Siêu cản phá",
          "status": "recommended_unconfirmed",
          "fallback": "Chuyền dài"
        }
      }
    },
    {
      "slot": "RB",
      "player_name": "J. Koundé",
      "season": "FAC",
      "grade": 5,
      "archetype": "STAY_BACK_FULLBACK / RECOVERY",
      "innate_traits": ["Đánh đầu mạnh"],
      "trait_slots": {
        "slot_1_plus8_coach": {
          "equipped": None,
          "status": "locked_requires_plus8"
        },
        "slot_2_plus11_gold": {
          "equipped": None,
          "status": "locked_requires_plus11"
        },
        "slot_3_plus5_normal": {
          "equipped": "Siêu cản phá",
          "status": "confirmed_applied"
        }
      }
    },
    {
      "slot": "GK",
      "player_name": "K. Casteels",
      "season": "23HW",
      "grade": 9,
      "archetype": "GK",
      "innate_traits": ["Ném bóng xa", "Cản phá 1-on-1"],
      "trait_slots": {
        "slot_1_plus8_coach": {
          "equipped": "Cản phá cú sút chìm",
          "status": "recommended_unconfirmed"
        },
        "slot_2_plus11_gold": {
          "equipped": None,
          "status": "locked_requires_plus11"
        },
        "slot_3_plus5_normal": {
          "equipped": None,
          "status": "pool_gk_required"
        }
      }
    }
  ]
}

# ==========================================
# 05_PLAYER_CARDS_MASTER.csv
# ==========================================
PLAYER_CARDS_HEADERS = [
  "player_name", "season", "upgrade", "position", "ovr", "salary", 
  "height_cm", "weight_kg", "body_type", "preferred_foot", "weak_foot", 
  "skill_stars", "innate_traits", "status"
]

PLAYER_CARDS_ROWS = [
  ["K. Havertz", "CU", 8, "CAM", 129, 28, 189, 82, "Gầy", "Trái", 4, 5, "Tinh tế,Đánh đầu mạnh,Bấm bóng", "STARTER_XI"],
  ["E. Dinkci", "24EP", 8, "LM", 125, 23, 188, 77, "Gầy", "Phải", 4, 4, "Ma tốc độ,Tinh tế", "STARTER_XI"],
  ["S. Gerrard", "UT", 8, "LCM", 128, 28, 183, 83, "Trung bình", "Phải", 4, 4, "Sút xa,Chuyền dài,Lãnh đạo", "STARTER_XI"],
  ["S. McTominay", "25TS", 5, "RCM", 124, 27, 193, 88, "Trung bình", "Phải", 4, 3, "Cứng như thép,Sút xa", "STARTER_XI"],
  ["B. Schweinsteiger", "HG", 9, "RM", 127, 26, 183, 79, "Trung bình", "Phải", 4, 4, "Thánh chuyền bóng,Sút xa,Chuyền dài", "STARTER_XI"],
  ["N. Matić", "VTR", 12, "CDM", 131, 20, 194, 85, "Cao gầy", "Trái", 4, 3, "Chuyền dài,Cứng như thép", "STARTER_XI"],
  ["F. Mendy", "CU", 8, "LB", 126, 23, 180, 73, "Trung bình", "Trái", 5, 4, "Ma tốc độ,Tinh tế", "STARTER_XI"],
  ["M. Desailly", "WG", 5, "LCB", 122, 26, 185, 81, "Đầm người", "Phải", 3, 3, "Đánh đầu mạnh,Cứng như thép", "STARTER_XI"],
  ["R. Ferdinand", "DC", 9, "RCB", 137, 27, 189, 87, "TB(Special)", "Phải", 3, 2, "Đánh đầu mạnh", "STARTER_XI"],
  ["J. Koundé", "FAC", 5, "RB", 121, 25, 180, 75, "Gầy", "Phải", 3, 3, "Đánh đầu mạnh", "STARTER_XI"],
  ["K. Casteels", "23HW", 9, "GK", 128, 22, 197, 86, "Gầy", "Phải", 2, 1, "Ném bóng xa,Cản phá 1-on-1", "STARTER_XI"],
  ["M. Lacroix", "25DP", 5, "CB", 120, 24, 190, 88, "Trung bình", "Phải", 3, 2, "Ma tốc độ", "BENCH_RESERVE"]
]

# ==========================================
# 06_ROLE_PROFILES.json
# ==========================================
ROLE_PROFILES_DATA = {
  "_metadata": {
    "project": "FCOnlineSquadProject",
    "updated_at": "2026-09-20",
    "total_archetypes": 11,
    "notes": "Đặc tả chi tiết nhiệm vụ, hành vi mong muốn và hành vi cấm kỵ của 11 vai trò trong sơ đồ 4-1-4-1-0"
  },
  "roles": {
    "CAM_CONNECTOR / FALSE_9": {
      "representative_player": "K. Havertz CU +8",
      "position": "CAM",
      "core_mission": "Đóng vai trò trạm luân chuyển bóng trung tâm, hút trung vệ đối phương và xâm nhập dứt điểm đợt 2 (Second Wave Finisher).",
      "desired_behaviors": [
        "Lùi sâu nhận bóng giữa các tuyến khi đội nhà phát triển bóng",
        "Tung đường chuyền một chạm xé toang biên cho WIDE_RUNNER",
        "Xâm nhập thẳng vào điểm mù của cặp CB đối phương khi bóng được tạt từ cánh"
      ],
      "forbidden_behaviors": [
        "Rê dắt quá 3 nhịp làm chậm nhịp độ phản công",
        "Cắm chốt quá cao như một ST truyền thống làm tắc nghẽn không gian",
        "Bỏ vị trí lùi về quá sâu ngang hàng với CDM"
      ],
      "threshold_attributes": {
        "vision": ">= 120",
        "short_pass": ">= 125",
        "positioning": ">= 122",
        "finishing": ">= 120",
        "stamina": ">= 118"
      },
      "ideal_traits": ["Kiến tạo", "Thánh chuyền bóng", "Sút xoáy", "Dứt điểm 1 chạm"]
    },
    "WIDE_RUNNER": {
      "representative_player": "E. Dinkci 24EP +8",
      "position": "LM",
      "core_mission": "Khai thác tối đa tốc độ dọc biên, kéo giãn hàng thủ đối phương và thực hiện các pha băng cắt dứt điểm góc hẹp hoặc căng ngang.",
      "desired_behaviors": [
        "Bứt tốc đón các đường chuyền dài vượt tuyến từ CM/CDM",
        "Cắt mặt hậu vệ biên đối phương lao vào cột hai đón bóng",
        "Pressing nhanh hậu vệ biên đối phương khi mất bóng"
      ],
      "forbidden_behaviors": [
        "Dừng bóng chậm lại để chuyền ngược về sân nhà khi đang có khoảng trống bứt tốc",
        "Tự ý bó vào vòng tròn trung tâm làm mất chiều rộng đội hình"
      ],
      "threshold_attributes": {
        "pace": ">= 130",
        "acceleration": ">= 130",
        "crossing": ">= 118",
        "stamina": ">= 122"
      },
      "ideal_traits": ["Ma tốc độ", "Bậc thầy tốc độ", "Sát thủ băng cắt", "Tạt bóng sớm"]
    },
    "CM_PROGRESSOR / SECOND_WAVE": {
      "representative_player": "S. Gerrard UT +8",
      "position": "LCM",
      "core_mission": "Phát động tấn công tầm xa, giữ nhịp phân phối bóng và đe dọa khung thành bằng các cú đại bác sút xa uy lực.",
      "desired_behaviors": [
        "Xuất hiện tại rìa vòng cấm (Zone 14) nhận bóng nhả lại từ CAM",
        "Tung các đường chuyền đảo cánh chính xác 50-60m",
        "Quyết đoán dứt điểm từ cự ly 20-25m"
      ],
      "forbidden_behaviors": [
        "Bỏ vị trí dâng lên ngang hàng CAM làm hổng tuyến giữa",
        "Tranh chấp liều lĩnh dẫn đến thẻ phạt ở trung tuyến"
      ],
      "threshold_attributes": {
        "long_shots": ">= 128",
        "shot_power": ">= 128",
        "long_pass": ">= 125",
        "stamina": ">= 120"
      },
      "ideal_traits": ["Sút xa", "Thánh chuyền bóng", "Chuyền dài", "Cải thiện chuyền xuyên phá"]
    },
    "BOX_TO_BOX_CM": {
      "representative_player": "S. McTominay 25TS +5",
      "position": "RCM",
      "core_mission": "Cung cấp sức mạnh cơ bắp, tranh chấp tay đôi, hỗ trợ bọc lót cho cánh phải và áp sát đánh chặn từ xa.",
      "desired_behaviors": [
        "Lao vào tranh chấp bóng 50/50 ở giữa sân bằng thể hình hộ pháp",
        "Lùi về hỗ trợ CDM Matić khi đối phương phản công trung lộ",
        "Băng vào vòng cấm tận dụng chiều cao tranh chấp bóng bổng"
      ],
      "forbidden_behaviors": [
        "Cố gắng thực hiện các pha rê dắt mạo hiểm thoát pressing",
        "Hụt hơi ở hiệp 2 do phân phối thể lực kém"
      ],
      "threshold_attributes": {
        "physical": ">= 124",
        "stamina": ">= 122",
        "interceptions": ">= 120",
        "height_cm": ">= 190"
      },
      "ideal_traits": ["Cứng như thép", "Thánh chuyền bóng", "Nỗ lực đến cùng", "Chặn đà tấn công"]
    },
    "WIDE_CREATOR": {
      "representative_player": "B. Schweinsteiger HG +9",
      "position": "RM",
      "core_mission": "Tiền vệ cánh kiến thiết lối chơi, điều tiết nhịp độ tấn công bên cánh phải và thực hiện các đường tạt bóng có độ xoáy cao.",
      "desired_behaviors": [
        "Phối hợp tam giác bóng ngắn với RCM và RB Koundé",
        "Tung các đường chọc khe bổng (QW) hoặc tạt bóng điểm rơi vào cột xa",
        "Bó vào trung lộ hỗ trợ kiểm soát thế trận khi cần"
      ],
      "forbidden_behaviors": [
        "Đua tốc độ thuần túy với các hậu vệ cánh siêu tốc",
        "Mất vị trí phòng ngự để đối phương khoét sâu cánh phải"
      ],
      "threshold_attributes": {
        "short_pass": ">= 125",
        "crossing": ">= 122",
        "curve": ">= 122",
        "vision": ">= 122"
      },
      "ideal_traits": ["Thánh chuyền bóng", "Sút xoáy", "Chuyền dài", "Khả năng khéo léo"]
    },
    "ANCHOR_CDM": {
      "representative_player": "N. Matić VTR +12",
      "position": "CDM",
      "core_mission": "Chốt chặn mỏ neo duy nhất phía trước bộ tứ vệ; che chắn khoảng trống Zone 14 và giải tỏa áp lực bóng bổng trung lộ.",
      "desired_behaviors": [
        "Luôn giữ vị trí thấp nhất hàng tiền vệ, không dâng quá vạch giữa sân",
        "Bay người cản phá các cú sút xa (kích hoạt Gold Trait Chủ Động Cản Phá)",
        "Dùng chiều cao 1m94 đánh đầu phá các pha phát bóng dài của thủ môn đối phương"
      ],
      "forbidden_behaviors": [
        "Ham dâng cao sút xa hoặc xâm nhập vòng cấm",
        "Bỏ vị trí dạt biên quá xa trung lộ để lộ lỗ hổng trước mặt cặp CB"
      ],
      "threshold_attributes": {
        "interceptions": ">= 130",
        "defensive_awareness": ">= 130",
        "strength": ">= 130",
        "height_cm": ">= 192"
      },
      "ideal_traits": ["Chủ Động Cản Phá (Gold)", "Tập trung đánh chặn", "Thánh chuyền bóng", "Cứng như thép"]
    },
    "STAY_BACK_FULLBACK": {
      "representative_player": "F. Mendy CU +8",
      "position": "LB",
      "core_mission": "Khóa chặt hành lang cánh trái, dùng tốc độ và thể lực để bóp nghẹt các tiền đạo cánh nguy hiểm nhất của đối phương.",
      "desired_behaviors": [
        "Luôn ở lại phía sau khi đội nhà tấn công, tạo hàng thủ 3 hoặc 4 người",
        "Dùng tốc độ bám đuổi và ép góc tiền đạo đối phương ra đường biên",
        "Cắt các đường chọc khe sệt xuống nách biên"
      ],
      "forbidden_behaviors": [
        "Tự ý dâng cao quá nửa sân dẫn đến việc bị phản công hở cánh",
        "Xoạc bóng liều lĩnh trong vòng cấm"
      ],
      "threshold_attributes": {
        "pace": ">= 128",
        "stamina": ">= 122",
        "tackling": ">= 122"
      },
      "ideal_traits": ["Ma tốc độ", "Cải thiện phòng thủ bên trái", "Chuyền dài", "Chuyên gia đeo bám"]
    },
    "CB_STOPPER": {
      "representative_player": "M. Desailly WG +5",
      "position": "LCB",
      "core_mission": "Trung vệ dập chủ động; bước lên phía trước để áp sát, đè bẹp tiền đạo mục tiêu đối phương ngay khi họ vừa chạm bóng.",
      "desired_behaviors": [
        "Quyết đoán lao lên tranh chấp bóng một chạm trước mặt vòng cấm",
        "Dùng sức mạnh cơ bắp húc văng tiền đạo đối phương",
        "Thực hiện các pha tắc bóng đứng uy lực chính xác"
      ],
      "forbidden_behaviors": [
        "Lùi quá sâu phá vỡ bẫy việt vị",
        "Dập hụt bóng mà không có đồng đội bọc lót phía sau"
      ],
      "threshold_attributes": {
        "aggression": ">= 124",
        "strength": ">= 124",
        "standing_tackle": ">= 124"
      },
      "ideal_traits": ["Đánh đầu mạnh", "Cứng như thép", "Khả năng tắc bóng", "Chặn đà tấn công"]
    },
    "CB_COVER": {
      "representative_player": "R. Ferdinand DC +9",
      "position": "RCB",
      "core_mission": "Trung vệ thòng bọc lót; giữ vị trí sâu, sửa sai cho trung vệ dập, phòng chống bóng bổng và đua tốc độ đuổi bắt chọc khe QW.",
      "desired_behaviors": [
        "Phán đoán điểm rơi, lùi bước quét khoảng trống phía sau Desailly",
        "Nhảy tranh chấp đánh đầu phá bóng tạt cánh (Power Header)",
        "Bay người phá bóng cứu thua ngoạn mục (Fancy Clearance / Siêu cản phá)"
      ],
      "forbidden_behaviors": [
        "Lao lên cướp bóng cùng lúc với Desailly để lộ khoảng trống chết người",
        "Tự ý xoạc bóng trượt gây thẻ phạt"
      ],
      "threshold_attributes": {
        "height_cm": ">= 189",
        "pace": ">= 130",
        "interceptions": ">= 135",
        "defensive_awareness": ">= 135"
      },
      "ideal_traits": ["Siêu cản phá", "Đánh đầu mạnh", "Khả năng tắc bóng", "Cự ly đội hình ổn định"]
    },
    "STAY_BACK_FULLBACK / RECOVERY": {
      "representative_player": "J. Koundé FAC +5",
      "position": "RB",
      "core_mission": "Hậu vệ biên lai trung vệ lệch phải; phòng ngự kỷ luật tuyệt đối, sẵn sàng bó vào trong như một trung vệ thứ ba khi cần.",
      "desired_behaviors": [
        "Giữ cự ly phòng ngự chặt chẽ, không bao giờ dâng cao chồng biên",
        "Bọc lót cho Ferdinand khi đối phương phản công chuyển cánh",
        "Tắc bóng dứt khoát giải nguy"
      ],
      "forbidden_behaviors": [
        "Bỏ vị trí chạy lên hỗ trợ tấn công làm hở nách phải",
        "Để tiền đạo đối phương vượt qua bằng tốc độ dọc biên"
      ],
      "threshold_attributes": {
        "defensive_awareness": ">= 122",
        "jumping": ">= 122",
        "pace": ">= 124"
      },
      "ideal_traits": ["Siêu cản phá", "Đánh đầu mạnh", "Cải thiện phòng thủ bên phải"]
    },
    "GK": {
      "representative_player": "K. Casteels 23HW +9",
      "position": "GK",
      "core_mission": "Người gác đền tin cậy; tận dụng chiều cao khủng 1m97 để hóa giải các cú sút xa ZD hiểm hóc và làm chủ bóng bổng phạt góc.",
      "desired_behaviors": [
        "Khép góc chuẩn xác các cú sút cứa lòng ZD ngoài vòng cấm",
        "Lao ra đấm bóng hoặc bắt dính các pha tạt cánh",
        "Phản xạ xuất thần cản phá đối mặt 1-on-1"
      ],
      "forbidden_behaviors": [
        "Lao ra khỏi vòng cấm phá bóng hỏng",
        "Đẩy bóng nảy vào chân tiền đạo đối phương trong vòng 5m50"
      ],
      "threshold_attributes": {
        "height_cm": ">= 195",
        "gk_reflexes": ">= 128",
        "gk_diving": ">= 128",
        "gk_positioning": ">= 128"
      },
      "ideal_traits": ["Cản phá 1-on-1", "Ném bóng xa", "Cản phá tạt bóng"]
    }
  }
}

if __name__ == "__main__":
    write_text("00_README.md", README_CONTENT)
    write_text("01_PROJECT_RULES.md", PROJECT_RULES_CONTENT)
    write_json("02_CURRENT_SQUAD.json", CURRENT_SQUAD_DATA)
    write_json("03_CURRENT_TACTICS.json", CURRENT_TACTICS_DATA)
    write_json("04_PLAYER_CONFIGS.json", PLAYER_CONFIGS_DATA)
    write_csv("05_PLAYER_CARDS_MASTER.csv", PLAYER_CARDS_HEADERS, PLAYER_CARDS_ROWS)
    write_json("06_ROLE_PROFILES.json", ROLE_PROFILES_DATA)
    print("Batch 1 completed successfully!")
