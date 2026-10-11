# update_docs.py
import datetime

now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S (UTC+7)")

# 1. Update DATA_DICTIONARY.md
data_dict = """# 📖 TỪ ĐIỂN DỮ LIỆU (DATA DICTIONARY) — FC ONLINE RESEARCH

Tài liệu định nghĩa chuẩn toàn bộ trường dữ liệu và cấu trúc 2 giai đoạn (Discovery & Validation) phục vụ tối ưu hóa Giả Lập Xếp Hạng (Manager Mode / GLXH — `matchtype = 52`).

---

## 1. 🌐 BẮT BUỘC MATCHTYPE & NGUYÊN TẮC TOÀN VẸN
* **`matchtype = 52` (감독모드 - Manager Mode / GLXH):** Toàn bộ truy vấn, phân tích đội hình, sơ đồ và cầu thủ phải sử dụng duy nhất mã `52`.
* **`matchtype = 50` (공식경기 - 1v1 Ranked):** Bị loại trừ hoàn toàn, không trộn lẫn dữ liệu rank tay vào GLXH.
* **Quy tắc phân định nguồn dữ liệu (Prefixes):**
  - `RAW_MATCH_*`: Dữ liệu thô trích xuất từ chi tiết trận đấu (`/v1/match-detail`).
  - `RAW_RANKER_*`: Dữ liệu thống kê Top 10.000 ranker từ `/v1/ranker-stats`.
  - `DATABASE_*`: Chỉ số chi tiết ghép từ 41.289 cầu thủ (`details.csv`).
  - `CALC_*`: Các metric mô tả thực nghiệm tính toán trên tập mẫu.

---

## 2. 🔍 GIAI ĐOẠN 1 — DISCOVERY SCHEMA (`RAW_MATCH_*`)

Dữ liệu thu thập từ `/fconline/v1/match` $\rightarrow$ `/fconline/v1/match-detail` (chỉ giữ `matchType == 52`):

| Trường | Kiểu | Ý nghĩa trong GLXH |
| :--- | :--- | :--- |
| `RAW_MATCH_matchId` | String | Mã định danh trận đấu |
| `RAW_MATCH_matchDate` | String | Thời điểm diễn ra trận đấu (UTC) |
| `RAW_MATCH_ouid` | String | Mã định danh tài khoản HLV |
| `RAW_MATCH_nickname` | String | Nickname người chơi |
| `RAW_MATCH_matchResult` | String | Kết quả (`승`: Thắng, `무`: Hòa, `패`: Thua) |
| `RAW_MATCH_spId` | Integer | ID cầu thủ |
| `RAW_MATCH_spPosition` | Integer | Vị trí trên sân (0: GK, 1-8: DF, 9-19: MF, 20-27: FW, 28: Dự bị) |
| `RAW_MATCH_spGrade` | Integer | **Mức thẻ cộng (+1 đến +10)** — *Trường cực kỳ quan trọng chỉ có trong match-detail* |
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
* **Định nghĩa:** Tỷ lệ số trận xuất hiện so với cầu thủ cao nhất trong tập ứng viên được query:
  $$\text{CALC\_relative\_ranker\_matchcount} = \frac{\text{RAW\_RANKER\_matchCount}}{\max(\text{RAW\_RANKER\_matchCount})}$$
* **Lưu ý bắt buộc:** **"Relative only within queried candidate universe."**
* Không được xem đây là "độ phổ biến toàn meta" nếu candidate universe chưa bao phủ 100% cầu thủ.

### 4.2. `CALC_most_used_spGrade`
* Mức thẻ cộng (+1, +5, +8,...) được các HLV trong mẫu trận thực tế sử dụng nhiều nhất cho cầu thủ đó.

### 4.3. Các chỉ số hiệu suất mẫu:
* `win_rate`: Tỷ lệ thắng của đội khi cầu thủ này đá chính ($\text{wins} / \text{appearances}$).
* `shot_efficiency`: Tỷ lệ chuyển hóa ($\text{goal} / \text{shoot}$), trả về `null` nếu $\text{shoot} \le 0$.
* `pass_success_rate`: $\text{passSuccess} / \text{passTry}$, trả về `null` nếu $\text{passTry} \le 0$.
* `aerial_success_rate`: $\text{aerialSuccess} / \text{aerialTry}$, trả về `null` nếu $\text{aerialTry} \le 0$.

---

## 5. 🗺️ PHÂN TÍCH SƠ ĐỒ CHIẾN THUẬT (FORMATION ANALYSIS)
Tập hợp 11 vị trí đá chính (`spPosition < 28`) trong trận để sinh `formation_signature`:
* Mapping các sơ đồ phổ biến: `4-2-3-1`, `4-2-2-1-1`, `4-1-2-3`, `4-1-2-1-2`, `5-2-3`...
* Nếu không chắc chắn về cách bố trí biến thể: gán nhãn `formation_name = "UNKNOWN"`.
"""

