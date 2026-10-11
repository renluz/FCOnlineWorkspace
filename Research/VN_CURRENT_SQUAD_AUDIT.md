# 📋 BÁO CÁO KIỂM TOÁN ĐỘI HÌNH HIỆN TẠI (VN_CURRENT_SQUAD_AUDIT.md)
*Thời điểm cập nhật:* 2026-09-19 00:54:00 (UTC+7)  
*Mục tiêu:* `VN_GLXH_CURRENT_SQUAD_OPTIMIZATION` (Tối ưu hóa sơ đồ từ đúng 13 cầu thủ người dùng thực tế đang sở hữu)  
*Nguồn dữ liệu:* [data/vn_owned_players.json](file:///E:/FCOnlineWorkspace/Research/data/vn_owned_players.json) & [exports/vn_owned_player_identity_map.csv](file:///E:/FCOnlineWorkspace/Research/exports/vn_owned_player_identity_map.csv)

---

## 1. 💰 THÔNG SỐ QUỸ LƯƠNG (SALARY CAP)
* **Trần lương tài khoản Garena VN hiện tại:** `305`
* **Tổng lương 11 cầu thủ đá chính:** `263`
* **Quỹ lương còn dư:** `42` (Dư dồi dào, hoàn toàn không bị kịch trần)
* **Tổng lương toàn bộ 13 cầu thủ sở hữu:** `297 / 305`

---

## 2. 🛡️ 11 CẦU THỦ ĐÁ CHÍNH ĐƯỢC CHỌN (SƠ ĐỒ 4-2-3-1 / BIẾN THỂ SCREENSHOT)

| Slot Bố Trí (`current_slot`) | Cầu Thủ | Mùa Thẻ | Cấp Thẻ | OVR Hiển Thị (`displayed_ovr`) | Base OVR Thẻ (+1) | Lương | Vị Trí Tự Nhiên (`natural_positions`) | Nguồn Xác Minh | Vai Trò Vận Hành GLXH |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **ST** | V. Boniface | `WS` | `+3` | **119** | 117 | `28` | `['ST']` | FCOPLAYERS & FIFAAddict | Target Man càn lướt làm tường, 5/5 hai chân, dứt điểm một chạm |
| **CAM** | T. Rosicky | `WG` | `+1` | **118** | 118 | `30` | `['LM', 'CM']` | FCOPLAYERS | Nhạc trưởng trung lộ, chọc khe kiến tạo và phân phối nhịp |
| **CAM / LAM** | Park Ji Sung | `NO.7` | `+1` | **117** | 118 | `29` | `['CAM', 'LM']` | FCOPLAYERS & FIFAAddict | Tiền vệ công cơ động, pressing tầm cao và bao quát biên |
| **LW / RAM** | A. Del Piero | `HOT` | `+1` | **102** | 97 | `20` | `['CF', 'CAM']` | FCOPLAYERS & FIFAAddict | Tiền đạo lùi / Tiền vệ công dạt nách trung lộ dứt điểm ZD |
| **LCM / LDM** | R. Gullit | `HOT` | `+1` | **103** | 98 | `22` | `['CM', 'LW', 'ST']` | FIFAAddict Verified | Box-to-box cơ động, không chiến, sút xa tuyến hai |
| **RCM / RDM** | Rodri | `19` | `+1` | **95** | 92 | `17` | `['CDM', 'CM']` | FIFAAddict Verified | Mỏ neo thuần túy (Anchor), giữ cự ly bọc lót trước 2 trung vệ |
| **LB** | J. Gvardiol | `25DP` | `+1` | **118** | 118 | `29` | `['LB', 'CB']` | FCOPLAYERS & FIFAAddict | Hậu vệ biên phòng ngự, 5/5 hai chân, chống leo biên |
| **LCB / CB** | Sergio Ramos | `19` | `+1` | **94** | 94 | `18` | `['CB']` | FIFAAddict & details | Trung vệ dập, áp sát tranh chấp quyết liệt |
| **RCB / CB** | F. Schar | `25DP` | `+1` | **114** | 114 | `27` | `['CB']` | FCOPLAYERS & FIFAAddict | Trung vệ thòng bọc lót, chống bóng bổng và QW |
| **RB** | G. Zambrotta | `WG` | `+1` | **119** | 119 | `30` | `['RB', 'LB']` | FIFAAddict Verified | Hậu vệ cánh đẳng cấp thế giới, tốc độ 121, thủ 122, 5/5 hai chân |
| **GK** | W. Hennessey | `HOT` | `+1` | **96** | 91 | `13` | `['GK']` | FCOPLAYERS & FIFAAddict | Thủ môn 1m98, khép góc và khống chế bóng bổng |

*Tổng OVR trung bình 11 cầu thủ chính:* **108.6**

---

## 3. 🔄 CẦU THỦ DỰ BỊ (BENCH PLAYERS)

| Slot Dự Bị (`current_slot`) | Cầu Thủ | Mùa Thẻ | Cấp Thẻ | OVR Hiển Thị | Base OVR | Lương | Vị Trí Tự Nhiên | Nguồn Xác Minh | Vai Trò Dự Bị |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **RW** | Inaki Williams | `HOT` | `+1` | **95** | 90 | `16` | `['ST', 'RW']` | FCOPLAYERS & FIFAAddict | Cầu thủ tốc độ quấy phá hành lang biên (Đúng sở trường RW) |
| **ST** | P. Aubameyang | `LH` | `+1` | **96** | 92 | `18` | `['ST', 'LW', 'RW']` | FIFAAddict Verified | Tiền đạo cắm bứt tốc phản công khi Boniface xuống sức |

---

## 4. ⚠️ ĐÁNH GIÁ CẦU THỦ ĐÁ LỆCH SỞ TRƯỜNG (OUT-OF-POSITION ANALYSIS)
*Phần phân tích này đã được chuẩn hóa lại 100% dựa trên danh sách vị trí tự nhiên (`natural_positions`) từ FCOPLAYERS và FIFAAddict:*

1. **G. Zambrotta (WG)**:
   - *Vị trí tự nhiên:* `['RB', 'LB']`.
   - *Slot bố trí hiện tại:* `RB`.
   - *Đánh giá:* **HOÀN TOÀN ĐÚNG VỊ TRÍ SỞ TRƯỜNG**. Thẻ sở hữu sở trường cả hai biên RB và LB với chỉ số phòng thủ 122, tốc độ 121 và thể lực 123.
2. **Rodri (19)**:
   - *Vị trí tự nhiên:* `['CDM', 'CM']`.
   - *Slot bố trí hiện tại:* `RCM` (hoặc kéo lùi RDM).
   - *Đánh giá:* **HOÀN TOÀN ĐÚNG VỊ TRÍ SỞ TRƯỜNG**. Thẻ bao quát cả vị trí CM và CDM.
3. **R. Gullit (HOT)**:
   - *Vị trí tự nhiên:* `['CM', 'LW', 'ST']`.
   - *Slot bố trí hiện tại:* `LCM` (hoặc kéo lùi LDM).
   - *Đánh giá:* **HOÀN TOÀN ĐÚNG VỊ TRÍ SỞ TRƯỜNG CM/LCM**.
4. **Inaki Williams (HOT)**:
   - *Vị trí tự nhiên:* `['ST', 'RW']`.
   - *Slot bố trí hiện tại:* `RW`.
   - *Đánh giá:* **HOÀN TOÀN ĐÚNG VỊ TRÍ SỞ TRƯỜNG RW**.
5. **A. Del Piero (HOT)**:
   - *Vị trí tự nhiên:* `['CF', 'CAM']`.
   - *Slot bố trí hiện tại:* `LW` (hoặc RAM).
   - *Đánh giá:* Hơi lệch biên so với trục trung lộ (CF/CAM), tuy nhiên phong cách dạt nách trung lộ ZD của Del Piero tận dụng rất tốt vị trí tiền đạo cánh ảo.
6. **T. Rosicky (WG)**:
   - *Vị trí tự nhiên:* `['LM', 'CM']`.
   - *Slot bố trí hiện tại:* `CAM`.
   - *Đánh giá:* Đẩy cao 1 nấc từ CM lên CAM, phát huy tối đa nhãn quan kiến tạo.

---

## 5. 📉 3 VỊ TRÍ YẾU NHẤT TRONG ĐỘI HÌNH CHÍNH (WEAKEST POSITIONS)

Dựa trên OVR hiển thị, Base OVR và chất lượng phôi thẻ thực tế:

1. **🔴 Vị trí 1: LCB — Sergio Ramos (Mùa 19, +1, OVR Hiển Thị 94, Base OVR 94, Lương 18)**
   - *Điểm yếu:* Phôi thẻ mùa cũ 19 (+1) với OVR 94 thấp nhất đội hình chính. Tốc độ xuất phát và khả năng tranh chấp tay đôi trước các tiền đạo OVR 115+ hiện tại rất mong manh.
2. **🔴 Vị trí 2: RDM/RCM — Rodri (Mùa 19, +1, OVR Hiển Thị 95, Base OVR 92, Lương 17)**
   - *Điểm yếu:* Base OVR 92 ở mức +1 khiến tốc độ và thể lực chưa đáp ứng được nhịp độ pressing dồn dập ở GLXH, dễ bị hụt hơi ở nửa cuối hiệp 2.
3. **🔴 Vị trí 3: GK — W. Hennessey (Mùa HOT, +1, OVR Hiển Thị 96, Base OVR 91, Lương 13)**
   - *Điểm yếu:* Dù có chiều cao 1m98 lý tưởng, Base OVR 91 ở mức +1 khiến các chỉ số phản xạ và đổ người cơ bản còn hạn chế trước những pha nã đại bác ngoài vòng cấm.

---

## 6. 🚫 NGUYÊN TẮC BẢO TOÀN (NO BUYING RECOMMENDATION AT THIS STAGE)
Theo đúng chỉ thị cốt lõi, bước này **TUYỆT ĐỐI KHÔNG ĐỀ XUẤT MUA CẦU THỦ MỚI**. Toàn bộ phân tích và cấu hình sơ đồ được xây dựng để khai thác 100% tiềm năng của đúng 13 cầu thủ bạn đang nắm giữ trên tài khoản.
