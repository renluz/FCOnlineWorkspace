# Tham chiếu Chỉ số ẩn và HLV kỹ năng FC Online VN

**Ngày xác minh:** 20/09/2026  
**Phạm vi:** client FC Online VN và cơ chế Garena VN có hiệu lực từ 03/08/2026; NEXON chỉ dùng làm lịch sử/tham chiếu.

## Cách phân biệt

| Hệ thống | Ý nghĩa |
|---|---|
| Chỉ số ẩn gốc | Có sẵn trên exact card từ khi phát hành. |
| Đặc tính thường nhận thêm | Một ô mở từ +5. Pool phải kiểm tra trên exact card/client. |
| Chỉ số ẩn Vàng | Nhóm trait cấp cao như Chuyên Gia Đeo Bám, Bậc Thầy Chạy Chỗ. Mùa thường mở ở +11; nhóm mùa đặc biệt mở ở +7. |
| HLV kỹ năng | Hệ kỹ năng HLV, không phải chỉ số ẩn. Theo bản Garena VN 03/08/2026, ô theo mức thẻ mở ở +8. |

## Quy tắc theo mức cộng hiện hành

- **Mùa thường:** +5 chọn 1 Chỉ Số Ẩn Thường; +8 chọn thêm 1 HLV Kỹ năng; +11 chọn thêm 1 Chỉ số ẩn Vàng.
- **Mùa đặc biệt — 26TOTY winner, PRIME, Infinite Prime, ICON TM:** +5 chọn 1 Chỉ Số Ẩn Thường; +7 chọn thêm 1 Chỉ số ẩn Vàng; +8 chọn thêm 1 HLV Kỹ năng.
- Cách gọi mức thẻ: +8 là **Mạ Vàng**, +11–+13 là **Bạch Kim**. “Mạ Bạc” cho +5 được giữ là cách gọi cộng đồng/marketing; bản tin 03/08 không trực tiếp đặt tên mức +5.
- **GK +8:** chỉ chọn trait mới dành cho GK; nếu exact card đã có trait mới GK đó thì không được nhận trùng.

Khi client hiện **`(Đã chọn)`**, các trường hợp đã xác minh trên tài khoản này cho thấy đó là trait gốc đã có và không thể chọn lại. Sau patch lớn vẫn cần kiểm tra lại nếu giao diện đổi hành vi.

## Dữ liệu đã lưu

- `hidden_traits_vi.json`: 32 trait gốc/Chỉ Số Ẩn Thường và 17 Chỉ số ẩn Vàng thế hệ mới; tên VN chưa xác minh để `null`, không tự dịch.
- `skill_coaches_vi.json`: 41 nhãn kỹ năng HLV đọc từ ảnh client VN.
- `upgrade_trait_rules.json`: quy tắc +5, +8, +11–+13 và lịch hiệu lực.
- `manager_trait_role_map.json`: phân tích GLXH theo 13 vai trò; đây là phân tích, không phải dữ liệu chính thức.
- `current_squad_trait_config.json`: cấu hình đã xác nhận của đội hiện tại.

## Tên đặc tính mới đã xác minh trực tiếp bằng tiếng Việt

| Tên VN | Tên gốc | Mô tả chính thức rút gọn |
|---|---|---|
| Sát Thủ Băng Cắt | Cross Poacher | Di chuyển nhanh tới điểm rơi khi có bóng tạt. |
| Bậc Thầy Chạy Chỗ | Line Breaker | Chạy không bóng phá tuyến và bẫy việt vị. |
| Cao Thủ Tắc Bóng | Wild Tackler | Tăng phạm vi tắc bóng đứng, kể cả từ phía sau. |
| Chuyên Gia Đeo Bám | Chaser | Tăng tốc bám đuổi trong 10 giây sau khi đối phương phản công. |

Các nhãn Hàn/Anh như Acrobatic Finisher, Speedster, Titan, Commander, Blocker, Trickster, Laser Shooter, Predator và nhóm GK được giữ nguyên khi chưa thấy tên chính thức trong client/Garena VN.

## Ghi chú chất lượng

Ba tên kỹ năng HLV bị cắt một phần trong ảnh: `Cải thiện khả năng rê bóng khi đối mặt`, `Cải thiện khả năng sút xa trung bình`, `Xâm nhập ngay khi kêu gọi xâm nhập`. Database đánh dấu riêng để chụp lại client khi cần độ chính xác ký tự tuyệt đối. Mô tả cấp độ của phần lớn kỹ năng HLV chưa xuất hiện đầy đủ trong ảnh nên không được tự điền trị số.

## Nguồn chính

- [Garena VN: bộ chỉ số ẩn mới mùa Prime](https://fconline.garena.vn/chi-so-an-moi-mua-prime/)
- [Garena VN: điều chỉnh mốc mở khóa ngày 03/08/2026](https://fconline.garena.vn/ban-tin-cap-nhat-3-8-2026/)
- [Garena VN: cơ chế trải nghiệm trước ngày 12/06/2026](https://fconline.garena.vn/ban-tin-cap-nhat-12-06-2026/)
- [NEXON: cập nhật 28/08/2025, dữ liệu lịch sử](https://fconline.nexon.com/news/notice/view?bid=20250909215050265df0cbcef945e5873137_n&n4ArticleSN=5550)
- [NEXON: đặc tính mới tháng 01/2026](https://fconline.nexon.com/news/notice/view?n4ArticleSN=5769)
- [NEXON: đặc tính mới mùa hè 2026](https://fconline.nexon.com/news/notice/view?n4ArticleSN=5943)
- [NEXON: ô HLV bổ sung cho +11 đến +13](https://fconline.nexon.com/news/notice/view?n4ArticleSN=6006)
- Ảnh client VN do người dùng cung cấp và HTML thị trường VN lưu trong `../data/vn_market_raw_samples/`.

## Quy trình dùng cho exact card

1. Đọc trait gốc của đúng mùa thẻ và mức cộng.
2. Xác định mùa thường hay một trong bốn nhóm đặc biệt, rồi đọc ô được mở trong `upgrade_trait_rules.json`.
3. Loại mọi mục client đánh dấu `(Đã chọn)`.
4. Chỉ xếp hạng các mục thực sự xuất hiện trong pool exact card.
5. Đối chiếu vai trò trong `manager_trait_role_map.json` và cấu hình đội.
6. Chốt riêng một trait nhận thêm và một kỹ năng HLV; không trộn hai hệ thống.
