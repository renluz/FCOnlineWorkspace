# 📸 BÁO CÁO KIỂM TOÁN SNAPSHOT TTCN VIỆT NAM (VN_MARKET_SNAPSHOT_REPORT.md)
*Thời điểm kiểm toán:* 2026-09-19 00:59:28 (UTC+7)  
*Pipeline:* `tools/vn_market_screenshot_importer.py` (In-Game Screenshot Processing)  
*Chính sách:* **Không auto-buy, không can thiệp game, chỉ đọc dữ liệu hình ảnh người dùng cung cấp**.

---

## 1. 📊 THỐNG KÊ TỔNG QUAN

| Chỉ Số Kiểm Toán | Đợt Quét Vừa Qua | Tổng Tích Lũy Database | Ghi Chú Kỹ Thuật |
| :--- | :---: | :---: | :--- |
| **Số ảnh xử lý:** | `0` | `0` ảnh mới | Đã xử lý và lưu trữ trong `processed/` |
| **Số cầu thủ nhận diện:** | `0` | `14` thẻ theo dõi | Khớp định danh tên và mùa |
| **Số bản ghi HIGH confidence:** | `0` | `1` thẻ | Đầy đủ tên + mùa + cấp thẻ + giá bán |
| **Số bản ghi AVAILABLE:** | `0` | `0` thẻ | Có lệnh bán niêm yết thực tế (`sell_quantity > 0`) |
| **Số bản ghi UNKNOWN:** | `0` | `12` thẻ | Chỉ có giá tham chiếu hoặc thiếu sổ lệnh bán |
| **Timestamp mới nhất:** | `2026-09-19 00:59:28` | `2026-09-19 00:59:28` | Thời điểm snapshot gần nhất |


---

## 2. 📋 BẢNG TỔNG HỢP GIÁ TTCN GẦN NHẤT (LATEST SNAPSHOTS)

| Cầu Thủ | Mùa | Cấp | Giá Bán (BP) | Lượng Bán | Khả Dụng (Availability) | Độ Tin Cậy | Tuổi Snapshot |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **V. Boniface** | `N/A` | `N/A` | `15,400,000,000 BP` | `-` | `BUY_ORDERS_ONLY` | `LOW` | `3m` |
| **V. Boniface** | `WS` | `+3` | `900,000 BP` | `-` | `BUY_ORDERS_ONLY` | `HIGH` | `3m` |
| **G. Zambrotta** | `WG` | `+1` | *Chưa có giá* | `-` | `UNKNOWN` | `UNKNOWN` | `32m` |
| **J. Gvardiol** | `25DP` | `+1` | *Chưa có giá* | `-` | `UNKNOWN` | `UNKNOWN` | `32m` |
| **T. Rosicky** | `WG` | `+1` | *Chưa có giá* | `-` | `UNKNOWN` | `UNKNOWN` | `32m` |
| **Park Ji Sung** | `NO.7` | `+1` | *Chưa có giá* | `-` | `UNKNOWN` | `UNKNOWN` | `32m` |
| **F. Schar** | `25DP` | `+1` | *Chưa có giá* | `-` | `UNKNOWN` | `UNKNOWN` | `32m` |
| **A. Del Piero** | `HOT` | `+1` | *Chưa có giá* | `-` | `UNKNOWN` | `UNKNOWN` | `32m` |
| **R. Gullit** | `HOT` | `+1` | *Chưa có giá* | `-` | `UNKNOWN` | `UNKNOWN` | `32m` |
| **Rodri** | `19` | `+1` | *Chưa có giá* | `-` | `UNKNOWN` | `UNKNOWN` | `32m` |
| **Sergio Ramos** | `19` | `+1` | *Chưa có giá* | `-` | `UNKNOWN` | `UNKNOWN` | `32m` |
| **W. Hennessey** | `HOT` | `+1` | *Chưa có giá* | `-` | `UNKNOWN` | `UNKNOWN` | `32m` |
| **Inaki Williams** | `HOT` | `+1` | *Chưa có giá* | `-` | `UNKNOWN` | `UNKNOWN` | `32m` |
| **P. Aubameyang** | `LH` | `+1` | *Chưa có giá* | `-` | `UNKNOWN` | `UNKNOWN` | `32m` |

---

## 3. 🛡️ QUY TRÌNH TIẾP NHẬN ẢNH TTCN CỦA NGƯỜI DÙNG

1. **Thư mục nạp ảnh:** Người dùng chỉ cần thả ảnh chụp màn hình TTCN (PNG/JPG) vào:  
   `E:\FCOnlineWorkspace\Research\data\vn_market_screenshots\incoming\`
2. **Kích hoạt công cụ:**
   ```powershell
   python tools\vn_market_screenshot_importer.py
   ```
   *(Hoặc kèm cờ `MANUAL_ASSISTED` nếu dùng file JSON sidecar hỗ trợ)*
3. **Kết quả:**
   - Dữ liệu được trích xuất tự động bằng Windows Native OCR Engine.
   - Tự động append vào `data/vn_market_history.csv` (không ghi đè lịch sử).
   - Ảnh gốc được lưu trữ an toàn trong `data/vn_market_screenshots/processed/`.
   - Bảng giá thị trường mới nhất được cập nhật tại `exports/vn_market_latest.csv`.

---

## 4. 🎯 NGUYÊN TẮC PHÂN CẤP ĐỘ TIN CẬY (CONFIDENCE & AVAILABILITY)

* **HIGH Confidence:** Đầy đủ `player_name`, `season`, `grade`, `price`. Đạt chuẩn đưa vào mô hình tối ưu GLXH.
* **MEDIUM Confidence:** Nhận diện chắc chắn danh tính nhưng thiếu trường phụ (sàn/trần). Được phép tham chiếu.
* **LOW Confidence:** Thiếu season hoặc grade. **Tuyệt đối không dùng để ra quyết định mua.**
* **AVAILABLE:** Chỉ kích hoạt khi screenshot cho thấy số lượng bán `sell_quantity > 0`.
* **BUY_ORDERS_ONLY:** Sổ lệnh chỉ toàn người đặt mua, không có người bán.
* **NO_SELL_LISTING:** Không có thẻ nào được niêm yết bán (0 thẻ bán).
* **UNKNOWN:** Thiếu thông tin sổ lệnh thị trường.
