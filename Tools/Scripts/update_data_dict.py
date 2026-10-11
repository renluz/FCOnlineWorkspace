# update_data_dict.py
import os

new_content = """# 📖 TỪ ĐIỂN DỮ LIỆU (DATA DICTIONARY) — FC ONLINE RESEARCH

Tài liệu này định nghĩa chi tiết toàn bộ các trường dữ liệu được thu thập và xử lý trong dự án nghiên cứu FC Online Giả Lập Xếp Hạng (GLXH / Manager Mode — `matchtype = 52`), phân định rõ ràng giữa:
* `RAW_NEXON_*`: Dữ liệu gốc trả về trực tiếp từ NEXON Open API.
* `DATABASE_*`: Dữ liệu chi tiết về chỉ số cầu thủ từ cơ sở dữ liệu `details.csv` (41.289 cầu thủ).
* `CALC_*`: Các chỉ số thống kê mô tả thực nghiệm được tính toán từ dữ liệu thi đấu thật (KHÔNG tự tiện phong danh là "best player score").

---

## 1. 🌐 QUY TẮC PHÂN TÁCH MATCHTYPE & BẢO ĐẢM TÍNH TOÀN VẸN
* **`matchtype = 52`**: Chế độ **Giả Lập Xếp Hạng (Manager Mode / 감독모드)**. Toàn bộ dữ liệu ranker stats và hiệu suất phải sử dụng duy nhất mã này.
* **`matchtype = 50`**: Chế độ Xếp Hạng Đá Tay 1v1 (공식경기) — **BỊ LOẠI BỎ HOÀN TOÀN** khỏi bộ dữ liệu GLXH để tránh sai lệch hành vi AI.
* **Không dùng dữ liệu giả lập (No Synthetic Fallback):** Nếu NEXON Open API không có key hoặc request lỗi, hệ thống chỉ xuất `glxh_offline_candidates.csv` và tuyệt đối KHÔNG tạo `glxh_ranker_stats.csv` giả lập.

---

## 2. 📡 CÁC TRƯỜNG DỮ LIỆU GỐC TỪ NEXON OPEN API (`RAW_NEXON_*`)

Endpoint: `GET https://open.api.nexon.com/fconline/v1/ranker-stats?matchtype=52&players=[...]`

| Tên trường gốc | Nhãn chuẩn hóa | Kiểu | Ý nghĩa | Lưu ý |
| :--- | :--- | :--- | :--- | :--- |
| `spId` / `id` | `RAW_NEXON_spId` | Integer | Mã ID cầu thủ (3 chữ số đầu: Season ID, 6 chữ số sau: PID gốc) | Khóa định danh join với database |
| `spPosition` / `po` | `RAW_NEXON_spPosition` | Integer | Mã số vị trí trên sân theo `spposition.json` | 0: GK, 1-8: DF, 9-19: MF, 20-27: FW |
| `status.shoot` | `RAW_NEXON_shoot` | Float | Số lần dứt điểm trung bình mỗi trận của ranker | |
| `status.effectiveShoot` | `RAW_NEXON_effectiveShoot` | Float | Số lần sút trúng đích trung bình mỗi trận | |
| `status.assist` | `RAW_NEXON_assist` | Float | Số pha kiến tạo thành bàn trung bình mỗi trận | |
| `status.goal` | `RAW_NEXON_goal` | Float | Số bàn thắng ghi được trung bình mỗi trận | |
| `status.dribble` | `RAW_NEXON_dribble` | Float | Quãng đường rê bóng trung bình (yard) | |
| `status.dribbleTry` | `RAW_NEXON_dribbleTry` | Float | Số lần thực hiện nỗ lực rê dắt bóng | |
| `status.dribbleSuccess` | `RAW_NEXON_dribbleSuccess` | Float | Số lần rê dắt bóng qua người thành công | |
| `status.passTry` | `RAW_NEXON_passTry` | Float | Số đường chuyền thực hiện trung bình mỗi trận | |
| `status.passSuccess` | `RAW_NEXON_passSuccess` | Float | Số đường chuyền trúng đích trung bình mỗi trận | |
| `status.block` | `RAW_NEXON_block` | Float | Số lần cản phá cú sút thành công trung bình | |
| `status.tackle` | `RAW_NEXON_tackle` | Float | Số lần tranh cướp bóng thành công trung bình | |
| `status.matchCount` | `RAW_NEXON_matchCount` | Integer | Số trận mà Top 10.000 ranker sử dụng cầu thủ này tại vị trí này | Đo lường độ phổ biến (Usage) |
| `createDate` | `RAW_NEXON_createDate` | String | Thời điểm máy chủ Nexon tổng hợp dữ liệu | ISO 8601 UTC |

> [!WARNING]
> **Các trường KHÔNG CÓ trong API ranker-stats:**
> * Cấp thẻ cộng (`enhancement_level` / `spGrade`) — API ranker-stats không phân tách thẻ cộng.
> * Chỉ số cướp bóng (`interceptions`) — Không xuất hiện trong `status`.
> * Điểm đánh giá trận đấu (`rating` / `spRating`) — Chỉ có trong `match-detail`, không có trong `ranker-stats`.
> * Bối cảnh Thắng/Hòa/Thua (`win/draw/loss`) — Không có trong `ranker-stats`.

---

## 3. 🗄️ CÁC TRƯỜNG TỪ CƠ SỞ DỮ LIỆU CẦU THỦ (`DATABASE_*`)

Nguồn: `repos\fconline-player-search\data\details.csv` (41.289 cầu thủ)

| Tên trường gốc | Nhãn chuẩn hóa | Kiểu | Ý nghĩa trong GLXH |
| :--- | :--- | :--- | :--- |
| `player_name` | `DATABASE_player_name` | String | Tên cầu thủ |
| `season` | `DATABASE_season` | String | Tên mùa thẻ (ví dụ: 23UCL, CC, BWC, RTN) |
| `position` | `DATABASE_position` | String | Vị trí sở trường chính (ST, CAM, CDM, CB,...) |
| `ovr` | `DATABASE_ovr` | Integer | Chỉ số tổng quát cơ sở |
| `salary` | `DATABASE_salary` | Integer | Mức lương (quản lý trần lương 305 FP) |
| `height` | `DATABASE_height` | Integer | Chiều cao (cm) — Yếu tố sống còn cho CB, GK, ST GLXH |
| `weight` | `DATABASE_weight` | Integer | Cân nặng (kg) — Độ đầm khi va chạm auto |
| `left_foot`, `right_foot` | `DATABASE_left_foot`, `right_foot` | Integer | Độ thuận chân (1-5 sao) |
| `finishing` | `DATABASE_finishing` | Integer | Dứt điểm trong vòng cấm |
| `positioning` | `DATABASE_positioning` | Integer | Chọn vị trí đón bóng |
| `shot_power` | `DATABASE_shot_power` | Integer | Lực sút bóng |
| `long_shots` | `DATABASE_long_shots` | Integer | Sút xa ngoài vòng cấm (vũ khí then chốt GLXH) |
| `interceptions` | `DATABASE_interceptions` | Integer | Khả năng phán đoán cắt đường chuyền |
| `marking` | `DATABASE_marking` | Integer | Kèm người tự động |
| `standing_tackle` | `DATABASE_standing_tackle` | Integer | Chọc chân lấy bóng |
| `heading` | `DATABASE_heading` | Integer | Đánh đầu không chiến |
| `strength` | `DATABASE_strength` | Integer | Sức mạnh tì đè khi tranh chấp tay đôi |
| `stamina` | `DATABASE_stamina` | Integer | Thể lực duy trì pressing suốt trận |
| `traits` | `DATABASE_traits` | String | Chỉ số ẩn kích hoạt AI (Finesse Shot, Power Header,...) |
| `team_colors` | `DATABASE_team_colors` | JSON String | Danh sách Team Color CLB / ĐTQG |

---

## 4. 📐 CÁC METRIC THỐNG KÊ MÔ TẢ THỰC NGHIỆM (`CALC_*`)

Được tính toán bởi `tools\glxh_meta_analyzer.py` dựa trên dữ liệu thi đấu thực tế:

### 4.1. `CALC_usage_index` (Chỉ số tần suất sử dụng tương đối)
* **Ý nghĩa:** Đo lường mức độ ưu tiên chọn lựa cầu thủ của các ranker hàng đầu.
* **Công thức:**
  $$\text{CALC\_usage\_index} = \frac{\text{RAW\_NEXON\_matchCount}}{\max(\text{RAW\_NEXON\_matchCount})}$$
* **Quy tắc mẫu số:** Nếu $\max(\text{RAW\_NEXON\_matchCount}) = 0$ hoặc null thì giá trị là `null`.

### 4.2. `CALC_goal_per_appearance` (Bàn thắng trung bình mỗi trận)
* **Ý nghĩa:** Hiệu suất săn bàn thực tế mỗi lần ra sân.
* **Công thức:**
  $$\text{CALC\_goal\_per\_appearance} = \text{RAW\_NEXON\_goal}$$

### 4.3. `CALC_assist_per_appearance` (Kiến tạo trung bình mỗi trận)
* **Ý nghĩa:** Tần suất tạo cơ hội dẫn tới bàn thắng.
* **Công thức:**
  $$\text{CALC\_assist\_per\_appearance} = \text{RAW\_NEXON\_assist}$$

### 4.4. `CALC_shot_efficiency` (Hiệu suất chuyển hóa cú sút thành bàn thắng)
* **Ý nghĩa:** Tỷ lệ số cú sút biến thành bàn thắng của cầu thủ trong tay ranker.
* **Công thức:**
  $$\text{CALC\_shot\_efficiency} = \frac{\text{RAW\_NEXON\_goal}}{\text{RAW\_NEXON\_shoot}}$$
* **Quy tắc mẫu số:** Nếu $\text{RAW\_NEXON\_shoot} \le 0$ hoặc null thì giá trị trả về là `null` (không chia cho 0).

### 4.5. `CALC_defensive_action_index` (Chỉ số can thiệp phòng ngự)
* **Ý nghĩa:** Tổng khối lượng hành động phòng ngự chủ động (tắc bóng + cản phá) mỗi trận.
* **Công thức:**
  $$\text{CALC\_defensive\_action\_index} = \text{RAW\_NEXON\_block} + \text{RAW\_NEXON\_tackle}$$

---

## 5. ⚖️ ĐÁNH GIÁ ĐỐI CHIẾU HEURISTIC VS REAL RANKER
File: `exports\heuristic_vs_real_ranker.csv`
* `heuristic_score`: Điểm số lý thuyết tính từ `tools\glxh_player_analyzer.py` (dựa trên chỉ số in-game).
* `real_ranker_usage`: Tần suất ranker thực tế đưa vào sân thi đấu (`CALC_usage_index`).
* `agreement_flag`:
  - `AGREE_HIGH`: Cả heuristic cao ($\ge 80$) và usage cao ($\ge 0.5$).
  - `AGREE_LOW`: Cả heuristic thấp ($< 75$) và usage thấp ($< 0.3$).
  - `DISAGREE`: Heuristic cao nhưng ranker không dùng, hoặc ngược lại.
* **Hệ số tương quan (Correlations):**
  - Pearson Correlation: Đo lường mối quan hệ tuyến tính giữa điểm lý thuyết và tần suất sử dụng thực tế.
  - Spearman Correlation: Đo lường mối tương quan thứ hạng giữa điểm lý thuyết và thực tế.
"""

target = r"E:\FCOnlineWorkspace\Research\DATA_DICTIONARY.md"
with open(target, "w", encoding="utf-8") as f:
    f.write(new_content.strip() + "\n")

print("Updated DATA_DICTIONARY.md successfully.")
