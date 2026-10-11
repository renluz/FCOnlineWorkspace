# 🛡️ QUY TẮC CỐT LÕI CỦA DỰ ÁN (PROJECT DIRECTIVES)

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
  * `R. Ferdinand DC +9` $
eq$ `R. Ferdinand DC +8` (khác nhau về mốc chỉ số ngưỡng và mở slot).
  * `R. Ferdinand DC +9` $
eq$ `R. Ferdinand WB +8` $
eq$ `R. Ferdinand ICON +5` (hoàn toàn khác biệt về AI ẩn, thể hình chi tiết và đặc tính vận hành).
  * `N. Matić VTR +12` $
eq$ `N. Matić RTN +8`.
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
  3. `Luxury Upgrade (Nâng cấp xa xỉ):` Thẻ cộng cao của các mùa quá đắt đỏ, chỉ số tăng nhẹ nhưng giá gấp 5-10 lần thẻ tiêu chuẩn $ightarrow$ **Khuyến nghị trì hoãn**.
  4. `Team Color-only Upgrade:` Nâng cấp chỉ để lấy thêm 1 điểm chỉ số Team color $ightarrow$ Cân nhắc kỹ chi phí/lợi ích.
* **Quy tắc ngân sách:** Luôn giữ lại ít nhất **40% – 50% quỹ BP dự phòng** sau mỗi đợt mua sắm.

---

## 6. 🔄 CHÍNH SÁCH CẬP NHẬT PATCH (PATCH ROLLOVER)
Khi FC Online ra mắt bản cập nhật Gameplay Patch mới (ví dụ Next Field mới):
* Không xóa dữ liệu và phân tích cũ.
* Đánh dấu toàn bộ dữ liệu bị ảnh hưởng bởi patch cũ bằng tag `OUTDATED_PATCH`.
* Ghi nhận sự thay đổi vào `20_PATCH_CHANGELOG.md`.
