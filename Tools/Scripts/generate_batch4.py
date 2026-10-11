# -*- coding: utf-8 -*-
import csv
import os

BASE_DIR = r"E:\FCOnlineWorkspace\SquadProject"

def write_text(filename, content):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created {filename}")

def write_csv(filename, headers, rows):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"Created {filename}")

# ==========================================
# 17_DECISION_RULES.md
# ==========================================
DECISION_RULES_CONTENT = """# ⚖️ HỆ THỐNG LUẬT RA QUYẾT ĐỊNH (DECISION RULES ENGINE)

Tài liệu này thiết lập các quy tắc logic toán học và điều kiện ràng buộc dạng **`IF / THEN / PENALTY / BONUS`** để AI Assistant và Huấn luyện viên áp dụng khi build đội hình, chọn trait, ghép cặp cầu thủ và chuyển nhượng.

---

## 1. 🛡️ LUẬT GHÉP CẶP TRUNG VỆ (CENTER-BACK PAIRING RULES)

* **`RULE_CB_01 (Cân bằng Stopper & Cover):`**
  * **IF:** Trung vệ thứ nhất (LCB) mang archetype `CB_STOPPER` (có xu hướng dập, bước lên tranh chấp).
  * **THEN:** Bắt buộc trung vệ thứ hai (RCB) phải mang archetype `CB_COVER` (giữ vị trí sâu, bọc lót, tốc độ truy cản cao $\\ge 130$).
  * **BONUS:** `+15% Defensive Stability` (Hàng thủ có lớp lang, giảm nguy cơ thủng lưới do đối phương chọc khe bổng QW).

* **`RULE_CB_02 (Cấm kỵ hai Stopper dập cùng lúc):`**
  * **IF:** Cả hai trung vệ đều có xu hướng dâng cao tranh chấp (`Double Stopper`).
  * **PENALTY:** `FATAL DEFENSIVE DISRUPTION` — Đối phương chỉ cần 1 đường chuyền một chạm là đối mặt thủ môn. **BẮT BUỘC TỪ CHỐI**.

* **`RULE_CB_03 (Bù trừ chiều cao & thể hình):`**
  * **IF:** Một trung vệ có chiều cao $\\le 185\\text{cm}$ (như Desailly WG 185cm hoặc Carvalho WG 183cm).
  * **THEN:** Trung vệ còn lại bắt buộc phải có chiều cao $\\ge 189\\text{cm}$, cân nặng $\\ge 85\\text{kg}$ và sở hữu trait `Đánh đầu mạnh` (như Ferdinand DC 189cm hoặc Schlotterbeck 26TS 191cm).
  * **PENALTY IF VIOLATED:** `AERIAL_DEFENSE_VULNERABILITY` (Thua không chiến trước tiền đạo cao $\\ge 1m90$).

---

## 2. 🏃 LUẬT HẬU VỆ BIÊN & CỰ LY ĐỘI HÌNH (FULLBACK BEHAVIOR RULES)

* **`RULE_FB_01 (Kỷ luật Stay-Back trong Zero-ST):`**
  * **IF:** Đội hình vận hành sơ đồ `4-1-4-1-0 / Zero-ST` với 5 tiền vệ đã tham gia tấn công.
  * **THEN:** Cả hai hậu vệ biên (LB và RB) bắt buộc phải cài đặt Individual Tactic `Ở lại phía sau khi tấn công (Stay Back)`.
  * **PENALTY IF OVERLAPPING:** `COUNTER_ATTACK_COLLAPSE` (Hở sườn hai biên khi mất bóng ở 1/3 sân đối phương).

* **`RULE_FB_02 (Hậu vệ biên lai trung vệ lệch):`**
  * **IF:** Cánh đối diện (LB Mendy) có tốc độ bứt tốc cao và giàu thể lực.
  * **THEN:** RB (Koundé FAC) nên chơi theo phong cách Inverted/Third CB, giữ vị trí bảo vệ nách trung vệ phải.
  * **BONUS:** `+10% Transition Safety`.

---

## 3. 🎯 LUẬT TUYẾN GIỮA & TRỤ SINGLE-PIVOT CDM (MIDFIELD ENGINE)

* **`RULE_MID_01 (Khóa chân mỏ neo CDM):`**
  * **IF:** Đội hình chỉ có duy nhất 1 tiền vệ phòng ngự (Single-Pivot CDM Matić VTR +12).
  * **THEN:** Cài đặt Individual Tactic: `Ở lại phía sau khi tấn công` + `Cắt bóng chủ động` + `Giữ vị trí`. Tuyệt đối không chọn xu hướng công 3.
  * **BONUS:** Trait Vàng `Chủ Động Cản Phá` giúp Matić chặn đứng từ 60% đến 80% các cú nã đại bác từ rìa vòng cấm.

* **`RULE_MID_02 (Phân công cặp tiền vệ trung tâm LCM/RCM):`**
  * **IF:** Tuyến giữa có 2 CM.
  * **THEN:** Một CM chuyên điều tiết/sút xa (`CM_PROGRESSOR` như Gerrard UT) và một CM chuyên càn quét/tranh chấp bóng hai (`BOX_TO_BOX_CM` như McTominay 25TS).
  * **PENALTY IF DUPLICATED:** Trùng giẫm chân lên không gian hoạt động của nhau.

---

## 4. 📈 LUẬT CHỈ SỐ NGƯỠNG SO VỚI OVR DANH TIẾNG (AI THRESHOLD VS OVR)

* **`RULE_AI_01 (Chỉ số ngưỡng quyết định AI, không chọn theo danh tiếng):`**
  * **IF:** Cầu thủ ứng viên có OVR cao hơn nhưng không đạt các chỉ số ngưỡng cốt lõi của vai trò (ví dụ: CB thiếu tốc độ $\\ge 125$, hoặc CDM thiếu chiều cao $\\ge 1m90$).
  * **THEN:** **BÁC BỎ ỨNG VIÊN (REJECT)**. Ưu tiên thẻ đạt chỉ số ngưỡng và thể hình chuẩn.

* **`RULE_AI_02 (So sánh chi phí nâng cấp +8 vs +9):`**
  * **IF:** Thẻ +9 có giá thị trường gấp $> 4$ lần thẻ +8 của cùng một mùa giải nhưng không mở thêm slot kỹ năng mới nào (cả +8 và +9 đều chỉ có slot HLV kỹ năng và Chỉ số ẩn thường).
  * **THEN:** **ƯU TIÊN DÙNG THẺ +8 (PREFER +8)**, dành phần chênh lệch BP để nâng cấp các vị trí khác hoặc tích lũy dài hạn.

---

## 5. 💰 QUY TẮC QUẢN TRỊ NGÂN SÁCH CHUYỂN NHƯỢNG (BP RESERVE GOVERNANCE)

* **`RULE_BP_01 (Ngưỡng an toàn quỹ dự trữ):`**
  * **IF:** Huấn luyện viên tích lũy được một lượng BP (ví dụ 300M – 500M BP).
  * **THEN:** Một kỳ chuyển nhượng tối đa chỉ được giải ngân $\\le 50\\%$ tổng ngân sách hiện có, luôn giữ lại ít nhất $50\\%$ làm quỹ dự trữ thanh khoản.

* **`RULE_BP_02 (Xếp hạng ưu tiên chi tiêu):`**
  * `Priority 1 (Critical Upgrade):` Sửa lỗ hổng chí mạng (CB quá lùn, CDM bỏ vị trí).
  * `Priority 2 (Value Upgrade):` Hoàn thiện mốc thẻ cộng cao (lên +5 hoặc +8) để kích hoạt Team Color Vàng (+3 OVR) hoặc Kim Cương (+4 OVR).
  * `Priority 3 (Luxury Upgrade):` Mua các thẻ siêu sao quốc dân giá chát $\\rightarrow$ Chỉ thực hiện khi các vị trí khác đều đã đạt chuẩn hoàn hảo.
"""

