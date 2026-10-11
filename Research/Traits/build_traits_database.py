import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATE = "2026-09-20"

SRC_CLIENT = {"type": "FC Online VN client", "ref": "user screenshots and observed exact labels", "verified_date": DATE}
SRC_LOCAL = {"type": "FC Online VN market HTML", "ref": "../data/vn_market_raw_samples/player_*_raw.html", "verified_date": DATE}
SRC_KO_DB = {"type": "Korean FC Online database export", "ref": "../repos/fconline-player-search/피온탐색기V2-1.py ALL_TRAITS", "verified_date": DATE}
SRC_GARENA_NEW = {"type": "Garena FC Online VN", "url": "https://fconline.garena.vn/chi-so-an-moi-mua-prime/", "verified_date": DATE}
SRC_NEXON_AUG25 = {"type": "NEXON official patch note", "url": "https://fconline.nexon.com/news/notice/view?bid=20250909215050265df0cbcef945e5873137_n&n4ArticleSN=5550", "verified_date": DATE}
SRC_NEXON_MAY26 = {"type": "NEXON official notice", "url": "https://fconline.nexon.com/news/notice/view?n4ArticleSN=6006", "verified_date": DATE}
SRC_NEXON_JAN26 = {"type": "NEXON official patch note", "url": "https://fconline.nexon.com/news/notice/view?n4ArticleSN=5769", "verified_date": DATE}
SRC_NEXON_JUN26 = {"type": "NEXON official update preview", "url": "https://fconline.nexon.com/news/notice/view?n4ArticleSN=5943", "verified_date": DATE}
SRC_GARENA_JUN26 = {"type": "Garena FC Online VN patch note", "url": "https://fconline.garena.vn/ban-tin-cap-nhat-12-06-2026/", "verified_date": DATE}
SRC_GARENA_AUG26 = {"type": "Garena FC Online VN patch note", "url": "https://fconline.garena.vn/ban-tin-cap-nhat-3-8-2026/", "verified_date": DATE}

def trait(id_, vi, ko, en, desc, selectable=False, category="original_trait", positions=None,
          aliases=None, vi_status="client_verified", notes=""):
    sources = [SRC_KO_DB]
    if vi:
        sources.insert(0, SRC_CLIENT)
    return {
        "id": id_, "name_vi": vi, "aliases": aliases or [], "name_ko": ko, "name_en": en,
        "description_vi": desc, "description_status": "verified_or_conservative_summary",
        "type": category, "selectable": selectable,
        "selectability_note": "Khả năng xuất hiện trong pool phải kiểm tra trên exact card/client; không suy từ tên trait." if selectable else "Không xác nhận là lựa chọn tự do ở +5.",
        "original_trait_possible": True, "positions": positions or [],
        "manager_mode_notes": notes, "name_vi_status": vi_status if vi else "unverified_no_translation",
        "sources": sources, "verified_date": DATE
    }

