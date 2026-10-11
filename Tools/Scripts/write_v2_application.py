import sys
sys.stdout.reconfigure(encoding='utf-8')

v2_content = """# 🛡️ ỨNG DỤNG TRI THỨC VÀO ĐỘI HÌNH THỰC TẾ (CURRENT_SQUAD_KNOWLEDGE_APPLICATION_V2.MD)

> **Phiên bản:** V2 (Đã qua Kiểm toán Toàn diện - Verification Pass).  
> **Trạng thái:** ACTIVE | **Baseline:** `BASELINE_A_4231` (Salary 305/305).  
> **Nguồn đối chiếu:** [TACTIC_VALIDITY_MATRIX.csv](file:///E:/FCOnlineWorkspace/Research/knowledge/tactics/TACTIC_VALIDITY_MATRIX.csv) & [TACTIC_CODE_AUDIT.md](file:///E:/FCOnlineWorkspace/Research/TACTIC_CODE_AUDIT.md).  
> **Nguyên tắc cốt lõi:** Bắt buộc phân tách 4 phần độc lập cho từng cầu thủ: `FACTS`, `OBSERVATIONS`, `HYPOTHESES`, `UNKNOWNS`. Tuyệt đối không sử dụng mã chiến thuật sai vị trí hoặc ảo giác.

---

## 1. 📋 DANH SÁCH 11 VỊ TRÍ ĐÁ CHÍNH TRONG BASELINE_A_4231

Sơ đồ: **4-2-3-1 Đóng Băng Trung Tuyến** (`CURRENT_BASELINE`, Tổng Lương: 305/305).

---

### 1. 👑 ST: Victor Boniface
* **FACTS:**
  - Mùa thẻ: `WS`, Cấp thẻ: `+3`, OVR hiển thị: `119`, OVR cơ sở: `117`, Lương: `28`.
  - Vị trí tự nhiên: `ST`. Thuộc tính thể chất: Chiều cao 1m90, Cân nặng 91kg, Thể hình Đậm (Stocky), Chân thuận: Phải (Chân không thuận: 3).
  - Tình trạng sở hữu: **OWNED_PLAYER_DATA (Đang sở hữu thực tế trong kho)**.
  - Archetype phân tích: `ANALYTICAL_ARCHETYPE: TARGET_MAN_ST`.
* **OBSERVATIONS:**
  - Khả năng cài đè, che chắn bóng và không chiến vượt trội trước các trung vệ thể hình vừa; thu hút sự chú ý của 2 trung vệ đối phương tạo khoảng trống cho tuyến 2 dâng lên.
* **HYPOTHESES (Chiến thuật cá nhân đề xuất):**
  - `AR2` (Mục tiêu / Tiền đạo cắm làm tường): Giữ vị trí trung tâm, quay lưng về khung thành nhận bóng phối hợp.
  - `DP2` (Luôn ở trên - Không lùi về phòng ngự): **SỬA LỖI TỪ V1**. File cũ gán `DP1` với nhầm tưởng là giữ vị trí, nhưng theo Garena Official, `DP1` là "Luôn luôn hỗ trợ phòng thủ" (lùi sâu hao thể lực). Cần dùng `DP2` để giữ thể lực và sẵn sàng phản công.
  - `SR` (Chạy chỗ cân bằng) hoặc `SR1` (Chạy chỗ áp sát mép việt vị).
* **UNKNOWNS:**
  - Tỷ lệ chuyển hóa các pha dứt điểm góc hẹp bằng chân trái (chân không thuận 3/5) khi bị tì đè liên tục trong GLXH.

---

### 2. ⚡ LAM: Nicolás González
* **FACTS:**
  - Vị trí trong sơ đồ: `LAM` (Tiền vệ tấn công lệch trái). Vị trí tự nhiên thẻ: `LW`, `LM`, `RW`.
  - Chân thuận: Trái (5/4), Tốc độ cao, Khéo léo, Thể hình Nhỏ/Chuẩn.
  - Tình trạng sở hữu: `CANDIDATE_DATA` (Trong phôi đội hình thử nghiệm V1).
  - Archetype phân tích: `ANALYTICAL_ARCHETYPE: INVERTED_CREATOR`.
* **OBSERVATIONS:**
  - Tốc độ bứt biên tốt, tạt bóng chân trái xoáy, hỗ trợ pressing mép ngoài vòng cấm.
* **HYPOTHESES (Chiến thuật cá nhân đề xuất):**
  - **SỬA LỖI NGHIÊM TRỌNG TỪ V1:** File cũ gán `CC1` (Cắt vào trong) cho González tại LAM. **Nhóm `CC` KHÔNG TỒN TẠI trên vị trí LAM** (chỉ thuộc về LW/RW).
  - Thiết lập chuẩn xác cho LAM:
    - `DS1` (Luôn ở phía trên) hoặc `DS2` (Hỗ trợ phòng ngự tích cực tùy diễn biến).
    - `IN1` (Đánh chặn chủ động áp sát biên).
    - `SC1` (Xâm nhập vòng cấm khi tạt) hoặc `SC2` (Đợi rìa vòng cấm).
    - `PF1` (Di chuyển tự do - Free Roam). *(Lưu ý: Garena cấm LAM sử dụng `PF2` Di chuyển rộng).*
  - *Phương án thay thế:* Nếu muốn dùng lệnh `CC1` (Cắt vào trong), HLV phải chuyển sơ đồ sang `4-1-2-3` hoặc kéo slot từ LAM ra thành `LW`.
* **UNKNOWNS:**
  - Tần suất xâm nhập nách trung vệ của AI khi được đặt ở LAM so với khi đặt ở LW thuần túy.

---

### 3. 🎯 CAM: Frank Lampard
* **FACTS:**
  - Vị trí trong sơ đồ: `CAM` (Nhạc trưởng trung lộ). Vị trí tự nhiên: `CM`, `CAM`.
  - Thể hình Chuẩn, Lực sút & Sút xa cực cao, Chọn vị trí tấn công tốt.
  - Tình trạng sở hữu: `CANDIDATE_DATA` (Phôi đội hình thử nghiệm V1; kho hiện có Rosicky WG +1 và Park Ji Sung NO.7 +1).
  - Archetype phân tích: `ANALYTICAL_ARCHETYPE: SECOND_WAVE_FINISHER`.
* **OBSERVATIONS:**
  - Sút xa ZD/D căng từ tuyến hai uy lực, khả năng ập vào vòng cấm đón bóng hai nảy ra rất nhạy.
* **HYPOTHESES (Chiến thuật cá nhân đề xuất):**
  - `SC2` (Đợi bóng ở rìa vòng cấm đón bóng hai để nã đại bác).
  - `DS1` (Luôn ở phía trên để giữ cự ly phản công và không hao thể lực lùi về).
  - `PF` (Mặc định kỷ luật vị trí, giữ đúng trục dọc kết nối với Boniface).
* **UNKNOWNS:**
  - Khả năng thoát pressing khi bị 2 tiền vệ mỏ neo cơ bắp đối phương áp sát cùng lúc.

---

### 4. 🎨 RAM: Florian Wirtz
* **FACTS:**
  - Vị trí trong sơ đồ: `RAM` (Tiền vệ tấn công lệch phải). Vị trí tự nhiên: `CAM`, `LW`, `RW`.
  - Thể hình Nhỏ, Rê bóng dính chân, Tầm nhìn và Chọc khe sắc bén.
  - Tình trạng sở hữu: `CANDIDATE_DATA` (Phôi thử nghiệm V1).
  - Archetype phân tích: `ANALYTICAL_ARCHETYPE: CREATIVE_ENGANCHE`.
* **OBSERVATIONS:**
  - Đi bóng lắt léo, chọc khe QW hoặc chọc khe sệt xé toang hàng phòng ngự đối phương.
* **HYPOTHESES (Chiến thuật cá nhân đề xuất):**
  - `PF1` (Di chuyển tự do tìm khoảng trống). **LƯU Ý:** Tuyệt đối không dùng `PF2` vì Garena quy định RAM không hỗ trợ `PF2`.
  - `SC2` (Đợi bóng ở rìa vòng cấm phối hợp).
  - `DS1` (Luôn ở phía trên).
* **UNKNOWNS:**
  - Độ bền thể lực ở 15 phút cuối trận trước đối thủ cài áp lực phòng ngự cao (Aggression > 60).

---

### 5. ⚙️ RDM: Warren Zaïre-Emery
* **FACTS:**
  - Vị trí trong sơ đồ: `RDM` (Cặp Double Pivot). Vị trí tự nhiên: `CM`, `CDM`.
  - Thể lực dồi dào, Thăng bằng cao, Tốc độ cơ động, Tranh chấp quyết liệt.
  - Tình trạng sở hữu: `CANDIDATE_DATA` (Phôi thử nghiệm V1).
  - Archetype phân tích: `ANALYTICAL_ARCHETYPE: DYNAMIC_BALL_WINNER`.
* **OBSERVATIONS:**
  - Máy quét cơ động, áp sát nhanh bẻ gãy các đợt phát động tấn công từ trung lộ của đối phương.
* **HYPOTHESES (Chiến thuật cá nhân đề xuất):**
  - **SỬA LỖI TỪ V1:** File cũ gán `DP2` (Bảo vệ trung lộ). **Trên CDM KHÔNG TỒN TẠI MÃ `DP2`**. Mã bảo vệ trung lộ chuẩn của Garena trên CDM là `DP1`.
  - Thiết lập chuẩn xác:
    - `AS Mặc định` (hoặc `AS2` Tham gia tấn công khi cần bàn).
    - `IN1` (Đánh chặn chủ động / Gắt gao).
    - `DP1` (Tập trung ở trung lộ - Khóa Zone 14).
* **UNKNOWNS:**
  - Khả năng chống bóng bổng trong vòng cấm khi gặp các pha tạt cánh sớm (Early Cross) từ biên.

---

### 6. ⚓ LDM: Rodri
* **FACTS:**
  - Vị trí trong sơ đồ: `LDM` (Cặp Double Pivot). Vị trí tự nhiên: `CDM`, `CM`.
  - Chiều cao 1m91, Sải chân cản phá cực rộng, Cắt bóng & Quyết đoán cao.
  - Tình trạng sở hữu: **OWNED_PLAYER_DATA (Đang sở hữu thẻ Rodri mùa 19 +1, OVR 95, Lương 17)**.
  - Archetype phân tích: `ANALYTICAL_ARCHETYPE: ANCHOR_CDM`.
* **OBSERVATIONS:**
  - Khóa chặt hành lang trung lộ trước mặt 2 trung vệ, bẻ gãy các đường chọc khe sệt xuyên tuyến.
* **HYPOTHESES (Chiến thuật cá nhân đề xuất):**
  - **SỬA LỖI TỪ V1:** File cũ gán `DP2`. Sửa thành `DP1` (Tập trung ở trung lộ).
  - Thiết lập chuẩn xác:
    - `AS1` (Ở lại phía sau khi tấn công - Cố định trước vòng cấm).
    - `DB1` (Cắt đường chuyền - AI ưu tiên chắn khe chuyền bóng sệt).
    - `DP1` (Tập trung ở trung lộ - Giữ nguyên vị trí trung tâm, không dạt biên).
* **UNKNOWNS:**
  - Tốc độ bứt tốc đoạn ngắn của thẻ Rodri 19 khi phải đuổi theo tiền đạo cánh tốc độ cao phản công.

---

### 7. 🛡️ LB: Joško Gvardiol
* **FACTS:**
  - Mùa thẻ: `25DP`, Cấp thẻ: `+1`, OVR hiển thị: `118`, OVR cơ sở: `118`, Lương: `29`.
  - Vị trí tự nhiên: `LB`, `CB`. Chiều cao 1m85, Thể hình Đậm/Sức khỏe, Chân 4/5.
  - Tình trạng sở hữu: **OWNED_PLAYER_DATA (Đang sở hữu thực tế trong kho)**.
  - Archetype phân tích: `ANALYTICAL_ARCHETYPE: COMPLETE_DEFENSIVE_FULLBACK`.
* **OBSERVATIONS:**
  - Phòng ngự cánh kiên cố, không chiến chống tạt bóng xuất sắc, tì đè đè bẹp các tiền đạo cánh nhỏ con.
* **HYPOTHESES (Chiến thuật cá nhân đề xuất):**
  - `AR2` (Ở lại phía sau khi tấn công): Giữ nguyên cự ly hàng thủ 4 người, chống phản công biên.
  - `IN2` (Đánh chặn thận trọng): Giữ vị trí khép góc, tránh bị vặn sườn.
  - `SR Mặc định` (Hỗ trợ cân bằng).
* **UNKNOWNS:**
  - Độ hiệu quả khi chủ động kích hoạt `AR1` (Chồng biên) trong các thế trận bị dẫn bàn cần dồn ép cánh.

---

### 8. 🧱 LCB: Marcel Desailly
* **FACTS:**
  - Vị trí trong sơ đồ: `LCB`. Vị trí tự nhiên: `CB`, `CDM`.
  - Thể hình Đậm, Sức mạnh & Quyết đoán tối đa, Bật nhảy tranh chấp tay đôi như xe ủi.
  - Tình trạng sở hữu: `CANDIDATE_DATA` (Phôi thử nghiệm V1; kho hiện có Sergio Ramos 19 +1 và Schär 25DP +1).
  - Archetype phân tích: `ANALYTICAL_ARCHETYPE: STOPPER_CB`.
* **OBSERVATIONS:**
  - Dập bóng quyết liệt nhịp một, áp sát cướp bóng trước khi tiền đạo cắm đối phương kịp xoay lưng.
* **HYPOTHESES (Chiến thuật cá nhân đề xuất):**
  - `IN1` (Đánh chặn chủ động / Dập gắt): Trung vệ dập lao lên cắt bóng sớm.
* **UNKNOWNS:**
  - Khoảng trống phía sau lưng khi dập hụt nếu đối phương thực hiện đường chuyền 1-2 đập nhả bật tường cực nhanh.

---

### 9. 🧠 RCB: Fabian Schär
* **FACTS:**
  - Mùa thẻ: `25DP`, Cấp thẻ: `+1`, OVR hiển thị: `114`, OVR cơ sở: `114`, Lương: `27`.
  - Vị trí tự nhiên: `CB`. Chiều cao 1m88, Thể hình Chuẩn, Bình tĩnh cao, Chuyền dài tốt.
  - Tình trạng sở hữu: **OWNED_PLAYER_DATA (Đang sở hữu thực tế trong kho)**.
  - Archetype phân tích: `ANALYTICAL_ARCHETYPE: COVER_SWEEPER_CB`.
* **OBSERVATIONS:**
  - Bọc lót thông minh phía sau trung vệ dập, phán đoán điểm rơi bóng bổng và phát động phản công dài chuẩn xác.
* **HYPOTHESES (Chiến thuật cá nhân đề xuất):**
  - `IN2` (Đánh chặn thận trọng / Thòng bọc lót): Lùi sâu giữ cự ly che chắn phía sau lưng Desailly / trung vệ dập.
* **UNKNOWNS:**
  - Tốc độ xoay trở khi gặp các ST sở hữu trait Ma tốc độ bứt phá đoạn ngắn.

---

### 10. ⚡ RB: Gianluca Zambrotta
* **FACTS:**
  - Mùa thẻ: `WG`, Cấp thẻ: `+1`, OVR hiển thị: `119`, OVR cơ sở: `119`, Lương: `30`.
  - Vị trí tự nhiên: `RB`, `LB`. Hai chân `5/5`, Tốc độ 121, Thể lực 123, Phòng ngự 122.
  - Tình trạng sở hữu: **OWNED_PLAYER_DATA (Đang sở hữu thực tế trong kho)**.
  - Archetype phân tích: `ANALYTICAL_ARCHETYPE: ELITE_TWO_WAY_FULLBACK`.
* **OBSERVATIONS:**
  - Hậu vệ biên toàn diện số 1 meta; thoát pressing biên hai chân tuyệt đối không lỗi, tốc độ hồi phục vị trí thần tốc.
* **HYPOTHESES (Chiến thuật cá nhân đề xuất):**
  - `AR2` (Ở lại phía sau khi tấn công) để bảo toàn cánh phải; hoặc `AR1` khi cần tạo quân số áp đảo ở cánh.
  - `IN1` (Đánh chặn chủ động): Nhờ tốc độ và thăng bằng cao, Zambrotta có thể áp sát cướp bóng biên chủ động rất an toàn.
  - `SR Mặc định`.
* **UNKNOWNS:**
  - Chưa ghi nhận điểm yếu cơ chế rõ rệt ở phiên bản hiện tại.

---

### 11. 🧤 GK: Mailson / W. Hennessey
* **FACTS:**
  - Kho sở hữu thực tế: `W. Hennessey HOT +1` (OVR 96, Lương 13, Chiều cao 1m98).
  - Phôi thử nghiệm V1: `Mailson` (Chiều cao 1m97).
  - Vị trí tự nhiên: `GK`.
  - Archetype phân tích: `ANALYTICAL_ARCHETYPE: GIANT_SHOT_STOPPER_GK`.
* **OBSERVATIONS:**
  - Chiều cao trên 1m97 giúp khép góc xa và cản phá sút xa ZD vượt trội so với các GK thấp bé (<1m90) dù chỉ số OVR thấp hơn.
* **HYPOTHESES (Chiến thuật cá nhân đề xuất):**
  - Chiến thuật cá nhân: Mặc định của thủ môn.
* **UNKNOWNS:**
  - Khả năng xử lý các pha sút sệt chéo góc hiểm hóc ở cự ly gần 10m.

---

## 2. 🔄 ÁNH XẠ KHO CẦU THỦ THẬT (OWNED INVENTORY) VÀO HỆ THỐNG CHIẾN THUẬT

Để bảo toàn tính toàn vẹn giữa dữ liệu đang sở hữu thật và chiến thuật:

| Cầu thủ sở hữu | Mùa / Cấp | OVR / Lương | Natural Pos | Đề Xuất Slot Trong Baseline 4-2-3-1 | Vai Trò & Chiến Thuật Khuyến Nghị |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **V. Boniface** | WS +3 | 119 / 28 | ST | **ST (Đá chính)** | `AR2` (Mục tiêu) + `DP2` (Luôn ở trên) |
| **G. Zambrotta** | WG +1 | 119 / 30 | RB/LB | **RB (Đá chính)** | `AR2` (Ở lại sau) + `IN1` (Chủ động) |
| **J. Gvardiol** | 25DP +1 | 118 / 29 | LB/CB | **LB (Đá chính)** | `AR2` (Ở lại sau) + `IN2` (Thận trọng) |
| **F. Schar** | 25DP +1 | 114 / 27 | CB | **RCB (Đá chính)** | `IN2` (Thòng bọc lót) |
| **T. Rosicky** | WG +1 | 118 / 30 | LM/CM | **LAM / CAM (Cạnh tranh đá chính)** | `SC2` + `DS1` + `PF1` |
| **Park Ji Sung** | NO.7 +1 | 117 / 29 | CAM/LM | **LAM / RAM (Cạnh tranh đá chính)** | `IN1` + `DS1` + `SC1` (Quét cánh) |
| **R. Gullit** | HOT +1 | 103 / 22 | CM/LW/ST | **RDM / LCM / Dự bị chiến lược** | `AS Mặc định` + `DP1` (Bảo vệ trung lộ) |
| **Rodri** | 19 +1 | 95 / 17 | CDM/CM | **LDM (Cân đối quỹ lương)** | `AS1` + `DB1` + `DP1` |
| **Sergio Ramos** | 19 +1 | 94 / 18 | CB | **LCB (Cân đối lương / Dập)** | `IN1` (Dập gắt) |
| **W. Hennessey** | HOT +1 | 96 / 13 | GK | **GK (Bắt chính tối ưu lương 13)** | Mặc định hộ pháp 1m98 |
| **A. Del Piero** | HOT +1 | 102 / 20 | CF/CAM | **Dự bị CF / CAM** | `SC2` + `DS1` |
| **P. Aubameyang** | LH +1 | 96 / 18 | ST/LW/RW | **Dự bị ST tốc độ** | `AR1` (Phá bẫy việt vị) + `DP2` |
| **Inaki Williams**| HOT +1 | 95 / 16 | ST/RW | **Dự bị Winger / ST tốc độ** | `AR1` + `CC1` (nếu xếp RW) |

---

## 3. 🛡️ QUY TẮC VẬN HÀNH AN TOÀN TRONG GLXH

1. **Khóa Chặt Zone 14 (Khoảng trống trước vòng cấm):**
   - Tiền vệ phòng ngự mỏ neo BẮT BUỘC cài `AS1` + `DB1` + `DP1` (Không dùng mã `DP2` vì không tồn tại).
2. **Tiền Đạo Cắm Độc Lập:**
   - Cài `AR2` + `DP2` để giữ Boniface ở tuyến đầu làm trạm luân chuyển, không để ST lùi sâu phòng thủ hao hụt thể lực (`DP1`).
3. **LAM/RAM Không Sử Dụng Tactic Biên Của Tiền Đạo Cánh:**
   - Không gán `CC1` cho LAM/RAM. Nếu muốn cầu thủ cánh bó trong sút xa, dùng `SC1/SC2` phối hợp hoặc đổi slot sang `LW/RW`.
4. **Hậu Vệ Biên An Toàn:**
   - Cài `AR2` để giữ vững bộ tứ vệ 4 người khi đối thủ phản công tốc độ cao.
"""

with open("E:/FCOnlineWorkspace/Research/CURRENT_SQUAD_KNOWLEDGE_APPLICATION_V2.md", "w", encoding="utf-8") as f:
    f.write(v2_content)

print("Created CURRENT_SQUAD_KNOWLEDGE_APPLICATION_V2.md successfully.")
