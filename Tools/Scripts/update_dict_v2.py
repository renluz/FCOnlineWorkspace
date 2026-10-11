# update_dict_v2.py
content = """# 📖 TỪ ĐIỂN DỮ LIỆU (DATA DICTIONARY) — FC ONLINE RESEARCH

Tài liệu định nghĩa chuẩn toàn bộ trường dữ liệu và cấu trúc 2 giai đoạn (Discovery & Validation) phục vụ tối ưu hóa Giả Lập Xếp Hạng (Manager Mode / GLXH — `matchtype = 52`).

---

## 1. 🌐 BẮT BUỘC MATCHTYPE & NGUYÊN TẮC TOÀN VẸN
* **`matchtype = 52` (감독모드 - Manager Mode / GLXH):** Toàn bộ truy vấn, phân tích đội hình, sơ đồ và cầu thủ phải sử dụng duy nhất mã `52`.
* **`matchtype = 50` (공식경기 - 1v1 Ranked):** Bị loại trừ hoàn toàn, không trộn lẫn dữ liệu rank tay vào GLXH.
* **Phân định rõ ràng 2 tập mẫu (Sample Types):**
  - **`RECENT_GLXH_SAMPLE`**: Mẫu các trận Manager Mode gần đây thu thập từ endpoint `/v1/match`. Tuyệt đối không gọi tập này là "top rank meta" hay "top 10.000 sample".
  - **`NEXON_TOP_10000_RANKER_STATS`**: Dữ liệu thống kê Top 10.000 ranker từ endpoint `/v1/ranker-stats`.
* **Quy tắc phân định nguồn dữ liệu (Prefixes):**
  - `RAW_MATCH_*`: Dữ liệu thô trích xuất từ chi tiết trận đấu (`/v1/match-detail`).
  - `RAW_RANKER_*`: Dữ liệu thống kê Top 10.000 ranker từ `/v1/ranker-stats`.
  - `DATABASE_*`: Chỉ số chi tiết ghép từ 41.289 cầu thủ (`details.csv`).
  - `CALC_*`: Các metric mô tả thực nghiệm tính toán trên tập mẫu.

---

## 2. 🔍 GIAI ĐOẠN 1 — DISCOVERY SCHEMA (`RAW_MATCH_*`)

Dữ liệu thu thập từ `/fconline/v1/match` $\rightarrow$ `/fconline/v1/match-detail` (chỉ giữ `matchType == 52` và `matchEndType == 0` cho phân tích meta chính):

| Trường | Kiểu | Ý nghĩa trong GLXH |
| :--- | :--- | :--- |
| `RAW_MATCH_matchId` | String | Mã định danh trận đấu |
| `RAW_MATCH_matchDate` | String | Thời điểm diễn ra trận đấu (UTC) |
| `RAW_MATCH_ouid` | String | Mã định danh tài khoản HLV |
| `RAW_MATCH_nickname` | String | Nickname người chơi |
| `RAW_MATCH_matchResult` | String | Kết quả (`승`: Thắng, `무`: Hòa, `패`: Thua) |
| `RAW_MATCH_division_id` | Integer | ID phân hạng rank của người chơi (nếu live API cung cấp) |
| `RAW_MATCH_division_name` | String | Tên phân hạng tiếng Hàn giải mã qua `data/division.json` (ví dụ: 챌린저1, 챔피언스...) |
| `RAW_MATCH_spId` | Integer | ID cầu thủ |
| `RAW_MATCH_spPosition` | Integer | Vị trí trên sân (0: GK, 1-8: DF, 9-19: MF, 20-27: FW, 28: Dự bị) |
| `RAW_MATCH_spGrade` | Integer | **Mức thẻ cộng (+1 đến +10)** — *Chỉ có trong match-detail, không có trong ranker-stats* |
| `RAW_MATCH_shoot` | Float/Int | Số cú sút của cầu thủ trong trận |
| `RAW_MATCH_effectiveShoot` | Float/Int | Số cú sút trúng đích |
| `RAW_MATCH_assist` | Float/Int | Số kiến tạo thành bàn |
| `RAW_MATCH_goal` | Float/Int | Số bàn thắng |
| `RAW_MATCH_dribble` | Float/Int | Quãng đường rê bóng |
| `RAW_MATCH_intercept` | Float/Int | Số lần cắt bóng thành công |
| `RAW_MATCH_defending` | Float/Int | Điểm tham gia phòng ngự |
| `RAW_MATCH_passTry` / `passSuccess` | Float/Int | Số đường chuyền thử / thành công |
| `RAW_MATCH_dribbleTry` / `dribbleSuccess` | Float/Int | Số lần rê dắt thử / thành công |
| `RAW_MATCH_ballPossesionTry` / `ballPossesionSuc` | Float/Int | Tranh chấp kiểm soát bóng |
| `RAW_MATCH_aerialTry` / `aerialSuccess` | Float/Int | Không chiến thử / thành công |
| `RAW_MATCH_blockTry` / `block` | Float/Int | Cản phá cú sút thử / thành công |
| `RAW_MATCH_tackleTry` / `tackle` | Float/Int | Tắc bóng thử / thành công |
| `RAW_MATCH_yellowCards` / `redCards` | Integer | Thẻ vàng / thẻ đỏ |
| `RAW_MATCH_spRating` | Float | Điểm số đánh giá màn trình diễn trong trận (1.0 - 10.0) |

---

## 3. 🧪 GIAI ĐOẠN 2 — VALIDATION SCHEMA (`RAW_RANKER_*`)

Dữ liệu query từ `/fconline/v1/ranker-stats` cho các ứng viên tìm được:

| Trường | Kiểu | Ý nghĩa | Giới hạn |
| :--- | :--- | :--- | :--- |
| `RAW_RANKER_matchCount` | Integer | Số trận Top 10.000 sử dụng cặp (spId, spPosition) | Trong mẫu ranker Nexon |
| `RAW_RANKER_shoot` | Float | Số lần dứt điểm trung bình | |
| `RAW_RANKER_effectiveShoot` | Float | Số lần dứt điểm trúng đích trung bình | |
| `RAW_RANKER_goal` | Float | Số bàn thắng trung bình | |
| `RAW_RANKER_assist` | Float | Số kiến tạo trung bình | |
| `RAW_RANKER_passTry` / `passSuccess` | Float | Số đường chuyền trung bình | |
| `RAW_RANKER_block` / `tackle` | Float | Cản phá và tắc bóng trung bình | |
| `RAW_RANKER_createDate` | String | Thời gian Nexon chốt số liệu | |

---

## 4. 📐 CÁC METRIC MÔ TẢ THỰC NGHIỆM (`CALC_*`)

### 4.1. `CALC_relative_ranker_matchcount`
* **Định nghĩa:**
  $$\text{CALC\_relative\_ranker\_matchcount} = \frac{\text{RAW\_RANKER\_matchCount}}{\max(\text{RAW\_RANKER\_matchCount})}$$
* **Lưu ý bắt buộc:** **"Relative only within queried candidate universe."**
* Không xem đây là độ phổ biến toàn meta nếu tập candidate chưa bao phủ 100% cầu thủ.

### 4.2. `CALC_most_used_spGrade`
* Mức thẻ cộng (+1, +5, +8, +10) được các HLV trong mẫu trận thực tế sử dụng nhiều nhất cho cầu thủ đó.

### 4.3. `EXPERIMENTAL_CANDIDATE_SCORE`
* **Mục đích:** Sàng lọc ứng viên đối soát với ranker-stats.
* **Nguyên tắc:** Bắt buộc có ngưỡng xuất hiện tối thiểu (`min_sample_appearances = 10`), không dùng `win_rate` đơn thuần để tránh trường hợp 1 trận / 1 thắng vượt mặt 100 trận / 60 thắng.
* **Công thức tổng hợp:** Kết hợp trọng số giữa:
  - Tần suất xuất hiện chuẩn hóa (`sample_appearances`)
  - Điểm đánh giá trung bình (`avg_rating`)
  - Tỷ lệ thắng (`win_rate`)
  - Đóng góp tấn công (`avg_goal + avg_assist`)
  - Can thiệp phòng ngự (`avg_tackle + avg_block + avg_intercept`)

### 4.4. Các chỉ số hiệu suất mẫu:
* `win_rate`: Tỷ lệ thắng của đội khi cầu thủ này đá chính ($\text{wins} / \text{appearances}$).
* `shot_efficiency`: $\text{goal} / \text{shoot}$, trả về `null` nếu $\text{shoot} \le 0$.
* `pass_success_rate`: $\text{passSuccess} / \text{passTry}$, trả về `null` nếu $\text{passTry} \le 0$.
* `aerial_success_rate`: $\text{aerialSuccess} / \text{aerialTry}$, trả về `null` nếu $\text{aerialTry} \le 0$.

---

## 5. 🗺️ PHÂN TÍCH SƠ ĐỒ CHIẾN THUẬT (FORMATION ANALYSIS)
* **Đơn vị quan sát (Observation Unit):** `participant-team` (chống bias do 1 trận có 2 HLV dùng 2 sơ đồ khác nhau).
* **Trường chính:** `formation_signature` (dãy vị trí 11 cầu thủ đá chính được chuẩn hóa theo mã vị trí).
* **Quy tắc gán tên `formation_name`:**
  - Gán tên chuẩn (`4-2-3-1`, `4-2-2-1-1`, `4-1-2-3`, `4-1-2-1-2`, `5-2-3`...) **CHỈ KHI rule match EXACT 100%**.
  - Nếu signature có thể suy diễn thành nhiều sơ đồ: gán `AMBIGUOUS`.
  - Nếu không nhận diện được: gán `UNKNOWN`.
  - Tuyệt đối không tự ép tên 4-2-2-1-1 nếu không thỏa mãn exact rule.
"""

with open(r"E:\FCOnlineWorkspace\Research\DATA_DICTIONARY.md", "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print("Updated DATA_DICTIONARY.md completely.")