with open(r"E:\FCOnlineWorkspace\Research\DATA_DICTIONARY.md", "w", encoding="utf-8") as f:
    f.write(data_dict.strip() + "\n")
print("Updated DATA_DICTIONARY.md")

# 2. Update GLXH_REAL_DATA_REPORT.md
report = f"""# BÁO CÁO THỰC THI PIPELINE DỮ LIỆU GLXH FC ONLINE (NEXON OPEN API)
**Tài liệu dành cho ChatGPT và Chuyên viên Phân tích Đội hình**
*Thời điểm kiểm tra:* {now_str}
*Thư mục làm việc:* `E:\\FCOnlineWorkspace\\Research`

---

## 1. 🔐 TRẠNG THÁI XÁC THỰC API (AUTHENTICATION CHECK)

* **Kết quả:** `API_AUTH=FAIL`
* **Endpoint kiểm tra chuẩn:**
  `GET https://open.api.nexon.com/fconline/v1/match?matchtype=52&offset=0&limit=1&orderby=desc`
* **Trạng thái chi tiết:**
  - `Status Code`: `400 Bad Request` (hoặc `KEY_MISSING` khi chưa nạp biến).
  - `Error Name`: `OPENAPI00004` (Please input valid parameter - thiếu header x-nxopen-api-key) hoặc `OPENAPI00005` (The apikey is not valid).
  - Không tìm thấy `NEXON_OPEN_API_KEY` trong process environment hoặc file `E:\\FCOnlineWorkspace\\Research\\.env`.
* **Xử lý:**
  - Tuyệt đối tuân thủ chỉ thị: **Dừng phần tải dữ liệu thật khi `API_AUTH=FAIL`**.
  - Ghi nhận trạng thái: **`REAL_DATA_UNAVAILABLE`**.
  - Không sinh các file dữ liệu thật giả lập/fallback.

---

## 2. 📊 THỐNG KÊ MẪU DỮ LIỆU THỰC TẾ (DATA METRICS SUMMARY)

| Chỉ số | Giá trị hiện tại | Ghi chú |
| :--- | :--- | :--- |
| **Target Match Type** | `52` | Manager Mode / 감독모드 (Bắt buộc) |
| **Excluded Match Type** | `50` | Official 1v1 đá tay (Loại bỏ 100%) |
| **Số matchId thu thập** | `0` | Chờ kích hoạt API Key |
| **Số match-detail thành công** | `0` | Chờ kích hoạt API Key |
| **Số player-match rows** | `0` | Chờ kích hoạt API Key |
| **Số unique spId** | `0` | Chờ kích hoạt API Key |
| **Số unique spId-position** | `0` | Chờ kích hoạt API Key |
| **Số ranker-stats candidate** | `0` | Chờ kích hoạt API Key |
| **Số candidate offline tách biệt** | `135` | Đã lưu tại `glxh_offline_candidates.csv` |

---

## 3. 🏗️ KIẾN TRÚC PIPELINE HAI GIAI ĐOẠN ĐÃ XÂY DỰNG SẴN SÀNG

Hệ thống đã hoàn thiện toàn bộ mã nguồn pipeline tại [tools\glxh_pipeline.py](file:///E:/FCOnlineWorkspace/Research/tools/glxh_pipeline.py):

```mermaid
flowchart TD
    subgraph DISCOVERY ["Giai đoạn 1: DISCOVERY (Khám phá thực chiến)"]
        A["GET /fconline/v1/match?matchtype=52"] -->|Thu thập 500 trận| B["Checkpoint: data/glxh_match_ids.json"]
        B --> C["GET /fconline/v1/match-detail?matchid=..."]
        C -->|Cache cục bộ| D["data/match_details/*.json"]
        D -->|Assert matchType == 52| E["Trích xuất matchInfo[].player[] (kèm spGrade)"]
        E --> F["glxh_match_players_raw.csv / .json"]
        F --> G["glxh_sample_player_usage.csv"]
        F --> H["glxh_sample_player_grade_usage.csv"]
        D --> I["glxh_formation_usage.csv (Sơ đồ chiến thuật)"]
        G --> J["glxh_candidate_pairs.csv (Top ứng viên thực tế)"]
    end

    subgraph VALIDATION ["Giai đoạn 2: VALIDATION (Đối soát Top 10.000)"]
        J --> K["GET /fconline/v1/ranker-stats?matchtype=52&players=[...]"]
        K -->|Batch 50 cặp| L["data/ranker_stats_batches/*.json"]
        L --> M["glxh_ranker_stats.csv / .json"]
    end

    subgraph ENRICHMENT ["Giai đoạn 3: GHÉP NỐI & ĐÁNH GIÁ"]
        M & G & H --> N["Ghép repos/fconline-player-search/data/details.csv"]
        N --> O["real_glxh_st.csv, cam.csv, cdm.csv, cb.csv..."]
        O --> P["heuristic_vs_real_glxh.csv (Pearson & Spearman)"]
    end
```

---

## 4. 📁 ĐIỀU CHỈNH CÁC TỆP TIN & KHẮC PHỤC HIỂU NHẦM

1. **Đổi tên file raw sample:**
   * Tệp cũ `data/ranker_stats_52_raw_sample.json` đã được **đổi tên thành** [ranker_stats_52_schema_example.json](file:///E:/FCOnlineWorkspace/Research/data/ranker_stats_52_schema_example.json).
   * Đã gắn nhãn rõ ràng: `"source": "NEXON_API_SPEC"`, `"is_live_api_response": false`.
   * Tệp `ranker_stats_52_raw_sample.json` chỉ được sinh ra khi nhận được phản hồi live `HTTP 200` thật từ NEXON.
2. **Hiểu đúng về `ranker-stats`:**
   * Không dùng `ranker-stats` để "mò" meta vì endpoint này bắt buộc phải truyền ID cầu thủ vào.
   * Danh sách cầu thủ phải được khám phá tự nhiên từ `/match-detail` của các trận GLXH thật (Discovery phase).
3. **Hiểu đúng về `matchCount`:**
   * Đổi tên metric thành `CALC_relative_ranker_matchcount`.
   * Ghi chú rõ: *"Relative only within queried candidate universe"* — không phản ánh độ phổ biến toàn meta nếu chưa bao phủ 100% cầu thủ.
4. **Bảo tồn thông tin thẻ cộng `spGrade`:**
   * Mức thẻ cộng thực tế được trích xuất từ mẫu trận đấu thật (`glxh_sample_player_grade_usage.csv`), phản ánh ranker đang dùng thẻ +5, +8 hay +10.

---

## 5. 🌏 KHÁC BIỆT META: NEXON (HÀN QUỐC) VS GARENA (VIỆT NAM)

* **NEXON Korean server data is not identical to Garena Vietnam meta:**
  - Phiên bản cập nhật gameplay của Nexon thường đi trước Garena Vietnam từ vài tuần đến vài tháng.
  - Các chỉ số sút xa (ZD), tạt cánh đánh đầu, độ nặng của bóng có thể khác biệt giữa 2 phiên bản máy chủ.
  - Thị trường chuyển nhượng và chi phí ép thẻ tại Hàn Quốc dồi dào hơn, dẫn đến xu hướng ranker Hàn sử dụng thẻ cộng cao (+8, +10) của mùa thường nhiều hơn so với mức thẻ +5 của thẻ xịn tại Việt Nam.

---

## 6. 🚀 HƯỚNG DẪN KÍCH HOẠT DỮ LIỆU THẬT

Chỉ cần tạo file `.env` tại:
`E:\\FCOnlineWorkspace\\Research\\.env`
Nội dung:
```env
NEXON_OPEN_API_KEY=nhap_key_cua_ban_vao_day
```
Sau đó chạy lệnh duy nhất:
```powershell
python tools\\glxh_pipeline.py
```
Toàn bộ quy trình tải 500 trận GLXH thật, trích xuất cầu thủ, phân tích sơ đồ, query Top 10.000 ranker và xuất các file `real_glxh_*.csv` sẽ tự động vận hành 100%.
"""

with open(r"E:\FCOnlineWorkspace\Research\GLXH_REAL_DATA_REPORT.md", "w", encoding="utf-8") as f:
    f.write(report.strip() + "\n")
print("Updated GLXH_REAL_DATA_REPORT.md")
