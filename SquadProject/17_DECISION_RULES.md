# ⚖️ HỆ THỐNG LUẬT RA QUYẾT ĐỊNH (DECISION RULES ENGINE)

Tài liệu này thiết lập các quy tắc logic toán học và điều kiện ràng buộc dạng **`IF / THEN / PENALTY / BONUS`** để AI Assistant và Huấn luyện viên áp dụng khi build đội hình, chọn trait, ghép cặp cầu thủ và chuyển nhượng.

---

## 1. 🛡️ LUẬT GHÉP CẶP TRUNG VỆ (CENTER-BACK PAIRING RULES)

* **`RULE_CB_01 (Cân bằng Stopper & Cover):`**
  * **IF:** Trung vệ thứ nhất (LCB) mang archetype `CB_STOPPER` (có xu hướng dập, bước lên tranh chấp).
  * **THEN:** Bắt buộc trung vệ thứ hai (RCB) phải mang archetype `CB_COVER` (giữ vị trí sâu, bọc lót, tốc độ truy cản cao $\ge 130$).
  * **BONUS:** `+15% Defensive Stability` (Hàng thủ có lớp lang, giảm nguy cơ thủng lưới do đối phương chọc khe bổng QW).

* **`RULE_CB_02 (Cấm kỵ hai Stopper dập cùng lúc):`**
  * **IF:** Cả hai trung vệ đều có xu hướng dâng cao tranh chấp (`Double Stopper`).
  * **PENALTY:** `FATAL DEFENSIVE DISRUPTION` — Đối phương chỉ cần 1 đường chuyền một chạm là đối mặt thủ môn. **BẮT BUỘC TỪ CHỐI**.

* **`RULE_CB_03 (Bù trừ chiều cao & thể hình):`**
  * **IF:** Một trung vệ có chiều cao $\le 185\text{cm}$ (như Desailly WG 185cm hoặc Carvalho WG 183cm).
  * **THEN:** Trung vệ còn lại bắt buộc phải có chiều cao $\ge 189\text{cm}$, cân nặng $\ge 85\text{kg}$ và sở hữu trait `Đánh đầu mạnh` (như Ferdinand DC 189cm hoặc Schlotterbeck 26TS 191cm).
  * **PENALTY IF VIOLATED:** `AERIAL_DEFENSE_VULNERABILITY` (Thua không chiến trước tiền đạo cao $\ge 1m90$).

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
  * **IF:** Cầu thủ ứng viên có OVR cao hơn nhưng không đạt các chỉ số ngưỡng cốt lõi của vai trò (ví dụ: CB thiếu tốc độ $\ge 125$, hoặc CDM thiếu chiều cao $\ge 1m90$).
  * **THEN:** **BÁC BỎ ỨNG VIÊN (REJECT)**. Ưu tiên thẻ đạt chỉ số ngưỡng và thể hình chuẩn.

* **`RULE_AI_02 (So sánh chi phí nâng cấp +8 vs +9):`**
  * **IF:** Thẻ +9 có giá thị trường gấp $> 4$ lần thẻ +8 của cùng một mùa giải nhưng không mở thêm slot kỹ năng mới nào (cả +8 và +9 đều chỉ có slot HLV kỹ năng và Chỉ số ẩn thường).
  * **THEN:** **ƯU TIÊN DÙNG THẺ +8 (PREFER +8)**, dành phần chênh lệch BP để nâng cấp các vị trí khác hoặc tích lũy dài hạn.

---

## 5. 💰 QUY TẮC QUẢN TRỊ NGÂN SÁCH CHUYỂN NHƯỢNG (BP RESERVE GOVERNANCE)

* **`RULE_BP_01 (Ngưỡng an toàn quỹ dự trữ):`**
  * **IF:** Huấn luyện viên tích lũy được một lượng BP (ví dụ 300M – 500M BP).
  * **THEN:** Một kỳ chuyển nhượng tối đa chỉ được giải ngân $\le 50\%$ tổng ngân sách hiện có, luôn giữ lại ít nhất $50\%$ làm quỹ dự trữ thanh khoản.

* **`RULE_BP_02 (Xếp hạng ưu tiên chi tiêu):`**
  * `Priority 1 (Critical Upgrade):` Sửa lỗ hổng chí mạng (CB quá lùn, CDM bỏ vị trí).
  * `Priority 2 (Value Upgrade):` Hoàn thiện mốc thẻ cộng cao (lên +5 hoặc +8) để kích hoạt Team Color Mạ Vàng +8~+10 (+3 OVR) hoặc Team Color +5~+7 (+2 OVR).
  * `Priority 3 (Luxury Upgrade):` Mua các thẻ siêu sao quốc dân giá chát $\rightarrow$ Chỉ thực hiện khi các vị trí khác đều đã đạt chuẩn hoàn hảo.

---

## 6. 🧠 QUY TẮC ENGINE TỪ FC INFO & MANAGER MODE KOREA (FC INFO META RULES)

