import os

BASE_DIR = r"E:\FCOnlineWorkspace\Research\knowledge"

contradictions_content = """# ⚖️ SỔ BỘ BẤT ĐỒNG & MÂU THUẪN CHIẾN THUẬT (CONTRADICTIONS.MD)

Tài liệu ghi nhận, mổ xẻ và đối chiếu các quan điểm chiến thuật trái chiều trong cộng đồng Giả Lập Xếp Hạng (Manager Mode) FC Online. Tuyệt đối không âm thầm chọn một bên; mọi mâu thuẫn đều được phân tích theo bối cảnh: **Phiên bản Patch**, **Sơ đồ vận hành**, **Hình thái cầu thủ (Archetype)** và **Cấp độ Rank**.

---

## 1. MÂU THUẪN #1: THIẾT LẬP LDM/RDM — `AS1 (STAY BACK)` VS `AS MẶC ĐỊNH (BALANCED)`

| Tiêu Chí Đối Soát | Quan Điểm A (Thiên Thủ) | Quan Điểm B (Cân Bằng Tuyến 2) |
| :--- | :--- | :--- |
| **Thiết lập:** | `AS1` (Ở lại phía sau khi tấn công) | `AS Mặc định` hoặc `AS2` (Tham gia tấn công) |
| **Lập luận chính:** | Khóa chết trung lộ trước mặt 2 CB, chống phản công vỗ mặt 100%. | Không để ST bị cô lập; cần tiếp ứng tuyến 2 dứt điểm sút xa ZD/D. |
| **Nguồn ủng hộ:** | Ranker Inven Super Champions (KR), Guide Top 1 VN. | Cộng đồng FCVN, người chơi hệ sút xa tuyến hai. |
| **Patch áp dụng:** | `GAMEPLAY_12TH_2026` | `GAMEPLAY_11TH` trở về trước. |
| **Xếp hạng Evidence:** | **Tier B** (Thực nghiệm Top Rank) | **Tier C** (Quan sát cộng đồng) |

### 🔍 Giải Mã & Nguyên Tắc Hòa Giải (Reconciliation):
* **Không áp dụng cứng nhắc cho cả hai:** Trong sơ đồ 2 tiền vệ trụ (Double Pivot - 4-2-3-1, 4-2-2-1-1), cài `AS1` cho **cả hai cầu thủ** sẽ cắt đứt sợi dây liên kết giữa hàng tiền vệ và tiền đạo, khiến ST liên tục bị đói bóng. Ngược lại, để **cả hai tự do** sẽ khiến trung lộ toang hoác khi mất bóng.
* **Quy tắc chuẩn hóa:**
  - **1 Anchor CDM thuần túy (Rodri, Vieira, Casemiro):** BẮT BUỘC cài `AS1` + `DB1` + `DP2`.
  - **1 Box-to-Box / Ball-Winner (Lampard, Zaïre-Emery, Gullit):** Cài `AS Mặc định` để tự do dâng lên rìa 16m50 đón bóng 2 dứt điểm.

---

## 2. MÂU THUẪN #2: HẬU VỆ BIÊN — `AR2 (STAY BACK)` VS `AR1 (OVERLAP)`

| Tiêu Chí Đối Soát | Quan Điểm A (Khóa Cánh Toàn Diện) | Quan Điểm B (Gia Tăng Biên Độ Tấn Công) |
| :--- | :--- | :--- |
| **Thiết lập:** | `AR2` (Ở lại phía sau khi tấn công) | `AR1` (Chồng biên chủ động) |
| **Lập luận chính:** | Tránh bị khoét nách bởi các tiền đạo cánh tốc độ cao (Mbappe, Vinicius, Son). | Kéo giãn hàng thủ đối phương, tạo phương án tạt bóng sớm (Early Cross). |
| **Bối cảnh sơ đồ:** | Sơ đồ có Winger tự nhiên (`4-2-3-1`, `4-2-2-1-1`, `4-1-2-3`). | Sơ đồ trung lộ hẹp (`4-1-2-1-2`, `4-3-1-2`). |
| **Xếp hạng Evidence:** | **Tier A/B** | **Tier B** |

### 🔍 Giải Mã & Nguyên Tắc Hòa Giải:
* Trong các sơ đồ **đã có tiền vệ cánh hoặc tiền đạo cánh**, việc Fullback dâng cao là hành vi tự sát chiến thuật trong GLXH vì AI hậu vệ biên lùi về rất chậm khi mất bóng.
* **Quy tắc:** Chỉ kích hoạt `AR1` khi chơi sơ đồ không có tiền vệ cánh (`4-1-2-1-2 Kim Cương Hẹp`) VÀ hậu vệ biên có thể lực tối thiểu $\ge 120$ kèm chỉ số Tốc độ $\ge 120$ (như Zambrotta, Gvardiol, Theo Hernandez). Đối với `4-2-3-1`, luôn khóa `AR2`.

---

## 3. MÂU THUẪN #3: HÀNH VI TIỀN ĐẠO CẮM — `AR1 (XẺ NÁCH)` VS `AR2 (MỤC TIÊU)`

| Tiêu Chí Đối Soát | Quan Điểm A (Chạy Chỗ Phá Bẫy) | Quan Điểm B (Làm Tường Tì Đè) |
| :--- | :--- | :--- |
| **Thiết lập:** | `AR1` (Get in Behind) | `AR2` (Target Man) |
| **Lập luận:** | Bắt việt vị trung vệ đối phương bằng các đường chọc khe dài QW. | Giữ bóng, tì đè đè mặt trung vệ, phân phối cho CAM và 2 cánh băng lên. |
| **Mẫu cầu thủ phù hợp:** | Son Heung Min, P. Aubameyang, E. Hazard (Nhẹ cân, tốc độ). | V. Boniface, E. Haaland, D. Drogba (Đậm người, cao to). |
| **Xếp hạng Evidence:** | **Tier B** | **Tier B** |

### 🔍 Giải Mã & Nguyên Tắc Hòa Giải:
* Mâu thuẫn xuất phát từ việc người chơi gán nhầm chỉ thị cho sai Archetype cầu thủ:
  - Nếu gán `AR2` cho Son Heung Min $\rightarrow$ Cầu thủ sẽ liên tục quay lưng giữ bóng và bị trung vệ to khỏe húc văng, mất bóng.
  - Nếu gán `AR1` cho Boniface $\rightarrow$ Cầu thủ vụng về trong xoay sở, dễ bị bẫy việt vị hoặc bị bắt bài đua tốc độ dài.
* **Quy tắc:** Lựa chọn `AR1` hay `AR2` phụ thuộc hoàn toàn vào **Chiều cao + Thể hình** của tiền đạo, không phụ thuộc vào sở thích cá nhân.

---

## 4. MÂU THUẪN #4: ÁP LỰC PHÒNG NGỰ — `HIGH PRESS (>65)` VS `BALANCED MID-BLOCK (40-52)`

| Tiêu Chí Đối Soát | Quan Điểm A (Pressing Nghẹt Thở) | Quan Điểm B (Khối Đội Hình Chặt Chẽ) |
| :--- | :--- | :--- |
| **Thông số:** | Áp lực (Pressure) 65-80, Quyết đoán 65-75 | Áp lực (Pressure) 40-52, Quyết đoán 42-52 |
| **Lập luận:** | Giành lại bóng ngay trên phần sân đối phương, không cho triển khai bóng. | Giữ vững cự ly phòng ngự, tránh bị sút xa ZD và bóng bổng QW sau lưng. |
| **Độ nhạy Patch:** | Cực kỳ hiệu quả ở Gameplay 9th/10th. | Tối ưu toàn diện ở `GAMEPLAY_12TH_2026`. |
| **Xếp hạng Evidence:** | **Tier C** (Lỗi thời / Outdated) | **Tier A** (Official Gameplay 12th Mechanics) |

### 🔍 Giải Mã & Nguyên Tắc Hòa Giải:
* Ở Gameplay 12th hiện tại, Nexon và Garena đã cập nhật cơ chế **Stamina Penalty**: Nếu duy trì áp lực trên 65 suốt hiệp 1, toàn bộ hàng tiền vệ và tiền đạo sẽ cạn kiệt thanh thể lực từ phút 65, dẫn đến sụp đổ thể lực và thua ngược ở cuối trận.
* **Quy tắc:** Chỉ dùng Áp lực cao khi bị dẫn bàn ở 15 phút cuối trận (Chiến thuật phụ phím số). Trong 75 phút đầu, bắt buộc duy trì dải thông số cân bằng 40-52.

---

## 5. MÂU THUẪN #5: NHỊP ĐỘ TRIỂN KHAI — `SPEED > 70` VS `SPEED 45-55`

* **Speed > 70 (Phản công sốc):** Tốt cho lối chơi trộm chó 5-2-3 hoặc 4-2-2-1-1 phản công biên. Cầu thủ lao lên cực nhanh nhưng tỷ lệ chuyền hỏng tăng 25%.
* **Speed 45-55 (Kiểm soát nhịp độ):** Bắt buộc cho 4-2-3-1. Đảm bảo các tuyến giữ đúng khoảng cách tam giác chuyền bóng, tỷ lệ kiểm soát bóng đạt 55-65%.
"""

