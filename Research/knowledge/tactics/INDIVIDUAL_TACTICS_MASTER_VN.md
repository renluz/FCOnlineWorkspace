# FC ONLINE VIỆT NAM — CHIẾN THUẬT ĐƠN CẦU THỦ (MASTER GROUND TRUTH)

**Phiên bản đối chiếu:** 20/09/2026  
**Server:** Garena FC Online Việt Nam  
**Trạng thái kiểm chứng:** OFFICIAL_GARENA_VERIFIED / FVPL_2026_LEGAL_GROUNDED

---

## 1. Trạng thái hệ thống hiện tại

FC Online hiện sử dụng **10 nhóm mã chiến thuật đơn**:

| Mã | Tên gốc | Chức năng |
| :--- | :--- | :--- |
| `AR` | Attacking Runs | Cách cầu thủ tham gia/chạy chỗ khi tấn công |
| `CC` | Chance Creation | Cách cầu thủ tạo khoảng trống/cơ hội |
| `AS` | Attacking Support | Mức độ hỗ trợ tấn công |
| `DS` | Defensive Support | Mức độ hỗ trợ phòng ngự |
| `DP` | phụ thuộc nhóm vị trí | Hành vi phòng ngự/vị trí phòng ngự |
| `DB` | Defensive Behavior | Hành vi phòng ngự |
| `IN` | Interceptions | Mức độ chủ động đánh chặn |
| `PF` | Positioning Freedom | Mức độ tự do vị trí |
| `SC` | Support On Cross | Hành vi khi bóng được triển khai/tạt từ biên |
| `SR` | Support Runs | Hướng/chế độ chạy hỗ trợ |

Cấu trúc 10 nhóm AR/CC/AS/DS/DP/DB/IN/PF/SC/SR được ghi nhận từ hệ FC Online chính thức/NEXON và vẫn là nền của hệ hiện nay. Quan trọng: **cùng một mã không nhất thiết có cùng lựa chọn ở mọi vị trí**. Ví dụ `AR` của ST khác `AR` của LB/RB; `DP` của tiền đạo khác hoàn toàn `DP` của CM/CDM.

---

## 2. VỊ TRÍ NÀO CÓ NHỮNG NHÓM CHIẾN THUẬT NÀO?

* **ST / LS / RS / CF / LF / RF:** `AR + DP + IN + SR`
* **LW / RW:** `CC + DS + IN + SC + SR` *(CC3: Vai trò tự do; SR3: Tiền đạo mục tiêu)*
* **CAM / LAM / RAM:** `DS + IN + PF + SC` *(CAM có thêm PF2: Di chuyển rộng; LAM/RAM không dùng được PF2)*
* **CM / LCM / RCM:** `AS + DP + IN + PF + SC` *(Được bổ sung nhóm DP)*
* **CDM / LDM / RDM:** `AS + DB + DP + IN` *(Duy trì DB riêng biệt)*
* **LM / RM:** `CC + DS + IN + PF + SC + SR` *(Nhiều nhóm nhất - 6 nhóm chiến thuật)*
* **CB / LCB / RCB / SW:** `AS + IN` *(AS điều khiển dâng/giữ cấu trúc; IN điều khiển đánh chặn)*
* **LB / RB / LWB / RWB:** `AR + IN + SR` *(SR mở rộng cho fullback: SR/SR1/SR2)*
* **GK:** Không có hệ chiến thuật đơn AR/CC/AS/...

---

## 3. BẢNG TỔNG HỢP 10 NHÓM VÀ TÙY CHỌN CHUẨN

| Nhóm | Default | `1` | `2` | `3` |
| :--- | :--- | :--- | :--- | :--- |
| **IN** | Đánh chặn thông thường | Đánh chặn chủ động | Đánh chặn bị động | — |
| **DS** | Hỗ trợ phòng ngự cơ bản | Luôn hỗ trợ phòng ngự | Ở phía trên | — |
| **PF** | Giữ vị trí | Di chuyển tự do | Di chuyển rộng *(CAM)* | — |
| **SC** | Hỗ trợ tạt bóng cân bằng | Tham gia tình huống tạt bóng | Không tham gia tình huống tạt bóng | — |
| **CC** | Cân bằng | Di chuyển xâm nhập | Bám biên | Vai trò tự do |
| **AS – CM/CDM** | Tấn công cân bằng | Giữ vị trí | Tham gia tấn công | Vị trí giữa các hậu vệ |
| **DP – ST** | Cân bằng | Luôn luôn hỗ trợ phòng thủ | Luôn ở trên | — |
| **DP – CM/CDM** | Phòng thủ ở biên | Tập trung ở trung lộ | — | — |
| **DB – CDM** | mức chủ động cao nhất sau 6th NF | trung gian | thận trọng nhất | — |
| **SR – fullback** | Hỗ trợ xâm nhập cân bằng | Bó từ cánh vào trung tâm | Phối hợp chồng cánh | — |
| **AR – ST** | Tấn công cân bằng | Xẻ nách | Mục tiêu là anh ấy | Cuộc tấn công giả |
| **AR – fullback** | Tấn công cân bằng | Dâng/chồng cánh | Không tham gia tấn công | — |
| **SR – winger** | Hỗ trợ xâm nhập cân bằng | Xâm nhập sau hàng thủ | Hỗ trợ gần | Tiền đạo mục tiêu |

---

## 4. QUY TẮC CỐT LÕI & CÁC LƯU Ý SỐNG CÒN

1. **`DP1` có hai bản chất khác nhau:**
   * Tiền đạo: `DP1 = Luôn luôn hỗ trợ phòng thủ` (lùi sâu phòng ngự).
   * CM/CDM: `DP1 = Tập trung ở trung lộ` (bảo vệ Zone 14 trước 2 CB).
2. **`DS1` vs `DS2` (Quy định giải FVPL 2026):**
   * `DS1 = Luôn hỗ trợ phòng ngự` (bị cấm ở giải FVPL vì đổ bê tông).
   * `DS2 = Ở phía trên` (chờ phản công).
3. **Cơ chế `DB` của CDM sau 6th Next Field:**
   * Độ chủ động tăng dần: `DB2 < DB1 < DB`.
   * Càng chủ động thì phạm vi di chuyển can thiệp càng rộng, nhưng nếu bắt bài sai sẽ bỏ lại khoảng trống lớn.
4. **Hậu vệ biên (Fullback):**
   * `AR2`: Không tham gia tấn công.
   * `SR1`: Bó từ cánh vào trung tâm (Inverted Fullback).
   * `SR2`: Phối hợp chồng cánh (Overlap).