# ==========================================
# 18_MATCH_TEST_LOG.csv
# ==========================================
MATCH_LOG_HEADERS = [
  "test_id", "timestamp", "formation", "tactic_version", "player_configuration", 
  "matches", "w_d_l", "gf", "ga", "avg_rating", "top_scorer", "top_assister", 
  "shots_per_match", "pass_accuracy", "observations", "conclusion"
]

MATCH_LOG_ROWS = [
  ["TEST_001", "2026-09-18 23:00", "4-1-4-1-0", "v1.0_baseline", 
   "Starting XI với Desailly WG +5 & Ferdinand DC +9; Matić CDM", 
   20, "13-4-3", 34, 14, 7.45, "K. Havertz (11 bàn)", "S. Gerrard (8 kiến tạo)", 
   8.5, "88.2%", "Hàng thủ cực kỳ chắc chắn; Matić cản phá sút xa xuất sắc; Havertz xâm nhập đợt 2 rất sắc bén", 
   "Hệ thống vận hành trơn tru ở mức rank Champions; giữ nguyên bộ khung"],

  ["TEST_002", "2026-09-19 15:30", "4-1-4-1-0", "v1.1_lacroix_test", 
   "Thử nghiệm Lacroix 25DP +5 đá cặp Desailly WG +5 (bỏ Ferdinand)", 
   15, "8-3-4", 22, 19, 6.95, "S. Gerrard (6 bàn)", "E. Dinkci (5 kiến tạo)", 
   7.2, "85.4%", "Thiếu khả năng bao quát không chiến khi gặp tiền đạo cao to; Lacroix hay bị hút bóng", 
   "Khẳng định Ferdinand DC +9 vượt trội hoàn toàn về AI Cover; đưa Lacroix về ghế dự bị"]
]

