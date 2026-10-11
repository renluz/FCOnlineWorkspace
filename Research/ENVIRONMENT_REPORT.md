# FC Online Research Environment Report

Báo cáo chi tiết về môi trường thực thi, phiên bản phần mềm, cấu hình repository và trạng thái tích hợp của bộ công cụ **FC Online Research** (phục vụ Giả Lập Xếp Hạng - GLXH / Manager Mode).

---

## 1. Thông Tin Hệ Thống & Phiên Bản Môi Trường (System & Runtime)

| Thành phần | Phiên bản | Đường dẫn thực thi (Executable Path) | Trạng thái |
| :--- | :--- | :--- | :--- |
| **Hệ điều hành** | Windows 11 Pro 64-bit (Build 26200) | `C:\Windows\System32` | Sẵn sàng |
| **Git** | `2.55.0.windows.2` | `C:\Program Files\Git\cmd\git.exe` | Đạt yêu cầu |
| **Node.js** | `v24.18.0` | `C:\Program Files\nodejs\node.exe` | Đạt yêu cầu (>= 20.0) |
| **npm** | `11.16.0` | `C:\Program Files\nodejs\npm.cmd` | Đạt yêu cầu |
| **Python (System)** | `3.13.13` | `C:\Users\PhucVu\miniconda3\python.exe` | Đạt yêu cầu (>= 3.10) |
| **pip (System)** | `26.1.2` | `C:\Users\PhucVu\miniconda3\Scripts\pip.exe` | Đạt yêu cầu |
| **Python (Venv)** | `3.13.13` | `E:\FCOnlineWorkspace\Research\repos\fconline-player-search\.venv\Scripts\python.exe` | Kích hoạt |

---

## 2. Thông Tin Repositories (Codebases Cloned)

### 2.1. fconline-mcp (Nexon Open API MCP Server)
* **Thư mục:** `E:\FCOnlineWorkspace\Research\repos\fconline-mcp`
* **Nguồn (Origin):** `https://github.com/fbtmdgh4517/fconline-mcp.git`
* **Nhánh (Branch):** `master`
* **Commit Hash:** `8ff769fa87c7dfbc5cf37b328d59e8d61e57000a`
* **Kiểm tra mã độc / An toàn:** **PASSED** (Không có syscall/hook/dll injection; chỉ giao tiếp stdio MCP và gọi endpoint `https://open.api.nexon.com`).
* **Trạng thái Build:** Đã cài đặt npm dependencies (`audited 147 packages`), biên dịch TypeScript hoàn tất (`dist/index.js`), kiểm thử `npm test` đạt **7/7 tests passed**.
* **Khởi chạy Stdio MCP:** Kiểm tra stdio pass.

### 2.2. fconline-player-search (Dataset & Search Engine)
* **Thư mục:** `E:\FCOnlineWorkspace\Research\repos\fconline-player-search`
* **Nguồn (Origin):** `https://github.com/contlg/fconline-player-search.git`
* **Nhánh (Branch):** `main`
* **Commit Hash:** `373d0b293bf880f4b30ab108679250bfcf7faffa`
* **Kiểm tra mã độc / An toàn:** **PASSED** (Mã nguồn Python thuần, crawl qua BeautifulSoup/requests tới `fconline.nexon.com`, không can thiệp game).
* **Môi trường ảo (Venv):** Đã tạo `.venv` và cài đặt đầy đủ dependencies (`pandas`, `requests`, `beautifulsoup4`, `aiohttp`, `httpx`).
* **Dữ liệu Database:** File `data/details.csv` chứa dữ liệu của **41,289 cầu thủ** (kích thước ~10.79 MB), đã xác thực hoạt động lọc theo vị trí, chỉ số, thể hình, 2 chân và Team Color.

---

## 3. Trạng Thái API Key & Tích Hợp Nexon Open API

* **Biến môi trường:** `NEXON_OPEN_API_KEY`
* **Trạng thái hiện tại:** **CHƯA CẤU HÌNH (PENDING USER KEY)**
* **Tác động:**
  - ✅ **Hoạt động bình thường mà không cần key:**
    - Toàn bộ metadata hệ thống (vị trí `spposition.json`, mùa giải `seasonid.json`, phân hạng `division.json`, loại trận `matchtype.json`).
    - Toàn bộ tính năng tìm kiếm, trích xuất dữ liệu và chấm điểm AI cho 41,289 cầu thủ (`export_players.py`, `glxh_player_analyzer.py`).
    - Bộ dữ liệu khuyến nghị GLXH theo vị trí (`glxh_*.csv`).
  - ⚠️ **Cần API Key để kích hoạt:**
    - Gọi API ranker trực tiếp thời gian thực từ máy chủ Nexon Hàn Quốc (`get_ranker_stats`, `get_match_detail`, `get_user_matches`).
    - Đồng bộ lịch sử đấu và đội hình cá nhân theo nickname trên máy chủ Nexon.

### Hướng Dẫn Cấu Hình Khi Có API Key:
1. Đăng ký tài khoản và tạo API Key tại: [https://openapi.nexon.com](https://openapi.nexon.com) (chọn dịch vụ **FC Online**).
2. Thiết lập key trên Windows:
   - **Tạm thời trong phiên PowerShell:**
     ```powershell
     $env:NEXON_OPEN_API_KEY="your_api_key_here"
     ```
   - **Lâu dài cho toàn hệ thống (Persistent):**
     ```powershell
     [Environment]::SetEnvironmentVariable("NEXON_OPEN_API_KEY", "your_api_key_here", "User")
     ```

---

## 4. Xác Định Mã Trận Đấu Giả Lập Xếp Hạng (Manager Mode)

Từ file siêu dữ liệu chính thức `data/matchtype.json`:
* **Manager Mode (Giả Lập Xếp Hạng GLXH):** **`matchtype = 52`** (`desc`: `감독모드`)
* **Official 1v1 Ranked (Xếp hạng đá tay 1v1):** **`matchtype = 50`** (`desc`: `공식경기`)
* **Volta Live:** **`matchtype = 214`**
* **Lưu ý tối quan trọng:** Tuyệt đối không nhầm lẫn mã `52` với mã `50` khi truy vấn dữ liệu GLXH.

---

## 5. Danh Sách Công Cụ Đã Sẵn Sàng (CLI & Scripts)

| Tên Script | Mục đích | Lệnh chạy mẫu |
| :--- | :--- | :--- |
| `tools/export_players.py` | Lọc và trích xuất dữ liệu cầu thủ từ database sang CSV/JSON chuẩn 25 trường thông tin | `python tools/export_players.py --position ST --min-height 185 --min-strength 115 --output exports/my_st.csv` |
| `tools/glxh_research.py` | Tạo bộ dữ liệu meta cho ranker GLXH và top ứng viên theo từng vị trí | `python tools/glxh_research.py` |
| `tools/glxh_player_analyzer.py` | Chấm điểm công thức GLXH (ST, Winger, CAM, CM, CDM, CB, Fullback, GK) cho 4,568+ cầu thủ OVR 100+ | `python tools/glxh_player_analyzer.py --min-ovr 100` |

---

## 6. Cam Kết An Toàn & Bảo Mật Dữ Liệu

* Bộ công cụ đặt độc lập hoàn toàn tại: `E:\FCOnlineWorkspace\Research`.
* Thư mục game gốc `E:\Game\Garena\FCOnline\GameData`, thư mục `FFZik`, `bin`, v.v. được giữ nguyên 100%, không bị can thiệp hay chỉnh sửa bất kỳ file nào.
* Không có mã độc, không có runtime hooking, không can thiệp bộ nhớ RAM của tiến trình game.