* **`RULE_SCOUT_01 (Trục dọc Central Axis: Thể hình & Quyết đoán / Aggression):`**
  * **IF:** Tuyển mộ hoặc đánh giá cầu thủ ở trục giữa sân (`CAM ➔ CM ➔ CDM ➔ CB`).
  * **THEN:** Bắt buộc soi thể hình ($\ge 1m85$, tạng người TB trở lên cho CB/CDM/CAM) và chỉ số **Quyết đoán (적극성 / Aggression)**.
  * **PENALTY IF LOW AGGRESSION:** `NO_TACKLE_PENALTY` — Trong hệ thống pressing GLXH, cầu thủ có chỉ số Quyết đoán thấp chỉ chạy theo áp sát hình thức nhưng **KHÔNG thực sự thò chân tắc bóng (tackle)**, dễ để đối phương rê qua hoặc thoải mái chuyền bóng.

* **`RULE_TACTIC_01 (Cơ chế cô lập chống phản công 4-1-4-1-0):`**
  * **IF:** Sử dụng sơ đồ 4-1-4-1-0 trong GLXH.
  * **THEN:** Thiết lập chiến thuật đội **`Players in Box = 1 (Thấp nhất)`** kết hợp **`Attack Width rộng`**.
  * **MECHANISM:** Việc để Box = 1 ngăn chặn triệt để tình trạng cả 2 CM và CDM cùng lúc ùa vào vòng cấm dẫn đến hở sườn chết người khi mất bóng. Việc ai xâm nhập vòng cấm được điều phối chuyên biệt bằng thiết lập đơn (`SC1` cho Havertz, Bellingham, Vini; `AS2` cho Valverde, Modrić; CDM tuyệt đối không vào box).

* **`RULE_TRAIT_01 (Ưu tiên Trait tự động / Hai trái tim trong GLXH):`**
  * **IF:** Chọn Chỉ số ẩn và HLV kỹ năng cho chế độ Giả Lập Xếp Hạng (AI tự thi đấu 100%).
  * **THEN:** Ưu tiên tuyệt đối các Trait thụ động tự động kích hoạt theo hệ thống, đứng đầu là nhóm trait thể lực / "Hai trái tim" (`2개의 심장` — `Nỗ lực đến cùng`). Bác bỏ các trait chỉ phát huy tác dụng khi có phím bấm thủ công của người chơi.

---

## 7. 🎯 QUY TẮC THẨM ĐỊNH THAY THẾ CẦU THỦ (MONEYBALL SELECTION RULE)

* **`RULE_MONEYBALL_01 (Tiêu chuẩn công nhận "CU Killer" theo thang 100 điểm):`**
  * **IF:** Cân nhắc mua một card mùa mới hoặc card ngân sách để thay thế card CU chuẩn trong đội hình 4-1-4-1-0.
  * **THEN:** Chỉ phê duyệt giải ngân BP nếu ứng viên đạt tổng điểm $\ge 80 / 100$ theo hệ thống chấm điểm Moneyball 100 điểm:
    * `Role Fit đúng tactic (30đ)` + `Trait / Special-Trait Fit (20đ)` + `Physical & Work Profile (15đ)` + `Ranker Usage & Win Evidence (15đ)` + `Salary Efficiency (10đ)` + `Giá +8/+9 (10đ)`.
  * **MANDATORY CONDITIONS:**
    1. Không có điểm chết (fatal flaw) ở các stat cốt lõi của vai trò.
    2. Có bằng chứng dữ liệu ranker / bài test cộng đồng với mẫu thử đáng tin cậy.
    3. Thử nghiệm tối thiểu 100 trận in-game — win rate của cả đội không được tụt dốc.
  * **PENALTY IF VIOLATED:** **BÁC BỎ NGAY LẬP TỨC (REJECT)** nếu chỉ mua vì "mùa mới hơn" hoặc OVR cao hơn mà không chứng minh được hiệu suất AI trên mỗi BP/lương.

---

## 8. 🔍 QUY TẮC BẮT BUỘC TRA CỨU DỮ LIỆU THỰC TẾ (DATA VERIFICATION MANDATE)

* **`RULE_DATA_01 (Cấm suy diễn mùa thẻ — Bắt buộc xác minh FC INFO / FIFAAddict trước khi tư vấn):`**
  * **IF:** Đề xuất, phân tích, so sánh hoặc thảo luận về bất kỳ cầu thủ / mùa thẻ nào.
  * **THEN:** BẮT BUỘC phải tra cứu dữ liệu thực tế trực tiếp từ các nguồn Tier E / Tier A (FC INFO `fc-info.com/player/search`, FIFAAddict, Nexon Data Center, Garena) để xác nhận 100% sự tồn tại thực tế của thẻ:
    1. Tên cầu thủ & Mùa thẻ chính xác (không suy đoán).
    2. Chỉ số OVR gốc & mức lương thực tế.
    3. Thể hình (Chiều cao, cân nặng, tạng người) & Chân thuận/nghịch (Weak Foot).
    4. Điều kiện mùa giải (ví dụ: mùa CU chỉ dành cho cầu thủ từng vô địch Champions League).
  * **PENALTY IF VIOLATED:** `FATAL_WORKFLOW_BREACH` — Tuyệt đối KHÔNG suy diễn, phỏng đoán hoặc đưa ra cầu thủ thuộc mùa thẻ chưa được xác minh. Mọi phát ngôn không có căn cứ từ database chính thức đều bị coi là vi phạm nghiêm trọng kỷ luật dự án.



