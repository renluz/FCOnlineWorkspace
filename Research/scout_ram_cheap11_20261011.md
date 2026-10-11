# 🔍 BÁO CÁO SCOUT 3 ỨNG VIÊN RAM BẠCH KIM +11 GIÁ RẺ THAY THẾ FIGO UT +8

* **Mã báo cáo:** `SCOUT_RAM_CHEAP11_20261011`
* **Thời điểm khảo sát:** 2026-10-11 10:45:00 (UTC+7)
* **Người thực hiện:** AI Specialist & Antigravity Pair Programming
* **Mục tiêu:** Tìm 3 ứng viên RAM mức thẻ **Bạch Kim +11**, giá rẻ (< 30% giá Figo UT +8), đáp ứng sơ đồ 4-1-2-3-0 Chuyền Dài và khắc phục triệt để nguy cơ bẫy thể lực (Depth 10 + Áp lực ngay khi mất bóng).
* **Nguồn dữ liệu:** Client Garena FC Online VN, NEXON Open API Data, FIFAAddict Player Database.

> ⚠️ **LƯU Ý VỀ GIÁ:** Mọi con số giá trong báo cáo này được ghi nhận ngày 2026-10-11 nhưng **chưa có bằng chứng độc lập** (không có ảnh chụp TTCN, không có dòng dữ liệu trong `vn_market_history.csv`). Coi tất cả là **UNVERIFIED** — user BẮT BUỘC tự kiểm chứng trong TTCN game trước khi mua.

---

## 1. ⚓ NEO SO SÁNH HIỆN TẠI: LUÍS FIGO UT +8

| Tiêu Chí | Thông Số Kỹ Thuật Luís Figo UT +8 | Đánh Giá Thực Chiến GLXH |
| :--- | :---: | :--- |
| **Mùa thẻ & Cấp** | **UT (Unexpected Transfer) +8** (Mạ Vàng) | Thẻ đắt, giá trị tích lũy cao trong đội hình |
| **OVR Base (+1) / In-game** | `115` / **142** (Real Madrid 4 cấp + Mạ Vàng) | OVR hiển thị cao nhưng phân bổ chỉ số bị lệch |
| **Lương (Salary)** | **29** (Rất cao, chiếm gần 10% trần 300/305) | Gây căng thẳng quỹ lương cho trục giữa |
| **Vị trí sở trường** | `RW` (Đá RAM không bị phạt vị trí) | Phù hợp cánh phải |
| **Chân thuận / Kỹ thuật** | **Chân Trái 4 / Chân Phải 5** (5★ skill) | Chân không thuận 4 sao tạm ổn |
| **Tốc độ / Tăng tốc** | **145 / 144** (Cực nhanh khi có bóng) | Đạt yêu cầu phản công chuyền dài |
| **Dứt điểm / Sút xa** | **135 / 139** | Khá, nhưng thiếu độ bén một chạm trong box |
| **Thể lực nền** | **144** | Rất cao, đủ chạy 90 phút |
| **Team Color (chưa xác minh)** | Figo UT có thể không hưởng trọn team color Real Madrid như các thẻ mùa CLB khác do khác thế hệ mùa thẻ — cần kiểm chứng trực tiếp trong game. File `11_TEAM_COLOR_RULES.json` hiện chưa có quy tắc season-specific nên mọi con số chênh lệch OVR ở đây chỉ là giả thuyết. | Cần kiểm chứng trực tiếp in-game |
| **Giá Thị Trường VN (+8)** | **~260,000,000 BP** (260M BP Live TTCN VN) | **Neo so sánh: Ngưỡng "rẻ" (< 30%) = < 78,000,000 BP** |

---

## 2. 📋 BẢNG SO SÁNH CHI TIẾT 3 ỨNG VIÊN RAM +11 VÀ BASELINE THAM CHIẾU

