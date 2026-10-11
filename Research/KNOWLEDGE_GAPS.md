# 🔭 PHÂN TÍCH KHOẢNG TRỐNG TRI THỨC & VÙNG CẦN KIỂM CHỨNG (KNOWLEDGE_GAPS.MD)

Tài liệu xác định các giới hạn tri thức hiện tại, phân tách rạch ròi giữa **bằng chứng đã kiểm chứng**, **giả thuyết cộng đồng (Speculation)** và các **vùng hộp đen của Engine**. Đây là kim chỉ nam cho các đợt cập nhật và nghiên cứu tiếp theo.

---

## 1. ❓ NHỮNG GÌ ENGINE CHƯA CÔNG BỐ (ENGINE BLACK BOXES)

| Hạng Mục | Hiện Trạng Tri Thức | Giới Hạn Cần Làm Rõ | Mức Độ Ảnh Hưởng Đến GLXH |
| :--- | :--- | :--- | :---: |
| **Thuật toán Dynamic Difficulty (Kịch bản trận đấu / Momentum):** | Cộng đồng quan sát thấy chuỗi thắng thường bị ngắt bởi các trận cầu thủ đỡ bóng bật ra xa bất thường. | Nexon và Garena chưa từng thừa nhận sự tồn tại của script can thiệp kết quả trong code engine. | **CAO** (Cần theo dõi chuỗi trận) |
| **Trọng số thực tế của Chỉ Số Ẩn Vàng (Gold Traits):** | Được giới thiệu từ 2025-2026, mang lại hiệu ứng hình ảnh và buff chỉ số. | Chưa có công thức giải mã chính xác tỷ lệ kích hoạt (% proc rate) trong chế độ giả lập tự động. | **TRUNG BÌNH** |
| **Công thức tính điểm cản phá của Thủ Môn:** | Đã chứng minh chiều cao quan trọng hơn OVR. | Mối tương quan toán học giữa `Chiều cao * 0.X` + `Phản xạ * 0.Y` chưa có tài liệu chính thức. | **TRUNG BÌNH** |

---

## 2. ⚠️ NHỮNG ĐIỀU CHỈ LÀ PHỎNG ĐOÁN CỦA CỘNG ĐỒNG (SPECULATIONS)

1. **"Thẻ cộng cao (+8 đến +10) của mùa thường đá khôn hơn thẻ +1 của mùa xịn dù cùng chỉ số":**
   - *Phân tích:* Đây là quan sát cảm tính phổ biến. Code engine chỉ đọc các giá trị thuộc tính cuối cùng sau khi cộng chỉ số, không có biến số "độ khôn độc lập của cấp cộng".
   - *Trạng thái:* **SPECULATION_UNVERIFIED** (Chưa có bằng chứng code).
2. **"Chỉnh thanh chiến thuật đội lẻ (ví dụ: 49 thay vì 50) sẽ kích hoạt AI đột biến":**
   - *Phân tích:* Nexon xác nhận thanh trượt chiến thuật chia theo các ngưỡng bậc thang (Tier bands: 1-33, 34-66, 67-99). Việc đặt 49 hay 50 hoàn toàn nằm trong cùng một ngưỡng bậc thang.
   - *Trạng thái:* **DEBUNKED / SPECULATION**.

---

## 3. 🧪 CÁC HẠNG MỤC CẦN KIỂM THỬ TRỰC TIẾP TRÊN ACCOUNT THẬT

Đối với đội hình 17 cầu thủ của bạn, cần triển khai các bài test sau trong 20-30 trận GLXH tiếp theo:

### Test Case #1: Vị trí của F. Lampard (CAM vs LCM)
* **Giả thuyết:** Lampard đá `CAM` với chỉ thị `SC1` (Xâm nhập vòng cấm) sẽ ghi nhiều bàn thắng từ tuyến 2 hơn khi đá `LCM` lùi sâu.
* **Quy trình:** Đá 10 trận ở CAM (Wirtz dạt LAM) và 10 trận ở LCM (Wirtz đá CAM). Ghi nhận số cú sút trúng đích và số bàn thắng.

### Test Case #2: Hiệu quả của V. Boniface (AR2 làm tường vs AR1 xẻ nách)
* **Giả thuyết:** Với thể hình 1m90 và sức mạnh vượt trội, Boniface cài `AR2` sẽ tăng tỷ lệ kiểm soát bóng của toàn đội và kiến tạo nhiều hơn `AR1`.
* **Quy trình:** Đá 10 trận với `AR2` và 10 trận với `AR1`. Đối chiếu tỷ lệ chuyền thành công và số pha dứt điểm của 3 hộ công phía sau.

### Test Case #3: Độ an toàn của Thủ Môn Mailson
* **Giả thuyết:** Mailson (1m97) bắt các pha sút xa ZD ổn định hơn W. Hennessey (1m98) nhờ bộ chỉ số phản xạ và đổ người của mùa thẻ mới hơn.
* **Quy trình:** Luân phiên mỗi thủ môn 15 trận, theo dõi số bàn thua từ ngoài vòng 16m50.

---

## 4. 🔄 QUY TRÌNH NGHIÊN CỨU LẶP KHI CÓ BẢN CẬP NHẬT MỚI (RESEARCH LOOP)

Khi Garena hoặc Nexon phát hành Gameplay Patch mới:

```
[BƯỚC 1] Quét Thông Báo Chính Thức (Garena Patch Notes / Nexon Dev Notes)
   ↓
[BƯỚC 2] Quét Diễn Đàn Inven 감독모드 (Tìm các bài phân tích meta đầu tiên của Ranker)
   ↓
[BƯỚC 3] Đối Chiếu Với Sổ Bộ Tri Thức Hiện Tại (File FC_ONLINE_GLXH_KNOWLEDGE.md)
   ↓
[BƯỚC 4] Đánh Dấu Lỗi Thời (Gắn tag OUTDATED_PATCH cho các claims bị ảnh hưởng)
   ↓
[BƯỚC 5] Cập Nhật Tag Patch Mới & Gắn Nhãn RETEST_REQUIRED Cho Các Chiến Thuật Cần Thử Nghiệm
   ↓
[BƯỚC 6] Tuyệt Đối Lưu Lịch Sử (Không xóa các findings cũ, chuyển vào mục Historical Archive)
```