base = [
    trait("preferred_position", "Vị trí yêu thích", "선호포지션 고집", "Preferred position", "Ưu tiên hoạt động ở vị trí sở trường.", positions=["ALL"]),
    trait("long_throw_in", "Ném biên xa", "장거리 스로잉", "Long throw-in", "Ném biên xa hơn thông thường.", True, positions=["LB","RB"]),
    trait("dives", "Ăn vạ", "파울 유도 선호", "Tries to beat defensive line / draws fouls", "Có xu hướng tìm tình huống phạm lỗi có lợi.", True, positions=["ST","CAM","LM","RM"]),
    trait("injury_prone", "Dễ chấn thương", "유리몸", "Injury prone", "Nguy cơ chấn thương cao hơn.", positions=["ALL"], aliases=["Chấn thương"]),
    trait("solid_player", "Cứng như thép", "강철몸", "Solid player", "Khó chấn thương hơn.", True, positions=["ALL"]),
    trait("avoid_weak_foot", "Tránh sai chân thuận", "주발 선호", "Avoids weaker foot", "Ưu tiên dùng chân thuận.", True, positions=["ALL"]),
    trait("slide_tackle", "Xoạc bóng", "슬라이딩 태클 선호", "Dives into tackles", "Có xu hướng sử dụng xoạc bóng.", True, positions=["CB","LB","RB","CDM"], aliases=["Xoạc bóng ( AI )"]),
    trait("selfish", "Cá nhân", "개인 플레이 선호", "Selfish", "Có xu hướng giữ và tự xử lý bóng nhiều hơn.", True, positions=["ST","LM","RM"]),
    trait("argues", "Tranh cãi", "트러블 메이커", "Argues with officials", "Có xu hướng phản ứng/tranh cãi với quyết định trọng tài.", True, positions=["ALL"]),
    trait("early_crosser", "Tạt bóng sớm", "얼리 크로스 선호", "Early crosser", "Có xu hướng tạt sớm.", True, positions=["LB","RB","LM","RM"], aliases=["Tạt bóng sớm ( AI )"]),
    trait("finesse_shot", "Sút xoáy", "예리한 감아차기", "Finesse shot", "Cải thiện hoặc ưu tiên các pha cứa lòng.", True, positions=["ST","CAM","LM","RM"]),
    trait("flair", "Tinh tế", "화려한 개인기", "Flair", "Thực hiện các động tác và đường bóng kỹ thuật hơn.", True, positions=["ST","CAM","LM","RM"]),
    trait("long_passer", "Chuyền dài", "긴 패스 선호", "Long passer", "Ưu tiên hoặc cải thiện đường chuyền dài.", True, positions=["CB","CDM","CM"], aliases=["Chuyền dài ( AI )"]),
    trait("long_shot_taker", "Sút xa", "중거리 슛 선호", "Long shot taker", "Có xu hướng dứt điểm từ xa.", True, positions=["CM","CAM","ST"], aliases=["Sút xa ( AI )"]),
    trait("speed_dribbler", "Ma tốc độ", "스피드 드리블러", "Speed dribbler", "Có xu hướng rê bóng ở tốc độ cao.", True, positions=["ST","LM","RM"], aliases=["Ma tốc độ ( AI )"]),
    trait("playmaker", "Kiến tạo", "플레이 메이커", "Playmaker", "Có xu hướng làm trạm luân chuyển và kiến tạo.", True, positions=["CDM","CM","CAM"], aliases=["Kiến tạo ( AI )"]),
    trait("gk_rushes_out", None, "GK 공격 가담", "GK rushes out", "Tên tiếng Việt client chưa xác minh.", positions=["GK"]),
    trait("gk_puncher", None, "GK 능숙한 펀칭", "GK puncher", "Tên tiếng Việt client chưa xác minh.", positions=["GK"]),
    trait("gk_long_throw", None, "GK 멀리 던지기", "GK long throw", "Tên tiếng Việt client chưa xác minh.", positions=["GK"]),
    trait("power_header", "Đánh đầu mạnh", "파워 헤더", "Power header", "Tăng hiệu quả/uy lực đánh đầu.", True, positions=["CB","ST"]),
    trait("gk_one_on_one", None, "GK 침착한 1:1 수비", "GK one-on-one", "Tên tiếng Việt client chưa xác minh.", positions=["GK"]),
    trait("giant_throw_in", "Ném biên rất xa", "초 장거리 스로인", "Giant throw-in", "Ném biên xa hơn Ném biên xa.", True, positions=["LB","RB"]),
    trait("outside_foot", "Sút và tạt má ngoài", "아웃사이드 슈팅/크로스", "Outside foot shot/cross", "Cải thiện hoặc ưu tiên sút và tạt bằng má ngoài.", True, positions=["ST","CAM","LM","RM","LB","RB"]),
    trait("pass_master", "Thánh chuyền bóng", "패스마스터", "Pass master", "Cải thiện chất lượng các đường chuyền.", True, positions=["CB","CDM","CM","CAM"]),
    trait("never_give_up", "Nỗ lực đến cùng", "승부욕", "Competitive spirit", "Duy trì tinh thần thi đấu và nỗ lực trong trận.", True, positions=["ALL"]),
    trait("fancy_clearance", "Siêu cản phá", "화려한 걷어내기", "Fancy clearance", "Có xu hướng thực hiện pha phá/cản bóng đặc biệt.", True, positions=["CB","LB","RB"]),
    trait("chip_shot", "Bấm bóng", "칩슛 선호", "Chip shot", "Có xu hướng sử dụng dứt điểm bấm bóng.", True, positions=["ST","CAM"]),
    trait("technical_dribbler", "Qua người", "테크니컬 드리블러", "Technical dribbler", "Có xu hướng rê bóng kỹ thuật để vượt đối thủ.", True, positions=["ST","CAM","LM","RM"], aliases=["Qua người ( AI )"]),
    trait("sweeper_keeper", None, "스위퍼 키퍼", "Sweeper keeper", "Tên tiếng Việt client chưa xác minh.", positions=["GK"]),
    trait("gk_cautious_cross", None, "GK 소극적 크로스 수비", "GK cautious with crosses", "Tên tiếng Việt client chưa xác minh.", positions=["GK"]),
    trait("gk_aggressive_cross", None, "GK 적극적 크로스 수비", "GK comes for crosses", "Tên tiếng Việt client chưa xác minh.", positions=["GK"]),
    trait("second_wind", "Người không phổi", None, "Second wind", "Hỗ trợ duy trì/khôi phục thể lực theo cơ chế trait.", True, positions=["ALL"], aliases=[], vi_status="vn_market_verified"),
]

