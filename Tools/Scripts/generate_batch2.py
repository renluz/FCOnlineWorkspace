# -*- coding: utf-8 -*-
import json
import os

BASE_DIR = r"E:\FCOnlineWorkspace\SquadProject"

def write_json(filename, data):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Created {filename}")

# ==========================================
# 07_NORMAL_TRAITS_VI.json (23 Traits)
# ==========================================
NORMAL_TRAITS = [
  {"id": 1, "name_vi_exact": "Sút xoáy", "name_ko": "예리한 감아차기", "name_en": "Finesse Shot", 
   "description_vi": "Tăng độ cong và độ hiểm hóc cho các pha dứt điểm cứa lòng ZD.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Tăng độ cong và quỹ đạo xoáy khi sút ZD.", 
   "manager_observation": "Cực kỳ hiệu quả cho tiền đạo cánh và CAM khi dứt điểm từ rìa vòng cấm.", 
   "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_CREATOR"], "bad_roles": ["CB_STOPPER", "CB_COVER", "ANCHOR_CDM"], 
   "risks": "Gây lãng phí slot nếu gán cho cầu thủ phòng ngự.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  
  {"id": 2, "name_vi_exact": "Sút và tạt má ngoài", "name_ko": "아웃사이드 슈팅/크로스", "name_en": "Outside Foot Shot / Cross", 
   "description_vi": "Tự động sử dụng má ngoài chân thuận khi góc sút hoặc góc tạt không thuận lợi.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Kích hoạt dứt điểm và tạt bóng trivela.", 
   "manager_observation": "Hữu ích cho cầu thủ có chân không thuận kém (WF 3) để tránh dùng chân không thuận.", 
   "recommended_roles": ["WIDE_RUNNER", "WIDE_CREATOR"], "bad_roles": ["CB_COVER", "GK"], 
   "risks": "Có thể giảm độ căng của cú sút nếu so với dứt điểm chính diện.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 3, "name_vi_exact": "Đánh đầu mạnh", "name_ko": "파워 헤더", "name_en": "Power Header", 
   "description_vi": "Tăng uy lực đập bóng bằng đầu trong các pha không chiến và phạt góc.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Tăng lực đánh đầu phá bóng và dứt điểm.", 
   "manager_observation": "Must-have cho CB và ST trong GLXH để chống tạt cánh và ghi bàn phạt góc.", 
   "recommended_roles": ["CB_STOPPER", "CB_COVER", "STAY_BACK_FULLBACK / RECOVERY"], "bad_roles": ["WIDE_RUNNER"], 
   "risks": "Không có.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 4, "name_vi_exact": "Sút xa", "name_ko": "중거리 슛 선호", "name_en": "Long Shot Taker", 
   "description_vi": "Tăng xu hướng và độ chính xác của các cú nã đại bác từ cự ly ngoài vòng cấm.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Tăng độ căng và xác suất trúng đích sút xa.", 
   "manager_observation": "Cốt lõi cho CM và CAM trong GLXH, tạo đột biến cao khi đối thủ lùi sâu thủ xe buýt.", 
   "recommended_roles": ["CM_PROGRESSOR / SECOND_WAVE", "BOX_TO_BOX_CM"], "bad_roles": ["CB_STOPPER", "CB_COVER"], 
   "risks": "Cầu thủ có thể sút vội khi chưa có góc thuận lợi nếu stat sút xa thấp.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 5, "name_vi_exact": "Bấm bóng", "name_ko": "칩슛 선호", "name_en": "Chip Shot", 
   "description_vi": "Có xu hướng thực hiện cú tâng bóng qua đầu thủ môn khi đối mặt.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Tăng độ nhạy và quỹ đạo lốp bóng.", 
   "manager_observation": "Hiếm khi phát huy tối đa trong GLXH so với sút căng thông thường.", 
   "recommended_roles": ["CAM_CONNECTOR / FALSE_9"], "bad_roles": ["CB_STOPPER", "ANCHOR_CDM"], 
   "risks": "Dễ bị GK cao to bắt bài nếu quỹ đạo bóng đi chậm.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 6, "name_vi_exact": "Ném biên rất xa", "name_ko": "거대 스로인", "name_en": "Giant Throw-in", 
   "description_vi": "Tăng cự ly ném biên lên mức tối đa như một quả đá phạt góc.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Ném bóng thẳng vào vòng cấm từ đường biên.", 
   "manager_observation": "Tạo tình huống hỗn loạn trong vòng cấm đối phương.", 
   "recommended_roles": ["STAY_BACK_FULLBACK"], "bad_roles": ["CB_COVER", "GK"], 
   "risks": "Có thể gây mất bóng nguy hiểm nếu ném hỏng ở cự ly xa.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 7, "name_vi_exact": "Ném biên xa", "name_ko": "긴 스로인", "name_en": "Long Throw-in", 
   "description_vi": "Tăng tầm xa của các quả ném biên tiêu chuẩn.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Cải thiện cự ly ném biên.", 
   "manager_observation": "Ít hiệu quả chiến thuật hơn Ném biên rất xa.", 
   "recommended_roles": ["STAY_BACK_FULLBACK"], "bad_roles": ["CB_COVER", "GK"], 
   "risks": "Lãng phí slot nếu có lựa chọn phòng ngự tốt hơn.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 8, "name_vi_exact": "Thánh chuyền bóng", "name_ko": "플레이 메이커", "name_en": "Playmaker / Passer", 
   "description_vi": "Hút bóng về chân và tối ưu hóa nhãn quan, quỹ đạo phân phối bóng trên toàn sân.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Tăng chất lượng và độ mượt của các đường chuyền ngắn/trung bình.", 
   "manager_observation": "Trait quốc dân cho toàn bộ tuyến tiền vệ và trung vệ phát động tấn công trong Zero-ST.", 
   "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "CM_PROGRESSOR / SECOND_WAVE", "WIDE_CREATOR", "CB_STOPPER"], "bad_roles": ["GK"], 
   "risks": "Không có.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 9, "name_vi_exact": "Chuyền dài", "name_ko": "긴 패스 선호", "name_en": "Long Passer", 
   "description_vi": "Tăng xu hướng và độ chính xác của các đường chuyền bổng vượt tuyến và đảo cánh.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Cải thiện quỹ đạo bóng dài rơi đúng đà chạy của đồng đội.", 
   "manager_observation": "Chìa khóa mở khóa chiến thuật Chuyền Dài trong sơ đồ 4-1-4-1-0 phản công nhanh.", 
   "recommended_roles": ["CM_PROGRESSOR / SECOND_WAVE", "CB_COVER", "STAY_BACK_FULLBACK"], "bad_roles": ["WIDE_RUNNER"], 
   "risks": "Có thể chuyền hỏng nếu stat Chuyền dài gốc < 110.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 10, "name_vi_exact": "Tạt bóng sớm", "name_ko": "얼리 크로스 선호", "name_en": "Early Crosser", 
   "description_vi": "Tự động thực hiện các đường tạt bóng điểm rơi từ cự ly xa trước khi đến đáy biên.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Tăng quỹ đạo bóng cuộn vào nách trung vệ đối phương.", 
   "manager_observation": "Cực kỳ lợi hại khi phối hợp với các tiền đạo/tiền vệ băng cắt đợt hai.", 
   "recommended_roles": ["WIDE_RUNNER", "WIDE_CREATOR"], "bad_roles": ["CB_STOPPER", "CB_COVER", "ANCHOR_CDM"], 
   "risks": "Không phù hợp nếu lối chơi yêu cầu xuống sát đáy biên rồi trả ngược.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 11, "name_vi_exact": "Tinh tế", "name_ko": "화려한 개인기", "name_en": "Flair", 
   "description_vi": "Thực hiện các động tác khống chế bước một và chuyền bóng điệu nghệ, bất ngờ.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Tăng tỷ lệ xử lý bóng mềm mại trong không gian hẹp.", 
   "manager_observation": "Giúp CAM và cánh giữ thăng bằng và thoát pressing mượt mà.", 
   "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_RUNNER"], "bad_roles": ["CB_STOPPER", "CB_COVER"], 
   "risks": "Đôi khi làm rườm rà nhịp xử lý nếu bị pressing quá rát.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 12, "name_vi_exact": "Ma tốc độ", "name_ko": "스피드 드리블러", "name_en": "Speed Dribbler", 
   "description_vi": "Đẩy bóng dài và tăng tốc tối đa khi đang rê bóng dọc hành lang.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Tăng tốc độ di chuyển cùng quả bóng.", 
   "manager_observation": "Vũ khí hủy diệt cho các cầu thủ bám biên như Dinkci, Mendy.", 
   "recommended_roles": ["WIDE_RUNNER", "STAY_BACK_FULLBACK"], "bad_roles": ["ANCHOR_CDM", "CB_STOPPER"], 
   "risks": "Dễ bị CB đối phương bắt bài nếu đẩy bóng quá dài trong vòng cấm đông người.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 13, "name_vi_exact": "Qua người", "name_ko": "화려한 드리블", "name_en": "Technical Dribbler", 
   "description_vi": "Tăng sự mượt mà và khả năng luồn lách qua các hậu vệ đối phương.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Cải thiện rê bóng ngắn và chuyển hướng.", 
   "manager_observation": "Tốt cho CAM nhưng trong GLXH AI chuyền bóng quan trọng hơn rê dắt cá nhân.", 
   "recommended_roles": ["CAM_CONNECTOR / FALSE_9"], "bad_roles": ["CB_COVER", "ANCHOR_CDM"], 
   "risks": "Dễ bị đè bật nếu thể hình quá nhỏ bé.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 14, "name_vi_exact": "Cá nhân", "name_ko": "개인 플레이 선호", "name_en": "Selfish", 
   "description_vi": "Ưu tiên tự dứt điểm thay vì chuyền bóng cho đồng đội ở vị trí thuận lợi.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Tăng xu hướng tự tung ra cú sút.", 
   "manager_observation": "Cực kỳ nguy hiểm và gây hại cho lối chơi đồng đội của sơ đồ Zero-ST.", 
   "recommended_roles": [], "bad_roles": ["CAM_CONNECTOR / FALSE_9", "CM_PROGRESSOR / SECOND_WAVE", "WIDE_CREATOR"], 
   "risks": "PHÁ HỎNG LỐI CHƠI PHỐI HỢP NHÓM. CẤM TRANG BỊ TRONG GLXH.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 15, "name_vi_exact": "Siêu cản phá", "name_ko": "화려한 걷어내기", "name_en": "Fancy Clearance", 
   "description_vi": "Kích hoạt các pha bay người, ngả bàn đèn hoặc móc bóng giải nguy xuất thần trên vạch vôi.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Thực hiện động tác phá bóng nhào lộn cứu thua cận thành.", 
   "manager_observation": "Trait phòng ngự số 1 cho CB và Fullback; biến Ferdinand DC thành phiên bản ICON TM.", 
   "recommended_roles": ["CB_COVER", "CB_STOPPER", "STAY_BACK_FULLBACK / RECOVERY"], "bad_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_RUNNER"], 
   "risks": "Không có.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 16, "name_vi_exact": "Xoạc bóng", "name_ko": "슬라이딩 태클 선호", "name_en": "Dives Into Tackles", 
   "description_vi": "Tăng xu hướng thực hiện các pha trượt xoạc cản phá bóng.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Tự động bay người xoạc bóng khi đối thủ đột phá.", 
   "manager_observation": "Con dao hai lưỡi trong GLXH: rất dễ dẫn đến penalty oan hoặc thẻ đỏ.", 
   "recommended_roles": [], "bad_roles": ["CB_COVER", "CB_STOPPER", "ANCHOR_CDM"], 
   "risks": "NGUY CƠ BỊ PENALTY VÀ ĂN THẺ TRONG VÒNG CẤM GLXH RẤT CAO.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 17, "name_vi_exact": "Ăn vạ", "name_ko": "다이빙 선호", "name_en": "Diver", 
   "description_vi": "Có xu hướng ngã vờ kiếm phạt đền hoặc đá phạt khi có va chạm nhẹ.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Cố gắng đánh lừa trọng tài khi bị tì đè.", 
   "manager_observation": "Hoàn toàn vô dụng và phản tác dụng trong GLXH.", 
   "recommended_roles": [], "bad_roles": ["TẤT CẢ VỊ TRÍ"], 
   "risks": "Bị trọng tài phạt thẻ vàng và mất bóng vô duyên.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 18, "name_vi_exact": "Cứng như thép", "name_ko": "강철몸", "name_en": "Solid Player", 
   "description_vi": "Tăng độ lì đòn, giảm chấn thương và giữ trụ vững vàng trong tranh chấp tay đôi.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Giảm thiểu nguy cơ chấn thương và giữ thăng bằng va chạm.", 
   "manager_observation": "Tuyệt vời cho các vị trí cơ bắp cần tì đè đè bật đối thủ như McTominay, Desailly, Matić.", 
   "recommended_roles": ["BOX_TO_BOX_CM", "CB_STOPPER", "ANCHOR_CDM"], "bad_roles": [], 
   "risks": "Không có.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 19, "name_vi_exact": "Nỗ lực đến cùng", "name_ko": "승부욕", "name_en": "Second Wind", 
   "description_vi": "Hồi phục lại một phần thể lực khi bước vào những phút cuối trận hoặc khi đang bị dẫn bàn.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Hạn chế tình trạng tụt stat do cạn kiệt thanh thể lực.", 
   "manager_observation": "Cứu tinh cho các vị trí tiêu hao nhiều thể lực như Box-to-Box CM hay Winger.", 
   "recommended_roles": ["BOX_TO_BOX_CM", "WIDE_RUNNER"], "bad_roles": ["GK", "CB_COVER"], 
   "risks": "Không có tác dụng ở hiệp 1.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 20, "name_vi_exact": "Tranh cãi", "name_ko": "다혈질", "name_en": "Argues With Ref", 
   "description_vi": "Có xu hướng lao vào phản ứng với trọng tài khi bị thổi còi.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Tăng tính nóng nảy trên sân.", 
   "manager_observation": "Trait tiêu cực, làm chậm nhịp tổ chức phòng ngự.", 
   "recommended_roles": [], "bad_roles": ["TẤT CẢ VỊ TRÍ"], 
   "risks": "Nguy cơ ăn thẻ phạt ngu ngốc và mất tập trung vị trí.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 21, "name_vi_exact": "Kiến tạo", "name_ko": "킬패스 선호", "name_en": "Through Ball Passer", 
   "description_vi": "Tối ưu hóa các đường chọc khe sệt xuyên tuyến đặt tiền đạo vào thế đối mặt.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Tăng độ chuẩn xác và điểm rơi của chọc khe chìm.", 
   "manager_observation": "Vũ khí hủy diệt của Havertz CU +8 trong sơ đồ Zero-ST kiến thiết bóng cho Dinkci băng lên.", 
   "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_CREATOR"], "bad_roles": ["CB_COVER", "CB_STOPPER"], 
   "risks": "Cần đồng đội có tốc độ cao để đón bóng.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 22, "name_vi_exact": "Tránh sai chân thuận", "name_ko": "약발 기피", "name_en": "Avoids Using Weaker Foot", 
   "description_vi": "Luôn ưu tiên điều chỉnh tư thế để sử dụng chân thuận trong mọi pha bóng.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Giảm tần suất sử dụng chân không thuận.", 
   "manager_observation": "Chỉ dùng cho cầu thủ một kèo (Weak Foot 2 hoặc 1) để tránh dứt điểm hụt bằng chân gỗ.", 
   "recommended_roles": ["Cầu thủ Weak Foot <= 2"], "bad_roles": ["Cầu thủ hai chân 5-5", "Cầu thủ Weak Foot 4-5"], 
   "risks": "Làm chậm nhịp ra chân nếu bị hậu vệ ép đúng góc chân nghịch.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},

  {"id": 23, "name_vi_exact": "Vị trí yêu thích", "name_ko": "포지션 선호", "name_en": "Favorite Position", 
   "description_vi": "Tăng cường độ tập trung và tinh thần thi đấu khi được xếp đúng vị trí sở trường.", 
   "slot_type": "NORMAL_HIDDEN_TRAIT", "official_effect": "Duy trì phong độ ổn định xuyên suốt trận đấu.", 
   "manager_observation": "Tùy chọn an toàn khi cầu thủ chưa có trait chuyên biệt nào khác.", 
   "recommended_roles": ["TẤT CẢ VỊ TRÍ"], "bad_roles": [], 
   "risks": "Hiệu quả không đột biến bằng các trait kỹ thuật chuyên sâu.", "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"}
]

