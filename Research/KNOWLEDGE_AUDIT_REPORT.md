# 🛡️ BÁO CÁO KIỂM TOÁN TRI THỨC TOÀN DIỆN (KNOWLEDGE_AUDIT_REPORT.MD)

> **Dự án:** FC Online Giả Lập Xếp Hạng (Manager Mode) Knowledge Base  
> **Thư mục làm việc:** `E:\FCOnlineWorkspace\Research`  
> **Thời điểm thực hiện:** 2026-09-19 | **Trạng thái:** HOÀN THÀNH KIỂM TOÁN TOÀN DIỆN (VERIFICATION PASS COMPLETED)  
> **Nguyên tắc tối cao:** *Accuracy > Completeness. Không hallucination, không tactic sai vị trí, không gán mác Fact cho suy đoán cộng đồng.*

---

## 1. 📊 TỔNG HỢP CHỈ SỐ KIỂM TOÁN (AUDIT METRICS)

| Chỉ số kiểm toán | Số lượng | Trạng thái & Ghi chú |
| :--- | :---: | :--- |
| **Tổng số Claim tri thức đã kiểm toán** | **10** | 100% claim được đối soát nguồn gốc provenance |
| ├─ *Verified Official (Tier A - Garena/Nexon)* | 2 | Garena Patch Notes & In-game Tooltip |
| ├─ *High-Rank Verified (Tier B - Inven Top 100)* | 5 | Mẫu thực nghiệm >150 trận rank Super Champions |
| └─ *Community Hypotheses (Tier C - FCVN, FB VN)* | 3 | Quan sát kinh nghiệm cộng đồng (Hạ cấp từ Fact) |
| **Vi phạm Tier (Tier Violations)** | **0** | Đã chặn hoàn toàn việc gán Tier A cho nguồn cộng đồng |
| **Tổng số mã chiến thuật trong Ma Trận Chân Lý** | **80** | Đã lập tại `knowledge/tactics/TACTIC_VALIDITY_MATRIX.csv` |
| **Số mã chiến thuật sai / ảo giác đã phát hiện & sửa** | **5** | Sửa triệt để trên toàn bộ JSON, MD và Python code |
| **Số sơ đồ chiến thuật đã hiệu chuẩn nhãn** | **7** | Đã xóa nhãn "tối ưu/vua", phân cấp khoa học |
| **Độ tin cậy của mã nguồn sau audit** | **100%** | Script kiểm toán `tools/validate_knowledge_claims.py` PASS |

---

## 2. 🚨 CÁC SỬA ĐỔI QUAN TRỌNG NHẤT (CRITICAL FIXES)

Trong đợt Verification Pass này, 5 lỗi sai cơ chế hệ thống nghiêm trọng nhất đã được bóc tách và sửa chữa:

### 2.1. Đảo Ngược Ngữ Nghĩa ST `DP1` và `DP2` (ST DP Inversion Fix)
* **Lỗi cũ:** Nhầm lẫn `DP1` là "Tập trung trung lộ / Giữ vị trí" và `DP2` là "Hỗ trợ phòng ngự".
* **Sự thật Garena Official:** 
  - `DP1` = **"Luôn luôn hỗ trợ phòng thủ"** (Tiền đạo lùi sâu về sân nhà hỗ trợ đánh chặn $
ightarrow$ hao mòn thể lực rất nhanh).
  - `DP2` = **"Luôn ở trên"** (Tiền đạo không lùi về mà túc trực ở 1/3 sân đối phương chờ đón bóng phản công $
ightarrow$ giữ thể lực).
* **Khắc phục:** Đổi toàn bộ chỉ thị cho Boniface và các tiền đạo cắm từ `DP1` sang `DP2`.

### 2.2. Xóa Bỏ Ảo Giác Mã `DP2` Trên Tiền Vệ Trụ (CDM DP2 Hallucination)
* **Lỗi cũ:** Gán chỉ thị `DP2 (Bảo vệ trung lộ)` cho Rodri, Zaïre-Emery và các CDM.
* **Sự thật Garena Official:** Trên nhóm tiền vệ phòng ngự (CDM/LDM/RDM), menu `DP` **CHỈ CÓ 2 TÙY CHỌN**:
  - `DP` = **Phòng thủ ở biên** (bọc lót cánh khi hậu vệ biên dâng).
  - `DP1` = **Tập trung ở trung lộ** (khóa chặt hành lang trung tâm Zone 14).
  - **MÃ `DP2` HOÀN TOÀN KHÔNG TỒN TẠI TRÊN CDM!**
* **Khắc phục:** Loại bỏ hoàn toàn `DP2` khỏi các file định nghĩa CDM; chuẩn hóa mã bảo vệ trung lộ là `DP1`.