new_traits = [
    ("cross_poacher","Sát Thủ Băng Cắt","크로스 포처","Cross Poacher","Di chuyển nhanh đến điểm rơi trong tình huống tạt bóng.",["ST"],SRC_GARENA_NEW),
    ("line_breaker","Bậc Thầy Chạy Chỗ","라인 브레이커","Line Breaker","Di chuyển không bóng để phá hàng thủ, rõ nhất khi phá bẫy việt vị.",["ST","CAM","LM","RM"],SRC_GARENA_NEW),
    ("wild_tackler","Cao Thủ Tắc Bóng","와일드 태클러","Wild Tackler","Tăng phạm vi tắc bóng đứng, kể cả từ phía sau.",["CB","LB","RB","CDM"],SRC_GARENA_NEW),
    ("chaser","Chuyên Gia Đeo Bám","체이서","Chaser","Tăng tốc bám đuổi trong 10 giây sau khi đối phương phản công.",["CB","LB","RB","CDM"],SRC_GARENA_NEW),
    ("acrobat_finisher",None,"아크로바틱 피니셔","Acrobatic Finisher","Tên/mô tả tiếng Việt client chưa xác minh.",["ST"],SRC_NEXON_AUG25),
    ("two_hearts",None,"2개의 심장","Two Hearts","Tên/mô tả tiếng Việt client chưa xác minh.",["CM","CDM","LM","RM"],SRC_NEXON_AUG25),
    ("fighter",None,"파이터","Fighter","Tên/mô tả tiếng Việt client chưa xác minh.",["CB","CDM","CM"],SRC_NEXON_AUG25),
    ("gk_quick_reaction",None,"GK 빠른 반응","GK Quick Reaction","Tên/mô tả tiếng Việt client chưa xác minh.",["GK"],SRC_NEXON_AUG25),
    ("speedster",None,"스피드스터","Speedster","Sau một khoảng rê chậm, chuyển sang tăng tốc hoặc knock-on sẽ được tăng gia tốc; không kích hoạt với knock-on ở chạm đầu.",["ST","LM","RM"],SRC_NEXON_JAN26),
    ("titan",None,"타이탄","Titan","Tạo lợi thế thể chất trong tranh chấp bóng bổng; hai cầu thủ cùng có trait sẽ triệt tiêu hiệu ứng.",["CB","ST"],SRC_NEXON_JAN26),
    ("commander",None,"커맨더","Commander","Mở đường lobbed-through thấp, nhanh, có backspin khi đủ điều kiện; hạn chế theo khu vực, chân yếu và dạng chạm bóng.",["CB","CDM","CM"],SRC_NEXON_JAN26),
    ("blocker",None,"블로커","Blocker","Đọc thời điểm/quỹ đạo sút và chủ động đổ người chắn; hiệu quả phụ thuộc chỉ số.",["CB","CDM"],SRC_NEXON_JAN26),
    ("gk_aerial_control",None,"GK 공중볼 장악","GK Aerial Control","Tự chọn vị trí thuận lợi để can thiệp bóng tạt/lob thay vì đấm bóng thiếu an toàn; hiệu quả phụ thuộc chỉ số GK.",["GK"],SRC_NEXON_JAN26),
    ("trickster",None,"트릭스터","Trickster","Mở 4 động tác step-over mới và tăng hiệu quả 11 động tác hiện có.",["ST","CAM","LM","RM"],SRC_NEXON_JUN26),
    ("laser_shooter",None,"레이저 슈터","Laser Shooter","Khi bóng lăn tới từ hướng đối diện chiều tấn công, cú sút một chạm gần vạch cấm có quỹ đạo thấp và nhanh hơn.",["CM","CAM","ST"],SRC_NEXON_JUN26),
    ("predator",None,"프레데터","Predator","Tăng hiệu quả jockey chậm/nhanh khi ở gần người cầm bóng; hỗ trợ gia tốc khi chuyển sang sprint và giữ tư thế ổn định.",["CB","LB","RB","CDM"],SRC_NEXON_JUN26),
    ("gk_deadeye",None,"GK 데드아이","GK Deadeye","GK dự đoán quỹ đạo sút ở khoảng cách nhất định để chọn vị trí tốt hơn; tăng theo chỉ số vị trí và có lợi hơn cho GK thấp.",["GK"],SRC_NEXON_JUN26),
]
for id_,vi,ko,en,desc,pos,src in new_traits:
    base.append({"id":id_,"name_vi":vi,"aliases":[],"name_ko":ko,"name_en":en,"description_vi":desc,
                 "description_status":"official" if vi else "official_ko_name_only",
                 "type":"gold_hidden_trait","selectable":True,"selectability_note":"Thuộc pool Chỉ số ẩn Vàng. Từ 03/08/2026 tại máy chủ VN: mùa thường mở ở +11; 26TOTY winner, PRIME, Infinite Prime và ICON TM mở ở +7. Pool thực tế cần kiểm tra theo client/exact card.",
                 "original_trait_possible":True,"positions":pos,"manager_mode_notes":"Có áp dụng GLXH theo bảng NEXON; hiệu quả theo vai trò cần kiểm nghiệm.",
                 "name_vi_status":"garena_verified" if vi else "unverified_no_translation","sources":[src],"verified_date":DATE})