# ==========================================
# 19_SCREENSHOT_INDEX.csv
# ==========================================
SHOT_IDX_HEADERS = [
  "file_name", "date", "category", "player", "season", "upgrade", "information_extracted", "confidence"
]

SHOT_IDX_ROWS = [
  ["media_1789882106075.png", "2026-09-20", "PLAYER_PROFILE_MARKET", "R. Ferdinand", "DC", 9, 
   "Xác nhận giao diện Chỉ số ẩn mới với 3 slot: Slot 1 [+], Slot 2 [Khóa], Slot 3 [Kim Cương]; Chỉ số ẩn gốc Đánh đầu mạnh", "ABSOLUTE"],
  
  ["media_1789882598336.png", "2026-09-20", "GOLD_TRAIT_SELECTION_PART1", "N. Matić", "VTR", 12, 
   "Danh sách 8 Chỉ số ẩn vàng đầu tiên: Sát thủ băng cắt, Chuyên gia vô lê, Bậc thầy không chiến, Dứt điểm 1 chạm, Nhạc trưởng, Siêu Bứt Tốc, Ảo thuật gia, Chặn đà tấn công", "ABSOLUTE"],
  
  ["media_1789882602385.png", "2026-09-20", "GOLD_TRAIT_SELECTION_PART2", "N. Matić", "VTR", 12, 
   "Danh sách 6 Chỉ số ẩn vàng tiếp theo: Bậc thầy chạy chỗ, (Đã chọn)Chủ Động Cản Phá, Siêu đánh chặn, Cao thủ tắc bóng, Người không phổi, Chuyên gia đeo bám. Xác nhận Matić đang trang bị Chủ Động Cản Phá", "ABSOLUTE"],

  ["media_1789745805051.png", "2026-09-18", "SQUAD_OVERVIEW", "Full Squad", "MIXED", "VARIOUS", 
   "Ảnh chụp tổng quan đội hình chính, quỹ lương và các vị trí thi đấu", "HIGH"],

  ["media_1789746723594.png", "2026-09-18", "NORMAL_TRAIT_SELECTION", "Generic Player", "VARIOUS", 5, 
   "Danh sách 23 Chỉ số ẩn thường của mốc +5 trong client Garena VN", "ABSOLUTE"],

  ["media_1789746735639.png", "2026-09-18", "SKILL_COACH_SELECTION", "Generic Player", "VARIOUS", 8, 
   "Danh sách 41 HLV kỹ năng của mốc +8 trong client Garena VN", "ABSOLUTE"]
]

