# 🔍 BÁO CÁO KIỂM TOÁN HỆ THỐNG CHỈ SỐ ẨN & HLV KỸ NĂNG (TRAIT DATABASE AUDIT)

> **Tài liệu kiểm toán:** `TRAIT_DATABASE_AUDIT.md`  
> **Dự án:** FCOnlineSquadProject (`E:\FCOnlineWorkspace\SquadProject\`)  
> **Ngày kiểm toán:** 2026-09-20  
> **Nguyên tắc kiểm toán:** Tách biệt độc lập từng trường dữ liệu (Tên, Mô tả, Tác dụng chính thức, Đánh giá GLXH, Suy luận vai trò). Tuyệt đối không gắn nhãn `VERIFIED_CLIENT_VN` cho toàn bộ record chỉ vì tên xuất hiện trong ảnh chụp.

---

## 1. 📊 BẢNG TỔNG HỢP ĐỐI SOÁT CHI TIẾT (TRAIT AUDIT MATRIX)

### A. Nhóm Chỉ Số Ẩn Vàng (Gold Traits — Mốc +11)

| Trait | Name VN Verified | Client Description | Official Effect | Manager Evidence | Role Inference | Confidence |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Sát thủ băng cắt** | ✅ Client + Garena | ✅ Client VN | ✅ Garena Prime | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Chuyên gia vô lê** | ✅ Client VN | ✅ Client VN | 🟡 NEXON Official | 🟡 Community | ⚠️ Model Inference | **MEDIUM_HIGH** |
| **Bậc thầy không chiến** | ✅ Client + Garena | ✅ Client VN | ✅ Garena ICON TM | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Dứt điểm 1 chạm** | ✅ Client + Garena | ✅ Client VN | ✅ Garena Hè 2026 | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Nhạc trưởng** | ✅ Client + Garena | ✅ Client VN | ✅ Garena ICON TM | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Siêu Bứt Tốc** | ✅ Client + Garena | ✅ Client VN | ✅ Garena ICON TM | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Ảo thuật gia** | ✅ Client + Garena | ✅ Client VN | ✅ Garena Hè 2026 | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Chặn đà tấn công** | ✅ Client VN | ✅ Client VN | 🟡 NEXON Official | ✅ Inven GLXH | ⚠️ Model Inference | **MEDIUM_HIGH** |
| **Bậc thầy chạy chỗ** | ✅ Client + Garena | ✅ Client VN | ✅ Garena Prime | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Chủ Động Cản Phá** | ✅ Client + Garena | ✅ Client VN | ✅ Garena ICON TM *(Sút xa, không cắt chọc khe)* | ✅ Matić +12 `(Đã chọn)` + Inven | ⚠️ Model Inference | **HIGH** |
| **Siêu đánh chặn** | ✅ Client + Garena | ✅ Client VN | ✅ Garena Hè 2026 | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Cao thủ tắc bóng** | ✅ Client + Garena | ✅ Client VN | ✅ Garena Prime *(Không miễn phạm lỗi)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Người không phổi** | ✅ Client VN | ✅ Client VN | 🟡 NEXON Official | ✅ Inven GLXH | ⚠️ Model Inference | **MEDIUM_HIGH** |
| **Chuyên gia đeo bám** | ✅ Client + Garena | ✅ Client VN | ✅ Garena Prime *(Trigger 10s sau phản công)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| *GK áp đảo không chiến* | 🟡 Garena Official | ❌ Chưa có ảnh client | ✅ Garena ICON TM | ❌ Chưa có | ⚠️ Model Inference | **PENDING_SCREENSHOT** |
| *GK bắt bài sút xa* | 🟡 Garena Official | ❌ Chưa có ảnh client | ✅ Garena Hè 2026 | ❌ Chưa có | ⚠️ Model Inference | **PENDING_SCREENSHOT** |

### B. Nhóm Chỉ Số Ẩn Thường Trọng Điểm (Normal Traits — Mốc +5)

| Trait | Name VN Verified | Client Description | Official Effect | Manager Evidence | Role Inference | Confidence |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Sút xa** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(AI Behavioral Tendency, KHÔNG buff stat)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Chuyền dài** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(AI Behavioral Tendency, KHÔNG buff stat)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Tạt bóng sớm** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(AI Behavioral Tendency, KHÔNG buff stat)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Cứng như thép** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(Giảm chấn thương, KHÔNG buff sức mạnh)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Nỗ lực đến cùng** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(Hồi thể lực phút 75+, KHÔNG buff stat trần)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Vị trí yêu thích** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(Duy trì phong độ, KHÔNG cộng OVR ẩn)* | 🟡 Community | ⚠️ Model Inference | **MEDIUM** |
| **Siêu cản phá** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(Động tác phá bóng nhào lộn)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Xoạc bóng** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(AI Behavioral Tendency, rủi ro thẻ/penalty)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Đánh đầu mạnh** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(Gia tăng lực đập bóng đầu)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Thánh chuyền bóng** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(Team AI Interaction, hút bóng phát động)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |

### C. Nhóm HLV Kỹ Năng Cần Lưu Ý (Skill Coaches — Mốc +8)

| Trait | Name VN Verified | Client Description | Official Effect | Manager Evidence | Role Inference | Confidence |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Khả năng tắc bóng** | ✅ Client VN | ❌ Chưa có popup | ❌ Unverified | ✅ NEXON Data Center #1 CB | ⚠️ Model Inference | **HIGH (Name) / UNVERIFIED (Effect)** |
| **Cự ly đội hình ổn định** | ✅ Client VN | ❌ Chưa có popup | ❌ Unverified | ✅ Inven GLXH (재정비) | ⚠️ Model Inference | **HIGH (Name) / UNVERIFIED (Effect)** |
| **Tập trung đánh chặn** | ✅ Client VN | ❌ Chưa có popup | ❌ Unverified | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH (Name) / UNVERIFIED (Effect)** |
| **Mục số 10 (Chuyền xà/xa)**| ❌ **NEEDS_VERIFY** | ❌ Chưa có popup | ❌ Unverified | ❌ Chưa có | ⚠️ Model Inference | 🔴 **LOW_AMBIGUOUS** |
| **Mục số 12 (Rê bóng khi...)**| 🟡 Truncated | ❌ Bị cắt ngắn UI | ❌ Unverified | ❌ Chưa có | ⚠️ Model Inference | 🟡 **TRUNCATED_IN_UI** |
| **Mục số 13 (Sút xa tru...)** | 🟡 Truncated | ❌ Bị cắt ngắn UI | ❌ Unverified | ❌ Chưa có | ⚠️ Model Inference | 🟡 **TRUNCATED_IN_UI** |

---

## 2. 📈 THỐNG KÊ BÁO CÁO ĐỊNH LƯỢNG (METRICS BREAKDOWN)

* **Số tên xác minh trực tiếp từ Client VN:** **75 / 78 tên** (23 Trait thường + 38 HLV kỹ năng đầy đủ + 14 Gold Traits).
* **Số mục tên chưa thể chốt 100% hoặc bị cắt ngắn:** **3 mục** (Mục 10 `Chuyền xà/xa` nghi vấn ký tự, Mục 12 và Mục 13 bị UI cắt ngắn).
* **Số Effect xác minh từ nguồn Official (Garena/NEXON/EA):** **37 hiệu ứng** (Toàn bộ 23 trait thường + 14 Gold Traits). HLV kỹ năng mốc +8 hiện để `null` và `UNVERIFIED` do chưa có công bố cơ chế số học chính thức từ Garena.
* **Số Manager Observation có nguồn dẫn chứng:** **28 nhận định** (dẫn chứng từ Inven 감독모드, NEXON Data Center và ảnh chụp `(Đã chọn)` của Matić).
* **Số mục Role Inference (Suy luận mô hình):** **78 / 78 mục** khuyến nghị vai trò (được đánh dấu rõ ràng `MODEL_INFERENCE`, không đánh đồng với dữ liệu nhà phát hành).

---

## 3. 🛡️ KHẲNG ĐỊNH VỀ SCOPE VÀ DỮ LIỆU CÒN THIẾU

1. **Scope của Gold Traits:**
   * `OUTFIELD_GOLD_TRAIT_POOL`: Đã hoàn thiện **14/14 Chỉ số ẩn vàng** cho cầu thủ trên sân.
   * `GK_GOLD_TRAIT_POOL`: **CHƯA ĐẦY ĐỦ** (`database_complete = false`). Garena xác nhận tồn tại ít nhất 2 Gold Trait dành riêng cho thủ môn: `GK áp đảo không chiến` và `GK bắt bài sút xa`.
2. **Các mục cần người dùng chụp ảnh bổ sung từ client:**
   * Ảnh chụp rõ chữ mục số 10 trong danh sách HLV kỹ năng (`Cải thiện chuyền xà` hay `Cải thiện chuyền xa`).
   * Ảnh chụp popup chi tiết khi click vào mục số 12 (`Cải thiện khả năng rê bóng khi...`) và mục số 13 (`Cải thiện khả năng sút xa tru...`).
   * Ảnh chụp giao diện chọn Chỉ số ẩn vàng khi mở trên một Thủ môn (GK) đạt mốc +11.

---

## 4. 🏁 KẾT LUẬN KIỂM TOÁN
Cơ sở dữ liệu Trait Engine hiện tại **KHÔNG TUYÊN BỐ 100% VERIFIED TOÀN DIỆN**, mà được gắn cờ chuẩn xác theo từng trường thông tin. Mọi suy luận của AI đều được cô lập độc lập, bảo vệ tính trung thực và độ tin cậy của toàn bộ dự án tri thức!