hidden = {
  "schema_version":"1.0.0","game":"EA SPORTS FC Online VN","game_version":"live service; verified through 2026-09-20",
  "verified_date":DATE,
  "scope_note":"Danh mục hợp nhất 32 trait gốc/Chỉ số ẩn Thường và 17 đặc tính thế hệ mới được quản lý trong nhóm Chỉ số ẩn Vàng theo cơ chế Garena VN từ 03/08/2026. Tên VN null nghĩa là chưa thấy nhãn client/Garena, không phải thiếu bản dịch.",
  "ui_rule":{"label":"(Đã chọn)","meaning":"Trong các trường hợp đã xác minh trên client tài khoản này: trait là đặc điểm gốc đã có và không thể chọn lại.","status":"account-client verified; recheck after patch if behavior changes"},
  "traits":base
}

coach_names = [
"Bậc thầy tốc độ","Chiến thuật chuyền Tiki-Taka","Chiến thuật chuyền trực tiếp","Chiến thuật tiền đạo áp lực",
"Cải thiện chuyền chọc khe","Chuyền chọc khe vượt tuyến","Cải thiện chuyền kỹ thuật","Cải thiện chuyền vượt tuyến",
"Cải thiện chuyền xuyên phá","Cải thiện chuyền xa","Cải thiện căng ngang","Cải thiện khả năng rê bóng khi đối mặt",
"Cải thiện khả năng sút xa trung bình","Cải thiện phòng thủ bên phải","Cải thiện phòng thủ bên trái","Cải thiện sút tầm thấp",
"Cải thiện sút xoáy","Cải thiện tạt bóng","Cải thiện tạt bóng cao","Cải thiện đá phạt","Cự ly đội hình ổn định",
"Di chuyển ngay khi đỡ bước 1","Khả năng khéo léo","Khả năng tắc bóng","Khả năng xoạc bóng",
"Phản công khi đang phòng thủ","Xâm nhập ngay khi kêu gọi xâm nhập","Sút cự ly gần","Tránh tắc bóng","Tránh xoạc bóng",
"Khả năng phòng thủ Pressing","TD mục tiêu đặc biệt","Tạo cơ hội ghi bàn","Tấn công với nhịp độ nhanh",
"Tập trung vào bên phải","Tập trung vào bên trái","Tập trung đánh chặn","Tổ chức","Xâm nhập vòng cấm","Áp lực","Áp đảo toàn sân"]

