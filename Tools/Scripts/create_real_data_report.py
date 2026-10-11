# create_real_data_report.py
import datetime

now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S (UTC+7)")

content = f"""# BÁO CÁO DỮ LIỆU THỰC NGHIỆM GIẢ LẬP XẾP HẠNG FC ONLINE (GLXH / MANAGER MODE)
**Tài liệu dành cho ChatGPT và Chuyên viên Phân tích Đội hình**
*Thời điểm tạo báo cáo:* {now_str}
*Thư mục dự án:* `E:\\FCOnlineWorkspace\\Research`

---

## 1. 🔐 TRẠNG THÁI XÁC THỰC API (API AUTHENTICATION STATUS)

### Kết quả kiểm tra:
* **`API_AUTH = FAIL`**
* **Nguyên nhân cốt lõi:**
  Biến môi trường `NEXON_OPEN_API_KEY` không tồn tại trong tiến trình thực thi hiện tại và không tìm thấy trong Windows Registry (`HKEY_CURRENT_USER\\Environment` và `HKEY_LOCAL_MACHINE\\...\\Environment`).
* **Chi tiết mã lỗi HTTP thực tế (Actual HTTP Error):**
  - **Endpoint kiểm thử:** `GET https://open.api.nexon.com/fconline/v1/ranker-stats?matchtype=52`
  - **HTTP Status Code:** `400 Bad Request`
  - **Phản hồi lỗi chính thức từ máy chủ Nexon:**
    ```json
    {{"error": {{"name": "OPENAPI00004", "message": "Please input valid parameter"}}}}
    ```
    *(Mã lỗi xuất hiện khi thiếu tiêu đề xác thực `x-nxopen-api-key` hoặc tham số truy vấn).*
  - Khi gửi kèm key không hợp lệ (`dummy_key`):
    ```json
    {{"error": {{"name": "OPENAPI00005", "message": "The apikey is not valid."}}}}
    ```

---

## 2. 🛡️ CHÍNH SÁCH BẢO TOÀN DỮ LIỆU & LOẠI BỎ DỮ LIỆU GIẢ LẬP (ZERO FALLBACK POLICY)

Tuân thủ nghiêm ngặt chỉ thị của người dùng:
1. **Loại bỏ hoàn toàn file ranker offline:** Các file `glxh_ranker_stats.csv` và `glxh_ranker_stats.json` tạo từ phiên trước (dùng fallback rỗng) đã được **XÓA BỎ VĨNH VIỄN**.
2. **Trạng thái ghi nhận:** **`REAL_RANKER_DATA_UNAVAILABLE`**.
3. **Phân tách danh sách ứng viên offline:** Toàn bộ danh sách 135 cầu thủ lọc theo OVR từ database được chuyển sang tên mới:
   - `exports\\glxh_offline_candidates.csv`
   - `exports\\glxh_offline_candidates.json`
   Tuyệt đối không để lẫn lộn với dữ liệu ranker thật.
4. **Cam kết tồn tại file ranker thật:** File `glxh_ranker_stats.csv`, `glxh_ranker_stats.json` và các file `exports\\real_glxh_*.csv` **CHỈ ĐƯỢC PHÉP TỒN TẠI** khi được tạo ra từ dữ liệu thật nhận về từ máy chủ NEXON với `matchtype = 52`.

---

## 3. 🎯 THIẾT LẬP MATCH TYPE & PHẠM VI DỮ LIỆU
* **Match Type bắt buộc:** **`matchtype = 52`** (`감독모드` - Manager Mode / Giả Lập Xếp Hạng).
* **Tuyệt đối loại trừ:** **`matchtype = 50`** (Xếp hạng 1v1 đá tay). Dữ liệu rank tay phản ánh kỹ năng micro của người chơi, hoàn toàn sai lệch so với logic AI tự động của GLXH.

---

## 4. 🔬 PHÂN TÍCH CẤU TRÚC FIELD TỪ NEXON OPEN API (SCHEMA ANALYSIS)

Hệ thống phân định rành mạch 3 nhóm trường dữ liệu:

### 4.1. Nhóm Dữ Liệu Gốc từ NEXON API (`RAW_NEXON_*`)
Được trích xuất nguyên bản từ response JSON mẫu tại `data\\ranker_stats_52_raw_sample.json`:
* `RAW_NEXON_spId`: Mã ID định danh cầu thủ.
* `RAW_NEXON_spPosition`: Mã vị trí thi đấu trên sân.
* `RAW_NEXON_matchCount`: Số trận đấu mà Top 10.000 ranker đưa cầu thủ này vào sân.
* `RAW_NEXON_shoot`: Số cú sút trung bình/trận.
* `RAW_NEXON_effectiveShoot`: Số cú sút trúng đích trung bình/trận.
* `RAW_NEXON_goal`: Số bàn thắng ghi được trung bình/trận.
* `RAW_NEXON_assist`: Số kiến tạo trung bình/trận.
* `RAW_NEXON_passTry` & `RAW_NEXON_passSuccess`: Số đường chuyền thử/thành công.
* `RAW_NEXON_dribble`, `RAW_NEXON_dribbleTry`, `RAW_NEXON_dribbleSuccess`: Thống kê rê dắt.
* `RAW_NEXON_block` & `RAW_NEXON_tackle`: Cản phá và tắc bóng trung bình.
* `RAW_NEXON_createDate`: Thời điểm tổng hợp số liệu từ máy chủ.

### 4.2. Nhóm Dữ Liệu Từ Database Cầu Thủ (`DATABASE_*`)
Nguồn từ 41.289 cầu thủ trong `repos\\fconline-player-search\\data\\details.csv`:
* Chiều cao (`DATABASE_height`), Cân nặng (`DATABASE_weight`), Chân nghịch (`DATABASE_left_foot`, `DATABASE_right_foot`).
* Lương (`DATABASE_salary`), Chỉ số OVR (`DATABASE_ovr`).
* Chỉ số chi tiết: `finishing`, `positioning`, `shot_power`, `long_shots`, `interceptions`, `marking`, `standing_tackle`, `heading`, `strength`, `stamina`.
* Thuộc tính đặc biệt: `traits` (chỉ số ẩn), `team_colors` (buff đội bóng).

### 4.3. Nhóm Metric Mô Tả Thực Nghiệm (`CALC_*`)
Tính toán độc lập trong `tools\\glxh_meta_analyzer.py` (không phán xét hay gọi là "best player score"):
* `CALC_usage_index`: Tỷ lệ ra sân tương đối so với cầu thủ xuất hiện nhiều nhất.
* `CALC_goal_per_appearance`: Tỷ lệ ghi bàn / trận.
* `CALC_assist_per_appearance`: Tỷ lệ kiến tạo / trận.
* `CALC_shot_efficiency`: Tỷ lệ chuyển hóa bàn thắng từ cú sút (`goal / shoot`, null nếu shoot = 0).
* `CALC_defensive_action_index`: Tổng số lần can thiệp phòng ngự (`block + tackle`).

---

## 5. ⚠️ DỮ LIỆU BỊ THIẾU & GIỚI HẠN CỦA NEXON OPEN API (LIMITATIONS)

1. **Không có cấp thẻ cộng (`enhancement_level` / `spGrade`):** API `ranker-stats` gộp chung mọi mức thẻ của cùng một `spId`. Không thể biết ranker dùng thẻ +1, +5 hay +8 nếu chỉ nhìn vào endpoint này.
2. **Không có chỉ số cắt bóng (`interceptions`):** Thống kê phòng ngự trong `ranker-stats` chỉ ghi nhận `block` và `tackle`.
3. **Không có điểm số trận đấu (`rating`):** Chỉ số `spRating` chỉ xuất hiện khi cào chi tiết từng trận đơn lẻ (`/v1/match-detail`), không có trong tổng hợp meta `ranker-stats`.
4. **Không có bối cảnh Thắng / Thua:** Dữ liệu phản ánh thông số cá nhân cầu thủ, không gắn liền trực tiếp với kết quả chung cuộc của trận đấu.
5. **Cơ chế truy vấn đảo (Inverted Query Mechanism):** Endpoint `ranker-stats` **BẮT BUỘC** người gọi phải gửi danh sách cầu thủ cần tra cứu (`players=[{{"id":..., "po":...}}]`). Nexon không cung cấp endpoint kiểu `GET /top-100-players` trả về sẵn danh sách tự động.

---

## 6. 🌏 KHÁC BIỆT GIỮA MÁY CHỦ HÀN QUỐC (NEXON) & VIỆT NAM (GARENA)

ChatGPT và chuyên viên phân tích cần đặc biệt lưu ý khi áp dụng dữ liệu:
* **Độ trễ cập nhật mùa thẻ:** Máy chủ Hàn Quốc luôn ra mắt mùa thẻ mới (ví dụ thẻ mới nhất, ICON TM, thẻ mùa hiện tại) trước máy chủ Garena Việt Nam từ 2 - 6 tuần.
* **Quy định trần lương (Salary Cap):** Trần lương và giới hạn icon giữa hai máy chủ có thể chênh lệch theo từng mốc cập nhật.
* **Thị trường chuyển nhượng (TTCN):** Giá BP cầu thủ tại Garena Việt Nam thường chịu ảnh hưởng nặng nề bởi các sự kiện nạp thẻ cục bộ, tỷ lệ lạm phát BP khác biệt lớn so với máy chủ Hàn Quốc.
* **Phong cách chiến thuật (Playstyle):** Ranker Hàn Quốc ưu tiên kiểm soát bóng và sút xa chuẩn xác, trong khi meta GLXH tại Việt Nam thường chuộng các sơ đồ thể hình lực điền, tì đè và chọc khe bổng W/ZW.

---

## 7. 🚀 HƯỚNG DẪN KÍCH HOẠT DỮ LIỆU THẬT DÀNH CHO NGƯỜI DÙNG

Để hệ thống tự động tải toàn bộ dữ liệu ranker thật và tạo các file `real_glxh_*.csv`, người dùng cần:
1. Lưu biến môi trường vĩnh viễn trên Windows bằng lệnh PowerShell:
   ```powershell
   [Environment]::SetEnvironmentVariable("NEXON_OPEN_API_KEY", "nhap_key_that_vao_day", "User")
   ```
2. Hoặc tạo file `.env` tại thư mục gốc:
   `E:\\FCOnlineWorkspace\\Research\\.env`
   với nội dung:
   ```env
   NEXON_OPEN_API_KEY=nhap_key_that_vao_day
   ```
3. Sau đó chạy lệnh trích xuất:
   ```powershell
   python tools\\glxh_research.py
   python tools\\glxh_meta_analyzer.py
   ```
"""

target = r"E:\FCOnlineWorkspace\Research\GLXH_REAL_DATA_REPORT.md"
with open(target, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print("Created GLXH_REAL_DATA_REPORT.md successfully.")
