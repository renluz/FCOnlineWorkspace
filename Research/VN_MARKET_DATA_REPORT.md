# 📊 BÁO CÁO KHẢO SÁT & KIỂM TOÁN DỮ LIỆU TTCN VIỆT NAM (VN_MARKET_DATA_REPORT.md)
*Thời điểm kiểm toán:* 2026-09-19 00:26:50 (UTC+7)  
*Phạm vi mục tiêu:* Kiểm toán endpoint công khai của `https://fcoplayers.com` & Thị trường chuyển nhượng FC Online Việt Nam  
*Chính sách tuân thủ:* **100% Public HTTP Only** — Tuyệt đối không Garena Login, không đọc bộ nhớ game process, không packet sniff, không cookie stealing, không bypass authentication.

---

## 1. 🌐 DANH SÁCH HTTP ENDPOINTS ĐÃ KHẢO SÁT THỰC TẾ

| Endpoint URL | Phương thức | HTTP Status | Yêu cầu Auth | Trạng Thái Truy Cập | Mục Đích Dữ Liệu |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `https://fcoplayers.com` | `GET` | **200 OK** | Không | Public HTML | Trang chủ, nạp tài nguyên & cấu trúc script |
| `https://fcoplayers.com/api/ajax/search-person` | `POST` | **200 OK** | Không | Public AJAX API | Tìm kiếm cầu thủ theo từ khóa `q` và `page` |
| `https://fcoplayers.com/players/<player-slug>` | `GET` | **200 OK** | Không | Public HTML Profile | Hồ sơ chi tiết, OVR, lương, vị trí, chỉ số ẩn, traits |
| `https://fcoplayers.com/api/market` | `GET` | **404 Not Found** | — | Endpoint không tồn tại | Thử nghiệm endpoint TTCN giả thuyết |
| `https://fcoplayers.com/api/prices` | `GET` | **404 Not Found** | — | Endpoint không tồn tại | Thử nghiệm endpoint bảng giá giả thuyết |
| `https://fcoplayers.com/api/transfers` | `GET` | **404 Not Found** | — | Endpoint không tồn tại | Thử nghiệm endpoint lịch sử giao dịch giả thuyết |

> [!IMPORTANT]
> **KẾT LUẬN TRUY CẬP:**  
> `fcoplayers.com` là một website cung cấp **cơ sở dữ liệu chỉ số cầu thủ, squad builder và review AI**, hoàn toàn **KHÔNG CUNG CẤP SỔ LỆNH GIAO DỊCH THỰC TẾ (ORDER BOOK)** của TTCN FC Online Garena Việt Nam.  
> Trạng thái kỹ thuật ghi nhận: **`PUBLIC_MARKET_API_UNAVAILABLE`**.

---

## 2. 📋 BẢNG KIỂM TOÁN 10 TRƯỜNG DỮ LIỆU BẮT BUỘC

| Trường Dữ Liệu | Tình Trạng Thực Tế | Giá Trị Ghi Nhận | Rationale / Bản Chất Kỹ Thuật |
| :--- | :---: | :---: | :--- |
| `player` | **CÓ THẬT** | Chuỗi tên cầu thủ | Tên hiển thị đầy đủ trên tiêu đề và thẻ (ví dụ: Victor Boniface, Gianluca Zambrotta). |
| `season` | **CÓ THẬT** | Chuỗi mã mùa | Huy hiệu mùa giải chính thức (WS, WG, 25DP, NO7, HOT, 19, LH). |
| `grade` | **KHÔNG CÓ (null)** | `null` | Website chỉ có thanh trượt tương tác xem biến động chỉ số ảo (+1 đến +10), **không có dữ liệu giá giao dịch theo từng cấp thẻ**. |
| `price_min` | **KHÔNG CÓ (null)** | `null` | Không có trường giá sàn TTCN in-game. |
| `price_max` | **KHÔNG CÓ (null)** | `null` | Không có trường giá trần TTCN in-game. |
| `buy_price` | **KHÔNG CÓ (null)** | `null` | Không có sổ lệnh đặt mua (Buy Orders). |
| `sell_price` | **KHÔNG CÓ (null)** | `null` | Không có sổ lệnh đặt bán (Sell Orders). |
| `buy_quantity` | **KHÔNG CÓ (null)** | `null` | Không có số lượng lệnh chờ mua thực tế. |
| `sell_quantity` | **KHÔNG CÓ (null)** | `null` | **Không có số lượng thẻ đang niêm yết bán thực tế.** |
| `updated_at` | **KHÔNG CÓ (null)** | `null` | Không có timestamp cập nhật biến động giá TTCN. |

---

## 3. 🎯 KẾT QUẢ TEST THỰC TẾ TRÊN 6 CẦU THỦ MỤC TIÊU & RAW SAMPLES