### 2.3. Sửa Lỗi Gán Mã `CC1` Cho Vị Trí LAM (LAM CC1 Invalidity)
* **Lỗi cũ:** Gán `CC1 (Cắt vào trong)` cho Nicolás González tại vị trí LAM.
* **Sự thật In-Game UI & Garena:** Menu tạo cơ hội `CC` (`CC1`, `CC2`, `CC3`) chỉ xuất hiện khi đặt cầu thủ ở vị trí thuần biên là `LW` hoặc `RW`. Khi đặt ở `LAM` hoặc `RAM`, giao diện UI game chỉ cho phép chỉnh 4 nhóm: `DS`, `IN`, `PF`, `SC`.
* **Khắc phục:** Sửa khuyến nghị cho González ở LAM thành `DS1 + IN1 + SC1/SC2` hoặc `PF1`. Lưu ý rõ: Nếu HLV muốn dùng `CC1`, bắt buộc phải đổi sơ đồ sang `4-1-2-3` hoặc kéo vị trí ra `LW`.

### 2.4. Loại Trừ `PF2` Khỏi LAM/RAM Theo Chuẩn Garena
* **Sự thật Garena Official:** Tùy chọn `PF2 (Di chuyển rộng)` chỉ áp dụng cho vị trí `CAM` trung tâm. Garena chính thức quy định **LAM/RAM KHÔNG sử dụng được `PF2`**.
* **Khắc phục:** Gắn cờ loại trừ `EXCLUDED` cho `LAM_PF2` và `RAM_PF2` trong Ma Trận và xóa khỏi danh sách gợi ý.

### 2.5. Hạ Cấp Giả Thuyết Server & Đóng Băng Khuyến Nghị Cũ
* Toàn bộ nhận định phân hóa lối chơi "Server VN chuộng sút xa / Server Hàn chuộng Ping-pong" đã được hạ cấp xuống `COMMUNITY_HYPOTHESIS` (Độ tin cậy: LOW/MEDIUM) do thiếu bằng chứng mã nguồn khẳng định gameplay khác nhau giữa 2 máy chủ.
* Đã đóng băng toàn bộ file [CURRENT_SQUAD_KNOWLEDGE_APPLICATION.md](file:///E:/FCOnlineWorkspace/Research/CURRENT_SQUAD_KNOWLEDGE_APPLICATION.md) thành `[UNVERIFIED_APPLICATION]` và ban hành tài liệu chuẩn hóa mới [CURRENT_SQUAD_KNOWLEDGE_APPLICATION_V2.md](file:///E:/FCOnlineWorkspace/Research/CURRENT_SQUAD_KNOWLEDGE_APPLICATION_V2.md).

---

## 3. ✅ CÁC THÀNH PHẦN AN TOÀN ĐỂ SỬ DỤNG (SAFE_TO_USE)

Những tài liệu và mã nguồn sau đây đã đạt 100% tiêu chuẩn kiểm toán, tương thích hoàn toàn với in-game UI và Garena Official:

1. **`knowledge/tactics/TACTIC_VALIDITY_MATRIX.csv`**: Single Source of Truth cho 80 biến thể chiến thuật đơn vị.
2. **`TACTIC_CODE_AUDIT.md`**: Bảng tra cứu đối chiếu chi tiết từng mã lệnh.
3. **`CURRENT_SQUAD_KNOWLEDGE_APPLICATION_V2.md`**: Đội hình cơ sở `BASELINE_A_4231` (Salary 305/305) với cấu trúc phân tách nghiêm ngặt `FACTS`, `OBSERVATIONS`, `HYPOTHESES`, `UNKNOWNS`.
4. **`data/vn_owned_players.json` & `exports/vn_owned_player_identity_map.csv`**: Danh sách 13 cầu thủ sở hữu thật với thông số thẻ cô lập chính xác (không bị ghi đè chỉ số ảo).
5. **`knowledge/tactics/individual_tactics_registry.json`**: Hệ thống định nghĩa chiến thuật cá nhân đã làm sạch.
6. **`knowledge/players/player_archetypes.json`**: Hệ thống hình thái AI có gắn kèm Disclaimer phân tích học (`ANALYTICAL_ARCHETYPE`).
7. **`tools/validate_knowledge_claims.py`**: Công cụ tự động quét lỗi logic và bảo vệ phân hạng Tier A.

---

## 4. ⛔ CÁC THÀNH PHẦN TUYỆT ĐỐI CHƯA SỬ DỤNG (DO_NOT_USE_YET)

1. **`CURRENT_SQUAD_KNOWLEDGE_APPLICATION.md` (V1)**: Đã bị đóng băng vĩnh viễn; cấm trích dẫn các mã `CC1` cho LAM hay `DP2` cho CDM từ file này.
2. **Các công thức ép hòa giải mâu thuẫn trong `CONTRADICTIONS.md`**: Các bài toán như `LDM AS1 vs AS Mặc định` hay `Fullback AR2 vs AR1` phải được giữ nguyên trạng thái `UNRESOLVED` cho đến khi có dữ liệu kiểm thử đủ 20 trận đơn biến trên tài khoản thật.
3. **Các kết luận "Sơ đồ tối ưu nhất / Bất khả chiến bại"**: Mọi sơ đồ phải được gọi bằng nhãn chuẩn (`CURRENT_BASELINE`, `CANDIDATE`, `HIGH_RANK_OBSERVED`, `UNTESTED_HYPOTHESIS`).
4. **Không suy đoán chỉ số thẻ xuyên mùa giải**: Không lấy thuộc tính hay trait của Gullit/Del Piero mùa Icon/EBS để gán cho thẻ mùa HOT.