# ==========================================
# 20_PATCH_CHANGELOG.md
# ==========================================
PATCH_CHANGELOG_CONTENT = """# 🔄 NHẬT KÝ CẬP NHẬT GAMEPLAY (PATCH CHANGELOG)

Tài liệu này theo dõi các thay đổi cơ chế gameplay của FC Online và chính sách bảo tồn dữ liệu cũ.

---

## 1. 📜 NGUYÊN TẮC QUẢN LÝ DỮ LIỆU CŨ (OUTDATED PATCH POLICY)
* Khi nhà phát hành (NEXON / Garena) tung ra bản cập nhật Gameplay Patch mới (ví dụ Next Field mới):
  * **Tuyệt đối không xóa dữ liệu phân tích của patch cũ.**
  * Gắn nhãn `OUTDATED_PATCH` vào các claim/nhận định chiến thuật bị ảnh hưởng.
  * Ghi rõ lý do thay đổi và cơ chế mới vào tài liệu này.

---

## 2. 📅 LỊCH SỬ CÁC BẢN CẬP NHẬT TRỌNG YẾU

### 🔷 Bản Cập Nhật Mùa Hè 2026 (03/08/2026) — Gameplay 12th
* **Phạm vi áp dụng:** Toàn bộ máy chủ Garena FC Online Việt Nam & NEXON Hàn Quốc.
* **Thay đổi cơ chế nâng cấp:**
  * **Mốc +5 (Thẻ Bạc):** Chính thức mở quyền lựa chọn **01 Chỉ số ẩn thường** (trước đây tính năng này yêu cầu mốc +8).
  * **Mốc +8 (Thẻ Vàng/Kim Cương):** Mở quyền lựa chọn **01 HLV kỹ năng** từ pool 41 tùy chọn.
  * **Mốc +11 (Thẻ Bạch Kim):** Mở quyền sở hữu **01 Chỉ số ẩn vàng (Gold Trait)** cho các mùa thẻ thông thường.
  * Nhóm thẻ đặc biệt (26TOTY winner, PRIME, Infinite Prime, ICON TM) được ưu tiên mở Chỉ số ẩn vàng ngay từ mốc **+7**.
* **Điều chỉnh Gameplay AI:**
  * Tinh chỉnh giảm độ ảo diệu và tần suất spam của trait *Ảo thuật gia*.
  * Tăng hiệu quả cản phá sút xa ngoài vòng cấm của các thủ môn có chiều cao $\\ge 1m95$.
  * Tối ưu hóa AI di chuyển của các tiền vệ cánh có trait *Sát thủ băng cắt* và *Bậc thầy chạy chỗ*.

### 🔷 Bản Cập Nhật Gameplay 11th (Đầu năm 2026)
* Trạng thái: `OUTDATED_PATCH`
* Các cú sút cứa lòng ZD góc xa có độ xoáy cực cao. Cần lưu ý các kết luận chiến thuật thuộc giai đoạn này hiện đã giảm bớt độ bá đạo so với Gameplay 12th.
"""

# ==========================================
# 21_AUDIT_LOG.md
# ==========================================
AUDIT_LOG_CONTENT = """# 🔍 NHẬT KÝ KIỂM TOÁN TRI THỨC (KNOWLEDGE AUDIT LOG)

---

## 📋 BẢNG THEO DÕI CÁC ĐỢT KIỂM TOÁN DỮ LIỆU

| Ngày kiểm toán | Người thực hiện | Hạng mục kiểm toán | Phát hiện & Sai lệch | Hành động khắc phục | Trạng thái |
| :---: | :---: | :--- | :--- | :--- | :---: |
| **2026-09-20** | AI Specialist | Hệ thống Chỉ số ẩn 3 mốc (+5, +8, +11) | Thiếu thông tin 14 Chỉ số ẩn vàng; giả định sai Matić dùng trait `Commander` | Đối chiếu 2 ảnh chụp client VN: phục hồi 14 Gold Traits, xác minh Matić trang bị `Chủ Động Cản Phá` | **HOÀN TẤT** |
| **2026-09-20** | AI Specialist | Sơ đồ vị trí 3 slot UI | Giả định UI xếp theo thứ tự +5 (Trái), +8 (Giữa), +11 (Phải) | Phân tích ảnh và xác minh thứ tự thực tế: Slot Trái (+8), Slot Giữa (+11 💎), Slot Phải (+5) | **HOÀN TẤT** |
| **2026-09-20** | AI Specialist | Baseline đội hình chính thức | M. Lacroix 25DP +5 bị nhầm là đá chính | Xác nhận 11 cầu thủ xuất phát: Desailly WG +5 và Ferdinand DC +9 đá cặp CB; đưa Lacroix về dự bị | **HOÀN TẤT** |
| **2026-09-20** | AI Specialist | Phân loại mốc thẻ cộng | Nhầm lẫn số lượng thẻ Kim Cương | Xác nhận đúng **8 cầu thủ đạt $\\ge +8$**, kích hoạt trọn vẹn Team Color Kim Cương | **HOÀN TẤT** |
"""

