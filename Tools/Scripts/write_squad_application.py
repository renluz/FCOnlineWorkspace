import os

BASE_DIR = r"E:\FCOnlineWorkspace\Research"

content = """# 🛡️ ỨNG DỤNG TRI THỨC VÀO ĐỘI HÌNH THỰC TẾ (CURRENT_SQUAD_KNOWLEDGE_APPLICATION.MD)

Tài liệu phân tích chuyên sâu toàn bộ **17 cầu thủ** trong đội hình của bạn (11 cầu thủ đá chính + 6 cầu thủ dự bị) dựa trên hệ thống tri thức, hình thái hành vi AI (Archetypes), sự tương thích chiến thuật và đánh giá rủi ro thực tế trong FC Online Giả Lập Xếp Hạng (Manager Mode — `GAMEPLAY_12TH_2026`).

---

## 1. 📋 DANH SÁCH 11 CẦU THỦ ĐÁ CHÍNH (STARTING ELEVEN)

### 1. 👑 ST: Victor Boniface
* **Archetype Khuyến Nghị:** `TARGET_MAN_ST` (Tiền đạo mục tiêu làm tường / Đè mặt trung vệ).
* **Đặc Điểm Thể Chất & AI:** Chiều cao 1m90, cân nặng 91kg, thể hình Đậm (Stocky), sức mạnh vượt trội, khả năng tì đè giữ bóng và không chiến uy lực.
* **Chiến Thuật Cá Nhân Tương Thích:**
  - `AR2` (Mục tiêu làm tường): Giữ vị trí trung tâm, tì đè hai trung vệ đối phương và nhả bóng thuận lợi cho tuyến hai.
  - `DP1` (Tập trung trung lộ): Không dạt biên lãng phí sức lực, duy trì trục kết nối thẳng với CAM.
* **Độ Tương Thích Sơ Đồ:** Tối ưu 100% trong `4-2-3-1` và `4-2-2-1-1` (sơ đồ 1 tiền đạo cắm cần trạm trung chuyển).
* **Rủi Ro:** Xoay trở chậm trong không gian hẹp; không phù hợp để đua tốc độ quãng dài từ giữa sân (tránh dùng `AR1`).
* **Evidence & Confidence:** `CLM_002` (Tier B - Inven Super Champions) | **Confidence: HIGH**.

---

### 2. 🎯 CAM / LCM: Frank Lampard
* **Archetype Khuyến Nghị:** `BOX_TO_BOX_CM` / `SECOND_WAVE_FINISHER` (Họng pháo tầm xa tuyến hai).
* **Đặc Điểm Thể Chất & AI:** Thể hình Chuẩn, sút xa cực kỳ hiểm hóc, lực sút khủng khiếp, khả năng chọn vị trí thông minh đón bóng nảy.
* **Chiến Thuật Cá Nhân Tương Thích:**
  - Nếu đá CAM: `SC2` (Đợi bóng ở rìa vòng cấm để nã đại bác) + `DS1` (Luôn ở phía trên).
  - Nếu đá LCM: `AS Mặc định` (Tham gia tấn công nhịp hai) + `DP2` (Bảo vệ trung lộ).
* **Độ Tương Thích Sơ Đồ:** Hoàn hảo ở vị trí CAM trong `4-2-3-1` hoặc LCM trong `4-1-2-1-2`.
* **Rủi Ro:** Khả năng thoát pressing bằng rê bóng dắt ở mức trung bình; cần phối hợp 1-2 nhanh.
* **Evidence & Confidence:** `CLM_010` (Tier B - Inven) | **Confidence: HIGH**.

---

### 3. ⚡ LAM / LW: Nicolás González
* **Archetype Khuyến Nghị:** `INVERTED_WINGER` (Tiền đạo cánh nghịch chân cắt vào trong).
* **Đặc Điểm Thể Chất & AI:** Tốc độ xuất phát nhanh, rê bóng khéo léo, khả năng tạt bóng và cứa lòng ZD chân trái chuẩn xác.
* **Chiến Thuật Cá Nhân Tương Thích:**
  - `CC1` (Cắt vào trong) + `IN1` (Đánh chặn chủ động hỗ trợ ép sân biên) + `SR1` (Chạy chỗ đè mặt hậu vệ cánh).
* **Độ Tương Thích Sơ Đồ:** Vị trí LAM/LW trong `4-2-3-1`, `4-1-2-3`.
* **Rủi Ro:** Thể hình mỏng, dễ thất thế khi va chạm tay đôi trực diện với các hậu vệ biên to khỏe.
* **Evidence & Confidence:** `CLM_001` (Tier A) | **Confidence: HIGH**.

---

### 4. 🎨 RAM / CAM: Florian Wirtz
* **Archetype Khuyến Nghị:** `CREATIVE_ENGANCHE` (Nhạc trưởng kiến tạo không gian).
* **Đặc Điểm Thể Chất & AI:** Thể hình Nhỏ/Khéo, nhãn quan sắc bén, chọc khe bổng QW và chọc khe sệt xé toang hàng thủ đối phương.
* **Chiến Thuật Cá Nhân Tương Thích:**
  - `PF1` (Di chuyển tự do tìm khoảng trống) + `SC2` (Chờ bóng tuyến hai phối hợp).
* **Độ Tương Thích Sơ Đồ:** Cực kỳ biến hóa ở vị trí RAM (lệch phải bó trong) của `4-2-3-1` hoặc CAM của `4-1-2-3-0`.
* **Rủi Ro:** Tranh chấp tay đôi yếu, cần có tiền vệ mỏ neo cơ bắp phía sau bọc lót.
* **Evidence & Confidence:** `CLM_001`, `CLM_005` (Tier A/B) | **Confidence: HIGH**.

---

### 5. ⚙️ RDM / RCM: Warren Zaïre-Emery
* **Archetype Khuyến Nghị:** `DYNAMIC_BALL_WINNER` (Máy quét cơ động thu hồi bóng).
* **Đặc Điểm Thể Chất & AI:** Thể lực dồi dào, thăng bằng cao, tốc độ thu hồi bóng nhanh nhẹn, tranh chấp quyết liệt.
* **Chiến Thuật Cá Nhân Tương Thích:**
  - `AS Mặc định` + `IN1` (Đánh chặn chủ động) + `DP2` (Bảo vệ trung lộ).
* **Độ Tương Thích Sơ Đồ:** Cặp đôi bù trừ hoàn hảo với Rodri trong hệ thống Double Pivot `4-2-3-1`.
* **Rủi Ro:** Kinh nghiệm chọn vị trí không chiến trong vòng cấm ở mức vừa phải.
* **Evidence & Confidence:** `CLM_003`, `CLM_004` (Tier A/B) | **Confidence: HIGH**.

---

### 6. ⚓ LDM: Rodri
* **Archetype Khuyến Nghị:** `ANCHOR_CDM` (Mỏ neo tối thượng che chắn hàng phòng ngự).
* **Đặc Điểm Thể Chất & AI:** Chiều cao 1m91, sải chân dài cản phá bóng cực rộng, chỉ số Cắt bóng và Quyết đoán thượng thừa.
* **Chiến Thuật Cá Nhân Tương Thích:**
  - `AS1` (Ở lại phía sau khi tấn công) + `DB1` (Cắt đường chuyền) + `DP2` (Bảo vệ trung lộ).
* **Độ Tương Thích Sơ Đồ:** Trục xương sống bất khả xâm phạm của `4-2-3-1` và `4-2-2-1-1`.
* **Rủi Ro:** Tốc độ bứt tốc đoạn ngắn không quá cao; không được kéo Rodri dâng cao quá nửa sân.
* **Evidence & Confidence:** `CLM_003` (Tier A - Official Garena) | **Confidence: HIGH**.

---

### 7. 🛡️ LB: Joško Gvardiol
* **Archetype Khuyến Nghị:** `COMPLETE_DEFENSIVE_FULLBACK` (Hậu vệ biên công thủ toàn diện).
* **Đặc Điểm Thể Chất & AI:** Chiều cao 1m85, thể hình Đậm/Sức khỏe, chân không thuận 4/5, phòng ngự bóng bổng và tranh chấp cánh cực kỳ an toàn.
* **Chiến Thuật Cá Nhân Tương Thích:**
  - `AR2` (Ở lại phía sau khi tấn công) + `IN2` (Thận trọng giữ vị trí).
* **Độ Tương Thích Sơ Đồ:** LB trong `4-2-3-1`, hoặc có thể hoán đổi đá LCB khi cần gia cố chất thép.
* **Rủi Ro:** Không có rủi ro đáng kể; là một trong những hậu vệ biên toàn diện nhất meta.
* **Evidence & Confidence:** `CLM_007`, `CLM_009` (Tier B/C) | **Confidence: HIGH**.

---

### 8. 🧱 LCB: Marcel Desailly
* **Archetype Khuyến Nghị:** `STOPPER_CB` (Trung vệ dập áp sát tiêu diệt đối thủ).
* **Đặc Điểm Thể Chất & AI:** Thể hình Đậm (Stocky), sức mạnh và quyết đoán tối đa, bật nhảy và tranh chấp tay đôi như một chiếc xe ủi.
* **Chiến Thuật Cá Nhân Tương Thích:**
  - `IN1` (Đánh chặn chủ động / Dập gắt) để chủ động bẻ gãy ý đồ giữ bóng của ST đối phương.
* **Độ Tương Thích Sơ Đồ:** LCB trong mọi hệ thống phòng ngự 4 hậu vệ hoặc 5 hậu vệ.
* **Rủi Ro:** Đôi khi ham dập bóng có thể tạo ra khoảng trống phía sau lưng nếu đối phương chuyền 1 chạm quá nhanh. Cần có Sweeper bọc lót.
* **Evidence & Confidence:** `CLM_006` (Tier B) | **Confidence: HIGH**.

---

### 9. 🧠 RCB: Fabian Schär
* **Archetype Khuyến Nghị:** `COVER_SWEEPER_CB` (Trung vệ thòng bọc lót / Phân phối bóng dài).
* **Đặc Điểm Thể Chất & AI:** Chiều cao 1m88, bình tĩnh cao, phán đoán điểm rơi bóng bổng chuẩn xác, có kỹ năng chuyền dài phát động phản công.
* **Chiến Thuật Cá Nhân Tương Thích:**
  - `IN2` (Đánh chặn thận trọng / Lùi sâu bọc lót khi Desailly dâng dập).
* **Độ Tương Thích Sơ Đồ:** Ghép cặp hoàn hảo với Desailly tạo nên cặp Stopper - Sweeper chuẩn sách giáo khoa.
* **Rủi Ro:** Tốc độ xoay sở ở mức vừa phải; không nên cho dập sớm.
* **Evidence & Confidence:** `CLM_006` (Tier B - Inven) | **Confidence: HIGH**.

---

### 10. ⚡ RB: Gianluca Zambrotta
* **Archetype Khuyến Nghị:** `ELITE_TWO_WAY_FULLBACK` (Hậu vệ biên 5/5 hai chân hoàn hảo).
* **Đặc Điểm Thể Chất & AI:** Tốc độ 121, thể lực 123, phòng ngự 122, hai chân 5/5 thoát pressing biên không tì vết.
* **Chiến Thuật Cá Nhân Tương Thích:**
  - `AR2` (Ở lại phía sau khi tấn công) để khóa chặt cánh phải; chuyển sang `AR1` khi cần dồn quân tìm bàn thắng.
* **Độ Tương Thích Sơ Đồ:** RB số 1 trong mọi sơ đồ GLXH.
* **Rủi Ro:** Không có rủi ro; chỉ số vượt ngưỡng meta.
* **Evidence & Confidence:** `CLM_007` (Tier B - Inven Top 100) | **Confidence: HIGH**.

---

### 11. 🧤 GK: Mailson
* **Archetype Khuyến Nghị:** `GIANT_SHOT_STOPPER_GK` (Thủ môn hộ pháp khép góc).
* **Đặc Điểm Thể Chất & AI:** Chiều cao khủng 1m97, sải tay dài, cản phá các pha cứa lòng ZD góc xa và phạt góc cực kỳ chắc chắn.
* **Chiến Thuật Cá Nhân:** Mặc định của thủ môn (AI tự vận hành theo chiều cao).
* **Rủi Ro:** Khả năng chơi chân phát động bóng ngắn ở mức cơ bản; nên ưu tiên ném bóng xa hoặc phát bóng dài an toàn.
* **Evidence & Confidence:** `CLM_008` (Tier C - Cộng đồng GLXH VN) | **Confidence: HIGH**.

---

## 2. 💺 PHÂN TÍCH 6 CẦU THỦ DỰ BỊ (BENCH ROLES & HYPOTHESES)

### 1. 🔄 Adrien Thomasson
* **Role Fit:** `UTILITY_ATTACKING_SUB` (Dự bị chiến lược đa năng).
* **Điểm Mạnh:** Thể lực tốt, chạy chỗ tích cực quấy rối hàng thủ mệt mỏi của đối phương từ phút 70.
* **Thay Thế Tối Ưu Cho:** Wirtz hoặc González khi cần bổ sung sức chiến đấu biên ở cuối trận.

### 2. 🎯 David Beckham
* **Role Fit:** `SET_PIECE_&_CROSSING_SPECIALIST` (Chuyên gia bóng chết và tạt cánh).
* **Điểm Mạnh:** Những quả tạt bổng cong vút chuẩn xác từng milimet cho Boniface đánh đầu; sút phạt trực tiếp cực kỳ nguy hiểm.
* **Tình Huống Sử Dụng:** Đưa vào sân ở hiệp 2 khi đội nhà bị dẫn bàn và cần các bài tạt cánh đánh đầu gỡ hòa.

### 3. 🧱 Sol Campbell
* **Role Fit:** `IRON_STOPPER_SUB` (Bức tường thép củng cố tỷ số).
* **Điểm Mạnh:** Thể hình Đậm, sức mạnh càn quét kinh hoàng, sẵn sàng vào sân khóa chặt các tiền đạo đối phương.
* **Tình Huống Sử Dụng:** Thay thế Desailly hoặc Schär khi bị dính thẻ vàng hoặc khi cần bảo toàn tỷ số ở 15 phút cuối.

### 4. 🎛️ Rodrigo Zalazar
* **Role Fit:** `TECHNICAL_CENTRAL_MIDFIELDER` (Tiền vệ tổ chức kỹ thuật).
* **Điểm Mạnh:** Xoay sở khéo, chuyền bóng sắc bén, sút xa ổn định.
* **Tình Huống Sử Dụng:** Thay thế Zaïre-Emery hoặc Lampard khi tuyến giữa cần kiểm soát bóng cù cưa ru ngủ đối phương.

### 5. 🌟 Ruud Gullit (Mùa FAC)
* **Role Fit:** `UNIVERSAL_SUPER_SUB` (Quân bài vạn năng thay đổi cục diện).
* **Điểm Mạnh:** Chơi được mọi vị trí từ ST, CAM, CM đến CDM. Chiều cao 1m91, hai chân 5/5, công thủ toàn diện.
* **Tình Huống Sử Dụng:** Cầu thủ dự bị quan trọng nhất đội hình; có thể vào sân thay thế bất kỳ ai từ hàng tiền vệ lên tiền đạo tùy theo diễn biến trận đấu.

### 6. ⚡ Son Heung Min (Mùa PTG)
* **Role Fit:** `CLUTCH_TWO_FOOTED_FINISHER` (Sát thủ kết liễu 2 chân 5/5).
* **Điểm Mạnh:** Tốc độ xé gió, cứa lòng ZD bằng cả hai chân đạt độ hiểm tuyệt đối, khả năng phá bẫy việt vị nhạy bén.
* **Tình Huống Sử Dụng:** Tung vào sân ở phút 60 thay Boniface (đổi lối đá sang phản công nhanh `AR1`) hoặc thay González ở cánh trái để khoan phá hàng thủ đối phương.

---

## 3. 🧩 SƠ ĐỒ ĐỀ XUẤT TỐI ƯU VỚI TOÀN BỘ 17 CẦU THỦ

```
                     [ Boniface (ST) ]
        (Dự bị: Son Heung Min PTG / Gullit FAC)

 [ N. Gonzalez (LAM) ]   [ F. Lampard (CAM) ]   [ F. Wirtz (RAM) ]
 (Sub: Thomasson)        (Sub: Zalazar)          (Sub: D. Beckham)

             [ Rodri (LDM) ]     [ Zaïre-Emery (RDM) ]
             (Anchor - AS1)      (Ball-Winner - AS Def)

[ J. Gvardiol (LB) ] [ M. Desailly (LCB) ] [ F. Schär (RCB) ] [ G. Zambrotta (RB) ]
(Stay Back - AR2)    (Stopper - IN1)       (Sweeper - IN2)    (Stay Back - AR2)
                     (Sub: Sol Campbell)

                         [ Mailson (GK) ]
```
"""

with open(os.path.join(BASE_DIR, "CURRENT_SQUAD_KNOWLEDGE_APPLICATION.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("Created CURRENT_SQUAD_KNOWLEDGE_APPLICATION.md")