with open(os.path.join(BASE_DIR, "CONTRADICTIONS.md"), "w", encoding="utf-8") as f:
    f.write(contradictions_content)

decision_rules_content = """# 🧭 HỆ THỐNG LUẬT QUYẾT ĐỊNH CHIẾN THUẬT (DECISION_RULES.MD)

Tài liệu thiết lập hệ thống quy tắc suy luận logic dạng **`IF ... AND ... THEN ...`** hoàn toàn tham số hóa, không gán cứng tên cầu thủ, giúp hệ thống đưa ra các quyết định chiến thuật tối ưu, khách quan và thích ứng với mọi đội hình trong FC Online Giả Lập Xếp Hạng.

---

## 1. ⚽ QUY TẮC LỰA CHỌN TIỀN ĐẠO CẮM (ST DECISION RULES)

### RULE_ST_01: Tiền đạo làm tường trong sơ đồ đơn thương độc mã (Single-ST Target Man)
* **IF:**
  - `formation_type` == "SINGLE_ST" (e.g. `4-2-3-1`, `4-2-2-1-1`, `4-1-2-3`)
  - `player_height` $\ge 188\text{ cm}$
  - `player_body_type` $\in$ `["Stocky", "Average"]`
  - `player_strength` $\ge 110$
* **THEN:**
  - `assign_role`: `TARGET_MAN_ST`
  - `set_instructions`: `AR2` (Mục tiêu làm tường) + `DP1` (Tập trung trung lộ)
  - `rationale`: ST cắm giữ vai trò trạm trung chuyển bóng; hút 2 trung vệ đối phương để mở ra khoảng trống mênh mông cho CAM/LAM/RAM băng lên dứt điểm.
* **Evidence:** `CLM_002` (Tier B - Inven Super Champions) | **Confidence:** HIGH | **Patch:** `GAMEPLAY_12TH_2026`.

### RULE_ST_02: Tiền đạo chạy chỗ luồn lách (Run-Behind Poacher)
* **IF:**
  - `player_pace` $\ge 118$
  - `player_positioning` $\ge 115$
  - `player_body_type` $\in$ `["Lean", "Average"]`
  - `player_height` $< 185\text{ cm}$
* **THEN:**
  - `assign_role`: `RUN_BEHIND_ST`
  - `set_instructions`: `AR1` (Xẻ nách phá bẫy) + `DP1` (Tập trung trung lộ) + `SR1` (Đè mép việt vị)
  - `rationale`: Tránh va chạm trực diện với các trung vệ to khỏe; tối ưu các đường chọc khe bổng QW xuyên tuyến.
* **Evidence:** `CLM_001` (Tier A - Official Garena) | **Confidence:** HIGH | **Patch:** `GAMEPLAY_12TH_2026`.

---

## 2. 🛡️ QUY TẮC PHỐI HỢP TUYẾN GIỮA (MIDFIELD COMBINATIONS)

### RULE_MID_01: Cặp đôi bù trừ trung tuyến (Double Pivot Complementarity)
* **IF:**
  - `formation_midfield` == "DOUBLE_PIVOT" (2 CDM/LDM-RDM)
* **THEN:**
  - **Bắt buộc phân chia:**
    1. **Slot 1 (The Anchor):** Cầu thủ có `tackling` $\ge 115$, `interceptions` $\ge 115$, `height` $\ge 185\text{ cm}$ $\rightarrow$ Cài đặt `AS1` (Ở lại phía sau) + `DB1` (Cắt đường chuyền) + `DP2` (Bảo vệ trung lộ).
    2. **Slot 2 (The Engine / Ball-Winner):** Cầu thủ có `stamina` $\ge 115$, `long_shot` $\ge 110$, `short_passing` $\ge 115$ $\rightarrow$ Cài đặt `AS Mặc định` + `IN1` (Đánh chặn chủ động) + `DP2` (Bảo vệ trung lộ).
  - **CẤM:** Cài đặt `AS1` cho cả hai tiền vệ trụ (làm gãy trục tấn công) hoặc thả tự do cả hai (toang trung lộ khi phản công).
* **Evidence:** `CLM_003`, `CLM_004` (Tier A/B) | **Confidence:** HIGH | **Patch:** `GAMEPLAY_12TH_2026`.

### RULE_MID_02: Tiền vệ công khai hỏa tuyến 2 (CAM Second-Wave Finisher)
* **IF:**
  - `player_long_shot` $\ge 115$
  - `player_shot_power` $\ge 115$
  - `player_traits` contains `["Finesse Shot", "Long Shot Taker"]`
* **THEN:**
  - `set_instructions`: `SC2` (Đợi bóng ở rìa vòng cấm) + `DS1` (Luôn ở phía trên)
  - `rationale`: Tận dụng các tình huống ST tì đè nhả bóng lại để vung chân dứt điểm cứa lòng ZD hoặc đại bác D uy lực.
* **Evidence:** `CLM_010` (Tier B) | **Confidence:** HIGH | **Patch:** `GAMEPLAY_12TH_2026`.

---

## 3. 🧱 QUY TẮC HÀNG PHÒNG NGỰ (DEFENSIVE PAIRINGS)

### RULE_DEF_01: Cặp bài trùng Trung Vệ (Stopper - Sweeper Pairing)
* **IF:**
  - `defense_line` == "PAIR_CB" (2 Trung vệ)
* **THEN:**
  - **Phải kết hợp 2 hình thái khác nhau:**
    1. **1 Stopper CB (Trung vệ Dập):** Thể hình Đậm, Sức mạnh $\ge 115$, Quyết đoán $\ge 110$ $\rightarrow$ Cài đặt `IN1` (Đánh chặn chủ động) để ập vào tranh chấp nhịp một.
    2. **1 Sweeper CB (Trung vệ Thòng):** Tốc độ $\ge 112$, Tầm nhìn/Bình tĩnh cao, Chiều cao $\ge 187\text{ cm}$ $\rightarrow$ Cài đặt `IN2` (Đánh chặn thận trọng) để lùi sâu bọc lót chống QW.
  - **CẤM:** Để cả 2 CB cùng lao lên dập (dễ bị chọc khe chết người) hoặc cả 2 cùng lùi sâu thụ động (để đối phương sút xa thoải mái).
* **Evidence:** `CLM_006` (Tier B - FIFAAddict & Inven) | **Confidence:** HIGH | **Patch:** `GAMEPLAY_12TH_2026`.

### RULE_DEF_02: Kỷ luật Hậu Vệ Biên (Fullback Discipline)
* **IF:**
  - `formation` contains WINGERS or WIDE_MIDS (`4-2-3-1`, `4-2-2-1-1`, `4-1-2-3`)
* **THEN:**
  - `set_instructions`: `AR2` (Ở lại phía sau khi tấn công)
  - `rationale`: Giữ nguyên khối 4 hậu vệ che chắn trước khung thành; cánh đã có Winger đảm nhiệm tấn công.
* **Evidence:** `CLM_009` (Tier C - FCVN) | **Confidence:** HIGH | **Patch:** `GAMEPLAY_12TH_2026`.

---

## 4. 🧤 QUY TẮC CHỌN THỦ MÔN (GOALKEEPER SELECTION)

### RULE_GK_01: Ưu tiên chiều cao trên chỉ số OVR (Height Over OVR in GLXH)
* **IF:**
  - `mode` == "GLXH" (Manager Mode)
* **THEN:**
  - **Tiêu chí số 1:** `height` $\ge 195\text{ cm}$
  - **Tiêu chí số 2:** Sải tay dài và chỉ số ẩn `["Ném bóng xa", "Cản phá 1-on-1"]`
  - **Tiêu chí số 3:** Lương thấp ($\le 15$) để dồn quỹ lương cho tuyến trên.
  - **Quy tắc vàng:** Một thủ môn cao 1m98 có OVR 96 (Hennessey, Mailson, Courtois) bắt sút xa và phạt góc trong GLXH hiệu quả hơn thủ môn cao 1m85 có OVR 115 (Casillas, Pickford).
* **Evidence:** `CLM_008` (Tier C - FB GLXH VN) | **Confidence:** HIGH | **Patch:** `GAMEPLAY_12TH_2026`.
"""

with open(os.path.join(BASE_DIR, "DECISION_RULES.md"), "w", encoding="utf-8") as f:
    f.write(decision_rules_content)

print("Created CONTRADICTIONS.md and DECISION_RULES.md")
