# write_gemini_md.py
content = """# FC Online Research - Local Context & Project Memory (GEMINI.md)

Tài liệu bộ nhớ ngữ cảnh cục bộ (Project-Scoped Context Cache) cho dự án nghiên cứu dữ liệu FC Online & Giả Lập Xếp Hạng (GLXH).

---

## 1. 📌 Metadata Dự Án
* **Tên Dự Án:** FC Online Research Toolkit (Manager Mode / GLXH Focus)
* **Thư mục làm việc:** `E:\\FCOnlineWorkspace\\Research`
* **Target Game:** EA Sports FC Online (Nexon / Garena Vietnam)
* **Manager Mode Match Type Code:** `52` (`감독모드`)
* **Ranked 1v1 Match Type Code:** `50` (`공식경기`)
* **Python Virtualenv:** `repos\\fconline-player-search\\.venv\\Scripts\\python.exe`
* **Node.js Environment:** v24.18.0 (Build: `dist/index.js` in `repos\\fconline-mcp`)

---

## 2. 🗂️ Sổ Bộ Định Danh & Tiền Tố (ID & Prefix Registry)
* **Prefix File Xuất:** `glxh_` (Dành cho các dataset nghiên cứu meta giả lập xếp hạng)
* **Prefix Điểm Đánh Giá:** `EXPERIMENTAL_SCORE_*` (Dành cho các chỉ số chấm điểm tự động thử nghiệm)
* **Position Codes (spposition.json):**
  - GK: `0`
  - SW: `1`, CB: `2`, LCB: `3`, RCB: `4`
  - LB: `5`, RB: `6`, LWB: `7`, RWB: `8`
  - CDM: `9`, LDM: `10`, RDM: `11`
  - CM: `12`, LCM: `13`, RCM: `14`, LM: `15`, RM: `16`
  - CAM: `17`, LAM: `18`, RAM: `19`
  - LW: `20`, RW: `21`, LF: `22`, CF: `23`, RF: `24`, ST: `25`

---

## 3. 🗺️ Bản Đồ File Trọng Yếu (Key File Map)

```
E:\\FCOnlineWorkspace\\Research
├── DATA_DICTIONARY.md              # Từ điển 25+ trường chỉ số dữ liệu & công thức điểm GLXH
├── ENVIRONMENT_REPORT.md           # Báo cáo thông số môi trường Windows, Python, Git, Node.js
├── GEMINI.md                       # Bộ nhớ ngữ cảnh dự án (Persistent Project Memory)
├── data/                           # Siêu dữ liệu Nexon API tĩnh (Match Type, Season, Position, Division)
│   ├── division-volta.json
│   ├── division.json
│   ├── matchtype.json              # Chứa định danh matchtype 52 (감독모드)
│   ├── seasonid.json               # Danh mục mã mùa giải chính thức
│   └── spposition.json             # Danh mục vị trí và ID
├── exports/                        # Dataset CSV/JSON phục vụ đưa vào LLM / ChatGPT phân tích
│   ├── example_cdm_glxh.csv        # Mẫu lọc CDM theo chỉ số GLXH
│   ├── example_st_glxh.csv         # Mẫu lọc ST theo chỉ số GLXH
│   ├── glxh_analyzed_players.csv   # Toàn bộ 4,568 cầu thủ OVR 100+ kèm điểm chấm các vị trí
│   ├── glxh_analyzed_players.json  # Bản JSON cấu trúc chi tiết
│   ├── glxh_cam.csv / cm.csv / ... # Bộ ứng viên tối ưu theo từng vị trí (ST, CAM, CM, CDM, CB, Fullback, GK)
│   ├── glxh_ranker_stats.csv       # Tổng hợp cầu thủ thường dùng của ranker GLXH
│   └── glxh_ranker_stats.json
├── logs/                           # Log thực thi runtime
├── repos/                          # 2 repositories mã nguồn tích hợp
│   ├── fconline-mcp/               # Model Context Protocol server (TypeScript stdio)
│   └── fconline-player-search/     # Engine tìm kiếm & database 41,289 cầu thủ (details.csv)
└── tools/                          # CLI Scripts phục vụ trích xuất và phân tích
    ├── export_players.py           # CLI trích xuất người chơi theo tiêu chí tùy biến (25 cột chuẩn)
    ├── glxh_player_analyzer.py     # Engine chấm điểm cầu thủ theo trọng số vị trí GLXH
    └── glxh_research.py            # Engine phân tích meta ranker và tổng hợp dataset
```

---

## 4. ⚡ Quy Tắc & Quyết Định Kỹ Thuật (Decisions & Known Gotchas)
1. **Bảo toàn Vanilla Files:** Toàn bộ file cài đặt gốc tại `E:\\Game\\Garena\\FCOnline\\GameData`, `FFZik` là **READ-ONLY**. Nghiên cứu độc lập 100% ngoài thư mục game.
2. **Match Type Code:** Tuyệt đối dùng code `52` cho Giả Lập Xếp Hạng. Tránh mã `50` (1v1 tay).
3. **Mã hóa Windows UTF-8:** Khi chạy Python qua PowerShell, luôn khai báo `sys.stdout.reconfigure(encoding='utf-8')` để tránh vỡ font Tiếng Hàn/Tiếng Việt trên bảng mã `cp1252`.
4. **NEXON API Key:** Được quản lý qua `$env:NEXON_OPEN_API_KEY`. Nếu chưa có key, scripts tự fallback về metadata offline và database cục bộ an toàn, không bị crash gián đoạn.
"""

target_path = r"E:\FCOnlineWorkspace\Research\GEMINI.md"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print(f"File created successfully at {target_path}")