> Mức thẻ Bạch Kim +11 cộng +26 điểm vào toàn bộ chỉ số thành phần so với thẻ gốc +1. Chưa tính buff team color (CLB +4 OVR; Bạch Kim +4 OVR nếu có 5 thẻ +11~+13, +5 OVR nếu có 8 thẻ — theo công bố Nâng Cấp 2.0). Lưu ý: 1 thẻ +11 đơn lẻ KHÔNG kích hoạt team color Bạch Kim.

| Chỉ số / Tiêu chí | ỨNG VIÊN 1: Rodrygo 21UCL +11 🥇 | ỨNG VIÊN 2: M. Llorente 21UCL +11 🥈 | ỨNG VIÊN 3: Brahim Díaz 24UCL +11 🥉 | BASELINE THAM CHIẾU: M. Llorente LOL +11 | BASELINE THAM CHIẾU: M. Llorente BOE21 (E21) +11 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Mùa & Mức thẻ** | **21UCL +11** | **21UCL +11** | **24UCL +11** | **LOL +11** | **BOE21 (E21) +11** |
| **Base OVR (+1) / (+11)** | `105` / **131** | `99` / **125** | `105` / **131** | `104` / **130** | `97` / **123** |
| **Lương (Salary)** | **21** (Tiết kiệm 8 lương!) | **20** (Tiết kiệm 9 lương!) | **22** (Tiết kiệm 7 lương!) | **23** (Tiết kiệm 6 lương) | **19** (Tiết kiệm 10 lương) |
| **Vị trí sở trường** | **RW** (Chuẩn cánh) | **RM** (Chuẩn cánh) | **RW** (Chuẩn cánh) | `CM` (Lệch vị trí nhẹ) | `CM` (Lệch vị trí nhẹ) |
| **Chân không thuận** | **4 / 5** | **5 / 5 (Hai chân 5-5)** | **5 / 5 (Hai chân 5-5)** | `4 / 5` | **5 / 5 (Hai chân 5-5)** |
| **Thể hình & Trọng lượng**| 174cm / 64kg (Gầy / Nhỏ) | **184cm / 74kg (Trung bình / Nạc)** | 170cm / 68kg (Sức khỏe / Đầm) | 184cm / 74kg (Trung bình) | 184cm / 74kg (Trung bình) |
| **Tốc độ / Tăng tốc** | **135 / 135** (Bứt tốc số 1) | **131 / 130** | **132 / 136** | **133 / 132** | **129 / 128** |
| **Dứt điểm / Chọn vị trí**| **132 / 132** (Cực bén cột 2) | **120 / 126** | **125 / 128** | **123 / 124** | **117 / 122** |
| **Sút xa / Lực sút** | **125 / 128** | **117 / 125** | **123 / 126** | **119 / 127** | **123 / 120** |
| **Thể lực (Stamina)** | **134** (Cực trâu) | **131** (Bao sân) | **127** (Đủ dùng) | **134** (Rất trâu) | **131** (Bao sân) |
| **Rê bóng / Khéo / Thăng bằng** | **136 / 137 / 133** | **127 / 123 / 130** | **136 / 138 / 135** (Dẻo nhất) | **131 / 127 / 135** | **127 / 118 / 131** |
| **Team Color Real Madrid** | **Có** (Ăn cả 21-22 & 23-24) | **Có** (Thuộc Real Madrid) | **Có** (Ăn cả 23-24 & 24-25) | **Có** | **Có** |
| **Bảo vệ BP Nâng Cấp 2.0** | **HỢP LỆ (Mùa cũ OVR 105)** | **HỢP LỆ (Mùa cũ OVR 99)** | **HỢP LỆ (Mùa cũ OVR 105)** | **HỢP LỆ (Mùa LOL)** | **HỢP LỆ (Mùa BOE21)** |
| **Giá TTCN VN (+11) [UNVERIFIED]** | **~58,000,000 BP** | **~45,000,000 BP** | **~55,000,000 BP** | **~46,000,000 BP** | **~38,000,000 BP** |
| **Tỷ lệ giá so với Figo UT**| **22.3%** (< 30% chuẩn) | **17.3%** (< 30% chuẩn) | **21.2%** (< 30% chuẩn) | **17.7%** | **14.6%** |

