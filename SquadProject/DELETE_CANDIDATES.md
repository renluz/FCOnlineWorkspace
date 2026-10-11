# 🗑️ DANH SÁCH ỨNG VIÊN DỌN DẸP & PHÂN LOẠI XỬ LÝ (DELETE / MIGRATION CANDIDATES)

> **Tài liệu:** `DELETE_CANDIDATES.md`  
> **Thư mục rà soát:** `E:\Game\Garena\FCOnline`  
> **Workspace đích:** `E:\FCOnlineWorkspace\`  
> **Thời điểm lập:** 2026-09-20  
> **Nguyên tắc an toàn:** Không xóa vĩnh viễn bất kỳ file nào khi chưa đối soát bản sao lưu và xác minh nguồn gốc 100%. Không xóa bất kỳ file game nào.

---

## 1. 🛡️ BẢNG PHÂN LOẠI VÀ QUYẾT ĐỊNH XỬ LÝ TOÀN BỘ 8 CỤM THỰC THỂ

| Tên thực thể tại `E:\Game\Garena\FCOnline` | Số lượng file | Dung lượng | Phân loại | Hành động quyết định | Trạng thái thực tế |
| :--- | :---: | :---: | :---: | :--- | :---: |
| **`FFZik/`** | 6 files | 6.02 MB | `UNKNOWN` / Game Tool | **LEAVE_UNTOUCHED** (CẤM XÓA, CẤM DI CHUYỂN) | ✅ **Giữ nguyên 100% tại thư mục game** |
| **`GEMINI.md`** | 1 file | 1.09 KB | `GAME_CONFIG` | **LEAVE_UNTOUCHED** (Giữ nguyên, tinh gọn nội dung) | ✅ **Đang lưu tại thư mục game** |
| **`FCOnlineSquadProject/`** | 29 files | 0.27 MB | `RESEARCH_PROJECT` | **SAFE_MIGRATE** (Di chuyển sang `Workspace\SquadProject`) | ✅ **Đã di chuyển & đối soát khớp 100%** |
| **`FCOnlineResearch/`** | 11,548 files | 222.98 MB | `RESEARCH_PROJECT` | **SAFE_MIGRATE** (Di chuyển sang `Workspace\Research`) | ✅ **Đã di chuyển & đối soát khớp 100%** |
| **`FCOnlineResearch_Codex_Handoff/`**| 10 files | 0.03 MB | `RESEARCH_PROJECT` | **SAFE_MIGRATE** (Di chuyển sang `Workspace\Archive\OldReports`) | ✅ **Đã di chuyển an toàn** |
| **`CỘNG ĐỒNG...Facebook.html`** | 1 file | 6.91 MB | `RESEARCH_SOURCE` | **SAFE_MIGRATE** (Di chuyển sang `Workspace\Sources\FCVN`) | ✅ **Đã di chuyển an toàn** |
| **`CỘNG ĐỒNG...Facebook_files/`**| 399 files | 38.55 MB | `RESEARCH_SOURCE` | **SAFE_MIGRATE** (Di chuyển sang `Workspace\Sources\FCVN`) | ✅ **Đã di chuyển an toàn** |
| **`extracted_posts.txt`** | 1 file | 1.5 KB | `RESEARCH_SOURCE` | **SAFE_MIGRATE** (Di chuyển sang `Workspace\Sources\FCVN`) | ✅ **Đã di chuyển an toàn** |

---

## 2. 🔍 CHI TIẾT ĐÁNH GIÁ ỨNG VIÊN XÓA VĨNH VIỄN (PERMANENT DELETION AUDIT)

### Nhóm 1: File Game & Tool Hỗ Trợ (BẢO TỒN TUYỆT ĐỐI — 0% XÓA)
* **`FFZik/FFZik.exe`:** File thực thi công cụ auto GLXH.
* **`FFZik/Advance Tactics/Sample-Tactic.fzt`:** File chiến thuật mẫu.
* **`FFZik/Language/*`:** Toàn bộ file ngôn ngữ hiển thị giao diện (`vi.lang`, `en.lang`, `th.lang`, `lang.ini`).
* **Kết luận:** **CẤM XÓA**. Đã giữ nguyên vẹn tại `E:\Game\Garena\FCOnline\FFZik`.

### Nhóm 2: Thư mục nguồn Research sau khi đã đối soát (DỌN DẸP AN TOÀN)
* Thư mục gốc `FCOnlineSquadProject` và `FCOnlineResearch` tại `E:\Game\Garena\FCOnline` chỉ được gỡ bỏ khỏi thư mục game **SAU KHI** đã sao chép đầy đủ 11,577 files sang `E:\FCOnlineWorkspace\` và vượt qua kiểm thử tính toàn vẹn 100% (`assert count == dst_count`, `assert size == dst_size`).
* Không có bất kỳ dữ liệu tri thức nào bị mất mát trong quá trình dọn dẹp.

### Nhóm 3: Các file rác tạm thời trong tương lai (TEMPORARY RETENTION CANDIDATES)
* File `E:\FCOnlineWorkspace\Archive\Temporary\pre_migration_manifest.json`: Lưu trữ manifest đối soát trước khi di chuyển. Giữ lại làm bằng chứng kiểm toán, không cần xóa ngay.
* File `E:\FCOnline_CLEANUP_INVENTORY.csv`: Bảng kiểm kê 11,995 file quét ở Phase 1. Giữ lại ở ổ `E:\` để người dùng tiện tra cứu lịch sử.

---

## 3. 🏁 KẾT LUẬN KIỂM TOÁN AN TOÀN
* **Số lượng file game bị xóa:** **0 file** (Không có file cài đặt hay file hệ thống nào của game bị đụng chạm).
* **Số lượng công cụ/launcher bị ảnh hưởng:** **0** (FFZik được giữ nguyên vẹn).
* **Tình trạng thư mục game `E:\Game\Garena\FCOnline`:** Hoàn toàn sạch sẽ, giải phóng 274.76 MB dữ liệu research, chỉ lưu giữ đúng công cụ và cấu hình cần thiết.
