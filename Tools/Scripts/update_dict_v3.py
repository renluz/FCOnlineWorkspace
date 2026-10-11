# update_dict_v3.py
content = """# 📖 TỪ ĐIỂN DỮ LIỆU (DATA DICTIONARY) — FC ONLINE RESEARCH

Tài liệu định nghĩa chuẩn toàn bộ trường dữ liệu và cấu trúc 2 giai đoạn (Discovery & Validation) phục vụ tối ưu hóa Giả Lập Xếp Hạng (Manager Mode / GLXH — `matchtype = 52`).

---

## 1. 🌐 BẮT BUỘC MATCHTYPE & NGUYÊN TẮC TOÀN VẸN
* **`matchtype = 52` (감독모드 - Manager Mode / GLXH):** Toàn bộ truy vấn, phân tích đội hình, sơ đồ và cầu thủ phải sử dụng duy nhất mã `52`.
* **`matchtype = 50` (공식경기 - 1v1 Ranked):** Bị loại trừ hoàn toàn, không trộn lẫn dữ liệu rank tay vào GLXH.
* **Chiến lược lấy mẫu:** `RECENT_STRATIFIED_OFFSETS` với 3 tầng offsets `[0, 500, 1000]` để giảm thiểu temporal clustering bias.
* **Phân định rõ ràng các tập mẫu (Sample Types):**
  - **`RECENT_GLXH_SAMPLE`**: Mẫu các trận Manager Mode gần đây thu thập từ endpoint `/v1/match`. Tuyệt đối không gọi tập này là "top rank meta" hay "top 10.000 sample".
  - **`RECENT_GLXH_ELITE_SAMPLE`**: Mẫu con của các HLV thuộc tầng ELITE (divisionId in [800, 900, 1000]).
  - **`RECENT_GLXH_UPPER_LADDER_SAMPLE`**: Mẫu con của các HLV thuộc tầng UPPER LADDER (divisionId in [800-1300]).
  - **`NEXON_TOP_10000_RANKER_STATS`**: Dữ liệu thống kê Top 10.000 ranker từ endpoint `/v1/ranker-stats`.
* **Quy tắc tiền tố cột (Prefixes):**
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
| `RAW_MATCH_result_raw` | String | Kết quả gốc từ Nexon (`승`, `무`, `패`) |
| `CALC_match_result` | String | Kết quả chuẩn hóa (`WIN`, `DRAW`, `LOSS`, `UNKNOWN`) |
| `RAW_MATCH_division_id` | Integer | ID phân hạng rank của HLV (nếu live API cung cấp) |
| `RAW_MATCH_division_name` | String | Tên phân hạng tiếng Hàn giải mã qua `data/division.json` (ví dụ: 챌린저1, 챔피언스...) |
| `RAW_MATCH_is_complete_match` | Boolean | True nếu trận đấu kết thúc bình thường (`matchEndType == 0`) và đủ 2 bên (`participant_count == 2`) |
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

## 3. 🎯 PHÂN TẦNG RANK (DIVISION TIERS)

Division là thuộc tính của từng **Participant-Team** (`matchId + ouid`), không áp đặt cho cả trận đấu:
1. **`ELITE`**: HLV có `RAW_MATCH_division_id in [800, 900, 1000]`
   - `800`: 슈퍼 챔피언스 (Super Champions)
   - `900`: 챔피언스 (Champions)
   - `1000`: 슈퍼 챌린지 (Super Challenge)
2. **`UPPER_LADDER`**: HLV có `RAW_MATCH_division_id in [800, 900, 1000, 1100, 1200, 1300]`
   - Bao gồm cả nhóm ELITE và Challenger 1-3 (`1100, 1200, 1300`).
   - *Lưu ý: Tuyệt đối không gọi Challenger 1-3 là "Elite".*
3. **`ALL_RANKS`**: Toàn bộ các HLV có mặt trong tập mẫu hợp lệ.

---

## 4. 🧪 GIAI ĐOẠN 2 — VALIDATION SCHEMA (`RAW_RANKER_*`)

Dữ liệu query từ `/fconline/v1/ranker-stats` cho các ứng viên:

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

## 5. 📐 CÁC METRIC MÔ TẢ THỰC NGHIỆM (`CALC_*`)

### 5.1. `CALC_relative_ranker_matchcount`
* **Định nghĩa:**
  $$\text{CALC\_relative\_ranker\_matchcount} = \frac{\text{RAW\_RANKER\_matchCount}}{\max(\text{RAW\_RANKER\_matchCount})}$$
* **Lưu ý bắt buộc:** **"Relative only within queried candidate universe."**
* Không xem đây là độ phổ biến toàn meta nếu tập candidate chưa bao phủ 100% cầu thủ.

### 5.2. `CALC_most_used_spGrade`
* Mức thẻ cộng (+1, +5, +8, +10) được các HLV trong mẫu trận thực tế sử dụng nhiều nhất cho cầu thủ đó.

### 5.3. `EXPERIMENTAL_CANDIDATE_SCORE`
* **Định vị vai trò:** **Descriptive exploratory metric** (chỉ dùng để mô tả khám phá, tuyệt đối không dùng để tuyên bố "best player", "meta player", và không dùng để loại ứng viên khỏi ranker query nếu budget còn đủ).

### 5.4. Độ Bất Định Cho Tỷ Lệ Thắng (Wilson 95% Confidence Interval)
* Bổ sung khoảng tin cậy 95% Wilson:
  - `win_rate`: Tỷ lệ thắng danh nghĩa ($\text{wins} / \text{appearances}$).
  - `win_rate_ci_low`: Cận dưới khoảng tin cậy 95%.
  - `win_rate_ci_high`: Cận trên khoảng tin cậy 95%.
* Giúp ChatGPT nhận biết mẫu nhỏ (CI rất rộng) để tránh kết luận vội vã.

---

## 6. 🗺️ PHÂN TÍCH SƠ ĐỒ CHIẾN THUẬT (FORMATION ANALYSIS)
* **Đơn vị quan sát (Observation Unit):** `participant-team` (chống bias do 1 trận có 2 HLV dùng 2 sơ đồ khác nhau).
* **Trường chính:** `formation_signature` (dãy vị trí 11 cầu thủ đá chính sắp xếp chuẩn hóa).
* **Mức độ tin cậy mapping (`formation_mapping_confidence`):**
  - `1.0` (EXACT): Khớp 100% rule định sẵn (`4-2-3-1`, `4-2-2-1-1`, `4-1-2-3`, `4-1-2-1-2`, `5-2-3`...).
  - `0.5` (AMBIGUOUS): Cấu trúc vị trí có thể diễn giải thành nhiều sơ đồ.
  - `0.0` (UNKNOWN): Toàn bộ các sơ đồ dị hoặc không thể xác định.
* Các bảng thống kê chính phải aggregate theo `formation_signature`, bảng phụ mới aggregate theo `formation_name`.
"""

with open(r"E:\FCOnlineWorkspace\Research\DATA_DICTIONARY.md", "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print("Updated DATA_DICTIONARY.md to v3.")