def coach_meta(name):
    attack = any(x in name for x in ["sút","Sút","tạt","Tạt","xâm nhập","Xâm nhập","Tiki","chuyền","Chuyền","tốc độ","khéo léo","ghi bàn","tiền đạo"])
    defend = any(x in name for x in ["phòng thủ","tắc bóng","xoạc bóng","đánh chặn","Áp lực","Pressing","Tổ chức","Cự ly"])
    if defend and not attack: pos=["CB","LB","RB","CDM","CM"]
    elif attack and not defend: pos=["ST","CAM","CM","LM","RM"]
    else: pos=["ALL"]
    return pos

coaches=[]
for i,name in enumerate(coach_names,1):
    uncertain = name in {"Cải thiện khả năng rê bóng khi đối mặt","Cải thiện khả năng sút xa trung bình","Xâm nhập ngay khi kêu gọi xâm nhập"}
    coaches.append({
      "id":f"coach_{i:02d}","name_vi":name,"aliases":[],"name_ko":None,"name_en":None,
      "description_vi":None if uncertain else f"Kỹ năng HLV tác động theo cơ chế ‘{name}’ hiển thị trong client; trị số chính xác phụ thuộc cấp kỹ năng.",
      "description_status":"name_partly_clipped_needs_client_recapture" if uncertain else "name_client_verified_description_not_fully_captured",
      "positions":coach_meta(name),"manager_mode_notes":"Đánh giá theo đúng vai trò và tổ hợp 3–4 kỹ năng; không đồng nhất với trait gốc.",
      "sources":[SRC_CLIENT],"verified_date":DATE
    })
skill_db={"schema_version":"1.0.0","game":"EA SPORTS FC Online VN","verified_date":DATE,
          "completeness":"41 nhãn quan sát trong giao diện; chưa tuyên bố đầy đủ toàn server vì không có danh mục Garena công khai có version.",
          "skill_coaches":coaches}

rules={
 "schema_version":"2.0.0","verified_date":DATE,"server":"Garena FC Online Việt Nam","effective_from":"2026-08-03",
 "current_rules":[
  {"card_group":"regular","classes_note":"Các mùa còn lại, gồm các ví dụ VTR, CU, 24EP, UT, GRU, WG, 25DP.","milestones":[
    {"enhancement":"+5","tier_name_vi":"Mạ Bạc","tier_name_status":"community/marketing convention; patch 03/08 does not explicitly name this tier","opens":{"ordinary_hidden_trait_slots":1,"coach_skill_slots":0,"gold_hidden_trait_slots":0}},
    {"enhancement":"+8","tier_name_vi":"Mạ Vàng","tier_name_status":"Garena verified","opens":{"ordinary_hidden_trait_slots":1,"coach_skill_slots":1,"gold_hidden_trait_slots":0}},
    {"enhancement":"+11 đến +13","tier_name_vi":"Bạch Kim","tier_name_status":"Garena verified","opens":{"ordinary_hidden_trait_slots":1,"coach_skill_slots":1,"gold_hidden_trait_slots":1}}
  ],"sources":[SRC_GARENA_AUG26]},
  {"card_group":"special","classes":["26TOTY winner","PRIME","Infinite Prime","ICON TM"],"milestones":[
    {"enhancement":"+5","opens":{"ordinary_hidden_trait_slots":1,"coach_skill_slots":0,"gold_hidden_trait_slots":0}},
    {"enhancement":"+7","opens":{"ordinary_hidden_trait_slots":1,"coach_skill_slots":0,"gold_hidden_trait_slots":1}},
    {"enhancement":"+8 trở lên","opens":{"ordinary_hidden_trait_slots":1,"coach_skill_slots":1,"gold_hidden_trait_slots":1}}
  ],"sources":[SRC_GARENA_AUG26]}
 ],
 "superseded_rules":[
   {"period":"2026-06-12 đến trước 2026-08-03","rule":"+8 trở lên được chọn 1 Chỉ số ẩn Vàng; +11 đến +13 mở thêm 1 ô HLV kỹ năng.","sources":[SRC_GARENA_JUN26]},
   {"period":"NEXON/KR 2025-08 đến 2026-05 reference","rule":"+5 đặc tính thường; +8 đặc tính mới; +11 tập trung huấn luyện và sau đó thêm kỹ năng HLV.","scope":"Không dùng làm cơ chế hiện hành cho Garena VN sau 03/08/2026.","sources":[SRC_NEXON_AUG25,SRC_NEXON_MAY26]}
 ],
 "classification":{"original_trait":"Có sẵn trên exact card.","ordinary_hidden_trait":"Chỉ Số Ẩn Thường; ô tùy chọn mở ở +5.","coach_skill":"HLV Kỹ năng; ô tùy chọn theo mức thẻ mở ở +8.","gold_hidden_trait":"Chỉ số ẩn Vàng; mùa thường mở ở +11, nhóm mùa đặc biệt mở ở +7."},
 "ui_selected_rule":hidden["ui_rule"]
}

