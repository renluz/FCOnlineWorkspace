# 📋 BÁO CÁO TOÀN DIỆN CÀI ĐẶT ĐỘI HÌNH HIỆN TẠI (BASELINE IN-GAME 11/10/2026)

* **Mã tài liệu:** `SQUAD_BASELINE_REPORT_20261011`
* **Thời điểm xác lập:** 2026-10-11 11:30:00 (UTC+7)
* **Người thực hiện:** AI Specialist & Antigravity Pair Programming
* **Căn cứ nguồn sự thật (Ground Truth):** Đồng bộ trực tiếp từ 4 ảnh chụp màn hình client game ngày 11/10/2026 và bộ dữ liệu cấu hình đã nghiệm thu tại [`SquadProject/02_CURRENT_SQUAD.json`](file:///E:/FCOnlineWorkspace/SquadProject/02_CURRENT_SQUAD.json), [`SquadProject/03_CURRENT_TACTICS.json`](file:///E:/FCOnlineWorkspace/SquadProject/03_CURRENT_TACTICS.json), [`SquadProject/04_PLAYER_CONFIGS.json`](file:///E:/FCOnlineWorkspace/SquadProject/04_PLAYER_CONFIGS.json), [`SquadProject/11_TEAM_COLOR_RULES.json`](file:///E:/FCOnlineWorkspace/SquadProject/11_TEAM_COLOR_RULES.json).

---

## 1. ⚙️ TỔNG QUAN TÀI NGUYÊN & HỆ THỐNG ĐỘI BÓNG

* **Sơ đồ thi đấu:** **4-1-2-3-0** (1 False 9 CAM + 2 Cánh LAM/RAM + 2 Tiền vệ trung tâm LCM/RCM + 1 Mỏ neo CDM).
* **HLV Trưởng:** **Amund Skiri**.
* **Preset Chiến thuật:** `2. Mặc định` (`TACTIC_B_41230_GAMEDAY_BASELINE`).
* **Tổng quỹ lương:** **300 / 305** (Dư 5 điểm trần lương).
* **Giá trị đội hình hiển thị:** **2.94B BP**.
* **Số dư ví BP khả dụng:** **837.155M BP** (Ảnh 1) / Cập nhật sau các giao dịch ngày 11/10: **1.154B BP**.
* **Hiệu ứng Team Color (Đối chiếu nghiêm ngặt `11_TEAM_COLOR_RULES.json`):**
  - **Mạ Vàng (+8~+10):** 11/11 cầu thủ đá chính đạt mức +8 → **+3 OVR** (verified theo `11_TEAM_COLOR_RULES.json`).
  - **Real Madrid club color:** cluster trong rules file hiện chỉ có 1/11 (F. Mendy) — dữ liệu chưa đầy đủ, **không kết luận** 11/11. Cần kiểm chứng trực tiếp trong game (màn hình team color) trước khi ghi nhận.
  - *Lưu ý:* Mọi ước tính về tổng OVR cộng dồn từ Team Color CLB ở thời điểm hiện tại đều là giả thuyết chưa được xác minh toàn diện.

---

## 2. 🛡️ CHIẾN THUẬT ĐỘI (TEAM TACTICS)

> [!WARNING]
> **CẢNH BÁO BẪY THỂ LỰC (PR-05 WARNING):** Đội hình đang kích hoạt combo cực đoan: **Depth 10** + **Áp lực ngay khi mất bóng** + **Tổng tấn công**. Toàn đội sẽ dâng rất cao để vây ráp ngay khi mất bóng; từ phút 70–90 nguy cơ cạn thể lực rất lớn nếu cầu thủ không có Thể lực nền $\ge 130$ hoặc chỉ số ẩn *Nỗ lực đến cùng*.

### A. Phòng Thủ (Defense)
| Thông Số | Cài Đặt In-Game | Diễn Giải Thực Chiến |
| :--- | :---: | :--- |
| **Lối phòng thủ** | **Áp lực ngay khi mất bóng** | Tự động pressing tầm cao cực mạnh ngay trong 5–7 giây đầu sau khi mất quyền kiểm soát. |
| **Độ rộng (Width)** | **5** (Cân bằng) | Giữ cự ly 4 hậu vệ và 1 CDM ở mức trung tiêu chuẩn, không bị dạt biên quá mức. |
| **Độ sâu / Thấp (Depth)** | **10** (Cực cao/Dâng kịch khung) | Toàn bộ khối phòng ngự đẩy lên sát vạch giữa sân để bóp nghẹt không gian đối phương. |

### B. Tấn Công (Offense)
| Thông Số | Cài Đặt In-Game | Diễn Giải Thực Chiến |
| :--- | :---: | :--- |
| **Lối chơi xây dựng** | **Chuyền dài (Long Ball)** | Tuyến dưới và tiền vệ ưu tiên phất bóng dài vượt tuyến ra sau lưng hàng thủ đối phương. |
| **Tạo cơ hội** | **Chuyền dài (Long Ball)** | Cầu thủ tấn công chủ động bứt tốc đón đường chuyền điểm rơi/chọc khe bổng (QW). |
| **Độ rộng tấn công** | **5** (Cân bằng) | Cự ly phân phối bóng hài hòa giữa trung lộ và 2 nách. |
| **Cầu thủ trong vòng cấm (PIB)**| **3** | Chỉ có 3 mũi nhọn chủ lực (Mbappé LAM, Benzema CAM, Valverde RCM dâng đợt hai) ập vào box đón bóng. |
| **Phạt góc (Corners)** | **1** | Phòng ngự tối đa, chống đối phương phản công nhanh. |
| **Đá phạt (Free Kicks)** | **1** | Chỉ bố trí tối thiểu người dâng cao, giữ cự ly bọc lót. |
| **Xu hướng chung** | **Tổng tấn công** | Đẩy cao toàn bộ nhịp độ và cự ly dâng của đội hình về phần sân đối phương. |

---

## 3. 🎯 VAI TRÒ CỐ ĐỊNH & BAN CÁN SỰ (SET PIECES & ROLES)

| Vai Trò | Cầu Thủ Đảm Nhiệm | Trạng Thái Kiểm Chứng |
| :--- | :--- | :---: |
| **Đội trưởng (Captain)** | **Karim Benzema BLD +8** | ✅ **VERIFIED** *(Xác nhận có huy hiệu `[C]` trong Ảnh 1)* |
| **Sút phạt đền (Penalty)** | Karim Benzema BLD +8 | ⚠️ *UNVERIFIED_FROM_GAME (Tạm giữ theo baseline)* |
| **Phạt góc cánh trái (L-Corner)**| Jude Bellingham GRU +8 | ⚠️ *UNVERIFIED_FROM_GAME (Tạm giữ theo baseline)* |
| **Phạt góc cánh phải (R-Corner)**| Jude Bellingham GRU +8 | ⚠️ *UNVERIFIED_FROM_GAME (Tạm giữ theo baseline)* |
| **Đá phạt trực tiếp gần (FK)** | Karim Benzema BLD +8 | ⚠️ *UNVERIFIED_FROM_GAME (Tạm giữ theo baseline)* |
| **Đá phạt trực tiếp xa (Long FK)**| Federico Valverde CU +8 | ⚠️ *UNVERIFIED_FROM_GAME (Tạm giữ theo baseline)* |

---

## 4. 👥 CHI TIẾT 11 CẦU THỦ ĐÁ CHÍNH (STARTING XI 4-1-2-3-0)

### 4.1. Hàng Tiền Đạo & Tiền Vệ Công (Front Three)

```text
               K. Mbappé UT +8 (LAM)      K. Benzema BLD +8 [C] (CAM)      Luís Figo UT +8 (RAM)
```

#### 1. CAM: Karim Benzema BLD +8 [C] — *Nhạc Trưởng / False 9 Trung Tâm*
* **Thông số cơ bản:** OVR **144** | Lương **29** | Thể hình 185cm / 81kg | Chân 4-5.
* **Chiến thuật đơn:** `DS2 / IN / PF / SC1` (Công 3 / Thủ 1)
  * `DS2`: Ở lại phía trên (giữ thể lực, không lùi sâu).
  * `IN`: Đánh chặn thông thường.
  * `PF`: Duy trì vị trí (khóa chặt Zone 14 trước vòng cấm).
  * `SC1`: Xâm nhập vòng cấm (khi có cơ hội dứt điểm).
* **Chỉ số ẩn gốc:** Sút và tạt má ngoài, Đánh đầu mạnh, Kiến tạo, Sút xoáy.
* **Trait +5:** *Chờ kiểm toán client*.
* **HLV Tập Luyện:** **Antero Maria ★8** *(3 kỹ năng chi tiết: PENDING_SCREENSHOT)*.
* **Kỹ năng bổ sung +8:** **`Khả năng khéo léo`** (Hỗ trợ tì đè xoay lưng làm tường).

#### 2. LAM: Kylian Mbappé UT +8 — *Inside Runner Khoan Phá Cánh Trái*
* **Thông số cơ bản:** OVR **142** | Lương **29** | Thể hình 182cm / 75kg | Chân 4-5 | Tốc độ > 150.
* **Chiến thuật đơn:** `CC2 / DS1 / IN2 / SC1` (Công 3 / Thủ 2) *(UNVERIFIED dropdown)*
  * `CC2`: Cắt vào trong (đột phá nách half-space).
  * `DS1`: Luôn hỗ trợ phòng ngự.
  * `IN2`: Đánh chặn thận trọng (bảo tồn thể lực bứt tốc).
  * `SC1`: Xâm nhập vòng cấm đón căng ngang/chọc khe.
* **Chỉ số ẩn gốc:** Sút xoáy, Sút và tạt má ngoài, Bấm bóng, Đánh đầu mạnh, Ma tốc độ, Qua người.
* **Trait +5:** *Tinh thần chiến đấu*.
* **HLV Tập Luyện:** **Michelangelo ★8** *(Khéo léo / Phản ứng xâm nhập / Xâm nhập vòng cấm)*.
* **Kỹ năng bổ sung +8:** **`Di chuyển ngay khi đỡ bước 1`** (Tăng tốc tức thì khi nhận Long Ball).

#### 3. RAM: Luís Figo UT +8 — *Máy Tạt Bám Biên & Chống Phản Công Phải*
* **Thông số cơ bản:** OVR **142** | Lương **29** | Thể hình 180cm / 75kg | Chân 4-5 | Thể lực 144.
* **Team Color (chưa xác minh):** Figo UT có thể không hưởng trọn team color Real Madrid như các thẻ mùa CLB khác do khác thế hệ mùa thẻ — cần kiểm chứng trực tiếp trong game. File `11_TEAM_COLOR_RULES.json` hiện chưa có quy tắc season-specific nên mọi con số chênh lệch OVR ở đây chỉ là giả thuyết.
* **Chiến thuật đơn:** `CC1 / DS1 / IN2 / SC2` (Công 3 / Thủ 3) *(UNVERIFIED dropdown)*
  * `CC1`: Bám biên (kéo dãn hàng thủ đối phương).
  * `DS1`: Luôn hỗ trợ phòng ngự (bọc lót hành lang phải cho Carvajal).
  * `IN2`: Đánh chặn thận trọng.
  * `SC2`: Chờ ngoài rìa vòng cấm đón bóng hai nã đại bác.
* **Chỉ số ẩn gốc:** Sút xa, Ma tốc độ.
* **Trait +5:** *Nỗ lực đến cùng* (Hồi thể lực cuối trận).
* **HLV Tập Luyện:** **Raymond ★8** *(3 kỹ năng chi tiết: PENDING_SCREENSHOT)*.
* **Kỹ năng bổ sung +8:** **`Tổ chức (Candidate)`** (Hỗ trợ kỷ luật cự ly).

---

### 4.2. Tuyến Tiền Vệ Trung Tâm & Mỏ Neo (Midfield Engine & Single Pivot)

```text
               J. Bellingham GRU +8 (LCM)                     F. Valverde CU +8 (RCM)
               
                                      D. Alaba CU +8 (CDM)
```

#### 4. LCM: Jude Bellingham GRU +8 — *Tiền Vệ Giữ Nhịp & Thoát Pressing (Regista)*
* **Thông số cơ bản:** OVR **143** | Lương **28** | Thể hình 186cm / 75kg | Chân 4-5.
* **Chiến thuật đơn:** `AS / DP1 / IN2 / PF / SC2` (Công 2 / Thủ 3)
  * `AS`: Tấn công cân bằng (không lao lên tùy tiện).
  * `DP1`: Tập trung trung lộ (bảo vệ khoảng trống trung tâm).
  * `IN2`: Đánh chặn thận trọng (không lao dập ẩu).
  * `PF`: Duy trì vị trí.
  * `SC2`: Chờ ngoài rìa vòng cấm.
* **Chỉ số ẩn gốc:** Qua người, Sút xa, Đánh đầu mạnh, Kiến tạo, Tinh tế.
* **Trait +5:** *Tinh thần chiến đấu*.
* **HLV Tập Luyện:** **Antero Maria ★7** *(3 kỹ năng chi tiết: PENDING_SCREENSHOT)*.
* **Kỹ năng bổ sung +8:** **`Chiến thuật chuyền trực tiếp`** (Phân phối bóng chuẩn xác tuyến trên).

#### 5. RCM: Federico Valverde CU +8 — *Box-to-Box Runner / Nã Đại Bác Rìa Box*
* **Thông số cơ bản:** OVR **141** | Lương **27** | Thể hình 182cm / 78kg | Chân 4-5 | Thể lực dồi dào.
* **Chiến thuật đơn:** `AS2 / DP1 / IN2 / PF / SC2` (Công 3 / Thủ 3)
  * `AS2`: **Tham gia tấn công** (Cầu thủ duy nhất ở trung tuyến được dâng cao đợt hai).
  * `DP1`: Tập trung trung lộ.
  * `IN2`: Đánh chặn thận trọng.
  * `PF`: Duy trì vị trí.
  * `SC2`: Chờ ngoài rìa vòng cấm (đón bóng hai dứt điểm).
* **Chỉ số ẩn gốc:** Sút và tạt má ngoài, Chuyền dài, Sút xa, Ma tốc độ.
* **Trait +5:** *Tinh thần chiến đấu*.
* **HLV Tập Luyện:** **Afanasy ★8** *(Khéo léo / Phản ứng xâm nhập / Chuyền trực tiếp)*.
* **Kỹ năng bổ sung +8:** **`Tổ chức`** (Kỷ luật cự ly, tránh bị hút người bỏ lại Zone 14).

#### 6. CDM: David Alaba CU +8 — *Single Pivot / Mỏ Neo Chặn Cửa Zone 14*
* **Thông số cơ bản:** OVR **141** | Lương **27** | Thể hình 180cm / 78kg | Chân 4-5 | Chuyền dài & Phản xạ cắt bóng cao.
* **Chiến thuật đơn:** `AS1 / DP1 / DB1 / IN2` (Công 1 / Thủ 3) *(UNVERIFIED dropdown)*
  * `AS1`: **Ở lại phía sau khi tấn công** (Khóa cứng vị trí mỏ neo).
  * `DP1`: Tập trung trung lộ.
  * `DB1`: **Cắt đường chuyền** (Chủ động giăng bẫy bắt bài bóng sệt).
  * `IN2`: Đánh chặn thận trọng (ghìm bản năng xoạc bóng bẩm sinh).
* **Chỉ số ẩn gốc:** Xoạc bóng, Chuyền dài, Sút xa, Cứng như thép.
* **Trait +5:** *Chờ kiểm toán client*.
* **HLV Tập Luyện:** **Lasse ★7** *(Khéo léo / Cự ly ổn định / Tổ chức)*.
* **Kỹ năng bổ sung +8:** **`Khả năng tắc bóng`** (Bổ sung sức mạnh tranh chấp tay đôi).

---

### 4.3. Tuyến Phòng Ngự & Khung Thành (Backline & Goalkeeper)

```text
F. Mendy CU +8 (LB)   A. Rüdiger CU +8 (LCB)   Éder Militão CU +8 (RCB)   Carvajal CU +8 (RB)

                                T. Courtois CU +8 (GK)
```

#### 7. LB: Ferland Mendy CU +8 — *Hậu Vệ Biên Thuần Thủ / Khóa Cánh Trái*
* **Thông số cơ bản:** OVR **139** | Lương **26** | Thể hình 180cm / 73kg | Hai chân 5-5.
* **Chiến thuật đơn:** `AR2 / IN / SR` (Công 1 / Thủ 3)
  * `AR2`: Ở lại phía sau khi tấn công.
  * `IN`: Đánh chặn bình thường.
  * `SR`: Không dâng cao chồng biên (giữ chặt hàng thủ 4 người).
* **HLV Tập Luyện:** **Rodolfo ★7** *(3 kỹ năng chi tiết: PENDING_SCREENSHOT)*.

#### 8. LCB: Antonio Rüdiger CU +8 — *Trung Vệ Dập Hộ Pháp (Aggressive Stopper)*
* **Thông số cơ bản:** OVR **140** | Lương **26** | **190cm / 86kg** | Thể hình Sức khỏe | Chân 4-5.
* **Chiến thuật đơn:** `Stopper / AS / IN2` (Công 1 / Thủ 3)
  * Vai trò: Trung vệ dập áp sát (Stopper), không chiến và càn quét tiền đạo mục tiêu.
  * `AS`: Ở lại phía sau khi tấn công.
  * `IN2`: Đánh chặn thận trọng (tránh bị đối phương vỗ mặt bật nhả loại bỏ).
* **HLV Tập Luyện:** **Lasse ★8** *(Khéo léo / Pressing / Phản công khi thủ)*.
* **Kỹ năng bổ sung +8:** **`Tổ chức (Candidate)`** (Giữ phẳng tuyến việt vị cùng Militão).

#### 9. RCB: Éder Militão CU +8 — *Trung Vệ Thòng Tốc Độ (Recovery Cover)*
* **Thông số cơ bản:** OVR **140** | Lương **27** | 186cm / 78kg | Tốc độ xuất sắc.
* **Chiến thuật đơn:** `Cover / AS / IN2` (Công 1 / Thủ 3)
  * Vai trò: Trung vệ thòng bọc lót (Cover), sửa sai và đua tốc độ sau lưng Rüdiger.
  * `AS`: Ở lại phía sau khi tấn công.
  * `IN2`: Đánh chặn thận trọng (ghìm bản năng tự ý xoạc bóng).
* **HLV Tập Luyện:** **José Enrique ★8** *(Khéo léo / Tắc bóng / Cự ly ổn định)*.
* **Kỹ năng bổ sung +8:** **`Tổ chức`** (Khóa line bọc lót, không bỏ vị trí).

#### 10. RB: Dani Carvajal CU +8 — *Hậu Vệ Biên Thuần Thủ / Khóa Cánh Phải*
* **Thông số cơ bản:** OVR **142** | Lương **28** | Thể hình 173cm / 73kg | Đeo bám dai dẳng.
* **Chiến thuật đơn:** `AR2 / IN / SR` (Công 1 / Thủ 3)
  * `AR2`: Ở lại phía sau khi tấn công.
  * `IN`: Đánh chặn bình thường.
  * `SR`: Không dâng cao chồng biên.
* **HLV Tập Luyện:** **Lasse ★8** *(3 kỹ năng chi tiết: PENDING_SCREENSHOT)*.

#### 11. GK: Thibaut Courtois CU +8 — *Người Khổng Lồ 200cm Trấn Giữ Khung Thành*
* **Thông số cơ bản:** OVR **140** | Lương **24** | **200cm / 96kg**.
* **Chiến thuật đơn:**
  * `Xử lý tạt bóng (GK_CROSS)`: **Cân bằng**.
  * `Thủ môn quét (GK_SWEEPER)`: **Cân bằng**.
* **Trait +5:** **`TM đấm bóng`** (Khắc phục va chạm bóng bổng trong vòng cấm).
* **HLV Tập Luyện:** **Alijoša ★5** *(3 skill: PENDING_SCREENSHOT — "Cản phá sút / Cự ly gần / Trung bình" chỉ là MỤC TIÊU đề xuất, chưa xác minh)*.
* **Kỹ năng bổ sung +8:** **`Cản phá sút tầm thấp (Chỉ GK)`** (Hóa giải triệt để tử huyệt sút chìm của thủ môn cao 2m00).

---

## 5. 🪑 DANH SÁCH TOÀN BỘ 15 CẦU THỦ DỰ BỊ (`bench_and_reserves`)

> *Nguồn dữ liệu:* Đối chiếu chính xác 15 cầu thủ trong `02_CURRENT_SQUAD.json`. Các thông số Lương và OVR không có trong JSON được gắn nhãn `[UNVERIFIED]` trừ trường hợp thấy rõ trong Ảnh chụp game ngày 11/10/2026.

| STT | Cầu Thủ | Mùa Thẻ | Cấp Thẻ | Vai Trò Trong Đội Hình | Lương / OVR [Nguồn] | Ghi Chú Chi Tiết |
| :-: | :--- | :---: | :---: | :--- | :--- | :--- |
| 1 | **Casemiro** | CU | +8 | CDM mỏ neo thuần thủ / Cựu đá chính | Lương 27 (JSON) / OVR [UNVERIFIED] | Mạ Vàng +8, mỏ neo phòng ngự dự bị xoay tua Alaba |
| 2 | **Marcos Llorente** | UT | +9 | RM / RAM / CM đa năng hai chân 5-5 | Lương 28 (JSON) / OVR [UNVERIFIED] | Bạch Kim +9, thể lực 131, dự bị cánh và trung tâm |
| 3 | **Vinícius Jr.** | CU | +8 | LAM / LW siêu bứt tốc / Cựu đá chính | Lương 28 (JSON) / OVR [UNVERIFIED] | Mạ Vàng +8, dự bị cao cấp đột phá cánh trái |
| 4 | **A. Tchouaméni** | CU | +8 | LCB / CDM xoay tua chiến thuật | Lương 27 (JSON) / OVR [UNVERIFIED] | Mạ Vàng +8, dự bị chiến thuật cực mạnh cho LCB/CDM |
| 5 | **Rodrygo** | CU | +8 | RM / RW Super-Sub phút 70 | Lương 27 (JSON) / OVR [UNVERIFIED] | Mạ Vàng +8, siêu dự bị tốc độ quấy phá biên phải |
| 6 | **Kepa Arrizabalaga** | CU | +9 | GK phản xạ cao cấp / Cựu đá chính | Lương 23 (JSON) / OVR [UNVERIFIED] | Mạ Vàng +9, dự bị GK phản xạ cao cấp |
| 7 | **Koen Casteels** | 23HW | +9 | Cựu thủ môn baseline (197cm) | Lương 20 (JSON) / OVR 132 (JSON) | Mạ Vàng +9, giữ nguyên evidence và cấu hình dự bị |
| 8 | **Luka Modrić** | CU | +8 | LCM / CAM Nhạc trưởng phân phối bóng | Lương 29 (JSON) / OVR [UNVERIFIED] | Mạ Vàng +8, dự bị nhạc trưởng cao cấp tuyến giữa |
| 9 | **Rio Ferdinand** | DC | +9 | CB hộ pháp 189cm chống tiền đạo tì đè | Lương 28 (JSON) / OVR [UNVERIFIED] | Mạ Vàng +9, bọc lót chống tiền đạo hộ pháp |
| 10 | **Nemanja Matić** | VTR | +12 | CDM Bạch Kim thuần thủ | Lương 24 (JSON) / OVR [UNVERIFIED] | Bạch Kim +12, dự bị mỏ neo thuần thủ cao khi bảo toàn tỷ số |
| 11 | **Steven Gerrard** | UT | +8 | CM backup | Lương [UNVERIFIED] / OVR [UNVERIFIED] | Mạ Vàng +8, dự bị CM |
| 12 | **Marcel Desailly** | WG | +5 | CB backup | Lương [UNVERIFIED] / OVR [UNVERIFIED] | Thẻ Bạc +5, dự bị CB |
| 13 | **Jules Koundé** | FAC | +5 | RB / CB backup | Lương [UNVERIFIED] / OVR [UNVERIFIED] | Thẻ Bạc +5, dự bị RB/CB |
| 14 | **Maxence Lacroix** | 25DP | +5 | CB backup | Lương [UNVERIFIED] / OVR [UNVERIFIED] | Thẻ Bạc +5, dự bị CB tốc độ |
| 15 | **Álvaro García** | 24EP | +8 | LW cánh dự phòng | **Lương 23 / OVR 126** *(VERIFIED Ảnh 1)* | Thấy trực tiếp trong ảnh client game ngày 11/10/2026 |

---

## 6. 🔍 BẢNG TỔNG KẾT KIỂM TOÁN DỮ LIỆU (DATA INTEGRITY & GAPS)

| Hạng Mục | Trạng Thái Kiểm Chứng | Ghi Chú Hành Động |
| :--- | :---: | :--- |
| **11 Cầu thủ xuất phát & Mùa thẻ** | ✅ **100% VERIFIED** | Khớp chính xác 4 ảnh chụp màn hình game 11/10/2026. |
| **Chiến thuật đội (Team Tactic)** | ✅ **100% VERIFIED** | Đọc trực tiếp từ Ảnh 2 (Pressing, Depth 10, Chuyền dài, PIB 3, Xu hướng Tổng tấn công). |
| **Phân công 11 HLV Tập Luyện** | ✅ **100% VERIFIED** | Đọc chính xác tên HLV + số sao gắn trên từng cầu thủ. |
| **Team Color Mạ Vàng +8~+10** | ✅ **VERIFIED** | 11/11 cầu thủ đá chính đạt mốc +8 → +3 OVR theo `11_TEAM_COLOR_RULES.json`. |
| **Team Color Real Madrid CLB** | ⚠️ `DATA_INCOMPLETE` | Cluster trong `11_TEAM_COLOR_RULES.json` chỉ có 1/11 (F. Mendy). Chưa kết luận 11/11; cần ảnh màn hình Team Color in-game. |
| **Kỹ năng chi tiết HLV mới đổi** | ⚠️ `PENDING_SCREENSHOT` | Các HLV mới (Antero Maria, Raymond, Rodolfo...) chỉ biết tên + sao, chưa có ảnh chụp 3 skill chi tiết. |
| **Dropdown chiến thuật đơn LAM/RAM/CDM**| ⚠️ `UNVERIFIED_FROM_GAME` | Giữ nguyên bộ khung chuẩn của slot, chờ ảnh click popup dropdown trong game để chốt. |
| **Vị trí đá phạt (Set Pieces)** | ⚠️ `UNVERIFIED_FROM_GAME` | Chỉ có Captain Benzema BLD có badge `[C]` trong ảnh; các vị trí sút phạt còn lại giữ theo baseline. |
