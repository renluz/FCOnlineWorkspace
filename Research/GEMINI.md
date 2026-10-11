# FC Online Research - Local Context & Project Memory (GEMINI.md)

Tài liệu bộ nhớ ngữ cảnh cục bộ (Project-Scoped Context Cache) cho dự án nghiên cứu dữ liệu FC Online & Giả Lập Xếp Hạng (GLXH / Manager Mode).

---

## 1. 📌 Metadata Dự Án
* **Tên Dự Án:** FC Online Research Toolkit (Manager Mode / GLXH Focus)
* **Thư mục làm việc:** `E:\FCOnlineWorkspace\Research`
* **Target Game:** EA Sports FC Online (Nexon Korea / Garena Vietnam)
* **Manager Mode Match Type Code:** `52` (`감독모드`)
* **Trần Lương Hiện Tại (Garena VN):** `VN_CURRENT_SALARY_CAP = 305`
* **Trạng Thái Live API:** `KR_NEXON_LIVE_API = UNAVAILABLE_FROM_VIETNAM` (Xem chi tiết tại [REGION_LIMITATION.md](file:///E:/FCOnlineWorkspace/Research/REGION_LIMITATION.md))
* **Trạng Thái TTCN Trực Tiếp:** `PUBLIC_MARKET_API_UNAVAILABLE` (Website fcoplayers.com không cung cấp sổ lệnh giao dịch thực tế hoặc sell_quantity).
* **Nguyên Tắc Dữ Liệu Sở Hữu:** Tách biệt tuyệt đối giữa `OWNED_PLAYER_DATA` và `DATABASE_CANDIDATE_DATA`. Không tự ý nâng cấp hoặc thay đổi season của cầu thủ sở hữu.
* **Source of Truth Inventory:** [data/vn_owned_players.json](file:///E:/FCOnlineWorkspace/Research/data/vn_owned_players.json) (13 cầu thủ từ screenshot game kèm `current_slot`, `natural_positions`, `displayed_ovr`, `database_base_ovr`).
* **Bộ Kiểm Tra Nhất Quán:** [tools/validate_owned_inventory.py](file:///E:/FCOnlineWorkspace/Research/tools/validate_owned_inventory.py)
* **Bộ Định Danh Cầu Thủ & Vị Trí:** [tools/player_identity_resolver.py](file:///E:/FCOnlineWorkspace/Research/tools/player_identity_resolver.py)
* **Database Cầu Thủ Toàn Cầu:** 41,289 cầu thủ (`repos\fconline-player-search\data\details.csv`)

---

## 2. 🗂️ Sổ Bộ Định Danh & Tiền Tố (ID & Prefix Registry)
* **`OWNED_PLAYER_DATA`:** Dữ liệu cầu thủ sở hữu thực tế (`data/vn_owned_players.json`). Tuyệt đối bảo toàn `grade`, `displayed_ovr`, `database_base_ovr`, `salary`, `season`, `current_slot`, `natural_positions`.
* **`DATABASE_CANDIDATE_DATA`:** Dữ liệu ứng viên tiềm năng từ mô hình tính toán DB. Bắt buộc dùng `HYPOTHETICAL_GRADE` và `HYPOTHETICAL_OVR`.
* **`FCOPLAYERS_PUBLIC_MARKET`:** Nguồn dữ liệu thị trường công khai từ fcoplayers.com. Gắn nhãn `sell_quantity = null` và `market_availability = UNKNOWN`.
* **`KR_PUBLIC_*`:** Dữ liệu chiến thuật và đội hình Inven Hàn Quốc công khai có đầy đủ 8 trường provenance.
* **`vn_glxh_model_*`:** Dữ liệu ứng viên sinh từ công thức/mô hình thống kê.

---

## 3. 🗺️ Bản Đồ File Trọng Yếu (Key File Map)

```
E:\FCOnlineWorkspace\Research
├── FC_ONLINE_GLXH_KNOWLEDGE.md            # Sách giáo trình toàn diện 18 chương về GLXH
├── CURRENT_SQUAD_KNOWLEDGE_APPLICATION.md # Phân tích chuyên sâu 11 đá chính + 6 dự bị của người dùng
├── KNOWLEDGE_GAPS.md                      # Phân tích khoảng trống tri thức & hạng mục cần test
├── RESEARCH_INDEX.csv                     # Chỉ mục tra cứu nhanh toàn bộ Claims, Provenance & Evidence
├── knowledge/                             # Hệ thống tri thức có Provenance & Evidence Ranking (A-E)
│   ├── CONTRADICTIONS.md                  # Sổ bộ bất đồng & phân tích 5 mâu thuẫn chiến thuật
│   ├── DECISION_RULES.md                  # Hệ thống luật quyết định tham số hóa (IF-THEN)
│   ├── claims/                            # Atomic Claims (claims_master.json)
│   ├── entities/                          # Định nghĩa thực thể (mechanics_entities.json)
│   ├── formations/                        # Phân tích 7 sơ đồ cốt lõi (4-2-3-1, 4-2-2-1-1, ...)
│   ├── patches/                           # Lịch sử cập nhật gameplay (gameplay_patches.json)
│   ├── players/                           # Danh mục Archetype cầu thủ (player_archetypes.json)
│   ├── sources/                           # Registry nguồn (sources_registry.json)
│   └── tactics/                           # Từ điển chiến thuật cá nhân & đội (registries)
├── REGION_LIMITATION.md                  # Thông báo giới hạn vùng lãnh thổ NEXON Open API cho Việt Nam
├── VN_CURRENT_SQUAD_AUDIT.md             # Báo cáo kiểm toán đội hình hiện tại (out-of-position analysis recalculated)
├── VN_MARKET_DATA_REPORT.md              # Báo cáo kiểm toán thị trường fcoplayers.com & TTCN Việt Nam
├── VN_MARKET_SNAPSHOT_REPORT.md          # Báo cáo kiểm toán snapshot in-game TTCN VN (số ảnh, độ tin cậy, tuổi thẻ)
├── DATA_DICTIONARY.md                    # Từ điển dữ liệu v3.5 (OWNED_PLAYER, MARKET, IN_GAME_SCREENSHOT, HYPOTHETICAL)
├── GEMINI.md                             # Bộ nhớ ngữ cảnh dự án (Persistent Project Memory)
├── data/                                 # Dữ liệu nguồn và metadata
│   ├── vn_owned_players.json             # SOURCE_OF_TRUTH 13 cầu thủ sở hữu thực tế của người dùng
│   ├── vn_market_history.csv             # Lịch sử TTCN Việt Nam tích lũy (IN_GAME_SCREENSHOT, FCOPLAYERS)
│   ├── vn_market_screenshots/            # Quản lý ảnh chụp màn hình TTCN người dùng cung cấp
│   │   ├── incoming/                     # Thư mục nạp ảnh mới từ người dùng
│   │   └── processed/                    # Thư mục lưu trữ ảnh đã nhận diện an toàn
│   ├── kr_public_glxh_tactics.json       # Chiến thuật Inven Super Champions có trích dẫn provenance
│   ├── kr_public_glxh_squads.json        # Đội hình Super Champions / Champions công khai có provenance
│   ├── division.json / matchtype.json    # Metadata chuẩn NEXON
│   └── spposition.json / seasonid.json   # Danh mục vị trí và mã mùa giải
├── exports/                              # Dataset CSV/JSON xuất bản
│   ├── vn_market_latest.csv              # Snapshot TTCN mới nhất phục vụ trực tiếp cho GLXH Optimizer
│   ├── vn_market_candidate_scan.csv      # Báo cáo rà soát khả thi mua hàng (bộ lọc HIGH/MEDIUM, age <= 1440m)
│   ├── vn_owned_player_identity_map.csv  # Bảng đối soát 13 cầu thủ sở hữu (base OVR, natural_positions, sources)
│   ├── vn_glxh_current_squad_candidates.csv # Các phương án đội hình tối ưu từ 13 cầu thủ sở hữu
│   ├── vn_glxh_model_candidates.csv      # 175 ứng viên mô hình từ 41,289 DB (HYPOTHETICAL_*)
│   └── kr_public_glxh_candidates.csv     # Ứng viên top meta Hàn Quốc đối chiếu từ DB
└── tools/                                # Pipeline và CLI Scripts
    ├── vn_market_screenshot_importer.py  # Bộ nạp và nhận diện ảnh TTCN bằng Windows Native OCR Engine
    ├── vn_market_candidate_scanner.py    # Bộ quét tính khả thi thị trường (chỉ chấp nhận HIGH/MED, age <= 24h)
    ├── player_identity_resolver.py       # Bộ giải quyết định danh cầu thủ, base OVR & natural positions
    ├── validate_owned_inventory.py       # Bộ kiểm tra tính toàn vẹn (chặn sai lệch schema/thông số)
    ├── inspect_fcoplayers_market.py      # Khảo sát cấu trúc public endpoints của fcoplayers.com
    ├── vn_market_collector.py            # Thu thập dữ liệu TTCN và đồng bộ vào history/exports
    ├── vn_glxh_analyzer.py               # Engine tối ưu VN_GLXH_CURRENT_SQUAD_OPTIMIZATION
    └── kr_public_glxh_crawler.py         # Thu thập chiến thuật Inven Hàn Quốc kèm provenance
```

---

## 4. ⚡ Quy Tắc & Quyết Định Kỹ Thuật (Decisions & Known Gotchas)
1. **Không Tự Sửa Cầu Thủ Đang Sở Hữu:** Nghiêm cấm tự ý nâng cấp grade/OVR hoặc đổi season của cầu thủ người dùng. Mọi thay đổi trái phép sẽ gây lỗi validation.
2. **Current Slot vs Natural Positions:** `current_slot` là slot bố trí trong screenshot, không phải "vị trí gốc". `natural_positions` bắt buộc phải trích xuất từ database/card metadata (`["RB", "LB"]`, `["CF", "CAM"]`, `["CM", "LW", "ST"]`).
3. **Pipeline Ảnh Chụp Màn Hình TTCN (In-Game Screenshot):**
   * Hoàn toàn tuân thủ an toàn: không auto-buy, không auto-sell, không click trong game, không đọc RAM/process, không hook, không packet sniff.
   * Dùng Windows Native OCR (`Windows.Media.Ocr`) nhận diện văn bản.
   * Ưu tiên nguồn: `IN_GAME_SCREENSHOT > FC_ONLINE_M_SCREENSHOT > USER_MANUAL_INPUT > PUBLIC_REFERENCE_PRICE > KR_PRICE_REFERENCE`.
   * Thẻ chỉ được coi là `AVAILABLE` khi có `sell_quantity > 0` thực tế trên sổ lệnh bán.
   * Bộ quét mua (`vn_market_candidate_scanner.py`) chỉ chấp nhận snapshot `HIGH`/`MEDIUM` và thời hạn `snapshot_age_minutes <= 1440` (24 giờ).
4. **Salary Cap 305:** Trần lương tài khoản Garena VN là 305. Đội hình chính dùng 263/305 (dư 42 lương).

