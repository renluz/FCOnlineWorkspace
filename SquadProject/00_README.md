# ⚽ FCOnlineSquadProject: Persistent Knowledge Base & Squad Decision Engine

> **Máy chủ:** Garena FC Online Việt Nam  
> **Phiên bản tri thức:** 1.0.0 (Tháng 09/2026 - Gameplay 12th / Cập nhật mùa hè 2026)  
> **Chế độ trọng tâm:** Giả Lập Xếp Hạng (GLXH / Manager Mode)  
> **Sơ đồ vận hành baseline:** `4-1-4-1-0 / Zero-ST`  
> **Vị trí lưu trữ:** `E:\FCOnlineWorkspace\SquadProject\`

---

## 1. 🎯 Mục Đích Dự Án
Dự án **FCOnlineSquadProject** được xây dựng nhằm tạo ra một **Cơ sở tri thức phân tán, bền vững (Decentralized Project Memory)** phục vụ lâu dài cho AI Assistant (ChatGPT, Gemini, Claude) và huấn luyện viên:
1. **Không sửa file game:** Chỉ lưu trữ tri thức phân tích, nghiên cứu, cấu hình và lịch sử thực nghiệm.
2. **Loại bỏ hiện tượng ảo giác (Hallucination):** Dữ liệu được xác thực nghiêm ngặt theo phân cấp nguồn (Tier A đến Tier G).
3. **Chống trùng lặp & nhầm lẫn:** Phân biệt tuyệt đối theo nguyên tắc **Exact-Card** (Tên + Mùa thẻ + Mức cộng).
4. **Tối ưu hóa kinh tế (BP Efficiency):** Xây dựng chiến lược đầu tư tích lũy BP dài hạn, từ chối các nâng cấp hào nhoáng nhưng không mang lại hiệu quả AI trong GLXH.

---

## 2. 🗺️ Bản Đồ Cấu Trúc Dự Án (23 Files Core)

| Tệp tin | Định dạng | Chức năng chính |
| :--- | :---: | :--- |
| `00_README.md` | Markdown | Tổng quan kiến trúc dự án và chỉ dẫn truy xuất tri thức. |
| `01_PROJECT_RULES.md` | Markdown | Toàn bộ quy chuẩn kỹ thuật, bảo vệ dữ liệu gốc và chính sách nghiêm ngặt. |
| `02_CURRENT_SQUAD.json` | JSON | Đội hình chính thức 11 cầu thủ (Starting XI) và phân bổ cấp độ thẻ. |
| `03_CURRENT_TACTICS.json` | JSON | Thiết lập Chiến thuật đội và Chiến thuật đơn sơ đồ 4-1-4-1-0. |
| `04_PLAYER_CONFIGS.json` | JSON | Cấu hình chuyên sâu từng cầu thủ: Archetype, Trait gốc, Trait trang bị (+5, +8, +11). |
| `05_PLAYER_CARDS_MASTER.csv` | CSV | Sổ bộ danh mục toàn bộ thẻ cầu thủ master với chỉ số và thuộc tính thể hình. |
| `06_ROLE_PROFILES.json` | JSON | Đặc tả 11 vai trò chiến thuật: Nhiệm vụ, hành vi mong muốn và hành vi cấm kỵ. |
| `07_NORMAL_TRAITS_VI.json` | JSON | Bảng danh mục **23 Chỉ số ẩn thường** (Mốc +5) xác minh từ client VN. |
| `08_SKILL_COACHES_VI.json` | JSON | Bảng danh mục **41 HLV kỹ năng** (Mốc +8) xác minh từ client VN. |
| `09_GOLD_TRAITS_VI.json` | JSON | Bảng danh mục **14 Chỉ số ẩn vàng** (Mốc +11) xác minh từ client VN. |
| `10_UPGRADE_RULES.json` | JSON | Cơ chế mở khóa mốc thẻ, sơ đồ 3 slot UI và quy tắc thẻ đặc biệt. |
| `11_TEAM_COLOR_RULES.json` | JSON | Quy tắc cộng chỉ số Team Color Quốc gia, CLB và Team Color Nâng cấp. |
| `12_TEAM_COLOR_PLAYER_MAP.csv` | CSV | Bản đồ liên kết cầu thủ với các Team Color hợp lệ (Đức, Pháp, MU, Chelsea...). |
| `13_MANAGER_EVIDENCE.csv` | CSV | Kho dữ liệu thực nghiệm thi đấu GLXH được phân cấp độ tin cậy từ A+ đến E. |
| `14_SOURCE_REGISTRY.csv` | CSV | Sổ bộ phân cấp nguồn tin (Tier A đến Tier G). |
| `15_MARKET_VN.csv` | CSV | Lịch sử giá giao dịch thị trường chuyển nhượng Garena Việt Nam. |
| `16_CANDIDATE_POOL.csv` | CSV | Danh sách trinh sát cầu thủ tiềm năng / phương án dự phòng. |
| `17_DECISION_RULES.md` | Markdown | Bộ luật logic IF/THEN/PENALTY/BONUS cho mua bán và ghép cặp cầu thủ. |
| `18_MATCH_TEST_LOG.csv` | CSV | Nhật ký A/B testing hiệu năng trận đấu giả lập. |
| `19_SCREENSHOT_INDEX.csv` | CSV | Sổ mục lục định danh và trích xuất thông tin ảnh chụp màn hình client. |
| `20_PATCH_CHANGELOG.md` | Markdown | Lịch sử thay đổi cơ chế gameplay qua các bản cập nhật. |
| `21_AUDIT_LOG.md` | Markdown | Nhật ký kiểm toán tri thức và rà soát tính toàn vẹn dữ liệu. |
| `22_SYSTEM_SYNERGY.md` | Markdown | Phân tích tính liên kết hệ thống, các tam giác phối hợp và chuyển trạng thái. |
| `PROJECT_STATUS.md` | Markdown | Báo cáo kiểm toán tổng thể tình trạng hoàn thiện của dự án. |

---

## 3. 🧠 Hướng Dẫn Dành Cho AI Assistant (LLM Prompting Protocol)
Khi nhận câu hỏi từ người dùng về build đội hình hoặc mua bán cầu thủ:
1. Đọc ngay `02_CURRENT_SQUAD.json` và `04_PLAYER_CONFIGS.json` để nắm tình trạng đội hình hiện tại mà không cần hỏi lại.
2. Tra cứu `17_DECISION_RULES.md` trước khi đưa ra bất kỳ đề xuất chuyển nhượng hay ghép cặp CB/CM nào.
3. Sử dụng đúng tên tiếng Việt chính thức trong `07_NORMAL_TRAITS_VI.json`, `08_SKILL_COACHES_VI.json`, `09_GOLD_TRAITS_VI.json`.
4. Không đề xuất tiêu quá 30% quỹ BP dự trữ nếu không phải là `Critical Upgrade`.