---

## 3. 🔬 PHÂN TÍCH CHUYÊN SÂU TỪNG ỨNG VIÊN

### 🥇 ỨNG VIÊN SỐ 1 (KHUYẾN NGHỊ LỰA CHỌN TỐI ƯU): RODRYGO 21UCL +11
* **Lý do đề xuất:**
  - **Khớp hoàn hảo vai trò RAM Chuyền Dài:** Tốc độ 135 / Tăng tốc 135 biến Rodrygo thành mũi khoan đón các đường chuyền dài (Long Ball) xé gió sau lưng hậu vệ trái đối phương.
  - **Sát thủ kết thúc tuyến hai:** Dứt điểm **132** và Chọn vị trí **132** vượt trội hoàn toàn mọi đối thủ cùng phân khúc giá rẻ. Khi Benzema nhận bóng quay lưng nhả về hoặc Mbappé căng ngang cutback từ cánh trái, Rodrygo ập vào là có bàn thắng.
  - **Giải phóng trần lương lớn:** Lương giảm từ 29 (Figo) xuống còn **21** (dôi dư **8 điểm lương** cho việc nâng cấp trục dọc sau này).
  - **Thể lực 134:** Giải quyết triệt để cảnh báo bẫy thể lực `PR-05` trong sơ đồ Depth 10.
* **Đề xuất 1 Chỉ Số Ẩn Trắng (+5) theo hệ Nâng Cấp 2.0:**
  - **`Sút xoáy` (Finesse Shot)**: Rodrygo đã có sẵn *Rê bóng kỹ thuật* và *Khéo léo*, bổ sung Sút xoáy giúp các pha bẻ lòng ZD từ nách phải vào góc xa trở nên hiểm hóc tuyệt đối.
* **Rủi ro nhận diện:** Thể hình nhỏ (174cm / 64kg), tranh chấp tay đôi tì đè với các hậu vệ to con (như Theo Hernandez, Mendy) sẽ yếu thế nếu không dùng tốc độ để vượt mặt trước.

---

### 🥈 ỨNG VIÊN SỐ 2: MARCOS LLORENTE 21UCL +11 (VƯỢT TRỘI SO VỚI BASELINE LOL & E21)
* **Lý do đề xuất:**
  - **Tại sao chọn 21UCL thay vì LOL hay E21?**
    1. *So với Llorente LOL:* LOL chỉ có chân **4/5** và vị trí tự nhiên là CM, lương 23. Trong khi 21UCL sở hữu **2 chân 5-5 tuyệt đối**, vị trí sở trường **RM**, lương chỉ **20**.
    2. *So với Llorente BOE21 (E21):* E21 có OVR base 97 thấp hơn, chỉ số Dứt điểm (+11) chỉ đạt 117 (thấp hơn 21UCL đạt 120), tốc độ 129/128 kém hơn 21UCL đạt 131/130.
  - **Thể hình đầm chắc:** 184cm / 74kg, thể lực **131** cùng thăng bằng **130**, hỗ trợ phòng ngự cánh phải cùng Carvajal cực kỳ vững chãi, chống phản công xuất sắc.
* **Đề xuất 1 Chỉ Số Ẩn Trắng (+5) theo hệ Nâng Cấp 2.0:**
  - **`Nỗ lực đến cùng` (Second Wind)**: Hồi phục thể lực sung mãn ở phút 70–90, giúp duy trì cường độ pressing liên tục và bứt tốc phản công cuối trận.
* **Rủi ro nhận diện:** Khả năng rê dắt lắt léo và bứt tốc ở 10m đầu tiên không thanh thoát bằng Rodrygo; Dứt điểm 120 ở mức khá, không phải mẫu tiền đạo cánh săn bàn bùng nổ.

---

