# 📑 BÁO CÁO ĐÁNH GIÁ CRAWLER RANKER (ggongch2/fconline_crawling)

> **Mã báo cáo:** EVAL-CRAWLER-20261011  
> **Người thực hiện:** Antigravity  
> **Repo đối tượng:** [ggongch2/fconline_crawling](https://github.com/ggongch2/fconline_crawling)  
> **Mục tiêu đánh giá:** Khả năng tái sử dụng để thu thập dữ liệu Ranker GLXH và giá TTCN cho dự án FCOnlineWorkspace.

---

## 1. 🔍 TỔNG QUAN SCRIPT & NGUỒN CRAWL

* **URL Nguồn:** https://fconline.nexon.com/datacenter/playerstat (Data Center máy chủ Hàn Quốc - Nexon KR).
* **Công nghệ sử dụng:** Python (selenium, BeautifulSoup4, equests).
* **Các file trong repo:**
  * conline_top200.py: Script gốc crawl Top 200 cầu thủ theo chỉ số.
  * conline_top200_re.py: Phiên bản sửa đổi thử nghiệm kết hợp equests để bóc tách Player ID.
* **Các trường dữ liệu dự kiến thu thập:**
  1. Season (Mùa thẻ): Bóc tách từ URL ảnh .info_top .season img.
  2. Name (Tên cầu thủ): Text từ .info_top .name.
  3. Player ID (PID): Tách từ thẻ <input type="hidden" name="Strong[PID]">.
  4. OVR (Chỉ số tổng): Dự định lấy từ popup chi tiết .ovr.value.
  5. Price (Giá thẻ): Dự định lấy từ popup chi tiết .add_info .txt.

---

## 2. 🚨 KẾT QUẢ KIỂM TRA SELECTOR & PHÂN TÍCH KỸ THUẬT

Sau khi kéo mã nguồn về môi trường độc lập (scratch/fconline_crawling) và kiểm tra thực nghiệm, hệ thống ghi nhận **2 rào cản chí mạng** khiến script **KHÔNG THỂ CHẠY ĐƯỢC** trên môi trường máy người dùng tại Việt Nam:

### A. Rào cản Geo-IP Redirection (Chặn truy cập vùng)
* **Bằng chứng thực nghiệm:**
  `python
  r = requests.get('https://fconline.nexon.com/datacenter/playerstat', headers={'User-Agent': 'Mozilla/5.0'})
  print(r.history) # ['https://fconline.nexon.com/datacenter/playerstat', 'http://fconline.garena.vn/']
  print(r.url)     # https://fconline.garena.vn/
  `
* **Hiện tượng:** Máy chủ Nexon KR tự động chuyển hướng (HTTP 302 Redirect) toàn bộ dải IP xuất phát từ Việt Nam về thẳng trang chủ **Garena Việt Nam** (https://fconline.garena.vn/).
* **Hậu quả:** Selenium mở trình duyệt lên sẽ bị redirect ngay sang web Garena. Lệnh tìm phần tử //*[@id="middle"]... sẽ sụp đổ ngay lập tức với lỗi NoSuchElementException.

### B. Lỗi cú pháp và logic dở dang trong mã nguồn (Incomplete Code)
1. **Lỗi NameError:** Trong conline_top200.py (dòng 77), tác giả duyệt vòng lặp or info_element in info_elements: nhưng biến info_elements **chưa từng được khai báo** trước đó.
2. **Lỗi IndexError:** Phần click mở popup để cào OVR và Price bị tác giả comment out hoàn toàn bằng """ (dòng 90–115). Nhưng ở cuối script (dòng 123) vẫn cố truy xuất overall_list[i] và price_list[i], dẫn đến văng lỗi IndexError: list index out of range.
3. **Lỗi AttributeError:** Trong conline_top200_re.py (dòng 80), tác giả dùng equests.get để phân tích HTML tĩnh trong khi trang Nexon render động qua JavaScript. Kết quả info_top trả về None, dẫn đến lỗi văng chương trình: 'NoneType' object has no attribute 'find'.

---

## 3. 📊 MẪU DỮ LIỆU THỰC TẾ & BẢNG SO SÁNH NGUỒN CRAWL

| Tiêu chí | ggongch2/fconline_crawling (Nexon KR) | Nhu cầu thực tế FCOnlineWorkspace (Garena VN) |
| :--- | :--- | :--- |
| **Máy chủ** | Nexon Hàn Quốc | Garena Việt Nam |
| **Trạng thái chạy** | ❌ Lỗi Geo-IP + Lỗi Code dở dang | Cần tự động hóa ổn định |
| **Mùa thẻ** | Đầy đủ mùa Hàn | Cần mùa thẻ áp dụng tại Garena VN |
| **Mức cộng (+8 đến +11)** | ❌ Script không hỗ trợ chọn mức thẻ | ✅ Bắt buộc (Tối ưu meta Mạ Vàng / Bạch Kim) |
| **Giá TTCN** | Giá BP Hàn Quốc (Khác biệt hoàn toàn) | ✅ Bắt buộc giá BP TTCN Việt Nam |
| **Chỉ số ẩn / HLV** | Không hỗ trợ | ✅ Bắt buộc cho hệ thống Moneyball |

---

## 4. 🎯 KẾT LUẬN & ĐỀ XUẤT KIẾN TRÚC

### Kết luận:
> ❌ **KHÔNG NÊN TÁI SỬ DỤNG** script từ repo ggongch2/fconline_crawling.  
> Script này là một dự án bài tập cá nhân chưa hoàn thiện, đầy lỗi logic cơ bản, bị chặn IP Việt Nam và lấy dữ liệu của server Hàn Quốc (không có giá trị đối chiếu kinh tế BP cho server Garena).

### Giải pháp kiến trúc thay thế tối ưu:
1. **Thay thế Crawl Web bằng API Garena chính thức:**
   * Sử dụng endpoint chính thức của Garena DataCenter (https://dc.fconline.garena.vn/api/app/ranking/players) — repo ilfapi/api.fconline.garena là tài liệu tham khảo chính xác về cấu trúc endpoint này.
   * Ưu điểm: Lấy trực tiếp dữ liệu Top Ranker Pro Server Việt Nam, không cần Selenium, không sợ lỗi giao diện DOM/XPath.
2. **Đối chiếu Exact-card qua FC INFO:**
   * FC INFO (c-info.com) đã bọc sẵn toàn bộ Nexon Open API kèm bộ lọc chi tiết cho từng mức thẻ mạ vàng/bạch kim.

---
*Báo cáo được khởi tạo tự động và đồng bộ trực tiếp lên hệ thống Cloud GitHub.*