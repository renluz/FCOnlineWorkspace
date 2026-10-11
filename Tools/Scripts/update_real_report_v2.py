# update_real_report_v2.py
import datetime

now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S (UTC+7)")

report = f"""# BÁO CÁO TOÀN DIỆN THỰC THI PIPELINE DỮ LIỆU GLXH FC ONLINE (NEXON OPEN API)
**Tài liệu chuẩn bị trước khi kích hoạt key thật — Dành cho ChatGPT & HLV Phân tích**
*Thời điểm cập nhật:* {now_str}
*Thư mục làm việc:* `E:\\FCOnlineWorkspace\\Research`

---

## 1. 🔐 TRẠNG THÁI XÁC THỰC API & AN TOÀN BUDGET

* **Kết quả:** `API_AUTH=FAIL` (Hiện tại chưa nạp key thật vào env hoặc `.env`).
* **Endpoint kiểm thử chuẩn:**
  `GET https://open.api.nexon.com/fconline/v1/match?matchtype=52&offset=0&limit=1&orderby=desc`
* **Cơ chế quản trị Request Budget:**
  - Giới hạn tốc độ: **Tối đa 4 requests / giây** (khoảng nghỉ tối thiểu 260ms giữa mỗi request).
  - Giới hạn ngân sách an toàn: **900 requests / ngày** (giữ buffer an toàn 100 requests dưới mức trần 1.000 req/ngày của Development Key).
  - Tự động lưu tiến độ vào `data/api_budget_state.json`.

---

## 2. 🎯 QUY CHUẨN DỮ LIỆU & LẤY MẪU (SAMPLING METHODOLOGY)

1. **Bắt buộc Match Type:** **`matchtype = 52`** (Manager Mode / 감독모드). Bị loại trừ 100% `matchtype = 50`.
2. **Chiến lược Stratified Sampling 300 trận:**
   - Thu thập 3 tầng để giảm temporal bias (tránh lấy 300 trận liên tiếp dồn cục vào 1 khung giờ):
     * Strata A: `offset=0`, `limit=100`
     * Strata B: `offset=500`, `limit=100`
     * Strata C: `offset=1000`, `limit=100`
   - Merge và deduplicate `matchId` để đạt đúng 300 unique matches.
3. **Xử lý trận Incomplete & Abnormal:**
   - Tách riêng các trận bỏ cuộc/disconnect (`matchEndType != 0`) vào `exports/glxh_abnormal_matches.csv`.
   - Tách các trận thiếu bên (`participant_count != 2`) vào `exports/glxh_incomplete_matches.csv`.
   - Phân tích sơ đồ và win rate CHỈ DÙNG các trận bình thường trọn vẹn 2 bên (`matchEndType == 0` và `participant_count == 2`).
4. **Chuẩn hóa Kết quả:** `승 -> WIN`, `무 -> DRAW`, `패 -> LOSS`, giá trị khác `UNKNOWN`.
5. **Khoảng tin cậy Wilson 95%:** Toàn bộ win rate của cầu thủ và sơ đồ đều được tính kèm `win_rate_ci_low` và `win_rate_ci_high` để phản ánh trung thực mức độ bất định khi mẫu nhỏ.

---

## 3. 🏛️ PHÂN TẦNG RANK (3 TIERS DIVISION)

Division gắn liền với từng **Participant-Team** (`matchId + ouid`), dựa trên metadata `data/division.json`:
* **`ELITE`**: HLV có `divisionId in [800, 900, 1000]` (Super Champions, Champions, Super Challenge).
* **`UPPER_LADDER`**: HLV có `divisionId in [800, 900, 1000, 1100, 1200, 1300]` (Bao gồm Elite và Challenger 1-3).
* **`ALL_RANKS`**: Toàn bộ các HLV trong mẫu.

---

## 4. 🔬 ĐỐI SOÁT TOP 10.000 RANKER META (VALIDATION)

1. **Loại bỏ Selection Bias:**
   - Ứng viên gửi sang `/ranker-stats` là **toàn bộ các cặp (spId, spPosition) có `sample_appearances >= 3`**.
   - Tuyệt đối không dùng `EXPERIMENTAL_CANDIDATE_SCORE` hay `win_rate` để cắt trước ứng viên nếu ngân sách còn đủ.
2. **Tính toán ngân sách trước khi gọi (Pre-Request Budgeting):**
   - `estimated_ranker_requests = ceil(candidate_pairs / 50)`.
   - Nếu đủ ngân sách: Query toàn bộ 100%.
   - Nếu thiếu ngân sách: Ưu tiên theo `sample_appearances` giảm dần và đánh dấu cờ `candidate_truncated_due_to_request_budget = true`.

---

## 5. 🛑 QUY TRÌNH DỪNG KIỂM TOÁN (STOP POINT RULE)

* Sau khi hoàn tất 300 trận đầu tiên: **Hệ thống DỪNG LẠI NGAY LẬP TỨC**.
* Tuyệt đối không tự động mở rộng lên 500, 1000 hay 5000 trận.
* Tự động xuất [GLXH_300_MATCH_AUDIT.md](file:///E:/FCOnlineWorkspace/Research/GLXH_300_MATCH_AUDIT.md) để người dùng gửi ChatGPT rà soát chất lượng dữ liệu.
"""

with open(r"E:\FCOnlineWorkspace\Research\GLXH_REAL_DATA_REPORT.md", "w", encoding="utf-8") as f:
    f.write(report.strip() + "\n")

print("Updated GLXH_REAL_DATA_REPORT.md")