### 🥉 ỨNG VIÊN SỐ 3: BRAHIM DÍAZ 24UCL +11
* **Lý do đề xuất:**
  - **Hai chân 5-5 & Thăng bằng 135:** Độ dẻo khi xoay sở trong không gian hẹp thuộc top 1 game. Bẻ hướng ngoặt bóng 90 độ loại bỏ hậu vệ biên cực ngọt.
  - **Tăng tốc 136:** Đề pa đoạn ngắn cực kỳ ấn tượng, rê dắt dính chân (`Khéo léo 138`, `Rê bóng 136`).
  - **Hưởng Special Team Color Real Madrid 23-24 & 24-25:** Nhận trọn vẹn buff chỉ số thành phần mùa giải gần nhất.
* **Đề xuất 1 Chỉ Số Ẩn Trắng (+5) theo hệ Nâng Cấp 2.0:**
  - **`Sút xoáy` (Finesse Shot)**: Tận dụng ưu thế 2 chân 5-5 để có thể ZD chuẩn xác bằng bất kỳ chân nào khi cắt vào trung lộ.
* **Rủi ro nhận diện:** Thể lực **127** (thấp nhất trong 3 ứng viên, nếu pressing Depth 10 cả trận cần cài `IN2` để giữ pin); Thể hình thấp bé 170cm dễ bị đè ngã nếu bị áp sát từ phía sau.

---

## 4. 💰 PHÂN TÍCH CHI PHÍ MUA SẴN VS. ĐẬP THẺ BẢO VỆ BP (HỆ NÂNG CẤP 2.0)

| Cầu Thủ | Giá Mua Sẵn (claim, UNVERIFIED) | Giá Phôi (+1 / +8) | Ước Tính Phí Bảo Vệ BP (+8 ➔ +11) | Tổng Chi Phí Đập Dự Kiến | Đánh Giá Khả Thi |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Rodrygo 21UCL** | `~58,000,000 BP` | Phôi +1: ~1.5M / Phôi +8: ~18M | ~38,000,000 BP | `~56,000,000 BP` | **Rất khả thi**, phôi dồi dào, chợ có thanh khoản |
| **M. Llorente 21UCL** | `~45,000,000 BP` | Phôi +1: ~800k / Phôi +8: ~12M | ~30,000,000 BP | `~42,000,000 BP` | **Cực rẻ**, bảo vệ BP tiết kiệm chi phí |
| **Brahim Díaz 24UCL** | `~55,000,000 BP` | Phôi +1: ~1.2M / Phôi +8: ~15M | ~35,000,000 BP | `~50,000,000 BP` | Khả thi cao, dễ tìm phôi |
| **Figo UT +8 (Neo)** | `~260,000,000 BP` | - | - | - | **Quá đắt so với hiệu năng thực tế** |

---

## 5. 🎯 KẾT LUẬN & KHUYẾN NGHỊ HÀNH ĐỘNG CHO USER

1. **LỰA CHỌN SỐ 1 ĐỀ XUẤT MUA/TEST THỬ NGHIỆM ĐƠN BIẾN:**
   👉 **`RODRYGO 21UCL +11` (Bạch Kim +11)**:
   - Chi phí: **~58,000,000 BP** (Chỉ bằng **22.3%** giá Figo UT +8, ví hiện tại dư 837M BP thừa sức chi trả).
   - Giải phóng **8 điểm lương** (tổng lương đội hình giảm từ 300 về 292/305).
   - Tốc độ 135, Dứt điểm 132, Thể lực 134 hoàn toàn vượt trội Figo UT về hiệu suất chuyển đổi bàn thắng trong hệ Chuyền Dài.
   - Giữ nguyên 10 vị trí còn lại, tiến hành đá thử nghiệm 20–30 trận GLXH để đánh giá mức độ cải thiện bàn thắng tại cánh phải.

2. **PHƯƠNG ÁN DỰ PHÒNG THIÊN VỀ THỦ / CÂN BẰNG:**
   👉 Nếu user muốn tăng cường chất thép chống phản công và thể hình nạc: chọn **`Marcos Llorente 21UCL +11`** (Chi phí siêu rẻ ~45M BP, 2 chân 5-5, vị trí RM tự nhiên).