Toàn bộ raw sample responses được tải trực tiếp từ server `fcoplayers.com`, lưu trữ nguyên vẹn 100% không qua chỉnh sửa tại thư mục:  
`E:\FCOnlineWorkspace\Research\data\vn_market_raw_samples\`

| Cầu Thủ Thử Nghiệm | Mùa Thẻ | Cấp Thẻ | HTTP Status | File Raw Sample Đã Lưu | Dung Lượng | sell_quantity | market_availability |
| :--- | :---: | :---: | :---: | :--- | :---: | :---: | :---: |
| **V. Boniface** | `WS` | `+3` | **200 OK** | [player_boniface_ws_raw.html](file:///E:/FCOnlineWorkspace/Research/data/vn_market_raw_samples/player_boniface_ws_raw.html) | 94,140 bytes | `null` | **`UNKNOWN`** |
| **G. Zambrotta** | `WG` | `+1` | **200 OK** | [player_zambrotta_wg_raw.html](file:///E:/FCOnlineWorkspace/Research/data/vn_market_raw_samples/player_zambrotta_wg_raw.html) | 100,637 bytes | `null` | **`UNKNOWN`** |
| **J. Gvardiol** | `25DP` | `+1` | **200 OK** | [player_gvardiol_25dp_raw.html](file:///E:/FCOnlineWorkspace/Research/data/vn_market_raw_samples/player_gvardiol_25dp_raw.html) | 104,500 bytes | `null` | **`UNKNOWN`** |
| **T. Rosicky** | `WG` | `+1` | **200 OK** | [player_rosicky_wg_raw.html](file:///E:/FCOnlineWorkspace/Research/data/vn_market_raw_samples/player_rosicky_wg_raw.html) | 94,450 bytes | `null` | **`UNKNOWN`** |
| **Park Ji Sung** | `NO.7` | `+1` | **200 OK** | [player_park_ji_sung_no7_raw.html](file:///E:/FCOnlineWorkspace/Research/data/vn_market_raw_samples/player_park_ji_sung_no7_raw.html) | 100,098 bytes | `null` | **`UNKNOWN`** |
| **F. Schar** | `25DP` | `+1` | **200 OK** | [player_schar_25dp_raw.html](file:///E:/FCOnlineWorkspace/Research/data/vn_market_raw_samples/player_schar_25dp_raw.html) | 103,078 bytes | `null` | **`UNKNOWN`** |

---

## 4. 🔍 ĐÁNH GIÁ TÍNH KHẢ DỤNG THỊ TRƯỜNG (MARKET AVAILABILITY ASSESSMENT)

Tuân thủ nghiêm ngặt chỉ thị cốt lõi của người dùng:
1. **Quy ước trạng thái tính khả dụng:** Chỉ cho phép 4 giá trị:
   - `AVAILABLE`
   - `NO_SELL_LISTING`
   - `BUY_ORDERS_ONLY`
   - `UNKNOWN`
2. **Nguyên tắc bất biến:**
   - **Chỉ đặt `AVAILABLE` khi endpoint thực sự chứng minh có sell listing đang bày bán.**
   - Giá tồn tại hoặc bài viết review không đồng nghĩa đang có hàng bán trên TTCN.
   - Do `fcoplayers.com` không có dữ liệu sổ lệnh và số lượng bán thực tế: **Bắt buộc 100% bản ghi được gắn nhãn `sell_quantity = null` và `market_availability = UNKNOWN`.**
   - Nghiêm cấm mọi hành vi suy diễn hoặc giả lập số lượng bán.

---

## 5. 🛠️ DANH MỤC CÔNG CỤ & TỆP DỮ LIỆU ĐÃ THIẾT LẬP

1. **[tools/inspect_fcoplayers_market.py](file:///E:/FCOnlineWorkspace/Research/tools/inspect_fcoplayers_market.py):**  
   Bộ công cụ tự động thăm dò các endpoint HTTP của fcoplayers.com, kiểm tra 10 trường dữ liệu chuẩn, tải và lưu trữ nguyên vẹn các file raw response.
2. **[tools/vn_market_collector.py](file:///E:/FCOnlineWorkspace/Research/tools/vn_market_collector.py):**  
   Pipeline thu thập dữ liệu TTCN Việt Nam, đồng bộ thông tin danh tính từ `tools/player_identity_resolver.py`, ghi lịch sử vào `data/vn_market_history.csv` và xuất báo cáo `exports/vn_market_owned_players.csv`.
3. **[tools/vn_market_candidate_scanner.py](file:///E:/FCOnlineWorkspace/Research/tools/vn_market_candidate_scanner.py):**  
   Bộ quét tính khả thi thị trường cho các cầu thủ chuyển nhượng, tự động áp cờ `PUBLIC_MARKET_API_UNAVAILABLE` và cảnh báo khi thiếu dữ liệu sổ lệnh bán thực tế.
4. **[data/vn_market_history.csv](file:///E:/FCOnlineWorkspace/Research/data/vn_market_history.csv):**  
   Bảng lưu trữ lịch sử TTCN theo chuẩn schema:  
   `timestamp,spId,player_name,season,grade,price_min,price_max,buy_price,sell_price,buy_quantity,sell_quantity,market_availability,source`
5. **[exports/vn_market_owned_players.csv](file:///E:/FCOnlineWorkspace/Research/exports/vn_market_owned_players.csv):**  
   Dữ liệu TTCN được đồng bộ cho toàn bộ 13 cầu thủ người dùng thực tế đang sở hữu.
