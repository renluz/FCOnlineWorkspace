# NEXT_TASKS — Codex Work Queue

## P0 — Audit hiện trạng repo
1. Đọc tất cả file knowledge hiện có.
2. Tìm claim tactic code sai / unsupported.
3. Không xóa; đánh dấu invalid và tạo migration/audit report.
4. Kiểm tra script validator hiện có.

Output:
- `KNOWLEDGE_AUDIT_REPORT.md`
- `knowledge/tactics/TACTIC_VALIDITY_MATRIX.csv`
- `tools/validate_knowledge_claims.py` (nếu chưa có)

## P0 — Current inventory registry
Tạo/cập nhật một source-of-truth:
`data/vn_owned_players.json`

Phải phân biệt:
- `confirmed_starting_xi`
- `owned_inventory`
- `candidate_xi`

Mỗi record:
- player_name
- season
- enhancement
- displayed_ovr
- salary
- natural_position
- source
- last_seen_date
- notes

Không suy season từ card art nếu không chắc.

## P1 — Exact-card AI evidence
Tạo:
`research/exact_card_ai/EXACT_CARD_AI_MATRIX.csv`

Fields:
- player
- season
- enhancement_if_relevant
- position
- patch
- server
- source_url
- source_date
- reported_rank
- behavior_claim
- evidence_type
- confidence

Ưu tiên current patch / 2026.

## P1 — Formation candidates
So sánh:
- `4-2-3-1`
- `4-1-2-3-0`
- `4-1-4-1`

Không rank bằng cảm giác.
Tạo:
`research/formations/CURRENT_SQUAD_FORMATION_FIT.md`

Đánh giá:
- role fit
- salary fit
- exact-card AI evidence
- chống sút xa / Zone 14
- transition defense
- chance creation
- use of +8/+9 cards

## P1 — FFZik read-only stats
Nếu chưa làm:
- UIA/Win32/file-log audit
- ưu tiên local file nếu có
- fallback UIA
- OCR chỉ cuối cùng

Không click / send key / đổi tactic.
Output:
- `tools/ffzik_stats_watcher.py`
- `tools/glxh_quick_test.py`
- `FFZIK_QUICK_TEST_REPORT.txt`

## P2 — VN market
Tạm không build TTCN crawler nếu không có nguồn hợp lệ.
Chỉ ingest:
- user screenshots
- read-only local/public VN data
- manual CSV

Không dùng KR price để auto-buy/recommend.

## Definition of done
- Không còn recommendation dùng invalid tactic code.
- Current XI/inventory/candidate được tách riêng.
- Mọi AI claim season-specific có provenance.
- Report tiếng Việt, ngắn gọn, có confidence.
