# 🧠 BỘ NHỚ DỰ ÁN TOÀN DIỆN: FC ONLINE KNOWLEDGE WORKSPACE

## 1. 📌 METADATA DỰ ÁN
* **Tên dự án:** FC Online Knowledge Workspace
* **Thư mục làm việc chính:** `E:\FCOnlineWorkspace`
* **Sub-projects:**
  * `SquadProject/`: Dự án quản lý và cấu hình đội hình 4-1-4-1-0 baseline, cơ sở dữ liệu Trait Engine, Team Color và Luật quyết định.
  * `Research/`: Kho dữ liệu nghiên cứu chuyên sâu, scraper tools, raw datasets.
  * `Screenshots/`: Lưu trữ và phân loại các ảnh chụp màn hình client phục vụ kiểm chứng Ground Truth.
  * `Sources/`: Lưu trữ tài liệu trích xuất từ Garena, Nexon, Inven, FC INFO.
  * `Tools/`: Các script tự động hóa, kiểm toán và tiện ích.
  * `Archive/`: Nơi lưu trữ an toàn các bản sao lưu (.bak) và báo cáo cũ.
* **Server:** Garena FC Online Việt Nam (Gameplay Meta 2026).

---

## 2. 🛡️ TRẠNG THÁI ĐỘI HÌNH THỰC TẾ (STARTING XI 4-1-4-1-0 WING ZERO-ST — TACTIC A CHÍNH THỨC)

```text
                                Karim Benzema BLD +8 (CAM)

Vinícius Jr. CU +8 (LM)                                              Marcos Llorente UT +9/+10 (RM)

            J. Bellingham CU +8 [C] (LCM)        Federico Valverde CU +8 (RCM)

                                   Casemiro CU +8 (CDM)

Ferland Mendy CU +8 (LB)   Antonio Rüdiger CU +8 (LCB)   Éder Militão CU +8 (RCB)   Dani Carvajal CU +8 (RB)

                                    Thibaut Courtois CU +8 (GK)
```

* **Thông tin tài nguyên & Hệ thống (Current Baseline 2026-10-06):**
  * **Sơ đồ thi đấu chính thức:** **4-1-4-1-0 Wing Zero-ST (Tactic A)** (1 CAM + 2 Wings LM/RM + 2 CMs + 1 CDM).
  * **HLV trưởng:** **Dariusz Banasik**.
  * **Tổng quỹ lương:** **298 / 305** (Dư 7 điểm trần lương).
  * **Giá trị đội hình:** **~3.5B – 5.5B BP** (Ground Truth Live) | **BP khả dụng ví:** **529.5M BP**.
  * **2 Tân binh chính thức xuất phát:**
    1. **Antonio Rüdiger CU +8 (LCB Stopper 1m90 / 86kg)**: Thay thế Tchouaméni (về bench xoay tua CDM/CB).
    2. **Marcos Llorente UT +9 (RM Thể lực 119 nền, Chân 5-5)**: Thay thế Rodrygo CU +8 (về bench làm siêu dự bị phút 70).
  * **Khung thành:** Khóa chặt **Thibaut Courtois CU +8 (GK 2m00)**, trait +5 `TM đấm bóng`, HLV +8 `Cản phá sút tầm thấp`.
  * **Thống kê kích hoạt:** 11/11 Real Madrid (đạt Cấp 4: +3 OVR + chỉ số thành phần), 11/11 Mạ Vàng +8~+10.
* **Dự bị (Bench):**
  * Aurélien Tchouaméni CU +8 (Dự bị cao cấp LCB/CDM).
  * Rodrygo CU +8 (Siêu dự bị Super-Sub cánh phải phút 70).
  * Kepa CU +9 (Dự bị phản xạ GK cao cấp 188cm).
  * Luka Modrić CU +8 (Dự bị nhạc trưởng LCM/CAM cao cấp).
  * Koen Casteels 23HW +9 (Cựu GK baseline cao 197cm, giữ nguyên evidence và cấu hình dự bị).
  * R. Ferdinand DC +9 (Dự bị CB cao cấp 189cm).
  * N. Matić VTR +12 (Bạch Kim +12, dự bị CDM khi cần thuần thủ).
  * S. Gerrard UT +8 (Dự bị CM).
  * M. Desailly WG +5 (Dự bị CB).
  * J. Koundé FAC +5 (Dự bị RB/CB).
  * M. Lacroix 25DP +5 (Dự bị CB).
  * Álvaro García 24EP +8 (Dự bị cánh).