roles={
"GK":{"excellent":["gk_quick_reaction","gk_one_on_one"],"useful":["gk_long_throw","gk_aggressive_cross","sweeper_keeper"],"avoid":["gk_cautious_cross"],"reason":"Ưu tiên phản xạ, 1v1 và chủ động xử lý khoảng trống."},
"CB stopper":{"excellent":["wild_tackler","chaser","power_header"],"useful":["solid_player","fancy_clearance","slide_tackle"],"avoid":["selfish","argues"],"reason":"Cần thắng va chạm và đoạt bóng sớm."},
"CB cover":{"excellent":["chaser","pass_master","long_passer"],"useful":["power_header","solid_player"],"avoid":["selfish","argues"],"reason":"Cần bọc lót tốc độ và phát triển bóng an toàn."},
"LB/RB stay-back":{"excellent":["chaser","wild_tackler"],"useful":["long_passer","early_crosser","solid_player"],"avoid":["selfish"],"reason":"Ưu tiên hồi vị trí, theo người và thoát pressing."},
"CDM anchor":{"excellent":["chaser","wild_tackler","pass_master"],"useful":["long_passer","solid_player","fighter"],"avoid":["selfish"],"reason":"Che chắn trung lộ và chuyền nhịp một."},
"CM box-to-box":{"excellent":["two_hearts","pass_master"],"useful":["long_passer","finesse_shot","solid_player"],"avoid":["injury_prone"],"reason":"Cần thể lực, chuyển trạng thái và chuyền ổn định."},
"CM creator":{"excellent":["playmaker","pass_master","long_passer"],"useful":["finesse_shot","outside_foot"],"avoid":["selfish"],"reason":"Ưu tiên tạo đường chuyền tiến triển."},
"CAM connector":{"excellent":["playmaker","pass_master"],"useful":["technical_dribbler","finesse_shot","outside_foot"],"avoid":["selfish"],"reason":"Làm trạm nối và trả bóng nhanh."},
"CAM hidden-ST":{"excellent":["line_breaker","finesse_shot","cross_poacher"],"useful":["chip_shot","outside_foot","technical_dribbler"],"avoid":[],"reason":"Tối ưu chạy chỗ và dứt điểm tuyến hai."},
"LM/RM winger":{"excellent":["speed_dribbler","early_crosser"],"useful":["technical_dribbler","outside_foot","line_breaker"],"avoid":["selfish"],"reason":"Tạo chiều rộng, bứt tốc và đưa bóng vào vùng cấm."},
"LM/RM wide creator":{"excellent":["pass_master","playmaker","early_crosser"],"useful":["long_passer","outside_foot"],"avoid":["selfish"],"reason":"Sáng tạo từ biên thay vì chỉ đua tốc."},
"ST target man":{"excellent":["power_header","cross_poacher"],"useful":["solid_player","pass_master","outside_foot"],"avoid":["injury_prone"],"reason":"Làm tường, chiếm điểm rơi và kết thúc bóng bổng."},
"ST runner":{"excellent":["line_breaker","chaser","finesse_shot"],"useful":["speed_dribbler","chip_shot","outside_foot"],"avoid":[],"reason":"Phá tuyến và chuyển cơ hội thành cú sút nhanh."}
}
role_db={"schema_version":"1.0.0","verified_date":DATE,"data_class":"Manager Mode analysis, not official game data","rating_scale":["Excellent","Useful","Neutral","Poor","Avoid"],"default_rating":"Neutral unless listed","roles":roles}

