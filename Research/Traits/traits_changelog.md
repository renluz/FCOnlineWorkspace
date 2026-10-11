# Traits database changelog

## 2026-09-20 — 2.0.0

- Sửa cơ chế hiện hành theo bản tin Garena VN ngày 03/08/2026.
- Mùa thường: +5 Chỉ Số Ẩn Thường, +8 HLV Kỹ năng, +11 Chỉ số ẩn Vàng.
- Mùa đặc biệt 26TOTY winner, PRIME, Infinite Prime, ICON TM: +5 Chỉ Số Ẩn Thường, +7 Chỉ số ẩn Vàng, +8 HLV Kỹ năng.
- Chuyển cơ chế Garena 12/06/2026 và cơ chế NEXON cũ sang `superseded_rules` để không áp dụng nhầm.
- Đổi loại 17 đặc tính thế hệ mới thành `gold_hidden_trait`.

## 2026-09-20 — 1.0.1 (đã bị 2.0.0 thay thế)

- Bổ sung tên Team Color nâng cấp chính thức: Sóng bạc (+5), Sóng vàng (+8), Sóng bạch kim (+11).
- Bổ sung ngưỡng 5/8 cầu thủ và mức OVR tương ứng.
- Từng ghi theo nguồn NEXON rằng +8 không mở ô HLV và +11 không có hệ Chỉ số ẩn Vàng. Kết luận này không còn áp dụng cho Garena VN sau bản 03/08/2026.

## 2026-09-20 — Khởi tạo 1.0.0

- Tạo database trait gốc/legacy dựa trên danh mục Hàn và nhãn VN đã thấy trong client/market.
- Thêm 17 đặc tính mới được NEXON xác nhận qua các đợt 2025-06, 2025-08, 2026-01 và 2026-06.
- Chốt tên Garena VN: Sát Thủ Băng Cắt, Bậc Thầy Chạy Chỗ, Cao Thủ Tắc Bóng, Chuyên Gia Đeo Bám.
- Tạo danh mục 41 HLV kỹ năng từ ảnh client VN; đánh dấu ba tên bị cắt và mọi mô tả chưa đủ ảnh.
- Ghi lịch sử cơ chế +5/+8/+11 và bổ sung ô HLV cho +11–+13 từ 28/05/2026.
- Lưu quy tắc `(Đã chọn)` theo các trường hợp đã xác minh trên tài khoản người dùng.
- Lưu cấu hình đã áp dụng cho Havertz, Schweinsteiger, Lacroix, Koundé, Desailly; Dinkci và McTominay còn chờ xác nhận.
