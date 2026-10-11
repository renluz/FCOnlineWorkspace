# CURRENT_STATE — FC Online GLXH

Cập nhật ngữ cảnh: 2026-09-19 (VN / Garena).

## 1. Mục tiêu người dùng
Người dùng muốn tối ưu **Giả Lập Xếp Hạng**, không phải đá tay.
Mục tiêu cao nhất:
- đội hình có thể yếu/rẻ hơn đối thủ nhưng vẫn có xác suất thắng tốt,
- hạn chế lỗi AI,
- che điểm yếu card,
- tận dụng cự ly/geometry/role fit,
- ưu tiên AI của đúng season/card hơn OVR thô.

Không mặc định copy đội top rank. Ranker chỉ là evidence để kiểm chứng.

## 2. Account / cap đã biết
- Salary cap: **305**
- User dùng FFZik để chạy GLXH.
- Dự án local:
  `E:\FCOnlineWorkspace\Research`

## 3. XI gần nhất đã xác nhận trực tiếp trong game
Đây là **last confirmed in-game XI**, không phải recommendation mới nhất:

Formation: `4-2-3-1`
Salary: khoảng `304/305`

- ST: V. Boniface WS +3 — OVR ~124 — salary 28
- LAM: N. Gonzalez PTG +3 — OVR ~123 — salary 26
- CAM: F. Lampard FAC +3 — OVR ~128 — salary 32
- RAM: F. Wirtz 25 +1 — OVR ~123 — salary 29
- LDM: W. Zaïre-Emery 26TS +1 — OVR ~121 — salary 30
- RDM: N. Matić VTR +12 — OVR ~128 — salary 19
- LB: J. Gvardiol — OVR ~122 — salary 29
- LCB: Ricardo Carvalho WG +4 — OVR ~128 — salary 29
- RCB: W. Saliba PTG +2 — OVR ~121 — salary 26
- RB: G. Zambrotta WG +1 — OVR ~123 — salary 30
- GK: Mailson 26TS +1 — OVR ~122 — salary 26

Coach currently observed previously: Park Tae Ha.

## 4. Inventory mới đáng chú ý
Các thẻ user vừa mở / đã cho xem, chưa chắc đã được lắp XI:
- F. Mendy CU +8 — LB — OVR ~127 — salary 26
- K. Casteels 23HW +9 — GK — OVR ~124 — salary 20
- Yuri Berchiche +9 — LB — OVR ~124 — salary 23
- J. Litmanen CC +8 — CAM — OVR ~120 — salary 23
- Álvaro García +8 — LW — OVR ~122 — salary 23
- S. Gerrard UT +8 — CM — OVR ~125 — salary 27
- S. McTominay 25TS +1 — CM — OVR ~120 — salary 30
- D. Šuker WG +3 — ST — OVR ~124 — salary 32
- Doku 25 +3
- Gündoğan BLD +7
- Lukaku PTG +5
- Ricardo Carvalho WG +1 (duplicate/other copy)
- Campbell WG +1
- Kilman 25DP +1
- Thomasson 26TS +1
- Beckham WG +1
- Zalazar 26TS +1
- Gullit FAC +1
- Son PTG +1

## 5. Candidate formation đang được nghiên cứu — CHƯA xác nhận in-game
Một candidate gần nhất:
`4-1-2-3-0` / zero-ST style

Ý tưởng:
- LAM: Gonzalez
- CAM: Lampard
- RAM: Wirtz
- LCM: Gerrard UT +8
- RCM: McTominay 25TS
- CDM: Matić VTR +12
- LB: Mendy CU +8
- CB: Carvalho + Saliba
- RB: Zambrotta
- GK: Casteels +9

**Status: CANDIDATE / UNTESTED.**
Không được ghi thành “optimal” cho tới khi user áp dụng và có data.

## 6. Baseline 4-2-3-1 chống sút xa
Sau trận thua 1-4 trước 4-2-2-1-1, shot map cho thấy đối thủ có nhiều pha dứt điểm sạch ở trung lộ/rìa box.

Baseline đã đề xuất:
- Defensive style: `Áp lực khi xử lý bóng lỗi`
- Width: `4`
- Depth: `5`
- Build-up: `Chuyền ngắn`
- Chance creation: `Cân bằng`
- Attacking width: `5`
- Players in box: `4`
- Corners: `2`
- Free kicks: `2`

Status: **baseline hypothesis**, chưa đủ sample để gọi optimal.

## 7. Mục tiêu mua sắm / rebuild
Người dùng từng đặt ngân sách giả định **4 tỷ BP** để nghiên cứu xây lại đội.
Quy tắc:
- không quan tâm BP đang hiện trong acc khi làm bài toán ngân sách 4B,
- nhưng quyết định availability/price phải dựa TTCN VN,
- không dùng KR price để kết luận mua.

Casemiro CU +8 đã được user xác nhận có hàng trên VN khoảng 247–249M ở thời điểm chụp.
McTominay 25TS trên TTCN VN không có người bán, nhưng user sau đó tự mở được +1.

## 8. Insight quan trọng
- AI có thể khác theo **season/card**, không chỉ theo tên cầu thủ.
- Stat đẹp không đảm bảo AI Manager Mode tốt.
- `EXACT_CARD_AI` là gap nghiên cứu quan trọng.
- Team Color cần tính khi rebuild, nhưng không được để Team Color ép cầu thủ đá sai role.
