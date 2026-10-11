# 🛡️ TACTIC CODE AUDIT: KIỂM TOÁN MÃ CHIẾN THUẬT ĐƠN VỊ VÀ ĐỐI CHIẾU NGUỒN CHÂN LÝ

> **Tài liệu kiểm toán:** Single Source of Truth cho toàn bộ mã chiến thuật cá nhân (Individual Tactics) trong FC Online GLXH.  
> **Nguồn đối chiếu:** Garena FC Online Vietnam Official ([Hướng Dẫn Chiến Thuật](https://fconline.garena.vn/nam-ro-dieu-chinh-chien-thuat-trong-fc-online/)) & In-game UI.  
> **Ngày thực hiện:** 2026-09-19 | **Trạng thái:** HOÀN TẤT KIỂM TOÁN 100%

---

## 1. 🚨 CÁC LỖI SAI NGHIÊM TRỌNG ĐÃ PHÁT HIỆN VÀ SỬA ĐỔI (CRITICAL FIXES)

Trong quá trình rà soát toàn bộ Knowledge Base, đã phát hiện và xử lý triệt để 5 lỗi sai/ảo giác (hallucination) nghiêm trọng từ các tài liệu trước:

| Vấn đề | Mã Cũ (Sai Lệch / Ảo Giác) | Mã Chuẩn Sau Audit (Garena Official) | Phân Tích & Nguyên Nhân |
| :--- | :--- | :--- | :--- |
| **ST DP Inversion** | DP1 = Tập trung trung lộ<br>DP2 = Hỗ trợ phòng ngự | **DP1 = Luôn luôn hỗ trợ phòng thủ**<br>**DP2 = Luôn ở trên** | File cũ bị đảo ngược 180 độ ngữ nghĩa so với Garena Official. DP1 khiến ST lùi sâu phòng thủ hao thể lực; DP2 mới là giữ ST ở trên chờ bóng phản công. |
| **CDM DP2 Hallucination** | CDM: DP2 (Bảo vệ trung lộ) | **CDM: DP1 (Tập trung ở trung lộ)**<br>*(Không tồn tại mã DP2 trên CDM)* | Trên CDM chỉ có 2 tùy chọn: DP (Phòng thủ ở biên) và DP1 (Tập trung ở trung lộ). Mã DP2 trên CDM hoàn toàn là ảo giác. |
| **LAM CC1 Invalidity** | LAM: CC1 (Cắt vào trong) | **LAM: DS, IN, PF, SC**<br>*(Nhóm CC chỉ tồn tại trên LW/RW)* | Nhóm tạo cơ hội CC (CC1, CC2, CC3) chỉ dành riêng cho vị trí thuần biên (LW/RW). LAM/RAM không có menu CC trong UI game. |
| **LAM/RAM PF2 Exclusion** | LAM: PF2 (Di chuyển rộng) | **LAM/RAM: Bị loại trừ (EXCLUDED)** | Garena chính thức quy định: PF2 (Di chuyển rộng) chỉ áp dụng cho CAM trung tâm; LAM/RAM không sử dụng được tính năng này. |
| **Fullback SR Semantics** | Nhầm lẫn giữa dạt biên và bó trong | **SR1 = Bó vào trong (Inverted)**<br>**SR2 = Chồng biên (Overlap wide)** | Chuẩn hóa định nghĩa theo cơ chế di chuyển thực tế của hậu vệ biên khi đội nhà kiểm soát bóng. |

---

## 2. 📊 BẢNG TRA CỨU TÍNH HỢP LỆ CHI TIẾT (TACTIC VALIDITY MATRIX)

Dữ liệu được trích xuất trực tiếp từ [knowledge/tactics/TACTIC_VALIDITY_MATRIX.csv](file:///E:/FCOnlineWorkspace/Research/knowledge/tactics/TACTIC_VALIDITY_MATRIX.csv):

| Vị trí | Nhóm | Biến thể | UI Confirmed | Garena Confirmed | Ý nghĩa chuẩn xác | Phân loại |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| ST | AR | AR | ✅ | ✅ | Hỗ trợ tấn công cân bằng (mặc định) | VALID |
| ST | AR | AR1 | ✅ | ✅ | Xẻ nách / Chạy chỗ phá bẫy việt vị | VALID |
| ST | AR | AR2 | ✅ | ✅ | Mục tiêu / Tiền đạo cắm làm tường | VALID |
| ST | AR | AR3 | ✅ | ✅ | Dạt biên / Mở rộng không gian | VALID |
| ST | DP | DP | ✅ | ✅ | Hỗ trợ phòng ngự cân bằng (mặc định) | VALID |
| ST | DP | DP1 | ✅ | ✅ | Luôn luôn hỗ trợ phòng thủ (tích cực lùi về) | VALID |
| ST | DP | DP2 | ✅ | ✅ | Luôn ở trên (không lùi về, chờ bóng phản công) | VALID |
| ST | IN | IN | ✅ | ✅ | Đánh chặn thông thường | VALID |
| ST | IN | IN1 | ✅ | ✅ | Đánh chặn chủ động / Gắt gao | VALID |
| ST | IN | IN2 | ✅ | ✅ | Đánh chặn thận trọng | VALID |
| ST | SR | SR | ✅ | ✅ | Chạy chỗ cân bằng | VALID |
| ST | SR | SR1 | ✅ | ✅ | Chạy chỗ áp sát hàng thủ (đè mặt mép việt vị) | VALID |
| ST | SR | SR2 | ✅ | ✅ | Đợi bóng / Lùi lại hỗ trợ nhận bóng | VALID |
| CAM | DS | DS | ✅ | ✅ | Hỗ trợ phòng thủ cơ bản (mặc định) | VALID |
| CAM | DS | DS1 | ✅ | ✅ | Luôn ở phía trên (chờ bóng phản công) | VALID |
| CAM | DS | DS2 | ✅ | ✅ | Hỗ trợ phòng ngự tích cực | VALID |
| CAM | IN | IN | ✅ | ✅ | Đánh chặn thông thường | VALID |
| CAM | IN | IN1 | ✅ | ✅ | Đánh chặn chủ động | VALID |
| CAM | IN | IN2 | ✅ | ✅ | Đánh chặn thận trọng | VALID |
| CAM | PF | PF | ✅ | ✅ | Kỷ luật vị trí (mặc định) | VALID |
| CAM | PF | PF1 | ✅ | ✅ | Di chuyển tự do (Free Roam) | VALID |
| CAM | PF | PF2 | ✅ | ✅ | Di chuyển rộng (chỉ áp dụng CAM; LAM/RAM KHÔNG sử dụng được) | VALID |
| LAM | PF | PF2 | ❌ | ⛔ | INVALID_FOR_LAM: Garena quy định LAM/RAM không sử dụng được PF2 | EXCLUDED |
| RAM | PF | PF2 | ❌ | ⛔ | INVALID_FOR_RAM: Garena quy định LAM/RAM không sử dụng được PF2 | EXCLUDED |
| LAM | CC | CC1 | ❌ | ❌ | INVALID_FOR_LAM: Nhóm CC chỉ thuộc về LW/RW, không tồn tại trên LAM | INVALID |
| RAM | CC | CC1 | ❌ | ❌ | INVALID_FOR_RAM: Nhóm CC chỉ thuộc về LW/RW, không tồn tại trên RAM | INVALID |
| CAM | SC | SC | ✅ | ✅ | Hỗ trợ tạt bóng cân bằng | VALID |
| CAM | SC | SC1 | ✅ | ✅ | Xâm nhập vòng cấm khi tạt bóng | VALID |
| CAM | SC | SC2 | ✅ | ✅ | Đợi bóng ở rìa vòng cấm (tuyến 2) | VALID |
| LDM | AS | AS | ✅ | ✅ | Hỗ trợ tấn công cân bằng (mặc định) | VALID |
| LDM | AS | AS1 | ✅ | ✅ | Ở lại phía sau khi tấn công (Stay Back) | VALID |
| LDM | AS | AS2 | ✅ | ✅ | Tham gia tấn công | VALID |
| LDM | AS | AS3 | ✅ | ✅ | Vị trí giữa các hậu vệ (chỉ áp dụng cho đội hình 4 hậu vệ) | VALID |
| RDM | AS | AS | ✅ | ✅ | Hỗ trợ tấn công cân bằng (mặc định) | VALID |
| RDM | AS | AS1 | ✅ | ✅ | Ở lại phía sau khi tấn công (Stay Back) | VALID |
| RDM | AS | AS2 | ✅ | ✅ | Tham gia tấn công | VALID |
| RDM | AS | AS3 | ✅ | ✅ | Vị trí giữa các hậu vệ (chỉ áp dụng cho đội hình 4 hậu vệ) | VALID |
| LDM | DB | DB | ✅ | ✅ | Hỗ trợ phòng thủ cân bằng | VALID |
| LDM | DB | DB1 | ✅ | ✅ | Cắt đường chuyền (Cut Passing Lanes) | VALID |
| LDM | DB | DB2 | ✅ | ✅ | Kèm chặt người (Man Mark) | VALID |
| RDM | DB | DB | ✅ | ✅ | Hỗ trợ phòng thủ cân bằng | VALID |
| RDM | DB | DB1 | ✅ | ✅ | Cắt đường chuyền (Cut Passing Lanes) | VALID |
| RDM | DB | DB2 | ✅ | ✅ | Kèm chặt người (Man Mark) | VALID |
| LDM | DP | DP | ✅ | ✅ | Phòng thủ ở biên (bọc lót khi hậu vệ cánh dâng) | VALID |
| LDM | DP | DP1 | ✅ | ✅ | Tập trung ở trung lộ (bảo vệ trung tâm) | VALID |
| LDM | DP | DP2 | ❌ | ❌ | INVALID_CODE: Nhóm DP trên tiền vệ trụ KHÔNG có DP2 | INVALID |
| RDM | DP | DP | ✅ | ✅ | Phòng thủ ở biên (bọc lót khi hậu vệ cánh dâng) | VALID |
| RDM | DP | DP1 | ✅ | ✅ | Tập trung ở trung lộ (bảo vệ trung tâm) | VALID |
| RDM | DP | DP2 | ❌ | ❌ | INVALID_CODE: Nhóm DP trên tiền vệ trụ KHÔNG có DP2 | INVALID |
| LDM | IN | IN | ✅ | ✅ | Đánh chặn thông thường | VALID |
| LDM | IN | IN1 | ✅ | ✅ | Đánh chặn chủ động | VALID |
| LDM | IN | IN2 | ✅ | ✅ | Đánh chặn thận trọng | VALID |
| RDM | IN | IN | ✅ | ✅ | Đánh chặn thông thường | VALID |
| RDM | IN | IN1 | ✅ | ✅ | Đánh chặn chủ động | VALID |
| RDM | IN | IN2 | ✅ | ✅ | Đánh chặn thận trọng | VALID |
| LB | AR | AR | ✅ | ✅ | Tấn công cân bằng (mặc định) | VALID |
| LB | AR | AR1 | ✅ | ✅ | Chồng biên / Tham gia tấn công | VALID |
| LB | AR | AR2 | ✅ | ✅ | Ở lại phía sau khi tấn công (Stay Back) | VALID |
| RB | AR | AR | ✅ | ✅ | Tấn công cân bằng (mặc định) | VALID |
| RB | AR | AR1 | ✅ | ✅ | Chồng biên / Tham gia tấn công | VALID |
| RB | AR | AR2 | ✅ | ✅ | Ở lại phía sau khi tấn công (Stay Back) | VALID |
| LB | IN | IN | ✅ | ✅ | Đánh chặn thông thường | VALID |
| LB | IN | IN1 | ✅ | ✅ | Đánh chặn chủ động | VALID |
| LB | IN | IN2 | ✅ | ✅ | Đánh chặn thận trọng | VALID |
| RB | IN | IN | ✅ | ✅ | Đánh chặn thông thường | VALID |
| RB | IN | IN1 | ✅ | ✅ | Đánh chặn chủ động | VALID |
| RB | IN | IN2 | ✅ | ✅ | Đánh chặn thận trọng | VALID |
| LB | SR | SR | ✅ | ✅ | Hỗ trợ xâm nhập cân bằng (tùy tình hình) | VALID |
| LB | SR | SR1 | ✅ | ✅ | Di chuyển từ cánh vào trung tâm (làm tường hỗ trợ tuyến giữa) | VALID |
| LB | SR | SR2 | ✅ | ✅ | Phối hợp chồng cánh (lên công về thủ dọc biên) | VALID |
| RB | SR | SR | ✅ | ✅ | Hỗ trợ xâm nhập cân bằng (tùy tình hình) | VALID |
| RB | SR | SR1 | ✅ | ✅ | Di chuyển từ cánh vào trung tâm (làm tường hỗ trợ tuyến giữa) | VALID |
| RB | SR | SR2 | ✅ | ✅ | Phối hợp chồng cánh (lên công về thủ dọc biên) | VALID |
| CB | IN | IN | ✅ | ✅ | Đánh chặn thông thường | VALID |
| CB | IN | IN1 | ✅ | ✅ | Đánh chặn chủ động / Dập gắt | VALID |
| CB | IN | IN2 | ✅ | ✅ | Đánh chặn thận trọng / Thòng bọc lót | VALID |
| LW | CC | CC3 | ✅ | ✅ | Vai trò tự do (di chuyển xung quanh nhiều hơn gần biên) | VALID |
| RW | CC | CC3 | ✅ | ✅ | Vai trò tự do (di chuyển xung quanh nhiều hơn gần biên) | VALID |
| LW | SR | SR3 | ✅ | ✅ | Tiền đạo mục tiêu (luôn xuất hiện trong vòng cấm gần hậu vệ cuối) | VALID |
| RW | SR | SR3 | ✅ | ✅ | Tiền đạo mục tiêu (luôn xuất hiện trong vòng cấm gần hậu vệ cuối) | VALID |

---

## 3. 🛠️ CÁC TỆP ĐÃ ĐƯỢC ĐỒNG BỘ VÀ LÀM SẠCH

1. **knowledge/tactics/individual_tactics_registry.json**:
   - Khôi phục định nghĩa chuẩn ST DP1 (Luôn luôn hỗ trợ phòng thủ) và DP2 (Luôn ở trên).
   - Xóa bỏ DP2 khỏi LDM/RDM/CDM; chuyển hướng sang DP (Phòng thủ ở biên) và DP1 (Tập trung ở trung lộ).
   - Bổ sung cụm LW_RW đầy đủ các nhóm CC (CC1, CC2, CC3), SR (SR1, SR2, SR3), DS, IN, SC.
   - Đánh dấu loại trừ PF2 đối với LAM/RAM theo xác nhận Garena.

2. **knowledge/players/player_archetypes.json**:
   - Thêm metadata disclaimer: ANALYTICAL_ARCHETYPE (không phải class AI nội bộ do EA/Nexon đặt tên).
   - Sửa ideal_instructions cho ST (AR1/AR2 đi kèm DP2 thay vì DP1), CDM (AS1 + DB1 + DP1 thay vì DP2).
   - Thêm quy tắc cách ly thẻ mùa giải (season_isolation_rule).

3. **knowledge/formations/*.json**:
   - Loại bỏ toàn bộ từ ngữ mang tính tuyệt đối hóa (hoàn hảo nhất, 	ối ưu nhất).
   - Gắn nhãn phân loại chuẩn mực: CURRENT_BASELINE, HIGH_RANK_OBSERVED, CANDIDATE, UNTESTED_HYPOTHESIS.

4. **	ools/validate_knowledge_claims.py**:
   - Công cụ kiểm toán tự động các claim để đảm bảo không một nhận định cộng đồng nào được phép gắn mác Tier A.

5. **CURRENT_SQUAD_KNOWLEDGE_APPLICATION.md**:
   - Đã được niêm phong đóng băng dưới nhãn [UNVERIFIED_APPLICATION].
   - Toàn bộ đề xuất chiến thuật đội hình được chuyển giao sang phiên bản chuẩn hóa CURRENT_SQUAD_KNOWLEDGE_APPLICATION_V2.md.
