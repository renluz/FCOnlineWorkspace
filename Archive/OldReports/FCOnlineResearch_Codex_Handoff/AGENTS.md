# AGENTS.md — FCOnlineResearch

## Mục tiêu dự án
Tối ưu FC Online Việt Nam cho **Giả Lập Xếp Hạng (GLXH / Manager Mode)** dựa trên:
1. patch hiện tại,
2. AI của **đúng card + đúng mùa**,
3. role fit / formation fit,
4. dữ liệu account thực,
5. evidence có nguồn.

Mục tiêu chiến thuật: xây đội hình có thể tạo **upset** trước đội mạnh hơn bằng cấu trúc, AI positioning, role fit và hiệu quả salary — không chạy theo OVR đơn thuần.

## Bắt buộc đọc trước khi sửa
Đọc theo thứ tự:
1. `docs/codex/CURRENT_STATE.md`
2. `docs/codex/RESEARCH_RULES.md`
3. `docs/codex/TACTIC_VALIDITY.md`
4. `docs/codex/NEXT_TASKS.md`
5. Các knowledge-base hiện có trong repo nếu tồn tại:
   - `FC_ONLINE_GLXH_KNOWLEDGE.md`
   - `CURRENT_SQUAD_KNOWLEDGE_APPLICATION.md`
   - `KNOWLEDGE_GAPS.md`
   - `knowledge/DECISION_RULES.md`
   - `knowledge/CONTRADICTIONS.md`
   - `RESEARCH_INDEX.csv`

## Quy tắc độ tin cậy
- Không biến suy luận thành fact.
- Không suy từ **tên cầu thủ** sang mọi season. Đơn vị đánh giá là **player + season + enhancement + position + patch**.
- Không chọn cầu thủ chỉ vì OVR/stat đẹp.
- Giá Hàn/KR chỉ tham khảo; quyết định mua dùng **TTCN Garena VN live** hoặc dữ liệu local VN đã xác minh.
- Cầu thủ/card chỉ được coi là `VN_AVAILABLE` khi có bằng chứng tồn tại trên Garena VN/TTCN VN.
- Nếu không biết: ghi `UNKNOWN`.
- Nếu chỉ là cộng đồng: `COMMUNITY_OBSERVATION`.
- Nếu là suy luận: `MODEL_INFERENCE`.

## An toàn / phạm vi kỹ thuật
Được phép:
- đọc file/log/config local,
- UI Automation / Win32 **read-only**,
- phân tích screenshot/video local do user cung cấp,
- public web/API/documentation,
- thống kê CSV/SQLite.

Không làm:
- đọc memory game,
- inject/hook DLL,
- packet sniff,
- bypass anti-cheat,
- anti-ban/evasion,
- sửa process/game client để gian lận,
- dàn xếp/chuyển BP giữa account bằng TTCN.

## Ngôn ngữ
- Báo cáo cho user: tiếng Việt.
- Tên file / schema / code: ưu tiên English rõ nghĩa.
- Giữ nguyên mã tactic UI như `AS`, `DB1`, `DP1`, `IN`, `DS`, `PF`, `SC`, `AR`, `SR`.

## Nguyên tắc thay đổi
Trước khi sửa knowledge base:
1. audit source,
2. nêu claim nào được thay,
3. ghi provenance,
4. không xóa lịch sử mâu thuẫn,
5. chạy validator nếu có.

Accuracy > completeness.