---

## 3. ⚖️ KỶ LUẬT NGHIÊN CỨU & XÁC MINH NGUỒN TIN (BẮT BUỘC TUÂN THỦ)

### A. Phân tầng nguồn tin chính thức:
* `Tier A (Official Garena / NEXON):` Nguồn tối thượng cho thể thức giải, cơ chế gameplay, patch notes chính thức.
* `Tier C (In-game Client Screenshots):` Ground Truth tuyệt đối về đội hình, chỉ số, tài nguyên của người dùng.
* `Tier E (FC INFO Structured Data qua NEXON Open API):` **Nguồn tra cứu Exact-card cốt lõi**, bộ lọc đa năng (thể hình, chân, work rate, giá chợ, squad maker).
* `Tier D (FC INFO Manager Mode Board):` Review thực chiến GLXH, meta AI (ưu tiên bài viết có mẫu thử 500–1.000+ trận).
* `Tier E (FIFAAddict):` Đối chiếu chéo raw stats và hệ thống chỉ số ẩn.
* `Tier B (Inven Korea):` Tham khảo meta và góc nhìn cộng đồng Hàn Quốc bổ trợ.

### B. Điều luật `RULE_DATA_01` (CẤM SUY DIỄN / BỊA MÙA THẺ):
* **BẮT BUỘC TRA CỨU TRƯỚC KHI TRẢ LỜI:** Trước khi đưa ra bất kỳ cái tên, chỉ số hay mùa thẻ nào, BẮT BUỘC phải chạy công cụ tra cứu trực tiếp qua FC INFO (`fc-info.com/player/search`) hoặc FIFAAddict để xác nhận 100% thẻ có tồn tại trong game.
* **BÀI HỌC "HARRY KANE CU":** Kane chưa từng vô địch Champions League nên theo quy chế Nexon/Garena, anh không thể có thẻ mùa Champions of Europe (CU). Mọi phát ngôn không có căn cứ từ database chính thức đều bị coi là vi phạm nghiêm trọng kỷ luật dự án.

---

## 4. 🎯 HỆ THỐNG THẨM ĐỊNH MONEYBALL 100 ĐIỂM (RULE_MONEYBALL_01)

* **Triết lý cốt lõi:** *"Đừng săn cầu thủ mạnh nhất. Săn cầu thủ có nhiều stat được tactic sử dụng nhất với chi phí thấp nhất."*
* **Thang điểm 100:**
  1. `Role Fit đúng tactic (30đ)`: Khớp dải stat hành vi của vai trò trong 4-1-2-3-0 WiFi.
  2. `Trait / Special-Trait Fit (20đ)`: Trait tự động (Nỗ lực đến cùng, Tấn công nhịp độ nhanh, Tiki-taka, Tổ chức).
  3. `Physical & Work Profile (15đ)`: Thể hình nạc/trung bình, chiều cao, Work Rate không phá vỡ cấu trúc.
  4. `Ranker Usage & Win Evidence (15đ)`: Bằng chứng thực chiến từ FC INFO / ranker top với mẫu số lớn (>100 trận).
  5. `Salary Efficiency (10đ)`: Lương thấp, giải phóng trần lương 305 cho trục xương sống.
  6. `Giá +8/+9 (10đ)`: Rẻ, dễ tiếp cận, thanh khoản tốt.
* **Điều kiện công nhận "CU Killer":** Tổng $\ge 80/100$, không có điểm chết (fatal flaw) ở stat cốt lõi, test 100 trận in-game không tụt win rate.

---

## 5. ⚔️ BẢN CHUẨN CHIẾN THUẬT V3: 4-1-4-1-0 WING ZERO-ST (`TACTIC_A_41410_BALANCED_WING_ZERO_ST`)

