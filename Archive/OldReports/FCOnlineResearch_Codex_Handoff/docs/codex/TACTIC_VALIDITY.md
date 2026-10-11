# TACTIC_VALIDITY — Những gì đã xác nhận từ UI / official

Mục tiêu file này là ngăn Codex/Gemini/model **bịa mã tactic**.

## Position group đã xác nhận từ screenshot của user

### ST
Groups:
- `AR`
- `DP`
- `IN`
- `SR`

### CAM / LAM / RAM
Groups:
- `DS`
- `IN`
- `PF`
- `SC`

### LDM / RDM
Groups:
- `AS`
- `DB`
- `DP`
- `IN`

### LB / RB
Groups:
- `AR`
- `IN`
- `SR`

Không gán group ngoài danh sách trên nếu chưa có UI/source hiện tại.

## Official meanings đã dùng
Theo bài Garena về chiến thuật cá nhân:
- ST/CF/RF/LF:
  - `DP1` = luôn hỗ trợ phòng thủ
  - `DP2` = luôn ở trên
- CAM/LAM/RAM:
  - `PF2` = di chuyển rộng
  - LAM/RAM không sử dụng PF2
- CM/LCM/RCM/CDM/LDM/RDM:
  - `DP` = phòng thủ ở biên
  - `DP1` = tập trung ở trung lộ
  - `AS3` = đứng giữa các hậu vệ trong tình huống tấn công (context 4 hậu vệ)
- LB/RB/LWB/RWB:
  - `SR` = hỗ trợ xâm nhập cân bằng
  - `SR1` = di chuyển từ cánh vào trung tâm
  - `SR2` = phối hợp chồng cánh

## Current individual-tactic hypotheses
Các setup dưới đây là hypotheses, không phải official truth.

4-2-3-1:
- Matić RDM: anchor hypothesis
  - `AS1 / DB1 / DP1 / IN`
  - work rate `1/3`
- Zaïre LDM: mobile hypothesis
  - `AS / DB1 / DP1 / IN`
  - work rate `2/3`

Nếu chuyển sang hệ 1 CDM:
- Matić CDM:
  - ưu tiên giữ vị trí + cover center
  - exact remaining codes phải xác minh theo UI của position hiện tại.

## Do not do
- Không dùng `DP2` cho LDM/RDM nếu UI/current official không có.
- Không dùng `CC1` cho LAM nếu UI hiện tại chỉ có `DS/IN/PF/SC`.
- Không dịch một mã thành “stay back”, “free roam”, v.v. nếu không có mapping verified.
