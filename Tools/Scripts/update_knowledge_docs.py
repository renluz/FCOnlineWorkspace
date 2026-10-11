import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update FC_ONLINE_GLXH_KNOWLEDGE.md
with open('E:/FCOnlineWorkspace/Research/FC_ONLINE_GLXH_KNOWLEDGE.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix tactic codes in FC_ONLINE_GLXH_KNOWLEDGE.md
text = text.replace('`DP1 (Tập trung trung lộ)`: Giữ cự ly kết nối phản công, tiết kiệm thể lực.', '`DP2 (Luôn ở trên)`: Giữ cự ly phản công, không lùi về phòng ngự, tiết kiệm thể lực. (Lưu ý: DP1 là lùi về phòng ngự).')
text = text.replace('`DB1 (Cắt đường chuyền)` + `DP2 (Bảo vệ trung lộ)`', '`DB1 (Cắt đường chuyền)` + `DP1 (Tập trung ở trung lộ)`')
text = text.replace('cặp CDM `AS1` + `DP2`', 'cặp CDM `AS1` + `DP1`')
text = text.replace('1. **`4-2-3-1` (Vua Sơ Đồ GLXH):**', '1. **`4-2-3-1` (CURRENT_BASELINE - Đóng Băng Trung Tuyến):**')
text = text.replace('## 7. 🧬 HÌNH THÁI CẦU THỦ (PLAYER AI ARCHETYPES)', '''## 7. 🧬 HÌNH THÁI CẦU THỦ (ANALYTICAL ARCHETYPES)
> **DISCLAIMER KỸ THUẬT:** Các Archetype (`TARGET_MAN_ST`, `ANCHOR_CDM`, `STOPPER_CB`, v.v.) là mô hình phân loại học phân tích (Analytical Taxonomy) do cộng đồng và chuyên gia thiết lập nhằm mô hình hóa chiến thuật, **KHÔNG PHẢI là class AI nội bộ được EA Sports hay Nexon xác nhận**.''')
text = text.replace('## 15. 🌏 KHÁC BIỆT GIỮA SERVER VIỆT NAM (GARENA) & HÀN QUỐC (NEXON)', '''## 15. 🌏 GIẢ THUYẾT KHÁC BIỆT SERVER VIỆT NAM & HÀN QUỐC (COMMUNITY_HYPOTHESIS | Confidence: LOW/MEDIUM)
> **LƯU Ý:** Đây hoàn toàn là quan sát và giả thuyết từ cộng đồng người chơi (Community Observation), KHÔNG PHẢI dữ liệu khẳng định từ Nexon/Garena. Hiện tại chưa có bằng chứng thực nghiệm chứng minh gameplay engine có sự phân hóa mã nguồn giữa 2 cụm máy chủ.''')

with open('E:/FCOnlineWorkspace/Research/FC_ONLINE_GLXH_KNOWLEDGE.md', 'w', encoding='utf-8') as f:
    f.write(text)
print('Updated FC_ONLINE_GLXH_KNOWLEDGE.md')

# 2. Update DECISION_RULES.md
with open('E:/FCOnlineWorkspace/Research/knowledge/DECISION_RULES.md', 'r', encoding='utf-8') as f:
    rules = f.read()

rules = rules.replace('`set_instructions`: `AR2` (Mục tiêu làm tường) + `DP1` (Tập trung trung lộ)', '`set_instructions`: `AR2` (Mục tiêu làm tường) + `DP2` (Luôn ở trên)')
rules = rules.replace('`set_instructions`: `AR1` (Xẻ nách phá bẫy) + `DP1` (Tập trung trung lộ) + `SR1` (Đè mép việt vị)', '`set_instructions`: `AR1` (Xẻ nách phá bẫy) + `DP2` (Luôn ở trên) + `SR1` (Đè mép việt vị)')
rules = rules.replace('`AS1` (Ở lại phía sau) + `DB1` (Cắt đường chuyền) + `DP2` (Bảo vệ trung lộ)', '`AS1` (Ở lại phía sau) + `DB1` (Cắt đường chuyền) + `DP1` (Tập trung ở trung lộ)')
rules = rules.replace('`AS Mặc định` + `IN1` (Đánh chặn chủ động) + `DP2` (Bảo vệ trung lộ)', '`AS Mặc định` + `IN1` (Đánh chặn chủ động) + `DP1` (Tập trung ở trung lộ)')

with open('E:/FCOnlineWorkspace/Research/knowledge/DECISION_RULES.md', 'w', encoding='utf-8') as f:
    f.write(rules)
print('Updated DECISION_RULES.md')

# 3. Update CONTRADICTIONS.md
with open('E:/FCOnlineWorkspace/Research/knowledge/CONTRADICTIONS.md', 'r', encoding='utf-8') as f:
    contr = f.read()

contr = contr.replace('BẮT BUỘC cài `AS1` + `DB1` + `DP2`', 'BẮT BUỘC cài `AS1` + `DB1` + `DP1`')
contr = contr.replace('### 🔍 Giải Mã & Nguyên Tắc Hòa Giải (Reconciliation):', '### 🔍 Tình Trạng Tranh Luận: UNRESOLVED (Phụ thuộc cấu trúc nhân sự cụ thể)')
contr = contr.replace('### 🔍 Giải Mã & Nguyên Tắc Hòa Giải:', '### 🔍 Tình Trạng Tranh Luận: UNRESOLVED (Phụ thuộc sơ đồ và chỉ số hậu vệ)')

with open('E:/FCOnlineWorkspace/Research/knowledge/CONTRADICTIONS.md', 'w', encoding='utf-8') as f:
    f.write(contr)
print('Updated CONTRADICTIONS.md')
