# 📖 TỪ ĐIỂN DỮ LIỆU (DATA DICTIONARY) — FC ONLINE RESEARCH (v3.4)

Tài liệu định nghĩa chuẩn toàn bộ trường dữ liệu phục vụ nghiên cứu và tối ưu hóa Giả Lập Xếp Hạng (Manager Mode / GLXH — `matchtype = 52`).

---

## 1. 🌏 QUY TẮC PHÂN TÁCH DỮ LIỆU & NGUYÊN TẮC TOÀN VẸN

### 1.1. Phân tách rành mạch 2 tầng dữ liệu cầu thủ
1. **`OWNED_PLAYER_DATA` (Source of Truth):**
   - Nguồn: [data/vn_owned_players.json](file:///E:/FCOnlineWorkspace/Research/data/vn_owned_players.json) được trích xuất trực tiếp từ screenshot game của người dùng và card metadata chuẩn.
   - Các trường bất biến:
     * `player_name`: Tên cầu thủ
     * `season`: Mùa thẻ thực tế
     * `grade`: Mức thẻ cộng (+1 đến +3)
     * `displayed_ovr`: Chỉ số OVR nhìn thấy trên screenshot game của người dùng (không bị ghi đè)
     * `database_base_ovr`: Chỉ số OVR thẻ gốc (+1) được trích xuất từ database sau khi định danh qua [tools/player_identity_resolver.py](file:///E:/FCOnlineWorkspace/Research/tools/player_identity_resolver.py)
     * `salary`: Mức lương thực tế của thẻ
     * `current_slot`: Vị trí thẻ đang được đặt trong screenshot (KHÔNG được gọi là "vị trí gốc")
     * `natural_positions`: Danh sách vị trí tự nhiên được resolve từ database / card metadata
   - Cơ chế bảo vệ: Bất kỳ sự sai lệch nào so với nguồn này sẽ kích hoạt lỗi `OWNED_PLAYER_SEASON_MISMATCH` hoặc `OWNED_INVENTORY_VALIDATION_FAILED` thông qua [tools/validate_owned_inventory.py](file:///E:/FCOnlineWorkspace/Research/tools/validate_owned_inventory.py).
   - Tuyệt đối không so sánh candidate base OVR với owned displayed OVR như cùng một loại dữ liệu.
2. **`DATABASE_CANDIDATE_DATA` (Dữ liệu mô hình tính toán):**
   - Nguồn: Tra cứu từ cơ sở dữ liệu 41,289 cầu thủ (`details.csv`).
   - Các trường giả định bắt buộc dùng tiền tố: `HYPOTHETICAL_GRADE`, `HYPOTHETICAL_OVR`, `HYPOTHETICAL_stamina`, v.v.
   - Tên file xuất bản: [exports/vn_glxh_model_candidates.csv](file:///E:/FCOnlineWorkspace/Research/exports/vn_glxh_model_candidates.csv).

### 1.2. Thông số trần lương
* **Trần lương hiện tại của tài khoản:** `VN_CURRENT_SALARY_CAP = 305` (Không dùng 260, 265, 270 cho đội hiện tại).

### 1.3. Chuẩn mực Dữ liệu Thị Trường Chuyển Nhượng Việt Nam (`VN_MARKET_*`)
1. **Nguồn dữ liệu thị trường:**
   * `IN_GAME_SCREENSHOT`: Ảnh chụp màn hình TTCN trong game (ưu tiên cao nhất, đọc qua Windows Native OCR).
   * `FC_ONLINE_M_SCREENSHOT`: Ảnh chụp ứng dụng FC Online M.
   * `USER_MANUAL_INPUT`: Nhập liệu bán tự động/sidecar từ người dùng.
   * `PUBLIC_REFERENCE_PRICE`: Tham chiếu từ fcoplayers.com / FIFAAddict.
   * `KR_PRICE_REFERENCE`: Tham chiếu Nexon Hàn Quốc (**tuyệt đối không dùng làm giá TTCN VN**).
2. **Quy tắc bảo mật & an toàn:**
   * Tuyệt đối không auto-buy, không auto-sell, không click trong game.
   * Không đọc memory/process game, không packet sniffing, không hook API.
   * Chỉ đọc dữ liệu hình ảnh người dùng chủ động nạp vào `data/vn_market_screenshots/incoming/`.
3. **Quy tắc khả dụng & độ tin cậy:**
   * `price_confidence`:
     - `HIGH`: Thấy rõ ràng `player_name`, `season`, `grade`, `price`. Đạt chuẩn tối ưu GLXH.
     - `MEDIUM`: Nhận diện chắc chắn danh tính nhưng thiếu trường phụ. Được phép tham chiếu.
     - `LOW`: Không chắc chắn season hoặc grade. **Tuyệt đối không dùng để ra quyết định mua.**
   * `market_availability`:
     - `AVAILABLE`: Chỉ khi screenshot thật sự thấy số lượng bán `sell_quantity > 0`.
     - `BUY_ORDERS_ONLY`: Sổ lệnh chỉ toàn người đặt mua (`buy_quantity > 0`), không có ai bán.
     - `NO_SELL_LISTING`: Không có thẻ nào được niêm yết bán (`sell_quantity = 0`).
     - `UNKNOWN`: Chỉ có giá tham chiếu, thiếu sổ lệnh giao dịch.
   * **Quy tắc thời hạn (24h Age Rule):** Không dùng snapshot quá 24h (1440 phút) cho quyết định mua ngay. Cột `snapshot_age_minutes` bắt buộc được tính toán.

---

## 2. 📋 SCHEMA THỊ TRƯỜNG CHUYỂN NHƯỢNG VIỆT NAM

### 2.1. Lịch sử TTCN (`data/vn_market_history.csv`)
| Trường | Kiểu | Ý nghĩa |
| :--- | :--- | :--- |
| `timestamp` | String | Thời điểm thu thập dữ liệu (YYYY-MM-DD HH:MM:SS) |
| `spId` | String / Int | Mã định danh cầu thủ nếu xác định được (hoặc `null`) |
| `player_name` | String | Tên cầu thủ |
| `season` | String | Mùa thẻ |
| `grade` | Integer | Cấp thẻ cộng |
| `price_min` | Float / String | Giá sàn TTCN (`null` nếu không có) |
| `price_max` | Float / String | Giá trần TTCN (`null` nếu không có) |
| `buy_price` | Float / String | Giá đặt mua cao nhất (`null` nếu không có) |
| `sell_price` | Float / String | Giá đặt bán thấp nhất (`null` nếu không có) |
| `buy_quantity` | Int / String | Số lượng lệnh mua chờ khớp (`null` nếu không có) |
| `sell_quantity` | Int / String | Số lượng thẻ đang rao bán thực tế (`null` nếu không có) |
| `market_availability` | String | `AVAILABLE` \| `NO_SELL_LISTING` \| `BUY_ORDERS_ONLY` \| `UNKNOWN` |
| `source` | String | Nguồn thu thập (`IN_GAME_SCREENSHOT`, `FCOPLAYERS_PUBLIC_MARKET`, ...) |
| `price_confidence` | String | Độ tin cậy (`HIGH`, `MEDIUM`, `LOW`) |
| `source_image` | String | Tên file ảnh nguồn chụp màn hình (`null` nếu từ API web) |

### 2.2. Bảng Giá TTCN Mới Nhất (`exports/vn_market_latest.csv`)
Lưu trữ snapshot mới nhất của từng thẻ, làm nguồn cấp dữ liệu cho GLXH Optimizer:
`player_name,season,grade,sell_price,buy_price,sell_quantity,buy_quantity,market_availability,snapshot_timestamp,snapshot_age_minutes,price_confidence,source`

### 2.3. Báo Cáo Rà Soát Khả Thi Mua (`exports/vn_market_candidate_scan.csv`)
Bộ lọc ứng viên TTCN với điều kiện `price_confidence in ["HIGH", "MEDIUM"]`, `snapshot_age_minutes <= 1440`, và `market_availability == "AVAILABLE"`.


---

## 3. 📋 SCHEMA ĐỘI HÌNH HIỆN TẠI (`exports/vn_glxh_current_squad_candidates.csv`)

| Trường | Kiểu | Ý nghĩa |
| :--- | :--- | :--- |
| `squad_id` | String | Mã định danh phương án đội hình (`VN_CURRENT_SQUAD_4231`, `VN_CURRENT_SQUAD_4123`) |
| `squad_name` | String | Tên phương án chiến thuật tối ưu |
| `formation` | String | Sơ đồ vận hành (`4-2-3-1`, `4-1-2-3`) |
| `assigned_position` | String | Vị trí được phân công trên sân |
| `current_slot` | String | Slot bố trí thực tế trong game (LW, LCM, RCM, ST, RB, LB, CB, GK, ...) |
| `player_name` | String | Tên cầu thủ (khớp 100% Source of Truth) |
| `season` | String | Mùa thẻ thực tế (WS, WG, 25DP, NO.7, HOT, 19, LH) |
| `grade` | Integer | Cấp thẻ cộng thực tế (+1 đến +3) |
| `displayed_ovr` | Integer | Chỉ số OVR hiển thị trên screenshot |
| `database_base_ovr` | Integer | Chỉ số OVR gốc (+1) từ database |
| `salary` | Integer | Mức lương thực tế của thẻ |
| `natural_positions` | String | Vị trí tự nhiên theo thẻ (CF, ST, CM, CDM, LB, CB, ...) |
| `role_focus` | String | Vai trò và trách nhiệm AI khi vận hành GLXH |
| `is_starter` | Boolean | True nếu đá chính, False nếu dự bị |
| `sample_type` | String | Luôn là `OWNED_PLAYER_DATA` |

---

## 4. 🚫 CÁC THUẬT NGỮ BÃI BỎ HOÀN TOÀN
* Tuyệt đối không dùng: `Auto 24/7`, `anti-ban`, `safe automation` trong tài liệu và mã nguồn mô hình.
* Tuyệt đối không dùng: `real_ranker`, `top10000_live`, `live_nexon` khi chưa có live API xác thực.