squad={"schema_version":"2.0.0","verified_date":DATE,"formation":"4-1-4-1-0 / zero-ST","status_rule":"Chỉ ghi confirmed_applied khi người dùng xác nhận đã chọn. recommended_unconfirmed không được coi là đang dùng.","players":[
{"card":"K. Havertz CU +8","ordinary_acquired_trait":"Kiến tạo","coach_skill":"Khả năng khéo léo","status":"confirmed_applied"},
{"card":"E. Dinkci 24EP +8","role":"LM winger/runner","recommendation":{"ordinary_hidden_trait":"Ma tốc độ","coach_skill":"Bậc thầy tốc độ","fallback_ordinary":"Tạt bóng sớm"},"status":"recommended_unconfirmed"},
{"card":"S. Gerrard UT +8","role":"LCM creator","recommendation":{"ordinary_hidden_trait":"Thánh chuyền bóng","coach_skill":"Cải thiện chuyền xuyên phá","fallback_coach":"Chiến thuật chuyền trực tiếp"},"status":"recommended_unconfirmed"},
{"card":"S. McTominay 25TS +5","role":"RCM balance/duel","recommendation":{"ordinary_hidden_trait":"Thánh chuyền bóng","fallback_ordinary":"Nỗ lực đến cùng"},"status":"recommended_unconfirmed"},
{"card":"B. Schweinsteiger HG +9","ordinary_acquired_trait":"Sút xoáy","coach_skill":"Khả năng khéo léo","status":"confirmed_applied"},
{"card":"N. Matić VTR +12","role":"single-pivot CDM anchor","recommendation":{"ordinary_hidden_trait":"Thánh chuyền bóng","coach_skill":"Tập trung đánh chặn","gold_hidden_trait":"Chủ Động Cản Phá","gold_name_vi_status":"garena_client_verified","gold_description":"Bay người cản phá cú sút."},"status":"confirmed_applied_gold_trait"},
{"card":"F. Mendy CU +8","role":"LB stay-back","recommendation":{"ordinary_hidden_trait":"Chuyền dài","coach_skill":"Cải thiện phòng thủ bên trái","fallback_ordinary":"Tạt bóng sớm"},"status":"recommended_unconfirmed"},
{"card":"M. Desailly WG +5","ordinary_acquired_trait":"Thánh chuyền bóng","status":"confirmed_applied"},
{"card":"R. Ferdinand DC +9","role":"RCB cover/recovery","recommendation":{"ordinary_hidden_trait":"Siêu cản phá","coach_skill":"Khả năng tắc bóng","fallback_ordinary":"Chuyền dài"},"status":"recommended_unconfirmed"},
{"card":"J. Koundé FAC +5","ordinary_acquired_trait":"Siêu cản phá","status":"confirmed_applied"},
{"card":"K. Casteels 23HW +9","role":"GK","recommendation":{"ordinary_hidden_trait":None,"coach_skill":None,"note":"Cần pool GK hiển thị trên exact card; database hiện chưa có đủ tên VN kỹ năng GK để chốt an toàn."},"status":"pool_required"},
{"card":"M. Lacroix 25DP +5","ordinary_acquired_trait":"Thánh chuyền bóng","status":"former_player_confirmed_configuration"}
]}

for name,obj in [("hidden_traits_vi.json",hidden),("skill_coaches_vi.json",skill_db),("upgrade_trait_rules.json",rules),("manager_trait_role_map.json",role_db),("current_squad_trait_config.json",squad)]:
    (ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

print(len(base),len(coaches))