# ==========================================
# 08_SKILL_COACHES_VI.json (41 Coaches)
# ==========================================
SKILL_COACHES = [
  {"id": 1, "name_vi_exact": "Bậc thầy tốc độ", "name_ko": "질주 마스터", "name_en": "Sprint Master", "slot_type": "SKILL_COACH", "category": "Pace", "recommended_roles": ["WIDE_RUNNER"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 2, "name_vi_exact": "Chiến thuật chuyền Tiki-Taka", "name_ko": "티키타카 전술", "name_en": "Tiki-Taka Tactics", "slot_type": "SKILL_COACH", "category": "Passing", "recommended_roles": ["CAM_CONNECTOR / FALSE_9"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 3, "name_vi_exact": "Chiến thuật chuyền trực tiếp", "name_ko": "다이렉트 패스", "name_en": "Direct Passing", "slot_type": "SKILL_COACH", "category": "Passing", "recommended_roles": ["CM_PROGRESSOR / SECOND_WAVE"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 4, "name_vi_exact": "Chiến thuật tiền đạo áp lực", "name_ko": "전방 압박 전술", "name_en": "Forward Pressing Tactics", "slot_type": "SKILL_COACH", "category": "Pressing", "recommended_roles": ["CAM_CONNECTOR / FALSE_9"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 5, "name_vi_exact": "Cải thiện chuyền chọc khe", "name_ko": "스루 패스 향상", "name_en": "Through Pass Improvement", "slot_type": "SKILL_COACH", "category": "Passing", "recommended_roles": ["CAM_CONNECTOR / FALSE_9"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 6, "name_vi_exact": "Chuyền chọc khe vượt tuyến", "name_ko": "로빙 스루 향상", "name_en": "Over-the-Top Through Pass", "slot_type": "SKILL_COACH", "category": "Passing", "recommended_roles": ["CM_PROGRESSOR / SECOND_WAVE"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 7, "name_vi_exact": "Cải thiện chuyền kỹ thuật", "name_ko": "기술 패스 향상", "name_en": "Technical Pass Improvement", "slot_type": "SKILL_COACH", "category": "Passing", "recommended_roles": ["WIDE_CREATOR"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 8, "name_vi_exact": "Cải thiện chuyền vượt tuyến", "name_ko": "롱패스 향상", "name_en": "Long Pass Improvement", "slot_type": "SKILL_COACH", "category": "Passing", "recommended_roles": ["CB_COVER", "STAY_BACK_FULLBACK"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 9, "name_vi_exact": "Cải thiện chuyền xuyên phá", "name_ko": "침투 패스 향상", "name_en": "Penetrating Pass Improvement", "slot_type": "SKILL_COACH", "category": "Passing", "recommended_roles": ["CM_PROGRESSOR / SECOND_WAVE"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 10, "name_vi_exact": "Cải thiện chuyền xà", "name_ko": "낮은 패스 향상", "name_en": "Driven Pass Improvement", "slot_type": "SKILL_COACH", "category": "Passing", "recommended_roles": ["ANCHOR_CDM"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 11, "name_vi_exact": "Cải thiện căng ngang", "name_ko": "컷백 크로스 향상", "name_en": "Cutback Improvement", "slot_type": "SKILL_COACH", "category": "Crossing", "recommended_roles": ["WIDE_RUNNER"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 12, "name_vi_exact": "Cải thiện khả năng rê bóng khi…", "name_ko": "드리블 향상 (축약)", "name_en": "Dribble Under Pressure (Truncated)", "slot_type": "SKILL_COACH", "category": "Dribbling", "recommended_roles": ["CAM_CONNECTOR / FALSE_9"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 13, "name_vi_exact": "Cải thiện khả năng sút xa tru…", "name_ko": "중거리슛 향상 (축약)", "name_en": "Long Shot Improvement (Truncated)", "slot_type": "SKILL_COACH", "category": "Shooting", "recommended_roles": ["CM_PROGRESSOR / SECOND_WAVE"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 14, "name_vi_exact": "Cải thiện phòng thủ bên phải", "name_ko": "우측 수비 향상", "name_en": "Right Defense Improvement", "slot_type": "SKILL_COACH", "category": "Defending", "recommended_roles": ["STAY_BACK_FULLBACK / RECOVERY"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 15, "name_vi_exact": "Cải thiện phòng thủ bên trái", "name_ko": "좌측 수비 향상", "name_en": "Left Defense Improvement", "slot_type": "SKILL_COACH", "category": "Defending", "recommended_roles": ["STAY_BACK_FULLBACK"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 16, "name_vi_exact": "Cải thiện sút tầm thấp", "name_ko": "낮은 슛 향상", "name_en": "Low Shot Improvement", "slot_type": "SKILL_COACH", "category": "Shooting", "recommended_roles": ["CAM_CONNECTOR / FALSE_9"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 17, "name_vi_exact": "Cải thiện sút xoáy", "name_ko": "감아차기 향상", "name_en": "Curled Shot Improvement", "slot_type": "SKILL_COACH", "category": "Shooting", "recommended_roles": ["WIDE_CREATOR"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 18, "name_vi_exact": "Cải thiện tạt bóng", "name_ko": "크로스 향상", "name_en": "Crossing Improvement", "slot_type": "SKILL_COACH", "category": "Crossing", "recommended_roles": ["WIDE_CREATOR"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 19, "name_vi_exact": "Cải thiện tạt bóng cao", "name_ko": "높은 크로스 향상", "name_en": "High Cross Improvement", "slot_type": "SKILL_COACH", "category": "Crossing", "recommended_roles": ["WIDE_CREATOR"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 20, "name_vi_exact": "Cải thiện đá phạt", "name_ko": "프리킥 향상", "name_en": "Free Kick Improvement", "slot_type": "SKILL_COACH", "category": "Set Pieces", "recommended_roles": ["CM_PROGRESSOR / SECOND_WAVE"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 21, "name_vi_exact": "Cự ly đội hình ổn định", "name_ko": "재정비", "name_en": "Maintain Formation / Regroup", "slot_type": "SKILL_COACH", "category": "Positioning", "recommended_roles": ["CB_COVER", "ANCHOR_CDM"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 22, "name_vi_exact": "Di chuyển ngay khi đỡ bước 1", "name_ko": "퍼스트 터치 후 질주", "name_en": "Move Right After First Touch", "slot_type": "SKILL_COACH", "category": "Agility", "recommended_roles": ["WIDE_RUNNER"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 23, "name_vi_exact": "Khả năng khéo léo", "name_ko": "유연한 움직임", "name_en": "Agility / Dexterity", "slot_type": "SKILL_COACH", "category": "Agility", "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_CREATOR"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 24, "name_vi_exact": "Khả năng tắc bóng", "name_ko": "스탠딩 태클 향상", "name_en": "Standing Tackle Mastery", "slot_type": "SKILL_COACH", "category": "Defending", "recommended_roles": ["CB_COVER", "CB_STOPPER"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 25, "name_vi_exact": "Khả năng xoạc bóng", "name_ko": "슬라이딩 태클 향상", "name_en": "Sliding Tackle Mastery", "slot_type": "SKILL_COACH", "category": "Defending", "recommended_roles": [], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 26, "name_vi_exact": "Phản công khi đang phòng thủ", "name_ko": "수비 중 역습", "name_en": "Counter-attack on Defense", "slot_type": "SKILL_COACH", "category": "Transition", "recommended_roles": ["WIDE_RUNNER"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 27, "name_vi_exact": "Xâm nhập ngay khi kêu gọi xâm nhập", "name_ko": "침투 호출 시 즉각 침투", "name_en": "Instant Run on Call", "slot_type": "SKILL_COACH", "category": "Attacking", "recommended_roles": ["CAM_CONNECTOR / FALSE_9"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 28, "name_vi_exact": "Sút cự ly gần", "name_ko": "근거리 슛 향상", "name_en": "Close Range Shooting", "slot_type": "SKILL_COACH", "category": "Shooting", "recommended_roles": ["CAM_CONNECTOR / FALSE_9"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 29, "name_vi_exact": "Tránh tắc bóng", "name_ko": "태클 회피", "name_en": "Avoid Tackle", "slot_type": "SKILL_COACH", "category": "Dribbling", "recommended_roles": ["WIDE_RUNNER"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 30, "name_vi_exact": "Tránh xoạc bóng", "name_ko": "슬라이딩 태클 회피", "name_en": "Avoid Sliding Tackle", "slot_type": "SKILL_COACH", "category": "Dribbling", "recommended_roles": ["WIDE_RUNNER"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 31, "name_vi_exact": "Khả năng phòng thủ Pressing", "name_ko": "압박 수비 향상", "name_en": "Pressing Defense Mastery", "slot_type": "SKILL_COACH", "category": "Pressing", "recommended_roles": ["BOX_TO_BOX_CM"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 32, "name_vi_exact": "TD mục tiêu đặc biệt", "name_ko": "타겟맨 특화", "name_en": "Target Man Special", "slot_type": "SKILL_COACH", "category": "Attacking", "recommended_roles": ["CAM_CONNECTOR / FALSE_9"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 33, "name_vi_exact": "Tạo cơ hội ghi bàn", "name_ko": "찬스 메이킹", "name_en": "Chance Creation", "slot_type": "SKILL_COACH", "category": "Attacking", "recommended_roles": ["WIDE_CREATOR"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 34, "name_vi_exact": "Tấn công với nhịp độ nhanh", "name_ko": "빠른 템포 공격", "name_en": "Fast Tempo Attack", "slot_type": "SKILL_COACH", "category": "Attacking", "recommended_roles": ["WIDE_RUNNER"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 35, "name_vi_exact": "Tập trung vào bên phải", "name_ko": "우측 집중", "name_en": "Focus on Right Side", "slot_type": "SKILL_COACH", "category": "Tactical", "recommended_roles": ["WIDE_CREATOR"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 36, "name_vi_exact": "Tập trung vào bên trái", "name_ko": "좌측 집중", "name_en": "Focus on Left Side", "slot_type": "SKILL_COACH", "category": "Tactical", "recommended_roles": ["WIDE_RUNNER"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 37, "name_vi_exact": "Tập trung đánh chặn", "name_ko": "가로채기 집중", "name_en": "Focus on Interception", "slot_type": "SKILL_COACH", "category": "Defending", "recommended_roles": ["ANCHOR_CDM", "CB_COVER"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 38, "name_vi_exact": "Tổ chức", "name_ko": "조직력", "name_en": "Organization", "slot_type": "SKILL_COACH", "category": "Tactical", "recommended_roles": ["CB_COVER"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 39, "name_vi_exact": "Xâm nhập vòng cấm", "name_ko": "박스 침투", "name_en": "Box Penetration", "slot_type": "SKILL_COACH", "category": "Attacking", "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "BOX_TO_BOX_CM"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 40, "name_vi_exact": "Áp lực", "name_ko": "압박", "name_en": "Pressure", "slot_type": "SKILL_COACH", "category": "Pressing", "recommended_roles": ["BOX_TO_BOX_CM"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 41, "name_vi_exact": "Áp đảo toàn sân", "name_ko": "전방위 지배", "name_en": "All-Pitch Dominance", "slot_type": "SKILL_COACH", "category": "Dominance", "recommended_roles": ["BOX_TO_BOX_CM"], "sources": ["Client Garena VN Screenshot"], "confidence": "VERIFIED_CLIENT_VN"}
]

# ==========================================
# 09_GOLD_TRAITS_VI.json (14 Gold Traits)
# ==========================================
GOLD_TRAITS = [
  {"id": 1, "name_vi_exact": "Sát thủ băng cắt", "name_ko": "크로스 포쳐", "name_en": "Cross Poacher", "description_vi": "Di chuyển nhanh đến điểm rơi trong các tình huống tạt bóng.", "slot_type": "GOLD_HIDDEN_TRAIT", "official_effect": "Tăng tốc độ băng cắt và chọn vị trí đón bóng bổng từ biên.", "manager_observation": "Cực kỳ hiệu quả cho tiền đạo/tiền vệ cánh chạy chỗ đón tạt.", "recommended_roles": ["WIDE_RUNNER", "CAM_CONNECTOR / FALSE_9"], "bad_roles": ["CB_STOPPER", "CB_COVER", "ANCHOR_CDM"], "risks": "Không có.", "sources": ["Client Garena VN Screenshot media_1789882598336.png"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 2, "name_vi_exact": "Chuyên gia vô lê", "name_ko": "아크로바틱 피니셔", "name_en": "Acrobatic Finisher", "description_vi": "Thường xuyên tung ra các cú vô lê với tư thế ngả người móc bóng.", "slot_type": "GOLD_HIDDEN_TRAIT", "official_effect": "Tăng xác suất và uy lực dứt điểm vô lê ngả bàn đèn.", "manager_observation": "Tạo siêu phẩm bất ngờ khi đón bóng bật ra từ phạt góc.", "recommended_roles": ["CAM_CONNECTOR / FALSE_9"], "bad_roles": ["CB_COVER", "ANCHOR_CDM"], "risks": "Không có.", "sources": ["Client Garena VN Screenshot media_1789882598336.png"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 3, "name_vi_exact": "Bậc thầy không chiến", "name_ko": "공중전 지배자 / 타이탄", "name_en": "Aerial Master / Titan", "description_vi": "Cản trở cầu thủ đối phương trong các tình huống tranh chấp bóng bổng.", "slot_type": "GOLD_HIDDEN_TRAIT", "official_effect": "Giảm khả năng bật nhảy và thăng bằng của đối phương khi không chiến.", "manager_observation": "Biến trung vệ thành hòn đá tảng bất khả xâm phạm trên không.", "recommended_roles": ["CB_COVER", "CB_STOPPER", "ANCHOR_CDM"], "bad_roles": ["WIDE_RUNNER"], "risks": "Không có.", "sources": ["Client Garena VN Screenshot media_1789882598336.png"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 4, "name_vi_exact": "Dứt điểm 1 chạm", "name_ko": "원터치 피니셔", "name_en": "First Time Finisher", "description_vi": "Thực hiện cú sút trực tiếp với quỹ đạo thấp và nhanh khi bóng đến.", "slot_type": "GOLD_HIDDEN_TRAIT", "official_effect": "Tối ưu hóa độ hiểm của cú sút một chạm không cần khống chế.", "manager_observation": "Tận dụng đường căng ngang hạ gục thủ môn đối phương chớp nhoáng.", "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_RUNNER"], "bad_roles": ["CB_COVER", "CB_STOPPER"], "risks": "Không có.", "sources": ["Client Garena VN Screenshot media_1789882598336.png"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 5, "name_vi_exact": "Nhạc trưởng", "name_ko": "마에스트로", "name_en": "Maestro / Playmaker", "description_vi": "Tung đường chuyền chọc khe bổng thấp và nhanh có hiệu ứng xoáy.", "slot_type": "GOLD_HIDDEN_TRAIT", "official_effect": "Tạo đường chuyền QW sệt cuộn vượt qua tầm với trung vệ.", "manager_observation": "Vũ khí phản công số 1 cho CM/CAM phát động bóng cho Winger.", "recommended_roles": ["CM_PROGRESSOR / SECOND_WAVE", "WIDE_CREATOR", "CAM_CONNECTOR / FALSE_9"], "bad_roles": ["CB_STOPPER", "CB_COVER"], "risks": "Không có.", "sources": ["Client Garena VN Screenshot media_1789882598336.png"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 6, "name_vi_exact": "Siêu Bứt Tốc", "name_ko": "초가속 / 스피드스터", "name_en": "Rocket Sprint / Speedster", "description_vi": "Tăng tốc và đột phá vào khoảng trống trong khi rê bóng.", "slot_type": "GOLD_HIDDEN_TRAIT", "official_effect": "Cú rướn tốc độ bùng nổ khi bắt đầu dẫn bóng.", "manager_observation": "Bỏ rơi hậu vệ biên trong tích tắc khi mở tốc độ dọc biên.", "recommended_roles": ["WIDE_RUNNER"], "bad_roles": ["ANCHOR_CDM", "CB_COVER"], "risks": "Tiêu hao thể lực nếu lạm dụng.", "sources": ["Client Garena VN Screenshot media_1789882598336.png"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 7, "name_vi_exact": "Ảo thuật gia", "name_ko": "트릭스터", "name_en": "Trickster", "description_vi": "Sử dụng các kỹ năng cá nhân đa dạng để đánh lừa đối phương.", "slot_type": "GOLD_HIDDEN_TRAIT", "official_effect": "Tăng tốc độ xoay sở và qua người ảo diệu.", "manager_observation": "Hữu ích trong gameplay tay, trong GLXH cần kết hợp stat chuyền cao.", "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_CREATOR"], "bad_roles": ["CB_COVER", "CB_STOPPER"], "risks": "Bị điều chỉnh giảm tần suất spam trong patch mới.", "sources": ["Client Garena VN Screenshot media_1789882598336.png"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 8, "name_vi_exact": "Chặn đà tấn công", "name_ko": "공격 차단 / 파이터", "name_en": "Bruiser / Fighter", "description_vi": "Khi thực hiện tranh chấp sẽ làm giảm tốc độ bứt tốc và độ chính xác của đối thủ.", "slot_type": "GOLD_HIDDEN_TRAIT", "official_effect": "Áp sát làm đối phương chững lại và chuyền hỏng.", "manager_observation": "Rất mạnh cho tiền vệ phòng ngự và CB dập phá nhịp tấn công đối phương.", "recommended_roles": ["BOX_TO_BOX_CM", "CB_STOPPER", "ANCHOR_CDM"], "bad_roles": ["WIDE_RUNNER"], "risks": "Không có.", "sources": ["Client Garena VN Screenshot media_1789882598336.png"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 9, "name_vi_exact": "Bậc thầy chạy chỗ", "name_ko": "라인 브레이커", "name_en": "Line Breaker", "description_vi": "Di chuyển không bóng thông minh để phá vỡ hàng phòng ngự của đối thủ.", "slot_type": "GOLD_HIDDEN_TRAIT", "official_effect": "Phá bẫy việt vị và lẩn vào lưng trung vệ đối phương.", "manager_observation": "Cực phẩm cho lối chơi Zero-ST để CAM/Winger thoát xuống đối mặt.", "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_RUNNER"], "bad_roles": ["CB_COVER", "CB_STOPPER", "ANCHOR_CDM"], "risks": "Không có.", "sources": ["Client Garena VN Screenshot media_1789882602385.png"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 10, "name_vi_exact": "Chủ Động Cản Phá", "name_ko": "능동적 블록 / 블로커", "name_en": "Active Block / Blocker", "description_vi": "Bay người cản phá cú sút.", "slot_type": "GOLD_HIDDEN_TRAIT", "official_effect": "Tự động bay người hoặc quăng chân chặn đường sút xa và chọc khe.", "manager_observation": "ĐÃ XÁC MINH TRANG BỊ TRÊN MATIĆ VTR +12! Cứu thua vô số bàn thua sút xa trong GLXH.", "recommended_roles": ["ANCHOR_CDM", "CB_COVER", "CB_STOPPER"], "bad_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_RUNNER"], "risks": "Không có.", "sources": ["Client Garena VN Screenshot media_1789882602385.png"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 11, "name_vi_exact": "Siêu đánh chặn", "name_ko": "인터셉트", "name_en": "Super Intercept", "description_vi": "Thu hẹp khoảng cách với đối thủ để chặn các tình huống đột phá bằng rê bóng.", "slot_type": "GOLD_HIDDEN_TRAIT", "official_effect": "Tăng tốc độ thu hẹp khoảng cách và thò chân đoạt bóng khi đối thủ rê qua.", "manager_observation": "Khắc chế cứng các cầu thủ rê dắt khéo léo.", "recommended_roles": ["ANCHOR_CDM", "CB_COVER", "STAY_BACK_FULLBACK"], "bad_roles": ["CAM_CONNECTOR / FALSE_9"], "risks": "Không có.", "sources": ["Client Garena VN Screenshot media_1789882602385.png"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 12, "name_vi_exact": "Cao thủ tắc bóng", "name_ko": "와일드 태클러", "name_en": "Wild Tackler", "description_vi": "Tăng phạm vi thực hiện pha tắc bóng đứng, kể cả từ phía sau đối thủ.", "slot_type": "GOLD_HIDDEN_TRAIT", "official_effect": "Sải chân tắc bóng cực rộng, cướp bóng ngay sau lưng mà không phạm lỗi.", "manager_observation": "Cực kỳ bá đạo cho CB có chiều cao tốt như Ferdinand, Desailly.", "recommended_roles": ["CB_COVER", "CB_STOPPER", "STAY_BACK_FULLBACK / RECOVERY"], "bad_roles": ["CAM_CONNECTOR / FALSE_9"], "risks": "Không có.", "sources": ["Client Garena VN Screenshot media_1789882602385.png"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 13, "name_vi_exact": "Người không phổi", "name_ko": "무한 체력 / 2개의 심장", "name_en": "Relentless / Two Hearts", "description_vi": "Khi bứt tốc, thể lực tiêu hao ít hơn và việc giảm chỉ số do cạn thể lực diễn ra chậm hơn.", "slot_type": "GOLD_HIDDEN_TRAIT", "official_effect": "Bảo toàn chỉ số tốc độ và tranh chấp suốt 90 phút.", "manager_observation": "Giải quyết triệt để bài toán tụt thể lực ở hiệp 2 cho tiền vệ con thoi.", "recommended_roles": ["BOX_TO_BOX_CM", "WIDE_RUNNER"], "bad_roles": ["CB_COVER", "GK"], "risks": "Không có.", "sources": ["Client Garena VN Screenshot media_1789882602385.png"], "confidence": "VERIFIED_CLIENT_VN"},
  {"id": 14, "name_vi_exact": "Chuyên gia đeo bám", "name_ko": "체이서", "name_en": "Chaser", "description_vi": "Bám đuổi cầu thủ đối phương nhanh hơn khi họ phản công.", "slot_type": "GOLD_HIDDEN_TRAIT", "official_effect": "Tăng tốc độ thu hồi và đuổi bắt khi đội nhà bị phản công nhanh.", "manager_observation": "Cần thiết cho hậu vệ biên và tiền vệ phòng ngự khi dâng cao chống phản công.", "recommended_roles": ["STAY_BACK_FULLBACK", "ANCHOR_CDM"], "bad_roles": ["CAM_CONNECTOR / FALSE_9"], "risks": "Không có.", "sources": ["Client Garena VN Screenshot media_1789882602385.png"], "confidence": "VERIFIED_CLIENT_VN"}
]

# ==========================================
# 10_UPGRADE_RULES.json
# ==========================================
UPGRADE_RULES_DATA = {
  "_metadata": {
    "project": "FCOnlineSquadProject",
    "updated_at": "2026-09-20",
    "server": "Garena FC Online Việt Nam",
    "effective_from": "2026-08-03 (Bản cập nhật mùa hè)",
    "verification_status": "VERIFIED_CLIENT_VN"
  },
  "ui_slot_positions": {
    "slot_1_left": {
      "milestone": "+8",
      "type": "SKILL_COACH",
      "pool_name": "HLV kỹ năng",
      "total_count": 41,
      "icon_style": "Hexagon bạc có dấu [+]"
    },
    "slot_2_middle": {
      "milestone": "+11",
      "type": "GOLD_HIDDEN_TRAIT",
      "pool_name": "Chỉ số ẩn vàng",
      "total_count": 14,
      "icon_style": "Hexagon viền vàng / biểu tượng Kim cương [💎]"
    },
    "slot_3_right": {
      "milestone": "+5",
      "type": "NORMAL_HIDDEN_TRAIT",
      "pool_name": "Chỉ số ẩn thường",
      "total_count": 23,
      "icon_style": "Hexagon có dấu [+]"
    }
  },
  "upgrade_mechanisms": {
    "regular_cards": {
      "description": "Áp dụng cho tất cả các mùa thẻ thông thường (VTR, CU, UT, HG, WG, DC, 24EP, 25TS, FAC, 23HW...)",
      "milestones": {
        "plus_5": {
          "tier_name": "Thẻ Bạc / Thẻ Vàng",
          "opens": {"ordinary_hidden_trait_slots": 1, "coach_skill_slots": 0, "gold_hidden_trait_slots": 0}
        },
        "plus_8": {
          "tier_name": "Thẻ Kim Cương",
          "opens": {"ordinary_hidden_trait_slots": 1, "coach_skill_slots": 1, "gold_hidden_trait_slots": 0}
        },
        "plus_11_to_plus_13": {
          "tier_name": "Thẻ Bạch Kim",
          "opens": {"ordinary_hidden_trait_slots": 1, "coach_skill_slots": 1, "gold_hidden_trait_slots": 1}
        }
      }
    },
    "special_cards": {
      "description": "Áp dụng cho nhóm mùa đặc biệt: 26TOTY winner, PRIME, Infinite Prime, ICON TM",
      "milestones": {
        "plus_5": {
          "opens": {"ordinary_hidden_trait_slots": 1, "coach_skill_slots": 0, "gold_hidden_trait_slots": 0}
        },
        "plus_7": {
          "opens": {"ordinary_hidden_trait_slots": 1, "coach_skill_slots": 0, "gold_hidden_trait_slots": 1}
        },
        "plus_8": {
          "opens": {"ordinary_hidden_trait_slots": 1, "coach_skill_slots": 1, "gold_hidden_trait_slots": 1}
        }
      }
    }
  },
  "ui_rules": {
    "already_selected_tag": {
      "raw_text": "(Đã chọn)",
      "meaning": "Trait đó đã có sẵn trên thẻ gốc hoặc đã được HLV trang bị từ trước (ví dụ Chủ Động Cản Phá trên Matić +12). Game sẽ khóa không cho chọn trùng lặp."
    }
  }
}

if __name__ == "__main__":
    write_json("07_NORMAL_TRAITS_VI.json", NORMAL_TRAITS)
    write_json("08_SKILL_COACHES_VI.json", SKILL_COACHES)
    write_json("09_GOLD_TRAITS_VI.json", GOLD_TRAITS)
    write_json("10_UPGRADE_RULES.json", UPGRADE_RULES_DATA)
    print("Batch 2 completed successfully!")
