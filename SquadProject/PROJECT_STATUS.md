# 📊 BÁO CÁO TÌNH TRẠNG DỰ ÁN (PROJECT AUDIT & STATUS REPORT)

> **Dự án:** FCOnlineSquadProject  
> **Địa chỉ:** `E:\FCOnlineWorkspace\SquadProject\`  
> **Ngày lập báo cáo:** 2026-10-03  
> **Tình trạng tổng thể:** `CURRENT BASELINE = CU-CORE REAL MADRID 11/11 — 2026-10-03`  

---

## 1. 📁 BÁO CÁO DANH MỤC CÁC TỆP ĐÃ KHỞI TẠO (23 / 23 FILES)

| Nhóm chức năng | Tên file đã khởi tạo | Trạng thái | Tính toàn vẹn cú pháp |
| :--- | :--- | :---: | :---: |
| **Core & Governance** | `00_README.md` | ✅ Đã tạo | Markdown chuẩn GFM |
| | `01_PROJECT_RULES.md` | ✅ Đã tạo | Markdown chuẩn GFM |
| | `14_SOURCE_REGISTRY.csv` | ✅ Đã tạo | CSV 8 cột chuẩn RFC 4180 |
| | `17_DECISION_RULES.md` | ✅ Đã tạo | Markdown chuẩn GFM (Đã sửa Team Color) |
| | `20_PATCH_CHANGELOG.md` | ✅ Đã tạo | Markdown chuẩn GFM |
| | `21_AUDIT_LOG.md` | ✅ Đã tạo | Markdown chuẩn GFM (Cập nhật Final Audit) |
| **Squad & Tactics** | `02_CURRENT_SQUAD.json` | ✅ Đã tạo | JSON Valid 100% (Đã xóa Kim Cương, chuẩn hóa Mạ Vàng) |
| | `03_CURRENT_TACTICS.json` | ✅ Đã tạo | JSON Valid 100% |
| | `04_PLAYER_CONFIGS.json` | ✅ Đã tạo | JSON Valid 100% |
| | `05_PLAYER_CARDS_MASTER.csv` | ✅ Đã tạo | CSV 14 cột chuẩn |
| | `06_ROLE_PROFILES.json` | ✅ Đã tạo | JSON Valid 100% |
| | `22_SYSTEM_SYNERGY.md` | ✅ Đã tạo | Markdown chuẩn GFM |
| **Trait Engine** | `07_NORMAL_TRAITS_VI.json` | ✅ Đã tạo | JSON Valid 100% (Strict Provenance, 23/23 tên verified) |
| | `08_SKILL_COACHES_VI.json` | ✅ Đã tạo | JSON Valid 100% (38/41 full names verified, 3 needs verify) |
| | `09_GOLD_TRAITS_VI.json` | ✅ Đã tạo | JSON Valid 100% (14 Outfield verified, GK pool incomplete) |
| | `10_UPGRADE_RULES.json` | ✅ Đã tạo | JSON Valid 100% (Chuẩn hóa Mạ Vàng / Bạch Kim) |
| **Team Color & Evidence** | `11_TEAM_COLOR_RULES.json` | ✅ Đã tạo | JSON Valid 100% (Chuẩn hóa Garena Official) |
| | `12_TEAM_COLOR_PLAYER_MAP.csv` | ✅ Đã tạo | CSV 8 cột chuẩn |
| | `13_MANAGER_EVIDENCE.csv` | ✅ Đã tạo | CSV 17 cột chuẩn |
| | `15_MARKET_VN.csv` | ✅ Đã tạo | CSV 11 cột chuẩn |
| | `16_CANDIDATE_POOL.csv` | ✅ Đã tạo | CSV 12 cột chuẩn |
| | `18_MATCH_TEST_LOG.csv` | ✅ Đã tạo | CSV 16 cột chuẩn |
| | `19_SCREENSHOT_INDEX.csv` | ✅ Đã tạo | CSV 8 cột chuẩn |

---

## 2. 📈 THỐNG KÊ CHI TIẾT TÌNH TRẠNG XÁC MINH (VERIFICATION STATUS)

1. **Hệ thống Chỉ số ẩn thường (Mốc +5):**
   * **23 / 23 tên tiếng Việt** đã được xác minh trực tiếp từ ảnh chụp client VN (`media_1789746723594.png`).
   * Tác dụng engine: Phân định rõ giữa xu hướng hành vi AI (AI Behavioral Tendency) và buff cơ học; hạ cờ confidence xuống `MEDIUM` do thiếu URL bài viết cụ thể cho từng trait.
2. **Hệ thống HLV Kỹ Năng (Mốc +8):**
   * **38 / 41 tên đầy đủ** đã được xác minh từ ảnh chụp client VN (`media_1789747012277.png` & `media_1789747132314.png`).
   * **3 mục chưa hoàn tất xác minh:** Mục #10 (chữ mờ `Chuyền xà` vs `Chuyền xa`), Mục #12 và #13 (bị cắt ngắn trong giao diện UI client).
   * Tác dụng số học: Garena chưa công bố công thức số học chính thức -> để `null` và `UNVERIFIED`.
3. **Hệ thống Chỉ số ẩn Vàng (Mốc +11):**
   * **14 / 14 Chỉ số ẩn vàng Outfield** đã được thu thập và xác minh tên + mô tả từ ảnh chụp client VN (`media_1789882598336.png` & `media_1789882602385.png`).
   * **GK Gold Trait Pool:** **CHƯA ĐẦY ĐỦ** (`database_complete = false`), còn thiếu ảnh chụp giao diện client cho thủ môn (Garena công bố có *GK áp đảo không chiến* và *GK bắt bài sút xa*).
4. **Quy tắc Team Color:**
   * **Team Color CLB/ĐTQG level 4:** Đã sửa thành `+3 OVR + các chỉ số thành phần đặc thù` (loại bỏ generic +4 OVR).
   * **Team Color Nâng Cấp:** Đã sửa mốc +5~+7 (+1/+2 OVR), +8~+10 Mạ Vàng (+2/+3 OVR), +11~+13 Bạch Kim (+4/+5 OVR).
   * **Đội hình hiện tại:** 11 cầu thủ >= +5 (qualified); 8 cầu thủ >= +8 (ACTIVE = +3 OVR; 3 cầu thủ +5 nhận +2 OVR từ tier +5~+7; không cộng chồng); Bạch Kim INACTIVE (1/5).

---

## 3. 🔍 CÁC MỤC CHƯA HOÀN TẤT (UNRESOLVED ITEMS & DATA GAPS)

1. **Chưa có ảnh chụp bổ sung từ client cho 3 HLV kỹ năng:**
   * Mục #10: Cần ảnh chụp rõ nét để phân định `Cải thiện chuyền xà` hay `Cải thiện chuyền xa`.
   * Mục #12: Cần ảnh click popup để đọc toàn bộ chuỗi ký tự bị cắt `Cải thiện khả năng rê bóng khi...`.
   * Mục #13: Cần ảnh click popup để đọc toàn bộ chuỗi ký tự bị cắt `Cải thiện khả năng sút xa tru...`.
2. **Chưa có ảnh chụp client VN cho Gold Traits của Thủ Môn (GK mốc +11):**
   * Cần mở popup chọn Gold Trait trên một thủ môn đạt mốc +11 để xác minh danh sách chính thức trong client.
3. **ĐÃ HOÀN TẤT KIỂM TOÁN 11/11 CẦU THỦ STARTING XI (100% CLIENT VERIFIED):**
   * Toàn bộ 11 cầu thủ đá chính (Havertz, Dinkci, Gerrard, McTominay, Schweinsteiger, Matić, Mendy, Desailly, Ferdinand, Koundé, Casteels) đã được đối chiếu trực tiếp qua ảnh chụp client cá nhân.
   * Giải mã triệt để tử huyệt hàng thủ: Koundé (RB) bị gắn `Xoạc bóng` (tự ý trượt xoạc lố đà bỏ vị trí) và McTominay (RCM) bị gắn `Tinh tế` (vô dụng tranh chấp Zone 14). Đã có phương án khắc phục dứt điểm.

---

## 4. 🏁 KẾT LUẬN KIỂM TOÁN
Dự án được phân loại ở trạng thái:
`BASELINE_VERIFIED_11_PLAYERS / OUTFIELD_POOL_AUDITED`
* 11/11 cầu thủ xuất phát đã có bằng chứng client chính xác tuyệt đối.
* Cơ sở dữ liệu thẻ (`05_PLAYER_CARDS_MASTER.csv`) và cấu hình thực tế (`04_PLAYER_CONFIGS.json`) đã khớp 100% với client game.

---

## 5. 🚀 CẬP NHẬT TIẾN ĐỘ & BƯỚC NGOẶT CHIẾN LƯỢC (MILESTONE 2026-09-29)

### A. Tình trạng nhân sự thực tế:
* **Đã chiêu mộ thành công:** Luka Modrić CU +8 (LCM thay Gerrard UT +8) và Dani Carvajal CU +8 (RB thay Koundé FAC +5).
* **Định hình bộ khung Real/CU (7/11):** Havertz CU +8, Bellingham CU +8, Modrić CU +8, Valverde CU +8, Vini Jr. CU +8, Mendy CU +8, Carvajal CU +8.
* **Tchouaméni CU +8:** Khóa vai trò CDM chuyển tiếp khi cần kích mốc CU; build trait theo Casemiro.

### B. Giải mã triết lý Trait & HLV từ Acc Top:
* **Slot +5 (Thẻ Bạc):** 10/10 cầu thủ chạy ngoài sân lấy `Nỗ lực đến cùng` (chấm dứt triệt để tụt thể lực phút 70+ trong GLXH). Thủ môn Casteels lấy `TM đối mặt`.
* **Slot +8 (HLV Mạ Vàng):** Phân hóa nhiệm vụ theo đúng vai trò tuyến:
  * MF (Bellingham, Modrić, Valverde, Vini): `Tấn công với nhịp độ nhanh`.
  * CDM (Tchouaméni / Casemiro): `Chiến thuật chuyền Tiki-Taka`.
  * CAM (Havertz): `Tạo cơ hội ghi bàn` (mô phỏng vai Benzema).
  * FB (Mendy, Carvajal): `Áp đảo toàn sân`.
  * CB (Ferdinand): `Cự ly đội hình ổn định`.

### C. Cơ chế Club House & Chiến lược tiêu TC:
* **Đào tạo cá nhân:** Khả năng 5/5 là chọn tối đa 5 chỉ số (mỗi chỉ số 0/2 -> 2/2). Ưu tiên tiêu TC cho Core Real: Modrić ➔ Valverde ➔ Bellingham ➔ Vini ➔ Carvajal ➔ Mendy ➔ Tchouaméni. Không tiêu TC vào nhóm tạm bợ (Havertz, Matić, Desailly, Ferdinand, Koundé, Casteels).
* **Tập luyện chiến thuật:** Bỏ qua Lv2 ("Thay thế" vô dụng trong GLXH); ưu tiên Tiền vệ Lv1 ➔ Lv3 (Mục tiêu Lv3: `Chuyền thành công → Lực sút +3, Quyết đoán +2`).

### D. Roadmap chuyển nhượng tiếp theo:
`Éder Militão CU +8 ➔ K. Benzema BLD +8 ➔ Casemiro CU +8 ➔ A. Rüdiger CU +8 ➔ D. Alaba / Kepa`.
* Kỷ luật: Không tiêu BP hay TC ngoài roadmap.

---

## 6. 🌐 TÍCH HỢP HỆ SINH THÁI FC INFO VÀO WORKFLOW (MILESTONE 2026-09-30)

* **Nguồn dữ liệu mới:** Đã bổ sung `SRC_11` (FC INFO Structured Data qua NEXON Open API) và `SRC_12` (FC INFO Manager Mode Board) vào `14_SOURCE_REGISTRY.csv`.
* **Xác thực toàn diện Tactic 4-1-4-1-0:** Báo cáo thực chứng 1.000 trận GLXH Hàn Quốc trên FC INFO (Win rate 51% ➔ 54.8%) xác nhận 100% logic tactic của dự án:
  * `Players in Box = 1` ngăn 2 CM/CDM cùng ùa vào box gây hở sườn phản công.
  * Phân quyền xâm nhập vòng cấm thông qua thiết lập cá nhân: CAM/LM/RM (`SC1`) + 2 CM (`AS2`).
  * Thứ tự ưu tiên sức mạnh: `CAM > CM > Winger`.
* **Tiêu chí Scout mới:** Trục giữa (`CAM ➔ CM ➔ CDM ➔ CB`) bắt buộc phải có thể hình và chỉ số **Quyết đoán (적극성 / Aggression)** cao để đảm bảo AI thực sự thò chân tắc bóng (tackle) thay vì chỉ chạy áp sát lấy lệ.
* **Xác thực triết lý Trait:** Khẳng định trait thể lực tự động ("Hai trái tim" / `Nỗ lực đến cùng`) là chuẩn mực meta tối thượng trong môi trường AI tự đá.

---

## 7. 💡 BƯỚC NGOẶT TIẾP CẬN MONEYBALL & GIẢI MÃ KHẮC CHẾ (MILESTONE 2026-09-30 #2)

* **Thiết lập Framework Moneyball 100 Điểm (`19_MONEYBALL_FRAMEWORK.md` & `RULE_MONEYBALL_01`):**
  * Chuyển hẳn từ tư duy "Săn mùa mới/OVR cao" sang "Săn exact-card tối ưu hóa hiệu suất AI trên mỗi BP/Lương".
  * Thang điểm 100: `Role Fit đúng tactic (30đ)` + `Trait Fit (20đ)` + `Physical & Work Profile (15đ)` + `Ranker Usage & Win Evidence (15đ)` + `Salary Efficiency (10đ)` + `Giá +8/+9 (10đ)`.
  * Điều kiện công nhận "CU Killer": $\ge 80/100$, không có fatal flaw, win rate không giảm sau bài test tối thiểu 100 trận in-game.
* **Ma trận Đánh đổi Vị trí (Trade-off Matrix) trong 4-1-4-1-0:**
  * `CAM`: Ưu tiên Finish + Positioning + Link-up + Thể hình; hy sinh raw pace.
  * `LM/RM`: Ưu tiên Pace/Accel + Dribble + Positioning + Stamina + Cutback; hy sinh chỉ số thủ.
  * `LCM/RCM`: Ưu tiên Pass + Stamina + Shot Power/Long Shot + Aggression + Đủ thủ (105+); hy sinh stat đơn lẻ cực đại.
  * `CDM`: Ưu tiên Interception + Aggression + Physical + Pass an toàn; hy sinh OVR/kỹ thuật tấn công.
  * `CB`: Ưu tiên thể hình $\ge 190\text{cm}$, Pace + Strength + Interception; hy sinh chuyền hoa mỹ.
  * `LB/RB`: Ưu tiên Pace + Stamina + Defense + Lương thấp; hy sinh attack.
  * `GK`: Ưu tiên save profile thực chiến; hy sinh Team Color nếu bắt ngáo.
* **Giải mã Tử huyệt 4-1-4-1-0 & Tactic Khắc tinh:**
  * Tử huyệt: Lone CDM (1 mỏ neo đơn độc) và Zero-Top (dễ bị bế tắc khi đối thủ dùng 5 hậu vệ hoặc 2 CDM).
  * Khắc tinh hàng đầu: `4-2-2-2 Counter` (2 CDM bóp nghẹt trung lộ, 2 ST phản công trực diện khoét sau lưng 1 CDM) và `5-2-3 / 5-2-1-2` (khóa chết box, phản công nách biên).
* **Định vị Archetype Cần Săn:**
  * CAM: Havertz / Cantona / Gullit Type.
  * Wing: Vini Type (phá tuyến/cutback).
  * CM: Valverde Type (Hexagonal box-to-box).
  * CB: Militão / Rüdiger Type (tốc độ + càn lướt).
  * Budget Anomaly: 25DP, WG, FAC, WS, PTG.

---

## 8. 🛡️ CHIÊU MỘ ÉDER MILITÃO CU +8 & ĐIỀU CHỈNH ROADMAP (MILESTONE 2026-09-30 #3)

* **Chiêu mộ thành công:** **Éder Militão CU +8** chính thức vào **LCB đá chính thay Desailly WG +5**.
* **Trạng thái Đội hình Thực tế (Starting XI):**
  * `Havertz CU +8 (CAM) — Bellingham CU +8 (LM) — Vini CU +8 (RM) — Modrić CU +8 (LCM) — Valverde CU +8 (RCM) — Tchouaméni CU +8 (CDM) — Mendy CU +8 (LB) — Éder Militão CU +8 (LCB) — Ferdinand DC +9 (RCB) — Carvajal CU +8 (RB) — Casteels 23HW +9 (GK)`.
* **Cột mốc Đạt được:**
  * **9/11 Cầu thủ CU đá chính:** Kích hoạt vững chắc mốc Team Color CU 8 người (dư 1 slot, an toàn tuyệt đối).
  * **8/11 Cầu thủ Real Madrid:** Đạt mốc kích hoạt Team Color Real Madrid.
  * **11/11 Mạ Vàng (>= +8):** Toàn bộ đội hình xuất phát đều hưởng buff Team Color Mạ Vàng (+3 OVR).
* **Cấu hình Đã Chốt cho Éder Militão CU +8 (Chuẩn Acc Top):**
  * **Slot +5:** `Nỗ lực đến cùng` (2개의 심장).
  * **Slot +8:** `Cự ly đội hình ổn định`.
  * **Chiến thuật đơn:** `IN thường` (Normal Interceptions — giữ cự ly, không lao ra dập ẩu), Công/Thủ `1/3`.
* **Logic Cặp Trung Vệ Hiện Tại:**
  * `Militão CU +8` (Tốc độ + Khả năng bọc lót recovery + Giữ line cự ly) $\leftrightarrow$ `Ferdinand DC +9` (Bọc lót sâu cover + Không chiến 189cm + AI kinh nghiệm).
  * Bác bỏ việc vội vàng thay Ferdinand bằng Rüdiger để làm đẹp đội; tập trung kiểm chứng cặp Militão - Ferdinand trước.
* **Tái Cấu Trúc Roadmap Chuyển Nhượng Theo Chuẩn Moneyball:**
  1. 🥇 **Karim Benzema BLD +8 ➔ thay Havertz CU** (CAM là vị trí quyết định bàn thắng số 1 trong 4-1-4-1-0).
  2. 🥈 **Kepa CU +9 ➔ thay Casteels** (Nâng cấp save rate GK + củng cố mốc CU).
  3. 🥉 **Casemiro CU +8 ➔ thay Tchouaméni** (Trục CDM vững chắc).
  4. ④ **Antonio Rüdiger CU +8 ➔ thay Ferdinand** (Chỉ thực hiện sau khi đánh giá dữ liệu cặp CB).
  5. ⑤ **David Alaba CU +8 ➔ thay Mendy** (Hậu vệ biên ưu tiên thấp nhất).

---

## 9. 🔒 KỶ LUẬT XÁC MINH DỮ LIỆU CỐT LÕI (RULE_DATA_01 MANDATE)

* **Bài học trực tiếp:** Trường hợp nhầm lẫn *"Harry Kane CU"* là hồi chuông cảnh tỉnh nghiêm trọng về việc suy đoán chủ quan. Kane chưa từng vô địch Champions League nên theo quy chế Nexon/Garena, anh không thể có thẻ mùa Champions of Europe (CU).
* **Quy chuẩn bắt buộc từ nay trở đi:**
  * **TUYỆT ĐỐI KHÔNG SUY ĐOÁN MÙA THẺ.** Trước khi đưa ra bất kỳ cái tên, chỉ số hay mùa thẻ nào, BẮT BUỘC phải chạy công cụ tra cứu trực tiếp qua FC INFO (`fc-info.com/player/search`) hoặc FIFAAddict để xác nhận 100% thẻ có tồn tại trong game.
* **Hệ thống phân tầng nguồn tin chuẩn hóa:**
  * `Tier A (Official Garena / NEXON):` Nguồn tối thượng cho thể thức, cơ chế và quy định patch.
  * `Tier C (In-game Client Screenshots):` Ground Truth tuyệt đối về đội hình và tài nguyên thực tế của người dùng.
  * `Tier E (FC INFO Structured Data qua NEXON Open API):` Tra cứu exact-card, filter đa chiều (work rate, thể hình, chân yếu, OVR, lương, market price).
  * `Tier D (FC INFO Manager Mode Board):` Review thực chiến, meta GLXH chuyên sâu (ưu tiên bài viết có mẫu thử 500–1.000+ trận).
  * `Tier E (FIFAAddict):` Đối chiếu chéo raw stats và chỉ số ẩn.
  * `Tier B (Inven):` Tham khảo meta và góc nhìn cộng đồng Hàn Quốc bổ trợ.





