# 📖 CƠ SỞ DỮ LIỆU MASTER: CHỈ SỐ ẨN GỐC, TRAIT +5 (NỀN TẢNG) & HLV KỸ NĂNG +8 (CHUYÊN HÓA)
**Dự Án:** FC Online (Garena VN) GLXH Manager Mode — Real Madrid/CU 4-1-4-1-0 Zero-ST  
**Phiên bản:** v1.2.0 (Master Text Database — Chuẩn hóa kép theo vn.fifaaddict.com & In-game Client)  
**Ngày cập nhật:** 30/09/2026  
**Nguồn xác thực kép:** `vn.fifaaddict.com` (Database FC Online VN) + Client Screenshots (Ground Truth)

---

## 📌 MỤC LỤC
1. [Bảng Cấu Hình Toàn Diện Đội Hình (Chuẩn Hóa Theo vn.fifaaddict.com)](#1-bảng-cấu-hình-toàn-diện-đội-hình)
2. [Cơ Sở Dữ Liệu Chi Tiết: Chỉ Số Ẩn Gốc Của Đội Hình (Innate Traits)](#2-cơ-sở-dữ-liệu-chi-tiết-chỉ-số-ẩn-gốc-của-đội-hình)
3. [Cơ Sở Dữ Liệu Toàn Diện: Chỉ Số Ẩn Thường +5 (Special Traits)](#3-cơ-sở-dữ-liệu-toàn-diện-chỉ-số-ẩn-thường-5)
4. [Cơ Sở Dữ Liệu Toàn Diện: HLV Kỹ Năng +8 (Skill Coaches)](#4-cơ-sở-dữ-liệu-toàn-diện-hlv-kỹ-năng-8)
5. [Nguyên Lý Phối Hợp Synergy (Top Acc Blueprint V2)](#5-nguyên-lý-phối-hợp-synergy-top-acc-blueprint-v2)

---

## 1. BẢNG CẤU HÌNH TOÀN DIỆN ĐỘI HÌNH
> **Quy chuẩn phân định 3 tầng chỉ số:**
> * **Chỉ số ẩn gốc (Innate):** Thuộc tính nội tại có sẵn của phôi thẻ trên `vn.fifaaddict.com` và client Garena.
> * **Mốc +5 (Thẻ Bạc):** Mở 1 ô **Chỉ số ẩn thường** (Nền tảng thể lực / kiểm soát bóng).
> * **Mốc +8 (Thẻ Vàng):** Mở 1 ô **HLV kỹ năng** (Chuyên môn hóa vai trò phân khu chiến thuật).

### A. Đội hình xuất phát (Starting XI — 4-1-4-1-0 Wing Zero-ST Tactic A)

| Vị trí | Cầu thủ | Chỉ số ẩn gốc (Innate Traits)<br>*(vn.fifaaddict.com & Client)* | Trait +5 (Nền tảng)<br>`[Hiện tại ➔ Mục tiêu]` | HLV Kỹ năng +8 (Chuyên hóa)<br>`[Hiện tại ➔ Mục tiêu]` | Ý đồ vận hành chiến thuật trong 4-1-4-1-0 Wing Zero-ST GLXH | Trạng thái thực tế |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CAM** *(Central)* | **Karim Benzema BLD +8** | • Sút và tạt má ngoài<br>• Đánh đầu mạnh<br>• Kiến tạo<br>• Sút xoáy | **`Thánh chuyền bóng`** | **`Khả năng khéo léo`** *(HLV: Ezequiel ★7)* | Central False 9: Ở lại phía trên (`DS2`), nhận bóng quay lưng làm tường, phân phối cho LM/RM hoặc dứt điểm trong box (`SC1`). Không dùng IN2. | **🔒 LOCKED GROUND TRUTH** |
| **LM** | **Vini Jr. CU +8** | • Sút xoáy<br>• Sút và tạt má ngoài<br>• Bấm bóng (AI)<br>• Đánh đầu mạnh<br>• Ma tốc độ (AI)<br>• Qua người (AI) | **`Nỗ lực đến cùng`** | **`Di chuyển ngay khi đỡ bước 1`** *(HLV: Michelangelo ★8)* | Inside runner cánh trái: Cắt chéo vào box dứt điểm/cutback (`CC2`, `SC1`); HLV Michelangelo ★8 mang Xâm nhập vòng cấm + Phản ứng xâm nhập + Khéo léo; +8 Di chuyển ngay khi đỡ bước 1. | **🔒 LOCKED GROUND TRUTH** |
| **RM** | **Marcos Llorente UT +9** | • Sút xa (AI)<br>• Ma tốc độ (AI) | **`Nỗ lực đến cùng`** | **`Tổ chức (Candidate)`** *(HLV: Antero Maria B ★7)* | **Tân binh đá chính RM (184cm / 74kg, Stamina nền 119, Chân 5-5):** HLV Antero Maria B khá hợp RM (Khéo léo + Chọc khe + Phản ứng xâm nhập). Trait +5 `Nỗ lực đến cùng` hồi một phần thể lực cuối trận / khi bị dẫn. Slot +8 `Tổ chức` là candidate thử nghiệm lâm sàng quan sát hành vi hồi line cùng Carvajal. | **🟡 PROVISIONAL TEST CONFIG** |
| **LCM** | **J. Bellingham CU +8 [C]** | • Qua người (AI)<br>• Sút xa (AI)<br>• Đánh đầu mạnh<br>• Kiến tạo (AI)<br>• Tinh tế | **`Nỗ lực đến cùng`** | **`Chiến thuật chuyền trực tiếp`** *(HLV: Lasse bộ 1 ★8)* | **Balanced Connector / Nhạc trưởng [C]:** Ép bóng, giữ vị trí (`PF`), tập trung trung lộ (`DP1`), nã đại bác rìa box (`SC2`). Lasse bộ 1 đã có Tổ chức, +8 thêm Chuyền trực tiếp (#2 CM Garena). | **🔒 LOCKED GROUND TRUTH** |
| **RCM** | **F. Valverde CU +8** | • Sút và tạt má ngoài<br>• Chuyền dài (AI)<br>• Sút xa (AI)<br>• Ma tốc độ (AI) | **`Nỗ lực đến cùng`** | **`Tổ chức`** *(HLV: Afanasy ★8)* | Box-to-box runner duy nhất dâng cao đợt hai (`AS2`); nã đại bác rìa box (`SC2`). HLV `Tổ chức` giúp hồi vị trí RCM ngay khi mất bóng, giữ kỷ luật Zone 14. | **🔒 LOCKED GROUND TRUTH** |
| **CDM** | **Casemiro CU +8** | • Xoạc bóng (AI)<br>• Chuyền dài (AI)<br>• Sút xa (AI)<br>• Cứng như thép | **`Siêu cản phá`** | **`Khả năng tắc bóng`** *(HLV: Lasse ★7)* | Single pivot / Anchor: Ở lại sau (`AS1`), cắt đường chuyền (`DB1`), `IN2` kiềm chế dâng cao; HLV Lasse ★7 đã có Cự ly ổn định + Tổ chức; +8 Khả năng tắc bóng tăng tranh chấp mà không phá vỡ vai Anchor. | **🔒 LOCKED GROUND TRUTH** |
| **LB** | **F. Mendy CU +8** | • Đánh đầu mạnh<br>• Ma tốc độ (AI) | **`Siêu cản phá`** | **`PENDING`** | Khóa chặt cánh trái (`AR2` ở lại sau). Chờ rà soát 3 skill HLV tập luyện hiện tại trước khi khóa +8. | ⏳ PENDING HLV SKILLS |
| **LCB** | **Antonio Rüdiger CU +8** | • Đánh đầu mạnh<br>• Chuyền dài (AI)<br>• Xoạc bóng (AI) | **`Siêu cản phá`** | **`Tổ chức (Candidate)`** *(HLV: Lasse bộ 2 ★8)* | **Tân binh đá chính LCB Stopper (190cm / 86kg):** Trait +5 `Siêu cản phá` giải nguy trong khu vực nguy hiểm. HLV Lasse bộ 2 ★8 (Khéo léo + Pressing + Phản công khi thủ) đáng thử nghiệm cho Stopper. Slot +8 `Tổ chức` là candidate thử nghiệm lâm sàng theo dõi hành vi giữ line sau 30-50 trận. | **🟡 PROVISIONAL TEST CONFIG** |
| **RCB** | **Éder Militão CU +8** | • Cứng như thép<br>• Sút xa (AI)<br>• Xoạc bóng (AI) | **`Siêu cản phá`** | **`Tổ chức`** *(HLV: José Enrique ★8)* | Stopper / Recovery CB dập áp sát. HLV José Enrique ★8 có cả Khả năng tắc bóng + Cự ly ổn định, +8 Tổ chức giữ line phòng ngự. | **🔒 LOCKED GROUND TRUTH** |
| **RB** | **Dani Carvajal CU +8** | • Tạt bóng sớm (AI) | **`Siêu cản phá`** | **`PENDING`** | Khóa chặt hành lang phải (`AR2` ở lại sau). Chờ rà soát 3 skill HLV tập luyện hiện tại trước khi khóa +8. | ⏳ PENDING HLV SKILLS |
| **GK** | **Thibaut Courtois CU +8** | • TM lưu ý tạt bóng<br>• TM đối mặt<br>• TM ném xa | **`TM đấm bóng`** | **`Cản phá sút tầm thấp`** *(HLV: Mục tiêu 3 skill sút/gần/xa)* | Thể hình 200cm/96kg giữ khung thành số 1; Trait +5 `TM đấm bóng` giải nguy bóng bổng chống ói bóng; Slot +8 `Cản phá sút tầm thấp` hóa giải điểm yếu sút chìm/sệt. | **🔒 LOCKED GROUND TRUTH** |

---

### B. Cầu thủ Dự bị cốt lõi (Bench Matrix)

| Cầu thủ | Vị trí dự bị | Chỉ số ẩn gốc (Innate Traits)<br>*(vn.fifaaddict.com)* | Trait +5 (Nền tảng) | HLV Kỹ năng +8 (Chuyên hóa) | Ý đồ & Quyết định | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Kepa CU +9** | GK (Phản xạ/1v1) | • TM ném bóng xa | **`TM đối mặt`** | `Cản phá cú sút chìm` | Cựu GK đá chính, dự bị phản xạ cao cấp khi cần thủ môn nhanh nhẹn. | **✅ Dự bị chiến lược** |
| **K. Casteels 23HW +9** | GK (Bắt bóng bổng/Phản xạ) | • TM ném bóng xa<br>• TM đấm bóng | **`TM đối mặt`** | **`Cản phá cú sút chìm`** | Cựu GK baseline cao 197cm; giữ nguyên bằng chứng và cấu hình dự bị cao cấp. | **✅ Dự bị chiến lược** |
| **R. Ferdinand DC +9** | CB (Không chiến/Bọc lót) | • Đánh đầu mạnh<br>• Cứng như thép | **`Siêu cản phá`** | **`Khả năng tắc bóng`** | Siêu trung vệ cao cấp 189cm, sẵn sàng vào sân khi đối thủ dùng ST hộ pháp đè bóng bổng. | **✅ Dự bị chiến lược** |
| **A. Tchouaméni CU +8** | CB / CDM (Bọc lót/Đánh chặn) | • Đánh đầu mạnh<br>• Xoạc bóng (AI)<br>• Thánh chuyền bóng<br>• Sút xa (AI) | **`Nỗ lực đến cùng`** | **`Tổ chức`** *(HLV: Demetrius ★7)* | Dự bị cao cấp đa năng cho LCB và CDM; Tiki-Taka thoát pressing từ đáy sân. | **✅ Dự bị cao cấp** |
| **Rodrygo CU +8** | RM / RW (Super-Sub phút 70) | • Tinh tế<br>• Sút xoáy (AI)<br>• Ma tốc độ (AI)<br>• Qua người (AI) | **`Nỗ lực đến cùng`** | **`Xâm nhập vòng cấm`** *(HLV: Antero Maria B ★7)* | Siêu dự bị cánh phải phút 70: tốc độ xé gió đâm box khi hàng thủ đối phương xuống sức. | **✅ Siêu dự bị tốc độ** |
| **N. Matić VTR +12** | CDM (Chặn quét) | • Cứng như thép | **`Thánh chuyền bóng`** | **`Tập trung đánh chặn`** *(+11 Bạch Kim: `Chủ Động Cản Phá`)* | Siêu mỏ neo thuần thủ khi cần bảo toàn tỷ số. Chuyền bóng phát động từ sâu, chân dài tự động cắt chọc khe. | **✅ Giữ nguyên 100%** |
| **S. Gerrard UT +8** | CM (Điều tiết) | • Sút và tạt má ngoài<br>• Chuyền dài (AI)<br>• Sút xa (AI)<br>• Dễ chấn thương<br>• Tinh tế | **`Thánh chuyền bóng`** | `Cải thiện chuyền xuyên phá` ➔ **`Tấn công với nhịp độ nhanh`** | Tiền vệ chuyền bóng tầm xa, sút xa đại bác. Đổi +8 để đồng bộ nhịp bứt tốc với Valverde/Modrić. | *Cần đổi +8* |
| **M. Desailly WG +5** | CB (Dập) | • Bậc thầy không chiến<br>• Cứng như thép<br>• Sút xa (AI)<br>• Đánh đầu mạnh<br>• Xoạc bóng (AI)<br>• Cứng cỏi<br>• Nỗ lực đến cùng | **`Thánh chuyền bóng`** *(Slot +5 hiện tại: `Siêu cản phá`)* | *[Chưa mở +8]* | Dự bị trung vệ dập tranh chấp cơ bắp sở hữu tới 7 ẩn gốc siêu khủng. | **✅ Giữ nguyên** |
| **J. Koundé FAC +5** | RB / CB | • Chuyên gia đeo bám<br>• Sút xa (AI)<br>• Xoạc bóng (AI) | **`Siêu cản phá`** *(Slot +5 hiện tại: `Xoạc bóng`)* | *[Chưa mở +8]* | Dự bị đa năng hậu vệ biên / trung vệ đeo bám khó chịu. | **✅ Giữ nguyên** |
| **M. Lacroix 25DP +5** | CB (Tốc độ) | • Ma tốc độ (AI) | *[Chưa mở]* | *[Chưa mở]* | Máy bay bọc lót tốc độ thuần túy. | **Dự bị sâu** |
| **Álvaro García 24EP +8** | LW / LAM | • Ma tốc độ (AI) | *[Chưa mở]* | *[Chưa mở]* | Dự bị bứt tốc cánh trái. | **Dự bị** |

---

### C. Mục tiêu Chuyển nhượng (Transfer Roadmap Targets)

| Cầu thủ | Vị trí thay thế | Chỉ số ẩn gốc (Innate Traits)<br>*(vn.fifaaddict.com)* | Trait +5 Mục tiêu | HLV +8 Mục tiêu | Lý do & Ưu thế vượt trội |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Karim Benzema BLD +8** | Thay Havertz CU (CAM) | • Sút xoáy<br>• Bấm bóng (AI)<br>• Cứng như thép<br>• Tinh tế | **`Nỗ lực đến cùng`** *(hoặc `Điềm tĩnh`)* | **`Tạo cơ hội ghi bàn`** | Hai chân 5-5, Dứt điểm 120, Thăng bằng 117, Bình tĩnh 118; sát thủ số 1 trong sơ đồ Zero-ST. |
| **Casemiro CU +8** | Thay Tchouaméni (CDM) | • Chuyền dài (AI)<br>• Sút xa (AI)<br>• Cắt bóng / Đeo bám | **`Nỗ lực đến cùng`** | **`Chiến thuật chuyền Tiki-Taka`** | Mỏ neo thép trứ danh Real Madrid, tranh chấp cực rát, Zone 14 bất khả xâm phạm. |
| **Kepa CU +9** | Thay Casteels (GK) | • TM cản tạt bóng / TM đối mặt | **`TM đối mặt`** | **`Cản phá cú sút chìm`** | Phản xạ 144, Bay người 140, gia cố mốc kích hoạt Team Color CU. |
| **Antonio Rüdiger CU +8** | Thay Ferdinand (RCB) | • Đánh đầu mạnh<br>• Chuyền dài (AI)<br>• Xoạc bóng (AI) | **`Siêu cản phá`** | **`Tổ chức`** | Tốc độ 142, Thể lực 141, sải chân 1m90 càn quét toàn diện. |
| **David Alaba CU +8** | Thay Mendy (LB) | • Sút xoáy<br>• Chuyền dài (AI)<br>• Cản phá / Tạt bóng sớm | **`Nỗ lực đến cùng`** | **`Áp đảo toàn sân`** | Chân 5-4, tạt bóng và thoát pressing biên mượt mà bậc nhất. |

---

## 2. CƠ SỞ DỮ LIỆU CHI TIẾT: CHỈ SỐ ẨN GỐC CỦA ĐỘI HÌNH
> Đây là các thuộc tính bẩm sinh được nạp sẵn vào phôi thẻ trên `vn.fifaaddict.com` và Nexon Open API, quyết định hành vi AI tự nhiên của cầu thủ.

### 1. Ma tốc độ (Speed Dribbler / 스피드 드리블러)
* **Tên tiếng Việt trên vn.fifaaddict.com:** `Ma tốc độ (AI)`
* **Cầu thủ sở hữu:** Vini Jr. CU, F. Valverde CU, F. Mendy CU, Marcos Llorente UT, M. Lacroix 25DP.
* **Cơ chế kích hoạt:** Khi cầu thủ đang dốc bóng dọc hành lang trống trải, AI tự động kích hoạt động tác đẩy bóng dài bằng mu bàn chân và đạt vận tốc bứt phá tối đa (Top Speed) nhanh hơn các cầu thủ không có ẩn này.
* **Ý nghĩa GLXH:** Giúp tiền đạo cánh (Vini Jr.), tiền vệ cánh (Llorente) và tiền vệ con thoi (Valverde) thoát khỏi sự áp sát của đối phương chỉ sau một nhịp dốc bóng.

### 2. Sút xa (Long Shot Taker / 중거리 슛)
* **Tên tiếng Việt trên vn.fifaaddict.com:** `Sút xa (AI)`
* **Cầu thủ sở hữu:** J. Bellingham CU, L. Modrić CU, F. Valverde CU, Marcos Llorente UT, A. Tchouaméni CU, Éder Militão CU, S. Gerrard UT, M. Desailly WG, J. Koundé FAC.
* **Cơ chế kích hoạt:** Tăng tần suất vung chân sút xa khi cầu thủ nhận bóng ở khoảng trống Zone 14 (rìa vòng 16m50 đến cự ly 25m). Tăng vận tốc bay của trái bóng và giảm thiểu tỷ lệ bóng ăn ra má ngoài bay chệch cột.
* **Ý nghĩa GLXH:** Cực kỳ ăn khớp với thiết lập `SC2` (Chờ ngoài rìa vòng cấm) của Modrić, Valverde và Llorente; tạo ra mối đe dọa thường trực từ tuyến hai.

### 3. Kiến tạo (Through Ball Passer / 스루 패스)
* **Tên tiếng Việt trên vn.fifaaddict.com:** `Kiến tạo (AI)`
* **Cầu thủ sở hữu:** J. Bellingham CU, L. Modrić CU.
* **Cơ chế kích hoạt:** AI tự động tính toán độ trễ và lực chuyền chọc khe (W / ZW) để bóng lượn qua khe giữa hai trung vệ đối phương. Giảm tỷ lệ chuyền bóng sửa lưng đồng đội hoặc chuyền thẳng vào chân đối thủ.
* **Ý nghĩa GLXH:** Cốt lõi của các pha phản công nhanh; Modrić và Bellingham là 2 ngòi nổ phát động bóng quyết định.

### 4. Sút và tạt má ngoài (Outside Foot Shot / Cross / 바깥쪽 슈팅)
* **Tên tiếng Việt trên vn.fifaaddict.com:** `Sút và tạt má ngoài`
* **Cầu thủ sở hữu:** L. Modrić CU, F. Valverde CU, Vini Jr. CU, K. Havertz CU, S. Gerrard UT.
* **Cơ chế kích hoạt:** Khi góc sút hoặc tư thế nhận bóng không thuận lợi để sút mu chính diện hoặc cứa lòng ZD, cầu thủ tự động vung má ngoài chân thuận (Trivela) để đưa bóng lượn hình cánh cung vào góc xa.
* **Ý nghĩa GLXH:** Tăng tỷ lệ dứt điểm thành bàn ở các góc hẹp mà không mất thời gian đảo chân.

### 5. Cứng như thép (Solid Player / 강철 체력 / 단단한 신체)
* **Tên tiếng Việt trên vn.fifaaddict.com:** `Cứng như thép` (hoặc `Cứng cỏi`)
* **Cầu thủ sở hữu:** K. Havertz CU, Éder Militão CU, R. Ferdinand DC, N. Matić VTR, M. Desailly WG, K. Benzema BLD, Casemiro CU. (Lưu ý: Rüdiger CU và Llorente UT KHÔNG có ẩn này bẩm sinh).
* **Cơ chế kích hoạt:** Tăng chỉ số thăng bằng ẩn khi có va chạm vật lý; giảm thời gian loạng choạng khi bị đối phương tì đè hoặc húc vai. Hạn chế tối đa chấn thương.
* **Ý nghĩa GLXH:** Giúp trung vệ (Ferdinand, Militão) và CDM (Casemiro) đứng vững trước các tiền đạo to khỏe; giúp Havertz RM tì đè làm tường chắc chắn.

### 6. Đánh đầu mạnh (Power Header / 파워 헤더)
* **Tên tiếng Việt trên vn.fifaaddict.com:** `Đánh đầu mạnh`
* **Cầu thủ sở hữu:** Antonio Rüdiger CU, J. Bellingham CU, Vini Jr. CU, A. Tchouaméni CU, F. Mendy CU, R. Ferdinand DC, M. Desailly WG.
* **Cơ chế kích hoạt:** Khi bật nhảy đón bóng bổng (phạt góc hoặc tạt cánh), cầu thủ gập cổ và lắc đầu với lực đập bóng cực mạnh, bóng đi căng và cắm thẳng xuống đất khiến thủ môn khó cản phá.
* **Ý nghĩa GLXH:** Biến Rüdiger, Bellingham và Tchouaméni thành hiểm họa bóng chết cố định; giúp Mendy, Ferdinand và Rüdiger phá bóng bổng an toàn.

### 7. Qua người & Tinh tế (Technical Dribbler & Flair)
* **Tên tiếng Việt trên vn.fifaaddict.com:** `Qua người (AI)` & `Tinh tế`
* **Cầu thủ sở hữu:** J. Bellingham CU, Vini Jr. CU, L. Modrić CU, S. Gerrard UT.
* **Cơ chế kích hoạt:** Thu hẹp bán kính xoay xở; cầu thủ đỡ bước một gọn gàng, có thể thực hiện các pha gạt bóng ngẫu hứng loại bỏ đối thủ trong phạm vi hẹp.
* **Ý nghĩa GLXH:** Giúp tuyến giữa thoát pressing mượt mà, không bị cứng đơ khi bị đối thủ áp sát rát.

### 8. Xoạc bóng (Dives Into Tackles / 슬라이딩 태클 선호)
* **Tên tiếng Việt trên vn.fifaaddict.com:** `Xoạc bóng (AI)`
* **Cầu thủ sở hữu:** Éder Militão CU, A. Tchouaméni CU, M. Desailly WG, J. Koundé FAC, A. Rüdiger CU.
* **Cơ chế kích hoạt:** AI hậu vệ tự động kích hoạt các pha trượt xoạc cản bóng khi đối phương chuẩn bị tung cú sút hoặc bứt tốc qua người.

### 9. Tạt bóng sớm (Early Crosser / 얼리 크로스)
* **Tên tiếng Việt trên vn.fifaaddict.com:** `Tạt bóng sớm (AI)`
* **Cầu thủ sở hữu:** Dani Carvajal CU.
* **Cơ chế kích hoạt:** Tự động thực hiện quả tạt cong điểm rơi từ cự ly xa (ngang mép vòng cấm) mà không cần phải dốc bóng xuống tận đáy biên.
* **Ý nghĩa GLXH:** Phù hợp hoàn hảo với lệnh `AR2` (ở lại sau) của Carvajal; Carvajal đứng từ sân nhà phất bóng điểm rơi cho Havertz và Bellingham băng cắt.

### 10. TM đấm bóng & TM ném bóng xa (GK Puncher & Long Throw)
* **Tên tiếng Việt trên vn.fifaaddict.com:** `TM đấm bóng` & `TM ném bóng xa`
* **Cầu thủ sở hữu:** K. Casteels 23HW.
* **Cơ chế kích hoạt:** Chủ động đấm bóng giải nguy trong các pha phạt góc lộn xộn; ném bóng xa chính xác tới tận giữa sân để phát động phản công nhanh chớp nhoáng.

---

## 3. CƠ SỞ DỮ LIỆU TOÀN DIỆN: CHỈ SỐ ẨN THƯỜNG +5 (SPECIAL TRAITS)
> **Quy định hệ thống:** Mở khóa khi thẻ đạt mốc **+5 (Thẻ Bạc)**. Cầu thủ được chọn thêm **1 Chỉ số ẩn Thường** trong danh mục sau.

### Bảng Từ Điển Trait Thường Chi Tiết (Chuẩn vn.fifaaddict.com):

#### 1. Nỗ lực đến cùng (Two Hearts / Second Wind / 2개의 심장)
* **Tên trên vn.fifaaddict.com:** `Nỗ lực đến cùng` (Second Wind)
* **Cơ chế chính thức Garena/NEXON:** Kích hoạt cơ chế hồi phục một phần thanh thể lực khi trận đấu trôi về cuối trận hoặc khi đội nhà đang ở thế bị dẫn bàn; không tăng trần thể lực (stamina cap) và không tạo trạng thái bất tử thể lực tuyệt đối.
* **Cơ chế GLXH thực tế (FC INFO 2026):** Giúp giảm thiểu đáng kể hình phạt hao hụt thể lực vào cuối trận, hỗ trợ duy trì tốc độ và độ chuẩn xác hành vi cho các vị trí di chuyển nhiều trong sơ đồ pressing hoặc chuyển đổi trạng thái liên tục.
* **Đánh giá GLXH:** **TIER 0 (Ưu tiên hàng đầu cho trục di chuyển)**.
* **Vị trí phù hợp:** Các cầu thủ di chuyển liên tục ngoài sân (đặc biệt là tiền vệ cánh, tiền vệ con thoi và hậu vệ biên).

#### 2. Kiến tạo (Through Ball Passer / AI 스루 패스)
* **Tên trên vn.fifaaddict.com:** `Kiến tạo (AI)`
* **Cơ chế chính thức:** Tối ưu hóa quỹ đạo và độ xoáy của các đường chọc khe sệt xuyên tuyến, đưa bóng vừa tầm di chuyển của đồng đội.
* **Đánh giá GLXH:** **TIER 1 (Rất mạnh)** cho CAM kiến thiết hoặc Winger kiến tạo.

#### 3. Thánh chuyền bóng (Playmaker / 플레이 메이커)
* **Tên trên vn.fifaaddict.com:** `Thánh chuyền bóng` (hoặc `Chuyên gia chuyền bóng`)
* **Cơ chế chính thức:** Tăng tầm nhìn bao quát và độ chuẩn xác của các đường phân phối bóng trên toàn sân; cầu thủ có xu hướng chủ động xin bóng để làm bóng.
* **Đánh giá GLXH:** **TIER 1** cho tiền vệ kiến thiết lùi sâu (Deep-lying Playmaker) hoặc CDM phân phối bóng.

#### 4. Sút xoáy (Finesse Shot / 예리한 감아차기)
* **Tên trên vn.fifaaddict.com:** `Sút xoáy`
* **Cơ chế chính thức:** Tăng độ cong, độ xoáy và độ hiểm hóc của các pha cứa lòng (ZD).
* **Đánh giá GLXH:** **TIER 1** cho Winger hoặc CAM thích dứt điểm ZD.

#### 5. Sút xa (Long Shot Taker / 중거리 슛)
* **Tên trên vn.fifaaddict.com:** `Sút xa (AI)`
* **Cơ chế chính thức:** Tăng uy lực và độ chuẩn xác của các pha nã đại bác từ cự ly ngoài vòng 16m50.

#### 6. Siêu cản phá (Fancy Clearance / 화려한 걷어내기)
* **Tên trên vn.fifaaddict.com:** `Siêu cản phá`
* **Cơ chế chính thức:** Kích hoạt các động tác bay người, móc bóng, phá bóng ngoạn mục giải nguy trên vạch vôi.
* **Đánh giá GLXH:** **TIER 1 (Phòng ngự)** cho CB, LB, RB.

#### 7. TM đối mặt (GK One on One / 1:1 수비)
* **Tên trên vn.fifaaddict.com:** `TM đối mặt`
* **Cơ chế chính thức:** Tăng phản xạ khép góc và tỷ lệ cản phá thành công trong các pha đối mặt tiền đạo đối phương.
* **Đánh giá GLXH:** **TIER 0 cho Thủ môn (GK)**.

---

## 4. CƠ SỞ DỮ LIỆU TOÀN DIỆN: HLV KỸ NĂNG +8 (SKILL COACHES)
> **Quy định hệ thống:** Mở khóa khi thẻ đạt mốc **+8 (Thẻ Vàng)**. Mỗi cầu thủ được kích hoạt 1 HLV Kỹ Năng chuyên hóa.

### NHÓM 1: TẤN CÔNG & DỨT ĐIỂM
* **`Tạo cơ hội ghi bàn` (Chance Creation Mastery):** Buff độ chuẩn xác đường chuyền & cú sút trong vòng cấm 16m50. **TIER 0 cho ST / CAM đóng vai ST ảo**.
* **`Tấn công với nhịp độ nhanh` (Fast Tempo Attack):** Bứt tốc phá tuyến, đón bóng hai, chuyển trạng thái chớp nhoáng. **TIER 0 cho băng chuyền 4 tiền vệ runner LM - LCM - RCM - RM**.
* **`Xâm nhập vòng cấm` (Pass & Run):** Sau khi chuyền phối hợp QS lập tức chạy chỗ vào vòng cấm. **TIER 1**.
* **`Di chuyển ngay khi đỡ bước 1` (First Touch):** Đỡ bước 1 đẩy bóng bứt tốc tức thì. **TIER 1**.
* **`Khả năng khéo léo` (Physical Mastery):** Tăng khả năng tì đè và che chắn bóng khi bị áp sát. **TIER 1**.

### NHÓM 2: CHUYỀN BÓNG & KIỂM SOÁT
* **`Chiến thuật chuyền Tiki-Taka` (Tiki-Taka Mastery):** Chuyền ngắn dưới 3 chạm chuẩn xác tuyệt đối, bóng đi mượt mà. **TIER 0 cho Single Pivot (CDM)**.
* **`Cải thiện chuyền xuyên phá` (Driven Through Pass):** Tăng tốc độ và độ hiểm của chọc khe sệt xuyên tuyến. **TIER 1**.

### NHÓM 3: PHÒNG NGỰ & HÀNG THỦ
* **`Cự ly đội hình ổn định` (Defensive Reorganization / Regroup):** Khi mất bóng lập tức lùi về vị trí, tái lập cự ly khối phòng ngự nguyên vẹn. **TIER 0 cho CB và CDM**.
* **`Áp đảo toàn sân` (Pitch Dominance):** Bao quát kiểm soát không gian khi thi đấu pressing toàn sân. **TIER 0 cho Hậu vệ biên (LB - RB)**.
* **`Khả năng tắc bóng` (Standing Tackle Mastery):** Tăng tỷ lệ thành công khi tắc bóng đứng. **TIER 1**.
* **`Tập trung đánh chặn` (Focus on Interception):** Tăng phản xạ thò chân cắt chọc khe sệt. **TIER 1**.

### NHÓM 4: THỦ MÔN (GK SKILL COACHES)
* **`Cản phá cú sút chìm` (Low Shot Defense):** Tăng tốc độ đổ người cản phá sút sệt hiểm hóc (D / DD chéo góc). **TIER 0 BẮT BUỘC cho thủ môn cao kều**.
* **`Cản phá sút xa` (Long Shot Defense):** Tăng khả năng bay người đẩy đại bác ngoài cấm địa.

---

## 5. NGUYÊN LÝ PHỐI HỢP SYNERGY (TOP ACC BLUEPRINT V2)

```text
                                [CAM: Bellingham / Havertz]
                           Innate: Sút xa, Kiến tạo, Đánh đầu, Qua người
                           Trait: Nỗ lực đến cùng (Two Hearts)
                           HLV: Tạo cơ hội ghi bàn (Chance Creation)
                                         ▲
                                         │ (Phối hợp nhanh & Xâm nhập box)
   [LM: Vini Jr.]                                                        [RM: Havertz]
Innate: Ma tốc độ, Sút xoáy                                           Innate: Cứng như thép, Sút má ngoài
Trait: Nỗ lực đến cùng                                                Trait: Nỗ lực đến cùng (hoặc Kiến tạo)
HLV: Tấn công nhịp độ nhanh                                           HLV: Tấn công nhịp độ nhanh (hoặc Ghi bàn)
            ▲                                                                    ▲
            │                                                                    │
            └────────► [LCM: Modrić]                 [RCM: Valverde] ◄───────────┘
                  Innate: Kiến tạo, Sút xa        Innate: Ma tốc độ, Sút xa
                  Trait: Nỗ lực đến cùng          Trait: Nỗ lực đến cùng
                  HLV: Tấn công nhịp độ nhanh     HLV: Tấn công nhịp độ nhanh
                                         ▲
                                         │ (Thoát pressing 1-2 chạm)
                                [CDM: Tchouaméni]
                           Innate: Đánh đầu mạnh, Thánh chuyền bóng
                           Trait: Nỗ lực đến cùng (Two Hearts)
                           HLV: Chiến thuật chuyền Tiki-Taka
                                         ▲
                                         │ (Bọc lót chống phản công)
    [LB: Mendy]           [LCB: Militão]          [RCB: Ferdinand]          [RB: Carvajal]
Innate: Ma tốc độ       Innate: Cứng như thép   Innate: Đánh đầu mạnh    Innate: Tạt bóng sớm
Trait: Nỗ lực đến cùng  Trait: Nỗ lực đến cùng   Trait: Nỗ lực đến cùng   Trait: Nỗ lực đến cùng
HLV: Áp đảo toàn sân    HLV: Cự ly ổn định       HLV: Cự ly ổn định       HLV: Áp đảo toàn sân
                                         ▲
                                         │
                                [GK: Casteels 23HW]
                             Innate: TM ném xa, TM đấm bóng
                             Trait: TM đối mặt (1v1)
                             HLV: Cản phá cú sút chìm (Low Shot)
```
