# 🔄 NHẬT KÝ CẬP NHẬT GAMEPLAY (PATCH CHANGELOG)

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
  * Tăng hiệu quả cản phá sút xa ngoài vòng cấm của các thủ môn có chiều cao $\ge 1m95$.
  * Tối ưu hóa AI di chuyển của các tiền vệ cánh có trait *Sát thủ băng cắt* và *Bậc thầy chạy chỗ*.

### 🔷 Bản Cập Nhật Gameplay 11th (Đầu năm 2026)
* Trạng thái: `OUTDATED_PATCH`
* Các cú sút cứa lòng ZD góc xa có độ xoáy cực cao. Cần lưu ý các kết luận chiến thuật thuộc giai đoạn này hiện đã giảm bớt độ bá đạo so với Gameplay 12th.

---

## 3. ⚠️ ĐÍNH CHÍNH DỮ LIỆU TIMELINE MÙA THẺ (2026-09-30)

> Các thông tin sau **đã được sửa từ phán đoán sai** sang dữ liệu xác minh từ nguồn Garena chính thức.

### ✅ Timeline mùa thẻ chính xác (Nguồn: Garena Official)

| Mùa thẻ | Ngày ra mắt thực tế | Ghi chú |
|:---|:---|:---|
| **CU (Champions of Europe)** | **29/08/2024** | Ra mắt mùa hè 2024, KHÔNG phải T11/2025 |
| **26TY / 26TY-N (Team of the Year / Nominees)** | **Đầu năm 2026** (liệt kê trong Luật FVPL Spring 2026) | Ra trước 26TOTS |
| **Infinite Prime** | **12/06/2026** (+ bổ sung T7–8/2026) | Ra TRƯỚC 26TOTS, không phải sau |
| **26TOTS (Team of the Season)** | **01/07/2026** | Ra sau 26TY/TN và Infinite Prime |
| **UC (Untouchable Champions)** | **14/09/2026** | Mùa thẻ mới nhất hiện tại |

### ❌ Các kết luận bị thu hồi (Không có bằng chứng):

1. **"Mùa thẻ mới hơn = AI engine mới hơn"** — **BÁC BỎ HOÀN TOÀN.**
   - Patch gameplay áp dụng cho **toàn bộ game**, không gắn riêng vào một mùa thẻ.
   - Sự khác biệt AI giữa các mùa thẻ xuất phát từ **stat, trait, work rate, body type, vị trí và animation profile** của exact-card đó, không phải "AI engine riêng của mùa".
   - Không được kết luận "UC/26TOTS có AI tốt hơn CU" nếu không có bằng chứng exact-card cụ thể.

2. **"26TOTS mỗi card có 4 Gold Trait"** — **SAI.**
   - Garena thông báo 26TOTS **bổ sung 4 Gold Trait mới vào pool lựa chọn**, không có nghĩa mỗi exact-card tự động được trang bị 4 Gold Trait.

### 🔒 Quy tắc bổ sung vào Decision Rules:

**RULE_UPGRADE_01 (Kỷ luật giữ mốc Team Color CU):**
- Đội hình hiện tại có **8 CU đá chính** (Havertz, Bellingham, Modrić, Valverde, Vini, Tchouaméni, Mendy, Carvajal).
- **CẤM thay một CU bằng 26TOTS/UC** trước khi đạt dư số CU.
- Roadmap đúng: Mua **Militão CU +8** (lên 9 CU) → Benzema BLD +8 thay Havertz (về 8 CU) → Casemiro CU / Rüdiger CU / Kepa CU → Khi có dư mốc mới nghiên cứu nâng Vini/Valverde/Bellingham lên 26TOTS/UC.
- **Tiêu chí nâng cấp lên mùa mới**: Phải tra exact-card trên FC INFO, so sánh stat thực tế + Gold Trait pool + body type + lương, **không nâng chỉ vì mùa mới hơn**.