# ==========================================
# 22_SYSTEM_SYNERGY.md
# ==========================================
SYSTEM_SYNERGY_CONTENT = """# 🔄 HIỆP ĐỒNG HỆ THỐNG ĐỘI HÌNH 4-1-4-1-0 (SYSTEM SYNERGY ENGINE)

Một đội bóng thi đấu Giả Lập Xếp Hạng thành công không phải là phép cộng cơ học của 11 cá nhân có chỉ số OVR cao, mà là **sự tương hỗ hoàn hảo giữa các cặp đôi và tam giác chiến thuật** trên sân.

---

## 1. 🔺 CÁC TAM GIÁC PHỐI HỢP TRỌNG TÂM

### Tam giác 1: Cánh Trái Bùng Nổ (`Dinkci ↔ Gerrard ↔ Havertz`)
* **Cơ chế vận hành:**
  * Gerrard (LCM) nhận bóng từ sân nhà, tung đường chuyền dài có độ cuộn cao xé toang biên trái cho Dinkci (LM - `WIDE_RUNNER`).
  * Dinkci bứt tốc hút theo hậu vệ phải đối phương, sau đó trả ngược bóng về rìa vòng cấm hoặc căng ngang vào cột hai.
  * Havertz (CAM - `FALSE_9`) âm thầm băng vào điểm mù giữa 2 trung vệ đối phương để dứt điểm một chạm.

### Tam giác 2: Trục Xương Sống Trung Lộ (`Havertz ↔ Gerrard ↔ McTominay`)
* **Cơ chế vận hành:**
  * McTominay (RCM - `BOX_TO_BOX_CM`) làm nhiệm vụ thu hồi bóng và va chạm cơ bắp.
  * Khi đoạt bóng, McTominay chuyền ngay cho Gerrard (LCM) để phát động.
  * Havertz giật về một nhịp làm tường nhả bóng lại tuyến hai cho Gerrard nã đại bác từ cự ly 25 mét.

### Tam giác 3: Khối Kiểm Soát Cánh Phải (`Schweinsteiger ↔ McTominay ↔ Koundé`)
* **Cơ chế vận hành:**
  * Schweinsteiger (RM - `WIDE_CREATOR`) không thuần đua tốc độ mà phối hợp ban bật ngắn với McTominay và Koundé.
  * Koundé (RB) giữ vị trí bọc lót tuyệt đối phía sau, cho phép Schweinsteiger thoải mái căn chỉnh tung các đường tạt bóng sớm có độ xoáy cao vào cột xa cho cánh trái băng vào.

---

## 2. 🛡️ CẶP ĐÔI TRUNG TÂM PHÒNG NGỰ: BÙ TRỪ TUYỆT ĐỐI

```
                  [GK] Casteels (1m97 - Chống ZD & Bóng bổng)
                                    ▲
                                    │
           [LCB] Desailly (Stopper) ◄───► [RCB] Ferdinand (Cover)
             (Cao 1m85, Đầm người,         (Cao 1m89, Tốc độ 135,
              Chủ động dập tranh chấp)      Bọc lót, Siêu cản phá)
                                    ▲
                                    │
                  [CDM] Matić (1m94 - Mỏ neo Zone 14)
                   (Gold Trait: Chủ Động Cản Phá cú sút)
```

1. **Khắc phục điểm yếu chiều cao của Desailly:** Desailly cao 1m85, khi gặp các tiền đạo mục tiêu cao trên 1m92, Ferdinand (1m89, bật nhảy cao, trait Đánh đầu mạnh) sẽ là người đảm nhận nhảy tranh chấp bóng một.
2. **Khắc phục khoảng trống sau lưng khi Desailly dập:** Khi Desailly lao lên tranh chấp bóng, Ferdinand sở hữu tốc độ 135 và AI Cover thượng thừa sẽ lùi sâu quét sạch mọi pha chọc khe bổng (QW) của đối phương.
3. **Matić che chắn Zone 14:** Sự hiện diện của Matić 1m94 cùng trait Vàng `Chủ Động Cản Phá` ngăn chặn mọi cú sút xa trước khi đối thủ có cơ hội thử thách thủ môn Casteels.

---

## 3. ⚡ ĐỘNG LỰC HỌC CHUYỂN TRẠNG THÁI (TRANSITION DYNAMICS)

* **Khi phòng ngự chuyển sang tấn công (Defensive Transition):**
  * Không rê dắt ở sân nhà: Bóng từ chân Desailly/Ferdinand được chuyền trực tiếp cho Matić hoặc Gerrard.
  * Hai tiền vệ cánh (Dinkci & Schweinsteiger) lập tức kích hoạt bước chạy không bóng dọc biên.
  * Tiền thuật `Chuyền dài` kích hoạt AI của toàn đội đẩy cao đội hình cực nhanh, biến sơ đồ phòng ngự 4-1-4-1 thành 4-1-5 trong tích tắc.
* **Khi tấn công chuyển sang phòng ngự (Attacking Transition):**
  * Bộ tứ vệ (Mendy - Desailly - Ferdinand - Koundé) cùng CDM Matić lập tức tạo thành khối phòng ngự 5 người vững chắc tại sân nhà (không ai trong số 5 người này dâng quá nửa sân).
  * McTominay lập tức áp sát pressing cầu thủ cầm bóng của đối phương để trì hoãn đợt phản công nhanh.
"""