### A. Chiến thuật đội Tactic A (Balanced Wing Zero-ST — Chuẩn Ranker JiHyuk / FC INFO):
* **Phòng thủ:** **Cân bằng (Balanced)** | Rộng **5** | **Sâu (Depth) 4**. (Giải phóng hoàn toàn hiện tượng bó cụm, va chạm và hụt thể lực của Depth 10).
* **Tấn công:** Xây dựng **Cân bằng** | Tạo cơ hội **Chuyền dài (Long Ball)** | Rộng **6** | **Cầu thủ trong vòng cấm = 5** | Phạt góc **2** | Đá phạt **2** | Xu hướng: **Cân bằng / Chung**.
* **Triết lý kiểm soát V3:** *"Giữ cự ly phòng ngự cân bằng (Width 5 / Depth 4) để chống counter và QW; khi chuyển đổi trạng thái, mở biên rộng 6 để 2 cánh bứt tốc đón đường chuyền dài và hút trung vệ cho 2 CMs ập vào dứt điểm tuyến hai."*

### B. Cấu hình Chiến thuật đơn V3 chốt thực chiến:
* **CAM Karim Benzema:** `DS2 / IN / PF / SC1` (Công 3 / Thủ 1) — Ở lại phía trên (`DS2`), Central False 9, nhận bóng quay lưng nhả bóng cho LM/RM, giữ Zone 14 và dứt điểm trong box. Tuyệt đối KHÔNG dùng IN2.
* **LM Vinícius Jr.:** `CC2 / DS1 / IN2 / SC1` (Công 3 / Thủ 2) — Đột phá từ biên vào half-space (`CC2`), hỗ trợ phòng ngự (`DS1`), `IN2` giữ thể lực bứt tốc phút 70–90.
* **RM Marcos Llorente:** `CC1 / DS1 / IN2 / SC2` (Công 3 / Thủ 3) — Tân binh mới thay Rodrygo: Bám biên (`CC1`), tạt bóng điểm rơi, công thủ 3-3 bao sân hỗ trợ Carvajal, chờ rìa box (`SC2`).
* **LCM Jude Bellingham [C]:** `AS / DP1 / IN2 / PF / SC2` (Công 2 / Thủ 3) — Nhạc trưởng giữ nhịp: Giữ vị trí (`PF`), tập trung trung lộ (`DP1`), đánh chặn thận trọng (`IN2`), nã đại bác rìa box (`SC2`).
* **RCM Federico Valverde:** `AS2 / DP1 / IN2 / PF / SC2` (Công 3 / Thủ 3) — Box-to-box runner duy nhất dâng cao đợt hai (`AS2`) khi PIB = 5, tập trung trung lộ (`DP1`), nã đại bác rìa box (`SC2`).
* **CDM Casemiro:** `AS1 / DP1 / DB1 / IN2` (Công 1 / Thủ 3) — Single pivot / Anchor, tuyệt đối ở lại sau (`AS1`), giữ trung lộ (`DP1`), cắt đường chuyền (`DB1`), `IN2` kiềm chế dâng cao.
* **LB Ferland Mendy & RB Dani Carvajal:** `AR2 / IN / SR` (Công 1 / Thủ 3) — Ở lại phía sau (`AR2`), không overlap.
* **LCB Antonio Rüdiger:** `AS / IN2` (Công 1 / Thủ 3) — Tân binh Stopper 1m90 / 86kg: Giữ vị trí (`AS`), đánh chặn thận trọng (`IN2`), không chiến bóng bổng.
* **RCB Éder Militão:** `AS / IN2` (Công 1 / Thủ 3) — Recovery / Cover CB, bọc lót tốc độ cao sau lưng Rüdiger; `IN2` kiềm chế xoạc bóng bẩm sinh.
* **GK Thibaut Courtois:** Cản tạt Cân bằng / Quét Cân bằng (Trấn giữ 2m00 với trait +5 TM đấm bóng và HLV +8 Cản phá sút tầm thấp).

