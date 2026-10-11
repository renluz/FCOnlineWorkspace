# BÁO CÁO KIỂM TOÁN MẪU 300 TRẬN GLXH FC ONLINE (NEXON OPEN API)
*Thời điểm kiểm toán:* 2026-09-19 00:02:40 (UTC+7)
*Thư mục dự án:* `E:\FCOnlineWorkspace\Research`

---

## 1. 🔐 THÔNG SỐ XÁC THỰC & REQUEST BUDGET
* **API Authentication:** `FAIL`
* **HTTP Status / Message:** `UNAVAILABLE_FROM_VIETNAM: NEXON Open API live access is unavailable for the user's Vietnam region as of 2026-09-18. Live KR match/ranker datasets are therefore not available.`
* **Sampling Strategy:** `RECENT_STRATIFIED_OFFSETS`
* **Sampling Offsets:** `[0, 500, 1000]`
* **Tổng số Request đã thực hiện hôm nay:** `0 / 900`
* **Tốc độ giới hạn:** `4.0 req/s` (Rate-limiting enforced)
* **Số lỗi 429 (Rate Limit):** `0` lần
* **Số lỗi HTTP khác:** `0`

---

## 2. 📊 KẾT QUẢ THU THẬP MẪU 300 TRẬN (DISCOVERY SUMMARY)
* **Target Match Type:** `52` (Manager Mode / 감독모드 - Bắt buộc 100%)
* **Số matchId thu thập:** `0 / 300`
* **Số match-detail thành công:** `0`
* **Số match-detail thất bại:** `0`
* **Số trận đủ 2 bên (participant_count == 2):** `0`
* **Số trận thiếu 1 bên (participant_count == 1):** `0`
* **Số trận có participant_count khác:** `0`
* **Số trận kết thúc bình thường đủ 2 bên (Complete Normal Matches):** `0`
* **Số trận bất thường / bỏ cuộc (matchEndType != 0):** `0` *(Lưu tại `glxh_abnormal_matches.csv`)*
* **Số quan sát Participant-Team:** `0`
* **Số lượt cầu thủ ra sân (Player rows):** `0`
* **Số unique spId:** `0`
* **Số unique cặp (spId, spPosition):** `0`

---

## 3. 🎯 PHÂN TẦNG RANK (DIVISION TIERS)
* **Trạng thái trường Division trong live API:** `CHƯA PHÁT HIỆN / NULL`
* **Số lượng Participant theo tầng:**
  - **ALL_RANKS:** `0` participants
  - **UPPER_LADDER (800-1300):** `0` participants
  - **ELITE (800, 900, 1000):** `0` participants
  - **Division UNKNOWN / Null:** `0`

---

## 4. 🗺️ SƠ ĐỒ CHIẾN THUẬT (FORMATION SIGNATURES & CONFIDENCE)
* **Formation EXACT count (Confidence = 1.0):** `0`
* **Formation AMBIGUOUS count (Confidence = 0.5):** `0`
* **Formation UNKNOWN count (Confidence = 0.0):** `0`
* **Top sơ đồ phổ biến nhất:**
Chưa có dữ liệu

---

## 5. 🔬 ĐỐI SOÁT RANKER STATS (VALIDATION)
* **Số ứng viên trước khi query (appearances >= 3):** `0`
* **Số ứng viên thực tế được query:** `0`
* **Bị cắt giảm do ngân sách (candidate_truncated_due_to_request_budget):** `False`
* **Số batch gửi tới /ranker-stats:** `0`
* **Số requests ranker-stats đã dùng:** `0`
* **Trạng thái file `glxh_ranker_stats.csv`:** `CHƯA TẠO`

---

## 6. 🛑 ĐIỂM DỪNG KIỂM TOÁN (HALT FOR REVIEW)
Hệ thống đã dừng hoàn toàn sau mẫu 300 trận đầu tiên. Tuyệt đối không tự động mở rộng mẫu (500, 1000, 5000) để người dùng và ChatGPT tiến hành kiểm tra chất lượng dữ liệu.