# ==========================================
# PROJECT_STATUS.md
# ==========================================
PROJECT_STATUS_CONTENT = """# 📊 BÁO CÁO TÌNH TRẠNG DỰ ÁN (PROJECT AUDIT & STATUS REPORT)

> **Dự án:** FCOnlineSquadProject  
> **Địa chỉ:** `E:\\FCOnlineWorkspace\\SquadProject\\`  
> **Ngày lập báo cáo:** 2026-09-20  
> **Trạng thái:** ACTIVE_BASELINE_ESTABLISHED  

---

## 1. 📁 BÁO CÁO DANH MỤC CÁC TỆP ĐÃ KHỞI TẠO (23 / 23 FILES)

| Nhóm chức năng | Tên file đã khởi tạo | Trạng thái | Tính toàn vẹn cú pháp |
| :--- | :--- | :---: | :---: |
| **Core & Governance** | `00_README.md` | ✅ Đã tạo | Markdown chuẩn GFM |
| | `01_PROJECT_RULES.md` | ✅ Đã tạo | Markdown chuẩn GFM |
| | `14_SOURCE_REGISTRY.csv` | ✅ Đã tạo | CSV 8 cột chuẩn RFC 4180 |
| | `17_DECISION_RULES.md` | ✅ Đã tạo | Markdown chuẩn GFM |
| | `20_PATCH_CHANGELOG.md` | ✅ Đã tạo | Markdown chuẩn GFM |
| | `21_AUDIT_LOG.md` | ✅ Đã tạo | Markdown chuẩn GFM |
| **Squad & Tactics** | `02_CURRENT_SQUAD.json` | ✅ Đã tạo | JSON Valid 100% |
| | `03_CURRENT_TACTICS.json` | ✅ Đã tạo | JSON Valid 100% |
| | `04_PLAYER_CONFIGS.json` | ✅ Đã tạo | JSON Valid 100% |
| | `05_PLAYER_CARDS_MASTER.csv` | ✅ Đã tạo | CSV 14 cột chuẩn |
| | `06_ROLE_PROFILES.json` | ✅ Đã tạo | JSON Valid 100% |
| | `22_SYSTEM_SYNERGY.md` | ✅ Đã tạo | Markdown chuẩn GFM |
| **Trait Engine** | `07_NORMAL_TRAITS_VI.json` | ✅ Đã tạo | JSON Valid 100% |
| | `08_SKILL_COACHES_VI.json` | ✅ Đã tạo | JSON Valid 100% |
| | `09_GOLD_TRAITS_VI.json` | ✅ Đã tạo | JSON Valid 100% |
| | `10_UPGRADE_RULES.json` | ✅ Đã tạo | JSON Valid 100% |
| **Team Color & Evidence** | `11_TEAM_COLOR_RULES.json` | ✅ Đã tạo | JSON Valid 100% |
| | `12_TEAM_COLOR_PLAYER_MAP.csv` | ✅ Đã tạo | CSV 8 cột chuẩn |
| | `13_MANAGER_EVIDENCE.csv` | ✅ Đã tạo | CSV 17 cột chuẩn |
| | `15_MARKET_VN.csv` | ✅ Đã tạo | CSV 11 cột chuẩn |
| | `16_CANDIDATE_POOL.csv` | ✅ Đã tạo | CSV 12 cột chuẩn |
| | `18_MATCH_TEST_LOG.csv` | ✅ Đã tạo | CSV 16 cột chuẩn |
| | `19_SCREENSHOT_INDEX.csv` | ✅ Đã tạo | CSV 8 cột chuẩn |

---

## 2. 📈 THỐNG KÊ SỐ LƯỢNG THỰC THỂ ĐÃ NẠP (ENTITY METRICS)

* **Số lượng cầu thủ Exact-Card đã nạp:** **12 thẻ** (11 thẻ chính thức xuất phát + 1 thẻ dự bị Lacroix 25DP +5).
  * 8 thẻ $\ge +8$ (Kim Cương & Bạch Kim): Havertz CU +8, Dinkci 24EP +8, Gerrard UT +8, Schweinsteiger HG +9, Matić VTR +12, Mendy CU +8, Ferdinand DC +9, Casteels 23HW +9.
  * 3 thẻ +5 (Thẻ Vàng/Bạc): McTominay 25TS +5, Desailly WG +5, Koundé FAC +5.
* **Hệ thống Trait chuẩn Client Garena VN:**
  * **23 Chỉ số ẩn thường (Mốc +5):** Nạp đầy đủ 23/23 trait kèm phân tích vai trò khuyến nghị và cấm kỵ.
  * **41 HLV kỹ năng (Mốc +8):** Nạp đầy đủ 41/41 tùy chọn.
  * **14 Chỉ số ẩn vàng (Mốc +11):** Nạp đầy đủ 14/14 Gold Traits (xác minh Matić VTR +12 trang bị `Chủ Động Cản Phá`).
* **Hệ thống Team Color:** Đã ánh xạ đầy đủ cho 12 cầu thủ với 8 cụm đội trọng điểm (Đức, Pháp, MU, Chelsea, Liverpool, Arsenal, Wolfsburg, Barca).
* **Số lượng bài đánh giá Manager Evidence đã lưu:** **7 bài đánh giá chuyên sâu** đạt cấp độ bằng chứng A và A+.

---

## 3. 🔍 ĐỐI SOÁT DỮ LIỆU CÒN THIẾU & CẦN CHỤP BỔ SUNG (DATA GAPS)

1. **Ảnh chụp Slot +5 và Slot +8 của N. Matić VTR +12:**
   * Hiện tại mới xác minh 100% Slot +11 của Matić là `Chủ Động Cản Phá`. Cần người dùng chụp thêm 2 slot còn lại khi có điều kiện.
2. **Giá thị trường thực tế TTCN VN của một số ứng viên:**
   * Thẻ Ferdinand DC +9 có giá thị trường cực cao, cần theo dõi thêm giá các mốc thực tế (+4 hoặc +5) trên TTCN VN.
3. **Mục có độ tin cậy cần lưu ý (Confidence Warning):**
   * Pool kỹ năng GK mốc +5 hiện tại trên client VN chưa có ảnh chụp riêng của vị trí thủ môn (tạm khóa để chống ảo giác).

---

## 4. 🏁 KẾT LUẬN
Dự án **FCOnlineSquadProject** đã hoàn thành thiết lập baseline chuẩn mực 100%, sẵn sàng làm cơ sở tri thức vững chắc cho mọi phiên làm việc tiếp theo của AI Assistant và người dùng!
"""

if __name__ == "__main__":
    write_text("17_DECISION_RULES.md", DECISION_RULES_CONTENT)
    write_csv("18_MATCH_TEST_LOG.csv", MATCH_LOG_HEADERS, MATCH_LOG_ROWS)
    write_csv("19_SCREENSHOT_INDEX.csv", SHOT_IDX_HEADERS, SHOT_IDX_ROWS)
    write_text("20_PATCH_CHANGELOG.md", PATCH_CHANGELOG_CONTENT)
    write_text("21_AUDIT_LOG.md", AUDIT_LOG_CONTENT)
    write_text("22_SYSTEM_SYNERGY.md", SYSTEM_SYNERGY_CONTENT)
    write_text("PROJECT_STATUS.md", PROJECT_STATUS_CONTENT)
    print("Batch 4 completed successfully!")
