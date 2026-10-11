# 🔬 PHÂN TÍCH SÂU FCONLINE-COACH-AGENT & ĐỐI CHIẾU KIẾN TRÚC FCONLINEWORKSPACE

> **Mã tài liệu:** DEEPDIVE-COACH-AGENT-20261011  
> **Nguồn phân tích:** [hskimim/fconline-coach-agent](https://github.com/hskimim/fconline-coach-agent)  
> **Người thực hiện:** Antigravity  
> **Mục tiêu:** Bóc tách kiến trúc, prompt, và luật kiểm chứng (verifier) để thiết kế module kiểm định chiến thuật cho dự án FCOnlineWorkspace.

---

## 1. 🏗️ SƠ ĐỒ LUỒNG KIẾN TRÚC TỔNG THỂ (ARCHITECTURE FLOW)

Dưới đây là luồng xử lý của hệ thống conline-coach-agent:

`	ext
[Người dùng nhập yêu cầu / Voice Query]
                    │
                    ▼
          [1. Input Verifier] ──(False: Chửi bậy, hỏi về Nexon, phi bóng đá)──► [Báo lỗi / Dừng]
                    │ (True)
                    ▼
          [2. Intent Router] 
                    ├──► "DEFAULT" / "not-allowed" ──────► [Casual Chat / Từ chối]
                    │
                    ├──► "team_tactic" ──► [Team Tactic Updater]
                    │                             │
                    │                             ▼
                    │                   [Team Tactic JSON Verifier]
                    │                             │
                    │                             ├── (Fail) ──► [Retry loop: tol <= 5]
                    │                             └── (Pass) ──► [Trả kết quả JSON + Thuyết minh]
                    │
                    └──► "indiv_tactic" ─► [Indiv Tactic Updater]
                                                  │
                                                  ▼
                                        [Indiv Tactic JSON Verifier]
                                                  │
                                                  ├── (Fail) ──► [Retry loop: tol <= 5]
                                                  └── (Pass) ──► [Trả kết quả JSON + Thuyết minh]
`

### Đặc điểm cốt lõi của kiến trúc:
1. **Phân tách rạch ròi 2 cấp độ:** Chiến thuật đội (	eam_tactic) và Chiến thuật cá nhân (indiv_tactic) được xử lý bởi 2 Agent và 2 Verifier hoàn toàn tách biệt.
2. **Cơ chế Retry có kiểm soát (	ol = 5):** Khi LLM sinh JSON sai cú pháp, vượt ngoài dải 1–10 hoặc chọn giá trị enum không tồn tại, Verifier từ chối và kích hoạt gọi lại LLM tối đa 5 lần với 	emperature = 0.0.
3. **Guardrail phòng thủ 2 lớp:**
   * Lớp 1: Lọc ý định và an toàn ngữ nghĩa qua Prompt (input_verifier_prompt).
   * Lớp 2: Kiểm định cấu trúc dữ liệu xác định (Deterministic JSON Verifier) qua hàm Python thuần (	eam_tactic_json_verifier, indiv_tactic_json_verifier).

---

## 2. 📋 BẢNG ĐỐI CHIẾU KEY CHIẾN THUẬT (KR ➔ EN ➔ VN GARENA)

### A. CHIẾN THUẬT ĐỘI (TEAM TACTICS)

| Nhóm Tactic | Key Tiếng Hàn (Nexon KR) | Tên Tiếng Anh (FIFA/FC) | Thuật ngữ Client Garena VN | Dải giá trị / Danh mục hợp lệ | Ghi chú & Đánh giá |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Đội hình** | 포메이션 | Formation | Sơ đồ thi đấu | 4-3-3, 4-2-3-1, 4-1-4-1... | Danh mục 30+ sơ đồ chuẩn Nexon |
| **Phòng thủ** | 수비 스타일 | Defensive Style | Phong cách phòng thủ | • 후퇴 ➔ Lùi sâu (Drop Back)<br>• 밸런스 ➔ Cân bằng (Balanced)<br>• 볼 터치 실수 시 압박 ➔ Gây áp lực khi đỡ bóng hỏng (Press After Heavy Touch)<br>• 공 뺏긴 직후 압박 ➔ Gây áp lực sau khi mất bóng (Press After Possession Loss)<br>• 지속적인 압박 ➔ Cùng nhau gây áp lực / Áp lực liên tục (Constant Pressure) | 5 phong cách phòng thủ chuẩn game |
| **Xây dựng lối chơi** | 빌드업 플레이 | Build Up Play | Lối chơi tấn công | • 느린 빌드업 ➔ Xây dựng chậm (Slow Build Up)<br>• 밸런스 ➔ Cân bằng (Balanced)<br>• 긴 패스 ➔ Chuyền dài (Long Ball)<br>• 빠른 빌드업 ➔ Chuyển trạng thái nhanh / Xây dựng nhanh (Fast Build Up) | 4 phong cách triển khai bóng |
| **Vị trí phòng thủ** | 수비 포지셔닝: 폭 | Defensive Width | Cự ly phòng thủ: Rộng | 1 – 10 (Integer) | [1-3: Bó hẹp trung lộ, 4-7: Cân bằng, 8-10: Dàn biên] |
| **Vị trí phòng thủ** | 수비 포지셔닝: 깊이 | Defensive Depth | Cự ly phòng thủ: Thấp/Sâu | 1 – 10 (Integer) | [1-3: Tử thủ lùi sâu, 4-7: Cân bằng V3, 8-10: Dâng cao tự sát] |
| **Tấn công** | 공격 포지셔닝: 폭 | Attacking Width | Cự ly tấn công: Rộng | 1 – 10 (Integer) | Độ giãn biên khi mở bóng |
| **Tấn công** | 공격 포지셔닝: 박스 안 쪽 선수 | Players in Box | Cầu thủ trong vòng cấm | 1 – 10 (Integer) | Số lượng người xâm nhập box khi tạt |
| **Cố định** | 공격 포지셔닝: 코너킥 | Corners | Phạt góc | 1 – 10 (Thực tế client VN: 1 – 5) | [CẦN XÁC MINH]: Repo cho phép 1-10 nhưng Client game chỉ có thang 1-5 vạch |
| **Cố định** | 공격 포지셔닝: 프리킥 | Free Kicks | Đá phạt | 1 – 10 (Thực tế client VN: 1 – 5) | [CẦN XÁC MINH]: Tương tự phạt góc, client VN chỉ hiển thị tối đa 5 vạch |

---

### B. CHIẾN THUẬT CÁ NHÂN (INDIVIDUAL TACTICS)

| Category Key (Repo) | Vị trí áp dụng | Mã UI dự án VN | Các giá trị cho phép (English) | Thuật ngữ Tiếng Việt Garena tương ứng |
| :--- | :--- | :--- | :--- | :--- |
| Defensive Support | CAM, RM, RW, LM, LW, ST... | DS | • Come Back on Defence<br>• Basic Defence Support<br>• Stay Forward | • DS1: Hỗ trợ phòng ngự<br>• DS: Cơ bản / Cân bằng<br>• DS2: Ở lại phía trên |
| Interceptions | Toàn bộ Outfield (LS..RB) | IN | • Aggressive Interceptions<br>• Normal Interceptions<br>• Conservative Interceptions | • IN1: Đánh chặn chủ động / Hổ báo<br>• IN: Đánh chặn bình thường<br>• IN2: Đánh chặn thận trọng / Giữ sức |
| Position Freedom | CDM, CM, CAM | PF | • Free Roam (Trừ CDM)<br>• Stick to Position<br>• Drift Wide<br>• Deep Lying Playmaker (Chỉ CDM) | • PF1: Di chuyển tự do<br>• PF: Giữ vị trí / Kỷ luật<br>• PF2: Dạt biên<br>• PF3: Mỏ neo kiến thiết (Chỉ CDM) |
| Support on Crosses | CM, CAM, RM, RW, LM, LW | SC | • Get Into The Box For Cross<br>• Balanced Crossing Runs<br>• Stay On Edge Of Box For Cross | • SC1: Xâm nhập vòng cấm khi tạt bóng<br>• SC: Chạy chỗ cân bằng<br>• SC2: Chờ ở rìa vòng cấm nã đại bác |
| Support Runs (Strikers) | CF, ST | SR | • Drift Wide<br>• Balanced Width<br>• Stay Central | • SR1: Dạt cánh<br>• SR: Cân bằng<br>• SR2: Giữ trung lộ |
| Support Runs (Wings) | RM, RW, LM, LW, RF, LF | SR | • Get In Behind<br>• Balanced Support<br>• Come Short<br>• Target Man | • SR1: Xẻ nách / Chạy sau lưng<br>• SR: Cân bằng<br>• SR2: Xin bóng ngắn<br>• SR3: Làm tường nhận bóng |
| Attacking Runs (Strikers)| RF, LF, CF, ST | AR | • Get In Behind<br>• Mixed Attack<br>• Target Player<br>• False 9 | • AR1: Bứt tốc vượt tuyến<br>• AR: Tấn công hỗn hợp<br>• AR2: Mục tiêu làm tường<br>• AR3: Tiền đạo ảo (False 9) |
| Attacking Runs (Fullbacks)| RB, RWB, LB, LWB | AR | • Join the Attack<br>• Balanced Attack<br>• Stay Back While Attacking | • AR1: Tham gia tấn công / Overlap<br>• AR: Tấn công cân bằng<br>• AR2: Ở lại phía sau khi tấn công |
| Attacking Support (CM/CDM)| CDM, CM | AS | • Stay Back While Attacking<br>• Balanced Attack<br>• Get Forward | • AS1: Ở lại phía sau khi tấn công<br>• AS: Tấn công cân bằng<br>• AS2: Dâng cao hỗ trợ tấn công (Box-to-Box) |
| Attacking Support (CB) | CB | AS | • Join the Attack<br>• Stay Back While Attacking<br>• Play As Striker | • AS1: Tham gia tấn công khi cần<br>• AS: Ở lại phía sau (Mặc định)<br>• AS2: Lên làm tiền đạo phút bù giờ |
| Chance Creation | RM, RW, LM, LW | CC | • Cut Inside<br>• Balanced Width<br>• Stay Wide<br>• Free Roam | • CC2: Cắt vào trong / Đột phá nách<br>• CC: Rộng cân bằng<br>• CC1: Bám biên tạt bóng<br>• CC3: Tự do sáng tạo |
| Defensive Behaviour | CDM | DB | • Cut Passing Lanes<br>• Balanced Defence<br>• Tight Mark | • DB1: Cắt đường chuyền (Interception Line)<br>• DB: Phòng ngự cân bằng<br>• DB2: Kèm chặt áp sát (Man-marking) |
| Defensive Position (CM) | CDM, CM | DP | • Cover Center<br>• Cover Wing | • DP1: Tập trung trung lộ<br>• DP2: Bọc lót dạt cánh |
| Defensive Position (Backs)| RB, CB, LB... | DP | • Step Up<br>• Stick to Position | • DP1: Chủ động áp sát dập bước 1 (Stopper)<br>• DP: Giữ nguyên cự ly hàng thủ (Cover) |

---

## 3. 🧩 BẢNG PHÂN TÍCH HỆ THỐNG PROMPTS

| Tên File Prompt | Vai trò & Mục đích | Cấu trúc Input | Ràng buộc Output | Kỹ thuật nổi bật |
| :--- | :--- | :--- | :--- | :--- |
| erifier.py (input_verifier_prompt) | Kiểm duyệt an toàn đầu vào (Safety Guardrail). | {question} | Bắt buộc đúng 1 token: True hoặc False. Không giải thích. | Prompt phòng thủ nghiêm ngặt: cấm câu hỏi về Nexon, cấm chửi bậy, cấm tên người phi bóng đá. |
| outer.py (prompt & multi_prompt) | Phân loại ý định người dùng (Intent Routing). | {input}, {candidate_prompts} | Markdown code block ``json {"destination": "...", "next_inputs": "..."} `` | Hỗ trợ tinh chỉnh lại câu prompt (
ext_inputs) bằng tiếng Hàn chuẩn trước khi chuyển tiếp. |
| updater.py (persona_prefix, suffix) | Điều chỉnh chiến thuật đội (Team Tactic Tuning). | {current_tactic}, {query}, {tactic_components} | ``json [...] `` + Đoạn giải thích lý do chiến thuật (30–50 từ). | Áp dụng nguyên tắc **Minimal Change**: *"Chỉ điều chỉnh đúng thông số cần thiết, không thay đổi toàn bộ"* (khớp với triết lý A/B Test của ta). |
| indiv_updater.py | Điều chỉnh chiến thuật cá nhân từng cầu thủ. | {query}, {formation}, {selected_positions}, {data} | List JSON: [{"formation": "ST", "key": "Interceptions", "value": "Aggressive Interceptions"}] | Bắt buộc kiểm tra ràng buộc vị trí (Target Positions), không cho gán bừa chỉ thị ngoài danh mục. |
| casual.py | Phản hồi trò chuyện tự nhiên thân thiện. | {input} | Văn bản hội thoại thông thường mang phong cách HLV bóng đá. | Giữ persona chuyên gia bóng đá ấm áp, lịch sự. |
| parser.py | Chuẩn hóa giọng nói/text đầu vào. | {input} | Văn bản câu hỏi làm sạch. | Dọn dẹp câu chữ từ audio whisper. |

---

## 4. 💡 BÀI HỌC ÁP DỤNG & GIỚI HẠN SO VỚI DỰ ÁN FCONLINEWORKSPACE

### ✅ BÀI HỌC ÁP DỤNG ĐƯỢC:
1. **Kiến trúc Kiểm định Xác định (Deterministic Verifier):** 
   * Không bao giờ tin tưởng output thô của LLM. Mọi đề xuất chiến thuật bắt buộc phải đi qua một hàm parser & verifier bằng code Python thuần để kiểm tra ranh giới dữ liệu trước khi lưu vào  3_CURRENT_TACTICS.json.
2. **Cơ chế Retry Loop với 	emperature = 0.0:** 
   * Nếu đề xuất vi phạm luật, agent phải nhận phản hồi lỗi từ verifier và tự sửa lại (tối đa 3-5 lần), không để lộ lỗi cú pháp ra cho người dùng.
3. **Ràng buộc Vị trí Khắt khe (Target Position Mapping):** 
   * Bảng danh mục indiv_tactic_dict chỉ ra chính xác vị trí nào được phép nhận chỉ thị nào (ví dụ: Fullback không thể có chỉ thị Cut Inside, Center Back không thể có chỉ thị Drift Wide).

---

### ❌ NHỮNG ĐIỂM REPO GỐC CÒN THIẾU (CẦN TỰ XÂY DỰNG TRONG DỰ ÁN TA):
1. **Hoàn toàn thiếu Luật Cộng Hưởng Hàng Thủ (Stopper & Cover Matrix):**
   * Repo gốc coi 2 CB là giống hệt nhau (LCB = RCB = CB). Nó không hề biết luật bất thành văn của GLXH: Một trung vệ bắt buộc phải là **Stopper** (dập, áp sát) và một trung vệ phải là **Cover** (bọc lót tốc độ).
2. **Không kiểm tra Xung đột Vai trò Nội tại (Role Conflict):**
   * Repo gốc không chặn việc gắn AS1 (Ở lại phía sau) cho một Tiền vệ trung tâm giữ nhịp như Bellingham, hay thả rông tự do PF1 cho một mỏ neo duy nhất như Casemiro (điều mà dự án ta đã mất nhiều trận test để sửa).
3. **Không tích hợp Ma trận HLV 4 Tầng & Luật Anti-Overlap:**
   * Repo gốc chỉ quản lý tactic in-game cơ bản. Nó không hề biết đến hệ thống **HLV Tập luyện 3 sao + HLV Kỹ năng +8** và luật Nexon cấm trùng kỹ năng.
4. **Không neo vào Dữ liệu Thực nghiệm (Lack of Evidence Grounding):**
   * Mọi gợi ý của repo gốc chỉ dựa vào tri thức lý thuyết bóng đá của GPT-4, không hề đối chiếu với tỷ lệ thắng/thua thực tế (Win Rate) từ các bản log trận đấu (18_MATCH_TEST_LOG.csv) hay dữ liệu Meta Ranker Garena.

---
*Báo cáo được khởi tạo tự động và đồng bộ trực tiếp lên hệ thống Cloud GitHub.*