### C. Cấu Trúc Cộng Hưởng 4 Tầng & Ma Trận HLV Mới Nhất (Bản Cập Nhật 07/10/2026):
* **Nguyên lý cốt lõi:** $\text{Innate Traits} + \text{Trait +5} + \text{3 Kỹ năng HLV Tập Luyện} + \text{1 HLV Kỹ năng bổ sung (+8)}$.
* **Luật bất di dịch NEXON:** **Kỹ năng bổ sung từ mốc +8 TUYỆT ĐỐI KHÔNG ĐƯỢC TRÙNG với 3 kỹ năng của HLV Tập Luyện!** Mỗi cầu thủ nhận trọn vẹn 4 kỹ năng HLV khác nhau.
* **Bộ chốt 9 cầu thủ Trait & HLV (Starting XI 4-1-4-1-0 Wing Zero-ST):**
  1. **Vinícius Jr. CU +8 (LM):** +5 `Nỗ lực đến cùng` | HLV: **Michelangelo ★8** (`Khéo léo` / `Phản ứng xâm nhập` / `Xâm nhập box`) | +8 bổ sung: **`Di chuyển ngay khi đỡ bước 1`** (LOCKED).
  2. **Karim Benzema BLD +8 (CAM):** +5 `Thánh chuyền bóng` | HLV: **Ezequiel ★7** (`Chọc khe` / `Đỡ bước 1` / `Chuyền trực tiếp`) | +8 bổ sung: **`Khả năng khéo léo`** (LOCKED False 9 làm tường).
  3. **Marcos Llorente UT +9 (RM):** +5 **`Nỗ lực đến cùng`** (Hồi thể lực cuối trận / khi bị dẫn, Stamina nền 119) | HLV: **Antero Maria (B) ★7** (`Khéo léo` / `Chọc khe` / `Phản ứng xâm nhập`) | +8 bổ sung: **`Tổ chức (Candidate)`** (PROVISIONAL TEST CONFIG — Giả thuyết bọc lót Carvajal, theo dõi 30-50 trận).
  4. **J. Bellingham CU +8 [C] (LCM):** +5 `Nỗ lực đến cùng` | HLV: **Lasse bộ 1 ★8** (`Khéo léo` / `Pressing` / `Tổ chức`) | +8 bổ sung: **`Chiến thuật chuyền trực tiếp`** (LOCKED - #2 CM Garena).
  5. **Federico Valverde CU +8 (RCM):** +5 `Nỗ lực đến cùng` | HLV: **Afanasy ★8** (`Khéo léo` / `Phản ứng xâm nhập` / `Chuyền trực tiếp`) | +8 bổ sung: **`Tổ chức`** (LOCKED giữ vị trí SC2 rìa box).
  6. **Casemiro CU +8 (CDM):** +5 `Siêu cản phá` | HLV: **Lasse ★7** (`Khéo léo` / `Cự ly ổn định` / `Tổ chức`) | +8 bổ sung: **`Khả năng tắc bóng`** (LOCKED — bổ sung công cụ tranh chấp trực tiếp mà không phá vỡ vai Anchor, tránh lặp Đánh chặn vì đã có DB1+IN2).
  7. **Éder Militão CU +8 (RCB):** +5 `Siêu cản phá` | HLV: **José Enrique ★8** (`Khéo léo` / `Tắc bóng` / `Cự ly ổn định`) | +8 bổ sung: **`Tổ chức`** (LOCKED giữ line CB).
  8. **Antonio Rüdiger CU +8 (LCB):** +5 **`Siêu cản phá`** (Giải nguy khu vực nguy hiểm, sải chân 1m90 / 86kg) | HLV: **Lasse (bộ 2) ★8** (`Khéo léo` / `Pressing` / `Phản công khi thủ`) | +8 bổ sung: **`Tổ chức (Candidate)`** (PROVISIONAL TEST CONFIG — Giả thuyết hỗ trợ giữ phẳng line CB, theo dõi 30-50 trận).
  9. **Thibaut Courtois CU +8 (GK):** +5 **`TM đấm bóng`** | HLV Tập Luyện: Mục tiêu 3 skill (`Cản phá sút` / `Cản phá cự ly gần` / `Cản phá khoảng cách trung bình`) | +8 bổ sung: **`Cản phá sút tầm thấp ( Chỉ GK)`** (LOCKED — hóa giải tử huyệt sút chìm của thủ môn 200cm).
* **Dự bị cốt lõi (Bench):** Aurélien Tchouaméni CU +8 (+5 `Nỗ lực đến cùng` / +8 `Tổ chức`), Rodrygo CU +8 (+5 `Nỗ lực đến cùng` / +8 `Xâm nhập vòng cấm`).
* **2 vị trí PENDING (Mendy LB, Carvajal RB):** Giữ nguyên trạng thái `PENDING_3_TRAINING_SKILLS_VERIFICATION`; chỉ khóa kỹ năng +8 thứ tư sau khi kiểm tra chính xác 3 kỹ năng HLV Tập Luyện hiện tại để tránh trùng lặp.
* **Thứ tự ưu tiên gán HLV (Mục tiêu giảm GA thoát Tinh Anh 3):** Militão → Casemiro → Bellingham → Vini → Benzema → Rodrygo → Valverde.
* **Văn bản chi tiết đầy đủ:** Lưu tại [`SquadProject/24_CURRENT_BASELINE_V2_RANK_PUSH.md`](file:///E:/FCOnlineWorkspace/SquadProject/24_CURRENT_BASELINE_V2_RANK_PUSH.md).
* **Master Cơ Sở Dữ Liệu Trait & HLV:** Lưu tại [`SquadProject/23_TRAIT_AND_SKILL_COACH_MASTER_DATABASE.md`](file:///E:/FCOnlineWorkspace/SquadProject/23_TRAIT_AND_SKILL_COACH_MASTER_DATABASE.md).

---

## 6. 👑 LỘ TRÌNH CHUYỂN NHƯỢNG MỤC TIÊU (MONEYBALL ROADMAP)

### A. Giai đoạn 1 — VALUE / CU (Đội hình thực chiến hiện tại):
1. ✅ **ĐÃ HOÀN TẤT:** **Karim Benzema BLD +8 ➔ Mua thành công** (Đảm nhiệm CAM false 9 trung tâm, Havertz CU +8 đã bán).
2. 🥇 **MỤC TIÊU SỐ 1 MUA NGAY (BRIDGE UPGRADE RAM):**
   * **Rodrygo CU +8 (~82.9M BP):** RAM đệm hoàn hảo cho Giai đoạn 1. Giá siêu rẻ (~82.9M, dư gần 100M BP thanh khoản), Lương 27 (tổng lương 294/305), nhỏ, nhanh 117, Agility 118, chọn vị trí 116, chân 4/5, cutback tốt. Giúp trả Bellingham về vị trí trung tâm tự nhiên.
3. ❌ **RÚT KHUYẾN NGHỊ MUA (DISQUALIFIED / DROPPED):**
   * **Luís Figo CU +8 (~202M BP):** Dứt điểm 106 là điểm chết; lãng phí tạt bóng trong sơ đồ Box = 1; trùng vai làm bóng với Modrić và Benzema.
   * **Brahim Díaz CU +8 (~95M BP):** Thể lực 105 và tranh chấp 94 là tử huyệt trong Continuous Pressure Depth 10.
   * **Marcos Llorente UT +8:** Không mua bản trung gian UT; dành BP để lên thẳng **Marcos Llorente WS (Endgame)**.
4. 🥈 **TẠM HOÃN MUA:** **David Alaba CU +8** (chờ giá ổn định; trục Ferdinand + Tchouaméni vẫn đang đá tốt) và **Kepa CU +9** (Casteels vẫn bắt ổn định).

---

### B. Giai đoạn 2 — ENDGAME DREAM TEAM (CHUẨN 305 / 305 LƯƠNG):
* **Kiến trúc đột phá:** Khóa chuẩn xác 100% trần lương $305/305$ nhờ bước đi Moneyball đưa **Thibaut Courtois TC (Lương 13, cao 199cm)** vào gôn, dồn toàn bộ $292$ lương cho 10 quái vật outfield Real Madrid.
* **Đội hình xuất phát 305/305 Endgame:**
  * **LAM:** Vinícius Jr. WS (Lương 30) — Mũi xuyên phá số 1, Bậc thầy chạy chỗ (`DS1 / IN2 / PF / SC1`, Công 3 / Thủ 3).
  * **CAM:** Karim Benzema DCB (Lương 31) — False 9 trung tâm & Finisher trong box, chân 5-5 (`DS2 / IN / PF / SC1`, Công 3 / Thủ 1).
  * **RAM:** Marcos Llorente WS (Lương 31) — Máy chạy pressing không ngừng nghỉ, thể lực 125, chân 5-5 (`DS1 / IN2 / PF / SC1`, Công 3 / Thủ 3).
  * **LCM:** Jude Bellingham SPT (Lương 30) — Balanced connector, giữ nhịp hai chiều, **KHÔNG AS2** (`AS / DP1 / IN2 / PF / SC2`, Công 2 / Thủ 2).
  * **RCM:** Federico Valverde WS (Lương 30) — Second-wave runner duy nhất cài **AS2** (`AS2 / DP1 / IN / PF / SC2`, Công 3 / Thủ 3).
  * **CDM:** David Alaba WS (Lương 29) — Deep distributor / anchor phát động từ đáy sân (`AS1 / DP1 / DB1 / IN2`, Công 1 / Thủ 3).
  * **LB:** Ferland Mendy WS (Lương 28) — Recovery LB, bứt tốc 120, chân 5-5 (`AR2 / IN / SR`, Công 1 / Thủ 3).
  * **LCB:** Aurélien Tchouaméni 25UCL (Lương 28) — Cover CB chỉ huy bọc lót, 188cm/82kg, Chủ Động Cản Phá (`AS / IN`, Công 1 / Thủ 3).
  * **RCB:** Antonio Rüdiger FAC (Lương 27) — Stopper / Recovery CB dập áp sát, 190cm/85kg, Chuyên gia đeo bám (`AS / IN2`, Công 1 / Thủ 3).
  * **RB:** Dani Carvajal CU (Lương 28) — Stay-back RB giữ cấu trúc (`AR2 / IN / SR`, Công 1 / Thủ 3).
  * **GK:** Thibaut Courtois TC (Lương 13) — Moneyball Enabler 199cm, yêu cầu tối thiểu mạ vàng +8 hoặc +9.
* **Lộ trình nâng cấp 5 bước tránh bán tháo:**
  1. *Step 1 (Hiện tại):* Khung Value/CU + mua Rodrygo CU +8 RAM bridge upgrade.
  2. *Step 2 (Real Core):* Mua Courtois TC +8/+9 để đưa GK về 11/11 Real Madrid và giải phóng lương.
  3. *Step 3 (Defensive Engine):* Mua Rüdiger FAC +8, sau đó hoán đổi Alaba WS (CDM) + Tchouaméni 25UCL (LCB Cover).
  4. *Step 4 (Midfield Engine):* Nâng cấp Valverde WS, Bellingham SPT (chuyển về LCM), Mendy WS.
  5. *Step 5 (Luxury Attack):* Chốt hạ bộ ba xa xỉ nhất Vini WS + Benzema DCB + Llorente WS (RAM Endgame).
* **2 Điểm A/B Test Bắt Buộc Trước Khi Khóa Vĩnh Viễn:**
  1. *Alaba WS CDM Single Pivot:* Cao 180cm/76kg có bị đè bởi ST to cao ở bóng bổng/QW Zone 14 không? Cần test thực chiến.
  2. *Mức cộng Courtois TC:* Bắt buộc tối thiểu +8 hoặc +9 để đảm bảo chỉ số phản xạ $\ge 125+$ không trở thành lỗ hổng.

---

## 7. 🛡️ CƠ CHẾ KỸ THUẬT BẢO VỆ CHỐNG HALLUCINATION (3-LAYER DETERMINISTIC GUARDRAIL)

* **Lớp 1 (Data Ingestion — Dữ liệu sạch):**
  * Tuyệt đối KHÔNG gõ tay chỉ số hay ước lượng theo trí nhớ. 
  * Mọi ứng viên bắt buộc phải được lưu trữ trong dataset chuẩn (`SquadProject/16_CAM_CANDIDATE_DATASET.json`) kèm ID và URL trích xuất trực tiếp từ FC INFO.
* **Lớp 2 (Deterministic Execution — Tính toán xác định):**
  * Tuyệt đối CẤM tính nhẩm trong đầu, tự gán điểm hay phán xét thứ hạng cảm tính (như 94, 92, 91).
  * Mọi điểm số Moneyball BẮT BUỘC phải được tính toán tự động qua script Python độc lập (`Tools/Scripts/moneyball_cam_evaluator.py`).
* **Lớp 3 (Verifiable Output — Báo cáo tái lập 100%):**
  * Bảng xếp hạng và điểm số trình bày cho người dùng bắt buộc phải trích xuất trực tiếp từ kết quả chạy thực tế của script Python.
  * Bất kỳ mô hình hay con người nào đưa cùng bộ dữ liệu vào script đều bắt buộc phải ra cùng một kết quả số học duy nhất.

