# 🌏 THÔNG BÁO GIỚI HẠN VÙNG LÃNH THỔ (REGION LIMITATION NOTICE)

> **Official Declaration:**
> "NEXON Open API live access is unavailable for the user's Vietnam region as of 2026-09-18. Live KR match/ranker datasets are therefore not available. Public KR sources and VN community sources are analyzed separately."

---

## 1. 📌 Bối Cảnh & Nguyên Tắc Tuân Thủ (Compliance & Context)

* **Hiện trạng dịch vụ:** Cổng thông tin nhà phát triển NEXON Open API (Hàn Quốc) áp dụng chính sách giới hạn khu vực địa lý, hiện không hỗ trợ khu vực cư trú Việt Nam.
* **Nguyên tắc kỹ thuật an toàn:** 
  - Tuyệt đối **KHÔNG** sử dụng VPN, proxy, tài khoản giả lập vị trí địa lý hoặc bất kỳ phương pháp lách kiểm soát nào.
  - Bảo toàn 100% mã nguồn kết nối Live API (`tools/glxh_pipeline.py`) với cờ trạng thái `KR_NEXON_LIVE_API = "UNAVAILABLE_FROM_VIETNAM"`. Mã nguồn này được lưu giữ nguyên vẹn để kích hoạt ngay lập tức khi NEXON mở rộng hỗ trợ khu vực trong tương lai hoặc khi có điều kiện kết nối chính ngạch.
  - Vô hiệu hóa việc gọi các endpoint yêu cầu API Key đã bị hạn chế vùng nhằm tránh lãng phí tài nguyên và lỗi kết nối vô ích.

---

## 2. 🏛️ KIẾN TRÚC DỮ LIỆU HAI LỚP (DUAL-LAYER DATA ARCHITECTURE)

Để phục vụ nghiên cứu và tối ưu hóa đội hình Giả Lập Xếp Hạng (GLXH / Manager Mode) mà không phụ thuộc vào live API bị khóa vùng, dự án phân tách dữ liệu thành 2 tầng độc lập, minh bạch và có gắn nhãn xuất xứ rõ ràng:

1. **`KR_PUBLIC_GLXH` (Tầng Dữ Liệu Công Khai Hàn Quốc):**
   - Diễn đàn Inven Hàn Quốc chuyên mục 감독모드 (Manager Mode) & 전술 (Chiến thuật - Board 3145).
   - Các bài chia sẻ đội hình Super Champions (슈퍼 챔피언스) và Champions (챔피언스) được các ranker Hàn Quốc công bố công khai.
   - Bộ từ điển định danh và chỉ số 41,289 cầu thủ trích xuất từ Data Center public (`details.csv`, `codes.csv`, `seasonid.json`, `spposition.json`).
   - Các repository và công cụ mã nguồn mở cộng đồng (`fconline-player-search`, FIFAAddict).

2. **`VN_GLXH` (Tầng Dữ Liệu Thực Chiến Garena Việt Nam):**
   - Diễn đàn, cộng đồng GLXH Việt Nam, FCVN, Garena FC Online.
   - Đánh giá chất lượng cầu thủ tiếng Việt trên FIFAAddict.
   - Dữ liệu thực tế về giá trị chuyển nhượng (TTCN Garena), mức thẻ cộng (+3, +5, +8), giới hạn lương (260/265/270).
   - Dữ liệu đội hình farming cày cắm auto và danh sách cầu thủ hiện có của người dùng.

---

## 3. 🛡️ QUY TẮC ĐỊNH DANH VÀ CHỐNG GÂY HIỂU NHẦM (NOMENCLATURE INTEGRITY)

* **Tuyệt đối không sử dụng:** `real_ranker`, `top10000_live`, `live_nexon` cho các tập dữ liệu không trích xuất trực tiếp từ phiên xác thực live API đang hoạt động.
* **Quy chuẩn tiền tố tệp xuất bản:**
  - `kr_public_glxh_*`: Dữ liệu xuất phát từ nguồn công khai Hàn Quốc.
  - `vn_glxh_*`: Dữ liệu phân tích dành riêng cho môi trường Garena Việt Nam.
  - Mỗi file CSV/JSON luôn đi kèm file sidecar provenance `.meta.json` ghi rõ `sample_type` và nguồn gốc dữ liệu.
