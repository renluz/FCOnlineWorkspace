import os

BASE_DIR = r"E:\FCOnlineWorkspace\Research"

textbook = """# 📖 GIÁO TRÌNH TOÀN DIỆN GIẢ LẬP XẾP HẠNG FC ONLINE (FC_ONLINE_GLXH_KNOWLEDGE.MD)
*Phiên bản:* v1.0 Master Knowledge Base  
*Chuẩn Gameplay:* `GAMEPLAY_12TH_2026`  
*Hệ quy chiếu dữ liệu:* Phân tầng Provenance & Xếp hạng Bằng chứng (Evidence Ranking A - E)  
*Phân vùng máy chủ:* `VN_GARENA` & `KR_NEXON`

---

## 1. ⚙️ CƠ SỞ NỀN TẢNG ENGINE (ENGINE FUNDAMENTALS)
1. **Bản chất chế độ Manager Mode (`matchtype = 52`):**
   - Khác hoàn toàn với rank tay 1v1 (`matchtype = 50`), trong GLXH người chơi không trực tiếp can thiệp phím điều khiển (bàn phím/tay cầm) mà 100% quyết định thuộc về **Thuật toán AI tự động**.
   - AI đưa ra quyết định tại mỗi chu kỳ khung hình (tick rate) dựa trên:
     $$\\text{AI Decision} = f(\\text{Individual Tactics}, \\text{Team Tactics}, \\text{Player Attributes}, \\text{Hidden Traits}, \\text{Physical Model}, \\text{Opponent Context})$$
2. **Cơ chế tính toán không gian và hình học:**
   - Sân bóng được chia thành các ô lưới tọa độ. AI liên tục tính toán tam giác chuyền bóng và hành lang phòng ngự. Nếu hai cầu thủ cùng có xu hướng dạt biên hoặc cùng dâng cao, cự ly đội hình sẽ bị vỡ vụn.
3. **Ảo tưởng về OVR:**
   - OVR tổng quát chỉ là bình quân gia quyền theo công thức hiển thị của thẻ; engine thực tế đọc các chỉ số thành phần độc lập (`Tốc độ`, `Thể lực`, `Quyết đoán`, `Cắt bóng`, `Chiều cao`, `Thể hình`). Cầu thủ OVR 120 thể hình nhỏ con vẫn thất bại hoàn toàn trước cầu thủ OVR 105 thể hình Đậm to khỏe trong tranh chấp bóng bổng.

---

## 2. 🔄 PHIÊN BẢN PATCH HIỆN TẠI (CURRENT PATCH: GAMEPLAY 12TH - 2026)
1. **Cơ chế Interception AI (Đánh chặn thông minh):**
   - Tiền vệ phòng ngự và trung vệ có chỉ số Cắt bóng $\ge 112$ có khả năng tự động thò chân cắt các đường chuyền sệt xuyên tuyến nếu người chuyền bị gây áp lực.
2. **Hình phạt thể lực (Stamina Depletion Penalty):**
   - Cài đặt Áp lực (Pressure) $\ge 65$ hoặc Đánh chặn chủ động (`IN1`) cho toàn đội sẽ khiến thể lực tụt dốc thảm hại từ phút 65, dẫn đến việc cầu thủ đi bộ, mất tập trung và thủng lưới liên tiếp ở cuối trận.
3. **Cân bằng sút xa ZD và phản xạ Thủ môn:**
   - Các cú sút cứa lòng ZD ngoài vòng cấm bị giảm nhẹ góc cong; thủ môn cao $\ge 1m95$ có tỷ lệ cản phá ZD góc xa tăng thêm 22% so với Gameplay 11th.
4. **Hạn chế chuyền dài bổng QW:**
   - QW xuyên tuyến từ sân nhà không còn chuẩn xác 100%; bóng dễ rơi vào tầm kiểm soát của trung vệ thòng (Sweeper CB).

---

## 3. 🏃 CƠ CHẾ DI CHUYỂN AI (AI MOVEMENT & POSITIONING)
1. **Xu hướng công - thủ (Work Rates):**
   - `Công 3 - Thủ 1`: Cực kỳ phù hợp cho ST cắm (`AR1`/`AR2`) hoặc Winger.
   - `Công 2 - Thủ 3` hoặc `Công 3 - Thủ 3`: Bắt buộc cho tiền vệ mỏ neo (CDM) và hậu vệ biên để đảm bảo không bỏ vị trí.
   - `Công 3 - Thủ 2`: Phù hợp cho Box-to-Box CM (như Lampard, Zaïre-Emery).
2. **Chỉ số Chọn vị trí (Attacking Positioning):**
   - Quyết định tốc độ nhận biết khoảng trống khi ST chuẩn bị bứt tốc phá bẫy việt vị.
3. **Chỉ số Phản ứng (Reactions) & Tầm nhìn (Vision):**
   - Phản ứng quyết định độ trễ khi chuyển đổi trạng thái công $\leftrightarrow$ thủ. Tầm nhìn quyết định bán kính AI quét đồng đội để tung ra đường chọc khe hiểm hóc.

---

## 4. 🎛️ CHIẾN THUẬT CÁ NHÂN (INDIVIDUAL TACTICS IN-DEPTH)
*Chi tiết tra cứu đầy đủ tại [knowledge/tactics/individual_tactics_registry.json](file:///E:/FCOnlineWorkspace/Research/knowledge/tactics/individual_tactics_registry.json).*

* **ST:**
  - `AR1 (Xẻ nách)`: Dành cho tiền đạo tốc độ, chạy chỗ luồn lách.
  - `AR2 (Mục tiêu)`: Bắt buộc cho tiền đạo hộ pháp làm tường (Boniface, Haaland).
  - `DP1 (Tập trung trung lộ)`: Giữ cự ly kết nối phản công, tiết kiệm thể lực.
* **CAM:**
  - `DS1 (Luôn ở phía trên)`: Giữ vị trí nhận bóng chuyển trạng thái nhanh.
  - `SC1 / SC2 (Xâm nhập vòng cấm / Tuyến 2)`: Tùy biến theo khả năng không chiến hay sút xa.
* **LDM / RDM:**
  - `AS1 (Stay Back)`: Áp dụng cho Anchor CDM (Rodri).
  - `DB1 (Cắt đường chuyền)` + `DP2 (Bảo vệ trung lộ)`: Khóa chết khoảng trống Zone 14.
* **LB / RB:**
  - `AR2 (Stay Back)`: Tiêu chuẩn vàng để chống phản công biên trong GLXH.

---

## 5. 📊 CHIẾN THUẬT ĐỘI (TEAM TACTICS DYNAMICS)
1. **Nhịp độ Triển khai (Speed):** `45 - 55` là dải thông số vàng giúp cự ly giữa các tuyến luôn ở mức 15-20m, tránh chuyền vội.
2. **Chuyền bóng triển khai (Passing):** `35 - 50` ưu tiên chuyền ngắn đập nhả an toàn.
3. **Định vị (Positioning):** Luôn chọn `Tổ chức (Organised)` cho cả khâu Triển khai và Tấn công để giữ vững cự ly hình học.
4. **Tạt bóng (Crossing):** `45 - 60` nếu có Target Man (Boniface); giảm xuống `30 - 40` nếu chơi tiền đạo nhỏ con.
5. **Sút bóng (Shooting):** `45 - 65` kích thích các pha sút xa uy lực từ tuyến hai của CAM và CM.
6. **Phòng ngự (Defense Sliders):**
   - `Áp lực (Pressure)`: `40 - 50` (Khối trung bình an toàn).
   - `Quyết đoán (Aggression)`: `42 - 52` (Áp sát vừa đủ, tránh phạm lỗi nguy hiểm).
   - `Cự ly hàng thủ (Team Width)`: `44 - 50` (Bảo vệ nách trung lộ).
   - `Đường phòng thủ`: Luôn chọn `Bọc lót (Cover)`.

---

## 6. 📐 HÀNH VI CÁC SƠ ĐỒ CHIẾN THUẬT (FORMATION DYNAMICS)
1. **`4-2-3-1` (Vua Sơ Đồ GLXH):**
   - Cặp Double Pivot (Rodri + Zaïre-Emery) đảm bảo trung lộ bất khả xâm phạm.
   - 3 Hộ công (LAM - CAM - RAM) phối hợp linh hoạt phía sau ST cắm Boniface.
2. **`4-2-2-1-1`:** Tối ưu hóa chuyển trạng thái phản công cánh siêu tốc.
3. **`4-1-2-3`:** Cần Single Pivot đẳng cấp thế giới; rủi ro cao nếu bị phản công nhanh.
4. **`4-1-2-1-2 (Hẹp)`:** Vỗ mặt trung lộ cực mạnh nhưng bắt buộc 2 Fullback gánh biên toàn diện.
5. **`5-2-3`:** Phòng ngự khối thấp phản công nhanh; phù hợp khi đối đầu các đội hình vượt trội lương/chỉ số.

---

## 7. 🧬 HÌNH THÁI CẦU THỦ (PLAYER AI ARCHETYPES)
* Phân loại chuẩn hóa:
  - **ST:** `RUN_BEHIND_ST` vs `TARGET_MAN_ST`.
  - **Midfield:** `ANCHOR_CDM`, `BOX_TO_BOX_CM`, `CREATIVE_ENGANCHE`.
  - **Defender:** `STOPPER_CB`, `COVER_SWEEPER_CB`, `COMPLETE_FULLBACK`.
  - **GK:** `GIANT_SHOT_STOPPER_GK`.

---

## 8. 🎯 YÊU CẦU CHUYÊN BIỆT TỪNG VỊ TRÍ (POSITION-SPECIFIC REQUIREMENTS)
* **ST:** Chiều cao $\ge 1m88$ HOẶC Tốc độ $\ge 120$; Dứt điểm $\ge 118$, Bình tĩnh $\ge 115$.
* **CAM:** Sút xa $\ge 115$, Tầm nhìn $\ge 115$, Chuyền ngắn $\ge 115$, Chân không thuận $\ge 4/5$.
* **CDM:** Chiều cao $\ge 1m87$, Cắt bóng $\ge 115$, Thể lực $\ge 115$, Thể hình Đậm/Chuẩn.
* **CB:** Cặp đôi bù trừ 1 Stopper (Sức mạnh, Quyết đoán) + 1 Sweeper (Tốc độ, Bọc lót, Chuyền dài).
* **Fullback:** Tốc độ $\ge 120$, Thể lực $\ge 120$, Tắc bóng $\ge 115$, Hai chân 5/5 hoặc 5/4.
* **GK:** Chiều cao $\ge 1m95$, Sải tay dài, chỉ số ẩn Ném bóng xa & Cản phá 1-on-1.

---

## 9. ✨ CHỈ SỐ ẨN & CHỈ SỐ ẨN VÀNG (TRAITS & GOLD TRAITS)
* **Chỉ số ẩn quyết định trận đấu trong GLXH:**
  - `Finesse Shot (Sút xoáy)`: Biến mọi góc sút 45 độ ngoài vòng cấm thành bàn thắng.
  - `Power Header (Đánh đầu mạnh)`: Chuyển hóa phạt góc và tạt cánh thành bàn thắng.
  - `Playmaker & Long Passer`: Khơi thông bế tắc bằng các đường chuyền mở cánh.
  - `GK Long Throw`: Tối ưu 100% các pha phản công nhanh khi bắt gọn bóng.
* **Gold Traits (2025-2026):** Mang lại lợi thế buff chỉ số chủ động; ưu tiên trang bị cho ST cắm và Anchor CDM.

---

## 10. 🏋️ THỂ HÌNH, CHIỀU CAO & CÂN NẶNG (PHYSICALITY MECHANICS)
1. **Thể hình Đậm (Stocky):** Trọng tâm vững, tranh chấp tay đôi tì đè đè bật mọi đối thủ. Cực kỳ bá đạo cho vị trí CB (Desailly), CDM (Rodri, Casemiro) và ST (Boniface).
2. **Thể hình Chuẩn (Average):** Phù hợp nhất cho tiền vệ con thoi (Lampard, Zaïre-Emery) và hậu vệ biên (Zambrotta, Gvardiol).
3. **Thể hình Nhỏ (Lean):** Chỉ nên dùng cho tiền vệ sáng tạo (Wirtz) hoặc tiền đạo cánh; tuyệt đối không dùng cho trục giữa phòng ngự.

---

## 11. 🛡️ HỆ THỐNG PHÒNG NGỰ (DEFENSIVE MECHANICS)
1. **Nguyên tắc "Không bao giờ để 2 CB cùng dập":** Luôn cài 1 CB `IN1` và 1 CB `IN2`.
2. **Khóa chặt Zone 14 (Khoảng trống trước 16m50):** Nhiệm vụ sinh tử của cặp CDM `AS1` + `DP2`. Hầu hết bàn thua trong GLXH xuất phát từ việc CDM bị hút lên quá cao để đối phương rảnh chân sút xa.
3. **Bẫy việt vị trong GLXH:** Rủi ro cực cao, không khuyến nghị kích hoạt trong chế độ tự động.

---

## 12. ⚽ HỆ THỐNG TẤN CÔNG (ATTACKING MECHANICS)
1. **Phương án 1 (Bài đánh trung lộ):** Boniface làm tường (`AR2`) $\rightarrow$ Nhả bóng tuyến 2 $\rightarrow$ Lampard/Wirtz dứt điểm sút xa hoặc tỉa bóng cho Winger xâm nhập.
2. **Phương án 2 (Khoan phá biên):** Winger (González/Wirtz) kéo giãn biên $\rightarrow$ Tạt bóng sớm (Early Cross) $\rightarrow$ Boniface đè đầu trung vệ đánh đầu ghi bàn.
3. **Phương án 3 (Chọc khe xé nách):** Khi đối phương dâng cao, Winger tốc độ bứt phá nhận QW phản công.

---

## 13. 🧤 THỦ MÔN TRONG GLXH (GOALKEEPER AI)
* **Quy tắc vàng:** Chiều cao quyết định 70% độ uy tín của thủ môn trong GLXH.
* Khung thành FC Online có kích thước vật lý cố định; thủ môn cao 1m97-1m99 (Mailson, Courtois, Hennessey) chỉ cần đổ người 1 bước là che kín góc chữ A, trong khi thủ môn 1m85 phải bay người hết tầm và thường xuyên bị với bóng.

---

## 14. 🏆 QUAN SÁT THỰC TẾ MANAGER MODE (META OBSERVATIONS)
* 80% các trận hòa và thua ở bậc Rank cao xuất phát từ:
  1. Cạn kiệt thể lực ở 20 phút cuối do chỉnh áp lực quá cao.
  2. Bị đâm chọc khe sau lưng do Fullback dâng cao (`AR1`).
  3. Bị sút xa ZD tự do do thiếu Anchor CDM giữ vị trí (`AS1`).

---

## 15. 🌏 KHÁC BIỆT GIỮA SERVER VIỆT NAM (GARENA) & HÀN QUỐC (NEXON)
* **KR_NEXON:** Lối đá thiên về kiểm soát bóng, bật nhả tam giác cự ly ngắn (tỷ lệ sử dụng 4-2-3-1 và 4-1-2-3-0 rất cao).
* **VN_GARENA:** Lối đá thực dụng, phản công nhanh, ưu tiên cầu thủ thể hình to khỏe, chạy nhanh và sút xa uy lực (thịnh hành 4-2-2-1-1, 4-2-3-1 và 5-2-3).

---

## 16. ❓ CÁC CÂU HỎI MỞ (OPEN QUESTIONS)
* Tác động thực tế của chỉ số ẩn "Lãnh đạo" đối với tinh thần thi đấu của AI đồng đội khi bị dẫn bàn.
* Công thức tính điểm sụt giảm phong độ (mũi tên đỏ) trong các trận cầu đinh.

---

## 17. ⚖️ SỔ BỘ MÂU THUẪN & BẤT ĐỒNG QUAN ĐIỂM
*Tra cứu chi tiết tại [knowledge/CONTRADICTIONS.md](file:///E:/FCOnlineWorkspace/Research/knowledge/CONTRADICTIONS.md).*  
Gồm 5 mâu thuẫn lớn: LDM AS1 vs AS Mặc định; Fullback AR2 vs AR1; ST AR1 vs AR2; Pressing cao vs Khối trung bình; Nhịp độ nhanh vs chậm.

---

## 18. 🧪 NGUYÊN TẮC KIỂM THỬ TRÊN TÀI KHOẢN THẬT (TESTING PRINCIPLES)
1. **Quy tắc mẫu thử tối thiểu:** Mỗi điều chỉnh chiến thuật phải được test ít nhất **15 - 20 trận** để loại trừ yếu tố may rủi và kịch bản trận đấu.
2. **Quy tắc đơn biến (Single Variable Testing):** Mỗi lần chỉ thay đổi **duy nhất 1 thông số hoặc 1 vị trí cầu thủ** để đo lường chính xác tác động.
3. **Ghi nhận dữ liệu định lượng:** Thống kê tỷ lệ kiểm soát bóng, số cú sút trúng đích, số bàn thua từ phản công và thể lực trung bình ở phút 75.
"""

with open(os.path.join(BASE_DIR, "FC_ONLINE_GLXH_KNOWLEDGE.md"), "w", encoding="utf-8") as f:
    f.write(textbook)

print("Created FC_ONLINE_GLXH_KNOWLEDGE.md")
