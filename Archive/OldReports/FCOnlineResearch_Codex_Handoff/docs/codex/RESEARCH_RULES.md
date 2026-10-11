# RESEARCH_RULES — Evidence & Data Policy

## Evidence hierarchy
Ưu tiên:
1. `OWN_ACCOUNT_EMPIRICAL` cùng patch hiện tại
2. `OFFICIAL_GAME_FACT` — Garena/NEXON
3. `HIGH_RANK_MANAGER_OBSERVATION` — ranker Manager Mode có ngữ cảnh rõ
4. `COMMUNITY_OBSERVATION`
5. `MODEL_INFERENCE`

## Exact-card rule
Mọi đánh giá AI phải cố gắng định danh:
`player_name + season + enhancement + position + patch`

Ví dụ:
- Không ghi `Son AI tốt`.
- Ghi `Son FC +X ở ST/LW, Manager Mode, patch ... — community observed`.

Không được lấy evidence của `Matić RTN` áp cho `Matić VTR`.
Không được lấy evidence của một season Goretzka áp cho season khác.

## VN availability
Card chỉ được dùng trong shortlist mua nếu:
- user thấy trên TTCN VN, hoặc
- nguồn Garena VN xác nhận phát hành.

`vn.fifaaddict.com` có thể dùng để đọc metadata/stat/trait, nhưng **không tự động chứng minh card đang tradable/available trên Garena VN**.

## Market
- `VN_LIVE_MARKET` > mọi giá web.
- Giá KR chỉ dùng tham khảo tương đối.
- Nếu không có live VN price: ghi `PRICE_UNVERIFIED`.
- Không đề xuất farm/chuyển BP giữa account bằng giao dịch dàn xếp.

## Patch awareness
Mọi claim gameplay nhạy patch phải gắn patch/date.
Khi có gameplay update mới:
- mark claim cũ `PREVIOUS_PATCH`
- nếu ảnh hưởng movement/passing/defending/shooting/traits/tactics: `RETEST_REQUIRED`

## Manager Mode sources
Ưu tiên:
- Inven `감독모드`
- Garena / FCVN GLXH
- user-supplied Facebook group data
- YouTube có transcript/rank/tactic evidence

Reddit:
- chỉ dùng thread đúng FC Online / FIFA Online 4 PC,
- loại FUT Mobile / FC Mobile / EA FC Career.

## Decision style
Không dùng:
- “best” / “optimal” nếu chưa có own-account data
- AI score giả tạo
- kết luận causal từ 1 review

Dùng:
- `CURRENT_BASELINE`
- `CANDIDATE`
- `HIGH_RANK_OBSERVED`
- `UNTESTED_HYPOTHESIS`
- `OWN_ACCOUNT_PREFERRED` khi có empirical evidence.

## A/B testing
Ưu tiên interleaved blocks:
A 5 trận → B 5 → A 5 → B 5...
Không chạy hết A rồi mới B nếu muốn giảm bias thời gian/rank.

Mốc:
- <10 mỗi variant: insufficient
- 10–19: early signal
- 20–29: moderate
- >=30: stronger sample

Không bắt user gửi ảnh/video mỗi trận.
Ưu tiên FFZik/local read-only stats capture.
