# 🧭 HỆ THỐNG LUẬT QUYẾT ĐỊNH CHIẾN THUẬT (DECISION_RULES.MD)

Tài liệu thiết lập hệ thống quy tắc suy luận logic dạng **`IF ... AND ... THEN ...`** hoàn toàn tham số hóa, không gán cứng tên cầu thủ, giúp hệ thống đưa ra các quyết định chiến thuật tối ưu, khách quan và thích ứng với mọi đội hình trong FC Online Giả Lập Xếp Hạng.

---

## 1. ⚽ QUY TẮC LỰA CHỌN TIỀN ĐẠO CẮM (ST DECISION RULES)

### RULE_ST_01: Tiền đạo làm tường trong sơ đồ đơn thương độc mã (Single-ST Target Man)
* **IF:**
  - `formation_type` == "SINGLE_ST" (e.g. `4-2-3-1`, `4-2-2-1-1`, `4-1-2-3`)
  - `player_height` $\ge 188	ext{ cm}$
  - `player_body_type` $\in$ `["Stocky", "Average"]`
  - `player_strength` $\ge 110$
* **THEN:**
  - `assign_role`: `TARGET_MAN_ST`
  - `set_instructions`: `AR2` (Mục tiêu làm tường) + `DP2` (Luôn ở trên)
  - `rationale`: ST cắm giữ vai trò trạm trung chuyển bóng; hút 2 trung vệ đối phương để mở ra khoảng trống mênh mông cho CAM/LAM/RAM băng lên dứt điểm.
* **Evidence:** `CLM_002` (Tier B - Inven Super Champions) | **Confidence:** HIGH | **Patch:** `GAMEPLAY_12TH_2026`.

### RULE_ST_02: Tiền đạo chạy chỗ luồn lách (Run-Behind Poacher)
* **IF:**
  - `player_pace` $\ge 118$
  - `player_positioning` $\ge 115$
  - `player_body_type` $\in$ `["Lean", "Average"]`
  - `player_height` $< 185	ext{ cm}$
* **THEN:**
  - `assign_role`: `RUN_BEHIND_ST`
  - `set_instructions`: `AR1` (Xẻ nách phá bẫy) + `DP2` (Luôn ở trên) + `SR1` (Đè mép việt vị)
  - `rationale`: Tránh va chạm trực diện với các trung vệ to khỏe; tối ưu các đường chọc khe bổng QW xuyên tuyến.
* **Evidence:** `CLM_001` (Tier A - Official Garena) | **Confidence:** HIGH | **Patch:** `GAMEPLAY_12TH_2026`.

---

## 2. 🛡️ QUY TẮC PHỐI HỢP TUYẾN GIỮA (MIDFIELD COMBINATIONS)

### RULE_MID_01: Cặp đôi bù trừ trung tuyến (Double Pivot Complementarity)
* **IF:**
  - `formation_midfield` == "DOUBLE_PIVOT" (2 CDM/LDM-RDM)
* **THEN:**
  - **Bắt buộc phân chia:**
    1. **Slot 1 (The Anchor):** Cầu thủ có `tackling` $\ge 115$, `interceptions` $\ge 115$, `height` $\ge 185	ext{ cm}$ $
ightarrow$ Cài đặt `AS1` (Ở lại phía sau) + `DB1` (Cắt đường chuyền) + `DP1` (Tập trung ở trung lộ).
    2. **Slot 2 (The Engine / Ball-Winner):** Cầu thủ có `stamina` $\ge 115$, `long_shot` $\ge 110$, `short_passing` $\ge 115$ $
ightarrow$ Cài đặt `AS Mặc định` + `IN1` (Đánh chặn chủ động) + `DP1` (Tập trung ở trung lộ).
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
    1. **1 Stopper CB (Trung vệ Dập):** Thể hình Đậm, Sức mạnh $\ge 115$, Quyết đoán $\ge 110$ $
ightarrow$ Cài đặt `IN1` (Đánh chặn chủ động) để ập vào tranh chấp nhịp một.
    2. **1 Sweeper CB (Trung vệ Thòng):** Tốc độ $\ge 112$, Tầm nhìn/Bình tĩnh cao, Chiều cao $\ge 187	ext{ cm}$ $
ightarrow$ Cài đặt `IN2` (Đánh chặn thận trọng) để lùi sâu bọc lót chống QW.
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
  - **Tiêu chí số 1:** `height` $\ge 195	ext{ cm}$
  - **Tiêu chí số 2:** Sải tay dài và chỉ số ẩn `["Ném bóng xa", "Cản phá 1-on-1"]`
  - **Tiêu chí số 3:** Lương thấp ($\le 15$) để dồn quỹ lương cho tuyến trên.
  - **Quy tắc vàng:** Một thủ môn cao 1m98 có OVR 96 (Hennessey, Mailson, Courtois) bắt sút xa và phạt góc trong GLXH hiệu quả hơn thủ môn cao 1m85 có OVR 115 (Casillas, Pickford).
* **Evidence:** `CLM_008` (Tier C - FB GLXH VN) | **Confidence:** HIGH | **Patch:** `GAMEPLAY_12TH_2026`.
