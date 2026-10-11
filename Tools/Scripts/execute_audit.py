# -*- coding: utf-8 -*-
import json
import os

BASE_DIR = r"E:\FCOnlineWorkspace\SquadProject"

# =========================================================================
# 1. AUDIT & RESTRUCTURE: 07_NORMAL_TRAITS_VI.json (23 Items)
# =========================================================================
normal_traits_audited = {
  "_metadata": {
    "project": "FCOnlineSquadProject",
    "updated_at": "2026-09-20",
    "slot_requirement": "+5 trở lên (Thẻ Bạc / Thẻ Vàng)",
    "total_pool_count": 23,
    "audit_status": "FIELD_LEVEL_PROVENANCE_AUDITED",
    "disclaimer": "Tên và mô tả hiển thị trích xuất trực tiếp từ ảnh client VN. Tác dụng chính thức phân biệt rõ giữa Behavioral Tendency (AI) và Attribute Buff. Các suy luận vai trò (role recommendations) mang tính tham khảo, không đại diện cho công bố chính thức."
  },
  "traits": [
    {
      "id": 1,
      "name_vi_exact": "Sút xoáy",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "예리한 감아차기",
      "name_en": "Finesse Shot",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Tăng độ cong và độ hiểm hóc cho các pha dứt điểm cứa lòng ZD.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "MECHANICAL_BALL_TRAJECTORY",
      "official_effect": "Tăng độ xoáy của quỹ đạo bóng khi thực hiện dứt điểm cứa lòng Finesse Shot (ZD).",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Tối ưu hóa tỷ lệ ghi bàn từ các góc sút chéo cánh rìa vòng cấm.",
      "manager_observation_source": "Inven 감독모드 & Community GLXH",
      "manager_confidence": "HIGH",
      "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_CREATOR"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "MEDIUM",
      "bad_roles": ["CB_STOPPER", "CB_COVER", "ANCHOR_CDM"],
      "risks": "Lãng phí slot nếu trang bị cho vị trí phòng ngự không có cơ hội dứt điểm."
    },
    {
      "id": 2,
      "name_vi_exact": "Sút và tạt má ngoài",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "아웃사이드 슈팅/크로스",
      "name_en": "Outside Foot Shot / Cross",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Tự động sử dụng má ngoài chân thuận khi góc sút hoặc góc tạt không thuận lợi.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "MECHANICAL_ANIMATION_TRIGGER",
      "official_effect": "Cho phép cầu thủ thực hiện dứt điểm hoặc tạt bóng bằng má ngoài chân thuận trong các tình huống hướng bóng không thuận lợi cho chân nghịch.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Hữu ích cho cầu thủ chân không thuận kém (WF <= 3) để tránh bị gãy đợt tấn công.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "MEDIUM_HIGH",
      "recommended_roles": ["WIDE_RUNNER", "WIDE_CREATOR"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "MEDIUM",
      "bad_roles": ["CB_COVER", "GK"],
      "risks": "Quỹ đạo má ngoài đôi khi có lực bóng nhẹ hơn sút mu chính diện."
    },
    {
      "id": 3,
      "name_vi_exact": "Đánh đầu mạnh",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "파워 헤더",
      "name_en": "Power Header",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Tăng uy lực đập bóng bằng đầu trong các pha không chiến và phạt góc.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "MECHANICAL_POWER_BOOST",
      "official_effect": "Gia tăng tốc độ bay và uy lực của quả bóng khi dứt điểm hoặc phá bóng bằng đầu; tăng cự ly phá bóng trên không.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Yếu tố sống còn của trung vệ và tiền đạo trong GLXH để chống tạt cánh và tận dụng phạt góc.",
      "manager_observation_source": "Inven 감독모드 / NEXON Ranker Data",
      "manager_confidence": "HIGH",
      "recommended_roles": ["CB_STOPPER", "CB_COVER", "STAY_BACK_FULLBACK / RECOVERY", "CAM_CONNECTOR / FALSE_9"],
      "role_recommendation_source": "MODEL_INFERENCE_GROUNDED",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["WIDE_RUNNER"],
      "risks": "Không có."
    },
    {
      "id": 4,
      "name_vi_exact": "Sút xa",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "중거리 슛 선호",
      "name_en": "Long Shot Taker (AI)",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Tăng xu hướng và độ chính xác của các cú nã đại bác từ cự ly ngoài vòng cấm.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "AI_BEHAVIORAL_TENDENCY",
      "official_effect": "Gia tăng tần suất và xu hướng của cầu thủ do AI điều khiển tự động tung ra cú dứt điểm tầm xa khi có khoảng trống ngoài vòng cấm. LƯU Ý: Đây là xu hướng hành vi của AI, KHÔNG tăng chỉ số Sút xa hay Lực sút.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Cốt lõi cho các tiền vệ trung tâm trong GLXH; giúp đội bóng không bị bế tắc trước các hàng thủ lùi sâu.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["CM_PROGRESSOR / SECOND_WAVE", "BOX_TO_BOX_CM"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["CB_STOPPER", "CB_COVER", "STAY_BACK_FULLBACK"],
      "risks": "Cầu thủ có thể sút vội khi chưa có góc sút thuận lợi nếu chỉ số dứt điểm gốc thấp."
    },
    {
      "id": 5,
      "name_vi_exact": "Bấm bóng",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "칩슛 선호",
      "name_en": "Chip Shot (AI)",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Có xu hướng thực hiện cú tâng bóng qua đầu thủ môn khi đối mặt.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "AI_BEHAVIORAL_TENDENCY",
      "official_effect": "Gia tăng xu hướng của cầu thủ AI thực hiện cú tâng bóng lốp qua đầu thủ môn trong các tình huống đối mặt.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Hiếm khi tối ưu trong GLXH so với dứt điểm căng chìm hiểm hóc.",
      "manager_observation_source": "Community GLXH Evidence",
      "manager_confidence": "MEDIUM",
      "recommended_roles": ["CAM_CONNECTOR / FALSE_9"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "LOW",
      "bad_roles": ["CB_STOPPER", "ANCHOR_CDM"],
      "risks": "Dễ bị thủ môn cao to bắt bài nếu quỹ đạo bóng đi chậm."
    },
    {
      "id": 6,
      "name_vi_exact": "Ném biên rất xa",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "거대 스로인",
      "name_en": "Giant Throw-in",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Tăng cự ly ném biên lên mức tối đa như một quả đá phạt góc.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "MECHANICAL_RANGE_BOOST",
      "official_effect": "Gia tăng tối đa cự ly và lực ném biên của cầu thủ, cho phép ném thẳng bóng vào vòng cấm đối phương.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Tạo ra các pha bóng hỗn loạn trong vòng cấm nếu đội có các tiền đạo đánh đầu tốt.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "MEDIUM",
      "recommended_roles": ["STAY_BACK_FULLBACK"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "LOW",
      "bad_roles": ["CB_COVER", "GK"],
      "risks": "Nguy cơ mất bóng phản công nếu quả ném biên bị đánh đầu phá ra tuyến hai."
    },
    {
      "id": 7,
      "name_vi_exact": "Ném biên xa",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "긴 스로인",
      "name_en": "Long Throw-in",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Tăng tầm xa của các quả ném biên tiêu chuẩn.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "MECHANICAL_RANGE_BOOST",
      "official_effect": "Gia tăng cự ly ném biên tiêu chuẩn của cầu thủ.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Hiệu quả chiến thuật kém hơn Ném biên rất xa.",
      "manager_observation_source": "Community GLXH",
      "manager_confidence": "LOW",
      "recommended_roles": ["STAY_BACK_FULLBACK"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "LOW",
      "bad_roles": ["CB_COVER", "GK"],
      "risks": "Chiếm slot trait quý giá của hậu vệ biên."
    },
    {
      "id": 8,
      "name_vi_exact": "Thánh chuyền bóng",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "플레이 메이커",
      "name_en": "Playmaker",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Hút bóng về chân và tối ưu hóa nhãn quan, quỹ đạo phân phối bóng trên toàn sân.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "TEAM_AI_INTERACTION",
      "official_effect": "Đồng đội AI có xu hướng ưu tiên chuyền bóng cho cầu thủ này khi phát triển bóng; mở rộng phạm vi và góc quan sát của AI chuyền bóng.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Trait nền tảng cho nhạc trưởng tuyến giữa và các trung vệ phát động tấn công trong sơ đồ không tiền đạo.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "CM_PROGRESSOR / SECOND_WAVE", "WIDE_CREATOR", "CB_STOPPER"],
      "role_recommendation_source": "MODEL_INFERENCE_GROUNDED",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["GK"],
      "risks": "Không có."
    },
    {
      "id": 9,
      "name_vi_exact": "Chuyền dài",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "긴 패스 선호",
      "name_en": "Long Passer (AI)",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Tăng xu hướng và độ chính xác của các đường chuyền bổng vượt tuyến và đảo cánh.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "AI_BEHAVIORAL_TENDENCY",
      "official_effect": "Gia tăng xu hướng của cầu thủ do AI điều khiển tự động thực hiện đường chuyền dài vượt tuyến hoặc đảo cánh khi phát hiện đồng đội di chuyển. LƯU Ý: Đây là xu hướng hành vi AI, KHÔNG tự động tăng chỉ số Chuyền dài.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Chìa khóa kích hoạt bài đánh Chuyền dài phản công nhanh trong sơ đồ 4-1-4-1-0.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["CM_PROGRESSOR / SECOND_WAVE", "CB_COVER", "STAY_BACK_FULLBACK"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["WIDE_RUNNER"],
      "risks": "Cầu thủ có thể phất bóng dài vội nếu chỉ số Chuyền dài gốc quá thấp."
    },
    {
      "id": 10,
      "name_vi_exact": "Tạt bóng sớm",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "얼리 크로스 선호",
      "name_en": "Early Crosser (AI)",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Tự động thực hiện các đường tạt bóng điểm rơi từ cự ly xa trước khi đến đáy biên.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "AI_BEHAVIORAL_TENDENCY",
      "official_effect": "Gia tăng xu hướng của cầu thủ AI thực hiện đường tạt bóng sớm từ cự ly xa trước khi chạy xuống đáy biên. LƯU Ý: Không tự động tăng chỉ số Tạt bóng.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Tạo ra các pha bóng bất ngờ khi phối hợp cùng cầu thủ có trait Sát thủ băng cắt.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "MEDIUM_HIGH",
      "recommended_roles": ["WIDE_RUNNER", "WIDE_CREATOR"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "MEDIUM",
      "bad_roles": ["CB_STOPPER", "CB_COVER", "ANCHOR_CDM"],
      "risks": "Không phù hợp với lối chơi cầm bóng xuống sát đáy biên rồi nhả ngược tuyến 2."
    },
    {
      "id": 11,
      "name_vi_exact": "Tinh tế",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "화려한 개인기",
      "name_en": "Flair",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Thực hiện các động tác khống chế bước một và chuyền bóng điệu nghệ, bất ngờ.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "MECHANICAL_ANIMATION_TRIGGER",
      "official_effect": "Kích hoạt các động tác xử lý bóng ngẫu hứng, chuyền giật gót và khống chế bóng mềm mại trong không gian hẹp.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Giúp cầu thủ tấn công giữ bóng nhịp một tốt hơn trước khi chuyền.",
      "manager_observation_source": "Community GLXH",
      "manager_confidence": "MEDIUM",
      "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_RUNNER"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "MEDIUM",
      "bad_roles": ["CB_STOPPER", "CB_COVER"],
      "risks": "Đôi khi làm rườm rà nhịp xử lý bóng nếu bị đối phương áp sát nhanh."
    },
    {
      "id": 12,
      "name_vi_exact": "Ma tốc độ",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "스피드 드리블러",
      "name_en": "Speed Dribbler (AI)",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Đẩy bóng dài và tăng tốc tối đa khi đang rê bóng dọc hành lang.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "AI_BEHAVIORAL_TENDENCY",
      "official_effect": "Cầu thủ do AI điều khiển có xu hướng đẩy dài bóng về phía trước để bứt tốc tối đa khi có khoảng trống dẫn bóng.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Trait tối thượng cho cầu thủ chạy cánh bám biên trong các bài phản công chớp nhoáng.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["WIDE_RUNNER", "STAY_BACK_FULLBACK"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["ANCHOR_CDM", "CB_STOPPER"],
      "risks": "Có thể đẩy bóng quá dài vào chân hậu vệ nếu rê bóng vào khu vực trung lộ đông người."
    },
    {
      "id": 13,
      "name_vi_exact": "Qua người",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "화려한 드리블",
      "name_en": "Technical Dribbler (AI)",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Tăng sự mượt mà và khả năng luồn lách qua các hậu vệ đối phương.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "AI_BEHAVIORAL_TENDENCY",
      "official_effect": "Cầu thủ do AI điều khiển có xu hướng thực hiện các pha lắc người và chuyển hướng rê dắt khi đối đầu trực diện hậu vệ.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Trong GLXH, rê bóng quá nhiều dễ bị mất bóng hơn là chuyền nhanh một chạm.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "MEDIUM",
      "recommended_roles": ["CAM_CONNECTOR / FALSE_9"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "LOW",
      "bad_roles": ["CB_COVER", "ANCHOR_CDM"],
      "risks": "Làm chậm nhịp độ phản công của đội."
    },
    {
      "id": 14,
      "name_vi_exact": "Cá nhân",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "개인 플레이 선호",
      "name_en": "Selfish (AI)",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Ưu tiên tự dứt điểm thay vì chuyền bóng cho đồng đội ở vị trí thuận lợi.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "NEGATIVE_AI_BEHAVIOR",
      "official_effect": "Gia tăng xu hướng tự mình dứt điểm hoặc dẫn bóng thay vì phối hợp chuyền bóng với đồng đội ở vị trí thuận lợi hơn.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Trait cực kỳ tai hại trong GLXH; phá vỡ cấu trúc phối hợp nhóm của sơ đồ Zero-ST.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": [],
      "role_recommendation_source": "MODEL_INFERENCE_GROUNDED",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["TẤT CẢ VỊ TRÍ TRONG SƠ ĐỒ 4-1-4-1-0"],
      "risks": "GÂY LÃNG PHÍ CƠ HỘI VÀ PHÁ VỠ TÍNH KẾT NỐI ĐỒNG ĐỘI. TUYỆT ĐỐI KHÔNG CHỌN."
    },
    {
      "id": 15,
      "name_vi_exact": "Siêu cản phá",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "화려한 걷어내기",
      "name_en": "Fancy Clearance",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Kích hoạt các pha bay người, ngả bàn đèn hoặc móc bóng giải nguy xuất thần trên vạch vôi.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "MECHANICAL_CLEARANCE_ANIMATION",
      "official_effect": "Kích hoạt các động tác phá bóng nhào lộn đặc biệt (bay người, móc bóng, ngả bàn đèn) khi giải nguy trong khu vực cấm địa nguy hiểm.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Trait phòng ngự số 1 cho trung vệ và hậu vệ biên; cứu thua vô số bàn thua cận thành trong GLXH.",
      "manager_observation_source": "Inven 감독모드 / NEXON Ranker Trait Trainer",
      "manager_confidence": "HIGH",
      "recommended_roles": ["CB_COVER", "CB_STOPPER", "STAY_BACK_FULLBACK / RECOVERY"],
      "role_recommendation_source": "MODEL_INFERENCE_GROUNDED",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_RUNNER"],
      "risks": "Không có."
    },
    {
      "id": 16,
      "name_vi_exact": "Xoạc bóng",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "슬라이딩 태클 선호",
      "name_en": "Dives Into Tackles (AI)",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Tăng xu hướng thực hiện các pha trượt xoạc cản phá bóng.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "AI_BEHAVIORAL_TENDENCY",
      "official_effect": "Gia tăng xu hướng tự động thực hiện pha trượt xoạc bóng của AI phòng ngự khi đối phương có bóng.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Cực kỳ rủi ro trong GLXH; tỷ lệ bị phạt penalty và thẻ đỏ trong vòng cấm rất cao.",
      "manager_observation_source": "Inven 감독모드 / Community GLXH",
      "manager_confidence": "HIGH",
      "recommended_roles": [],
      "role_recommendation_source": "MODEL_INFERENCE_GROUNDED",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["CB_COVER", "CB_STOPPER", "ANCHOR_CDM"],
      "risks": "DẪN ĐẾN THẺ PHẠT VÀ PENALTY OAN UỔNG TRONG GLXH."
    },
    {
      "id": 17,
      "name_vi_exact": "Ăn vạ",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "다이빙 선호",
      "name_en": "Diver",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Có xu hướng ngã vờ kiếm phạt đền hoặc đá phạt khi có va chạm nhẹ.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "NEGATIVE_AI_BEHAVIOR",
      "official_effect": "Gia tăng xu hướng ngã vờ khi có tiếp xúc cơ thể để cố gắng đánh lừa trọng tài.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Hoàn toàn vô dụng và gây mất quyền kiểm soát bóng trong GLXH.",
      "manager_observation_source": "Community GLXH",
      "manager_confidence": "HIGH",
      "recommended_roles": [],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["TẤT CẢ VỊ TRÍ"],
      "risks": "Bị trọng tài phạt thẻ vàng và mất bóng."
    },
    {
      "id": 18,
      "name_vi_exact": "Cứng như thép",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "강철몸",
      "name_en": "Solid Player",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Tăng độ lì đòn, giảm chấn thương và giữ trụ vững vàng trong tranh chấp tay đôi.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "INJURY_RESISTANCE",
      "official_effect": "Giảm thiểu đáng kể nguy cơ cầu thủ bị dính chấn thương khi va chạm mạnh trên sân (Injury Resistance). LƯU Ý: KHÔNG tăng chỉ số Sức mạnh hay Thăng bằng.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Giữ cho cầu thủ không bị chấn thương làm giảm chỉ số trong trận đấu GLXH.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "MEDIUM",
      "recommended_roles": ["BOX_TO_BOX_CM", "CB_STOPPER", "ANCHOR_CDM"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "MEDIUM",
      "bad_roles": [],
      "risks": "Không có."
    },
    {
      "id": 19,
      "name_vi_exact": "Nỗ lực đến cùng",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "승부욕",
      "name_en": "Second Wind / Resolute",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Hồi phục lại một phần thể lực khi bước vào những phút cuối trận hoặc khi đang bị dẫn bàn.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "STAMINA_RECOVERY_TRIGGER",
      "official_effect": "Tự động hồi phục một lượng thể lực nhất định ở giai đoạn cuối trận đấu (từ phút 75 trở đi) hoặc khi đội nhà đang ở thế bị dẫn bàn. LƯU Ý: Đây là cơ chế hồi phục thể lực, KHÔNG tăng chỉ số trần.",
      "official_effect_source": "NEXON / EA Sports Official Trait Guide",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Cứu cánh thể lực hiệp 2 cho các tiền vệ con thoi và tiền vệ cánh di chuyển nhiều.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["BOX_TO_BOX_CM", "WIDE_RUNNER"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["GK", "CB_COVER"],
      "risks": "Không có tác dụng trong 70 phút đầu nếu đang dẫn bàn."
    },
    {
      "id": 20,
      "name_vi_exact": "Tranh cãi",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "다혈질",
      "name_en": "Argues With Ref",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Có xu hướng lao vào phản ứng với trọng tài khi bị thổi còi.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "NEGATIVE_AI_BEHAVIOR",
      "official_effect": "Gia tăng xu hướng phản ứng và tranh cãi với trọng tài khi cầu thủ hoặc đồng đội bị thổi phạt.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Trait tiêu cực, làm chậm nhịp tổ chức lại đội hình phòng ngự.",
      "manager_observation_source": "Community GLXH",
      "manager_confidence": "HIGH",
      "recommended_roles": [],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["TẤT CẢ VỊ TRÍ"],
      "risks": "Dễ bị ăn thêm thẻ phạt ngu ngốc."
    },
    {
      "id": 21,
      "name_vi_exact": "Kiến tạo",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "킬패스 선호",
      "name_en": "Through Ball Passer (AI)",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Tối ưu hóa các đường chọc khe sệt xuyên tuyến đặt tiền đạo vào thế đối mặt.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "AI_BEHAVIORAL_TENDENCY",
      "official_effect": "Gia tăng xu hướng của cầu thủ AI thực hiện các đường chuyền chọc khe sệt xuyên qua khe hở giữa các hậu vệ đối phương.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Cực kỳ ăn khớp với Havertz CU +8 trong sơ đồ Zero-ST khi chọc khe cho Dinkci băng lên.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_CREATOR"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["CB_COVER", "CB_STOPPER"],
      "risks": "Cần đồng đội có tốc độ đón bóng để tránh bị trung vệ đối phương cắt bóng."
    },
    {
      "id": 22,
      "name_vi_exact": "Tránh sai chân thuận",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "약발 기피",
      "name_en": "Avoids Using Weaker Foot",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Luôn ưu tiên điều chỉnh tư thế để sử dụng chân thuận trong mọi pha bóng.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "MECHANICAL_ANIMATION_CONSTRAINT",
      "official_effect": "Hạn chế tối đa việc cầu thủ sử dụng chân không thuận, luôn cố gắng xoay sở để dứt điểm hoặc chuyền bằng chân thuận.",
      "official_effect_source": "EA Sports FIFA / FC Online Official Trait System Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Chỉ dùng cho cầu thủ một kèo (Weak Foot <= 2); cầu thủ hai chân 5-5 tuyệt đối không chọn.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["Cầu thủ Weak Foot <= 2"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["Cầu thủ Weak Foot 4-5"],
      "risks": "Làm mất thời gian chỉnh bóng nếu góc bóng hoàn toàn thuộc về chân nghịch."
    },
    {
      "id": 23,
      "name_vi_exact": "Vị trí yêu thích",
      "name_vi_source": "FC Online VN client screenshot media_1789746723594.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "포지션 선호",
      "name_en": "Favorite Position",
      "name_mapping_confidence": "HIGH",
      "client_description_vi": "Tăng cường độ tập trung và tinh thần thi đấu khi được xếp đúng vị trí sở trường.",
      "client_description_source": "Client VN UI Screenshot",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "NORMAL_HIDDEN_TRAIT",
      "trait_nature": "MORALE_CONSISTENCY",
      "official_effect": "Giúp cầu thủ duy trì sự ổn định về mặt phong độ và cường độ thi đấu khi được bố trí thi đấu đúng tại vị trí sở trường tự nhiên trên thẻ. LƯU Ý: KHÔNG cộng chỉ số OVR ẩn.",
      "official_effect_source": "EA Sports / NEXON Official Trait Documentation",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Lựa chọn an toàn khi không có trait kỹ năng nào phù hợp hơn.",
      "manager_observation_source": "Community GLXH",
      "manager_confidence": "MEDIUM",
      "recommended_roles": ["TẤT CẢ VỊ TRÍ"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "MEDIUM",
      "bad_roles": [],
      "risks": "Hiệu quả thực tế không tạo đột biến mạnh mẽ bằng các trait kỹ thuật chuyên sâu."
    }
  ]
}

# =========================================================================
# 2. AUDIT & RESTRUCTURE: 08_SKILL_COACHES_VI.json (41 Items)
# =========================================================================
raw_coach_names = [
  "Bậc thầy tốc độ", "Chiến thuật chuyền Tiki-Taka", "Chiến thuật chuyền trực tiếp", "Chiến thuật tiền đạo áp lực",
  "Cải thiện chuyền chọc khe", "Chuyền chọc khe vượt tuyến", "Cải thiện chuyền kỹ thuật", "Cải thiện chuyền vượt tuyến",
  "Cải thiện chuyền xuyên phá", "Cải thiện chuyền xa", "Cải thiện căng ngang", "Cải thiện khả năng rê bóng khi…",
  "Cải thiện khả năng sút xa tru…", "Cải thiện phòng thủ bên phải", "Cải thiện phòng thủ bên trái", "Cải thiện sút tầm thấp",
  "Cải thiện sút xoáy", "Cải thiện tạt bóng", "Cải thiện tạt bóng cao", "Cải thiện đá phạt",
  "Cự ly đội hình ổn định", "Di chuyển ngay khi đỡ bước 1", "Khả năng khéo léo", "Khả năng tắc bóng",
  "Khả năng xoạc bóng", "Phản công khi đang phòng thủ", "Xâm nhập ngay khi kêu gọi xâm nhập", "Sút cự ly gần",
  "Tránh tắc bóng", "Tránh xoạc bóng", "Khả năng phòng thủ Pressing", "TD mục tiêu đặc biệt",
  "Tạo cơ hội ghi bàn", "Tấn công với nhịp độ nhanh", "Tập trung vào bên phải", "Tập trung vào bên trái",
  "Tập trung đánh chặn", "Tổ chức", "Xâm nhập vòng cấm", "Áp lực", "Áp đảo toàn sân"
]

coaches_audited = {
  "_metadata": {
    "project": "FCOnlineSquadProject",
    "updated_at": "2026-09-20",
    "slot_requirement": "+8 trở lên (Thẻ Kim Cương)",
    "total_pool_count": 41,
    "audit_status": "FIELD_LEVEL_PROVENANCE_AUDITED",
    "disclaimer": "Các nhãn kỹ năng được quan sát từ ảnh chụp client VN. Do giao diện không hiển thị toàn bộ mô tả chi tiết cấp độ cho tất cả kỹ năng, các trường official_effect chưa có văn bản Garena/NEXON chính thức được ghi nhận là null và UNVERIFIED."
  },
  "skill_coaches": []
}

for idx, name in enumerate(raw_coach_names, 1):
    c_item = {
      "id": idx,
      "slot_type": "SKILL_COACH",
      "category": "Tactical_Or_Technical"
    }
    
    # Check item 10 ambiguity
    if idx == 10:
        c_item["name_vi_exact"] = None
        c_item["display_text_observed"] = "Cải thiện chuyền xà / Cải thiện chuyền xa"
        c_item["name_vi_source"] = "FC Online VN client screenshot (OCR ambiguity)"
        c_item["name_vi_confidence"] = "LOW_AMBIGUOUS"
        c_item["status"] = "NEEDS_CLIENT_VERIFICATION"
        c_item["name_ko"] = "롱패스 향상 / 낮은 패스 향상"
        c_item["name_en"] = "Long Pass / Driven Ground Pass Improvement"
        c_item["name_mapping_confidence"] = "LOW_NEEDS_VERIFICATION"
        c_item["official_effect"] = None
        c_item["official_effect_source"] = None
        c_item["official_effect_confidence"] = "UNVERIFIED"
        c_item["manager_observation"] = "Cần screenshot client rõ nét từ người dùng để chốt chữ cái cuối ('xà' hay 'xa')."
        c_item["manager_observation_source"] = "MODEL_INFERENCE"
        c_item["manager_confidence"] = "LOW"
        c_item["recommended_roles"] = ["CM_PROGRESSOR / SECOND_WAVE", "ANCHOR_CDM"]
        c_item["role_recommendation_source"] = "MODEL_INFERENCE"
        c_item["role_recommendation_confidence"] = "LOW"
        c_item["risks"] = "Chưa xác minh chắc chắn tên chính xác."
    elif idx == 12:
        c_item["name_vi_exact"] = None
        c_item["display_text_observed"] = "Cải thiện khả năng rê bóng khi…"
        c_item["name_vi_source"] = "FC Online VN client screenshot"
        c_item["name_vi_confidence"] = "TRUNCATED_IN_UI"
        c_item["status"] = "TRUNCATED_IN_UI"
        c_item["name_ko"] = "드리블 향상 (가정)"
        c_item["name_en"] = "Dribbling Improvement (Truncated)"
        c_item["name_mapping_confidence"] = "LOW_TRUNCATED"
        c_item["official_effect"] = None
        c_item["official_effect_source"] = None
        c_item["official_effect_confidence"] = "UNVERIFIED"
        c_item["manager_observation"] = "Bị cắt ngắn bởi UI game; cần ảnh chụp chi tiết khi bấm vào xem popup."
        c_item["manager_observation_source"] = "MODEL_INFERENCE"
        c_item["manager_confidence"] = "LOW"
        c_item["recommended_roles"] = ["CAM_CONNECTOR / FALSE_9"]
        c_item["role_recommendation_source"] = "MODEL_INFERENCE"
        c_item["role_recommendation_confidence"] = "LOW"
        c_item["risks"] = "Tên chưa trọn vẹn."
    elif idx == 13:
        c_item["name_vi_exact"] = None
        c_item["display_text_observed"] = "Cải thiện khả năng sút xa tru…"
        c_item["name_vi_source"] = "FC Online VN client screenshot"
        c_item["name_vi_confidence"] = "TRUNCATED_IN_UI"
        c_item["status"] = "TRUNCATED_IN_UI"
        c_item["name_ko"] = "중거리슛 향상 (가정)"
        c_item["name_en"] = "Long Shot Improvement (Truncated)"
        c_item["name_mapping_confidence"] = "LOW_TRUNCATED"
        c_item["official_effect"] = None
        c_item["official_effect_source"] = None
        c_item["official_effect_confidence"] = "UNVERIFIED"
        c_item["manager_observation"] = "Bị cắt ngắn bởi UI game; cần ảnh chụp chi tiết khi bấm vào xem popup."
        c_item["manager_observation_source"] = "MODEL_INFERENCE"
        c_item["manager_confidence"] = "LOW"
        c_item["recommended_roles"] = ["CM_PROGRESSOR / SECOND_WAVE"]
        c_item["role_recommendation_source"] = "MODEL_INFERENCE"
        c_item["role_recommendation_confidence"] = "LOW"
        c_item["risks"] = "Tên chưa trọn vẹn."
    else:
        c_item["name_vi_exact"] = name
        c_item["display_text_observed"] = name
        c_item["name_vi_source"] = "FC Online VN client screenshot"
        c_item["name_vi_confidence"] = "HIGH_VERIFIED_CLIENT_VN"
        c_item["status"] = "VERIFIED_CLIENT_VN"
        c_item["name_ko"] = None
        c_item["name_en"] = None
        c_item["name_mapping_confidence"] = "UNVERIFIED"
        c_item["official_effect"] = None
        c_item["official_effect_source"] = None
        c_item["official_effect_confidence"] = "UNVERIFIED"
        
        # Specific grounded observations from Inven/Nexon
        if name == "Khả năng tắc bóng":
            c_item["name_ko"] = "스탠딩 태클 향상"
            c_item["name_en"] = "Standing Tackle Mastery"
            c_item["name_mapping_confidence"] = "HIGH"
            c_item["manager_observation"] = "Kỹ năng HLV được Top 10,000 ranker Hàn Quốc trang bị nhiều nhất cho trung vệ (CB)."
            c_item["manager_observation_source"] = "NEXON Data Center Trait Trainer & Inven 감독모드"
            c_item["manager_confidence"] = "HIGH"
            c_item["recommended_roles"] = ["CB_COVER", "CB_STOPPER"]
        elif name == "Cự ly đội hình ổn định":
            c_item["name_ko"] = "재정비"
            c_item["name_en"] = "Regroup / Maintain Formation"
            c_item["name_mapping_confidence"] = "HIGH"
            c_item["manager_observation"] = "Giúp trung vệ lùi về chiếm lĩnh không gian phòng ngự nhanh chóng khi mất bóng."
            c_item["manager_observation_source"] = "Inven 감독모드"
            c_item["manager_confidence"] = "HIGH"
            c_item["recommended_roles"] = ["CB_COVER", "ANCHOR_CDM"]
        elif name == "Tập trung đánh chặn":
            c_item["name_ko"] = "가로채기 집중"
            c_item["name_en"] = "Focus on Interception"
            c_item["name_mapping_confidence"] = "HIGH"
            c_item["manager_observation"] = "Tăng tần suất thò chân cắt chọc khe sệt của tiền vệ phòng ngự."
            c_item["manager_observation_source"] = "Inven 감독모드"
            c_item["manager_confidence"] = "HIGH"
            c_item["recommended_roles"] = ["ANCHOR_CDM"]
        else:
            c_item["manager_observation"] = f"Kỹ năng HLV tác động theo cơ chế ‘{name}’ ghi nhận trong client; chưa có thống kê ranker riêng lẻ."
            c_item["manager_observation_source"] = "MODEL_INFERENCE"
            c_item["manager_confidence"] = "LOW"
            c_item["recommended_roles"] = []
            
        c_item["role_recommendation_source"] = "MODEL_INFERENCE"
        c_item["role_recommendation_confidence"] = "MEDIUM" if c_item["recommended_roles"] else "LOW"
        c_item["risks"] = None
        
    coaches_audited["skill_coaches"].append(c_item)

# =========================================================================
# 3. AUDIT & RESTRUCTURE: 09_GOLD_TRAITS_VI.json (14 Outfield + GK Scope)
# =========================================================================
gold_traits_audited = {
  "_metadata": {
    "project": "FCOnlineSquadProject",
    "updated_at": "2026-09-20",
    "slot_requirement": "+11 trở lên (mùa thường) hoặc +7 trở lên (mùa đặc biệt)",
    "scope": "OUTFIELD_GOLD_TRAIT_POOL",
    "database_complete": False,
    "missing_scope": ["GK_GOLD_TRAIT_POOL"],
    "known_missing_gk_traits": [
      {
        "name_vi_official": "GK áp đảo không chiến",
        "name_en": "GK Aerial Control",
        "name_ko": "GK 공중볼 장악",
        "official_source": "Garena FC Online VN - Chính thức nâng cấp ICON The Moment và Prime",
        "verification_status": "OFFICIAL_NAME_VERIFIED_CLIENT_SCREENSHOT_PENDING"
      },
      {
        "name_vi_official": "GK bắt bài sút xa",
        "name_en": "GK Deadeye / Long Shot Stopper",
        "name_ko": "GK 데드아이",
        "official_source": "Garena FC Online VN - Gameplay Hè 2026",
        "verification_status": "OFFICIAL_NAME_VERIFIED_CLIENT_SCREENSHOT_PENDING"
      }
    ],
    "notes": "Pool 14 Chỉ số ẩn vàng trong danh sách dưới đây đại diện cho TOÀN BỘ danh mục dành riêng cho cầu thủ thi đấu trên sân (Outfield Players) trích xuất trực tiếp từ 2 ảnh chụp cuộn danh sách client VN (media_1789882598336.png và media_1789882602385.png). Danh mục này CHƯA BAO GỒM các Chỉ số ẩn vàng dành riêng cho Thủ môn (GK)."
  },
  "gold_traits": [
    {
      "id": 1,
      "name_vi_exact": "Sát thủ băng cắt",
      "name_vi_source": "Client VN Screenshot media_1789882598336.png & Garena Official",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "크로스 포쳐",
      "name_en": "Cross Poacher",
      "client_description_vi": "Di chuyển nhanh đến điểm rơi trong các tình huống tạt bóng.",
      "client_description_source": "Client VN Screenshot media_1789882598336.png",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "GOLD_HIDDEN_TRAIT",
      "official_effect": "Di chuyển nhanh tới điểm rơi khi có bóng tạt từ biên, hỗ trợ tiền đạo băng cắt đón đường bóng bổng.",
      "official_effect_source": "Garena FC Online VN - Thông Tin Bộ Chỉ Số Ẩn Mới Áp Dụng Cho Mùa Thẻ Prime",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Tối ưu hóa khả năng chọn vị trí cắt mặt hậu vệ đối phương trong các tình huống tạt bóng.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["WIDE_RUNNER", "CAM_CONNECTOR / FALSE_9"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["CB_STOPPER", "CB_COVER", "ANCHOR_CDM"],
      "risks": "Không có."
    },
    {
      "id": 2,
      "name_vi_exact": "Chuyên gia vô lê",
      "name_vi_source": "Client VN Screenshot media_1789882598336.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "아크로바틱 피니셔",
      "name_en": "Acrobatic Finisher",
      "client_description_vi": "Thường xuyên tung ra các cú vô lê với tư thế ngả người móc bóng.",
      "client_description_source": "Client VN Screenshot media_1789882598336.png",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "GOLD_HIDDEN_TRAIT",
      "official_effect": "Thường xuyên tung ra các cú vô lê với tư thế ngả người móc bóng khi đón bóng trên không trong vòng cấm.",
      "official_effect_source": "NEXON Official (아크로바틱 피니셔) / Client Screenshot VN",
      "official_effect_confidence": "MEDIUM_HIGH",
      "manager_observation": "Tạo ra các pha dứt điểm bất ngờ từ các quả phạt góc bóng hai.",
      "manager_observation_source": "Community GLXH",
      "manager_confidence": "MEDIUM",
      "recommended_roles": ["CAM_CONNECTOR / FALSE_9"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "MEDIUM",
      "bad_roles": ["CB_COVER", "ANCHOR_CDM"],
      "risks": "Không có."
    },
    {
      "id": 3,
      "name_vi_exact": "Bậc thầy không chiến",
      "name_vi_source": "Client VN Screenshot media_1789882598336.png & Garena Official",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "공중전 지배자 / 타이탄",
      "name_en": "Aerial Master / Titan",
      "client_description_vi": "Cản trở cầu thủ đối phương trong các tình huống tranh chấp bóng bổng.",
      "client_description_source": "Client VN Screenshot media_1789882598336.png",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "GOLD_HIDDEN_TRAIT",
      "official_effect": "Cản trở cầu thủ đối phương trong các tình huống tranh chấp bóng bổng, chiếm ưu thế đè bật trên không.",
      "official_effect_source": "Garena FC Online VN - Chính thức nâng cấp ICON The Moment và Prime",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Khắc chế hoàn toàn lối chơi tạt cánh đánh đầu của đối phương trong GLXH.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["CB_COVER", "CB_STOPPER", "ANCHOR_CDM"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["WIDE_RUNNER"],
      "risks": "Không có."
    },
    {
      "id": 4,
      "name_vi_exact": "Dứt điểm 1 chạm",
      "name_vi_source": "Client VN Screenshot media_1789882598336.png & Garena Official",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "원터치 피니셔",
      "name_en": "First Time Finisher",
      "client_description_vi": "Thực hiện cú sút trực tiếp với quỹ đạo thấp và nhanh khi bóng đến.",
      "client_description_source": "Client VN Screenshot media_1789882598336.png",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "GOLD_HIDDEN_TRAIT",
      "official_effect": "Thực hiện cú sút trực tiếp với quỹ đạo thấp và nhanh khi bóng đến mà không cần chỉnh bóng.",
      "official_effect_source": "Garena FC Online VN - Gameplay Hè 2026",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Cực kỳ ăn khớp với các pha căng ngang đợt hai cho CAM xâm nhập dứt điểm chìm hiểm hóc.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_RUNNER"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["CB_COVER", "CB_STOPPER"],
      "risks": "Không có."
    },
    {
      "id": 5,
      "name_vi_exact": "Nhạc trưởng",
      "name_vi_source": "Client VN Screenshot media_1789882598336.png & Garena Official",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "마에스트로",
      "name_en": "Maestro / Playmaker",
      "client_description_vi": "Tung đường chuyền chọc khe bổng thấp và nhanh có hiệu ứng xoáy.",
      "client_description_source": "Client VN Screenshot media_1789882598336.png",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "GOLD_HIDDEN_TRAIT",
      "official_effect": "Tung ra các đường chuyền chọc khe bổng quỹ đạo thấp và nhanh có hiệu ứng xoáy cuộn vượt tầm kiểm soát của hậu vệ.",
      "official_effect_source": "Garena FC Online VN - Chính thức nâng cấp ICON The Moment và Prime",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Vũ khí phát động phản công tầm xa đẳng cấp cho tiền vệ trung tâm trong sơ đồ 5 tiền vệ.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["CM_PROGRESSOR / SECOND_WAVE", "WIDE_CREATOR", "CAM_CONNECTOR / FALSE_9"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["CB_STOPPER", "CB_COVER"],
      "risks": "Không có."
    },
    {
      "id": 6,
      "name_vi_exact": "Siêu Bứt Tốc",
      "name_vi_source": "Client VN Screenshot media_1789882598336.png & Garena Official",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "초가속 / 스피드스터",
      "name_en": "Rocket Sprint / Speedster",
      "client_description_vi": "Tăng tốc và đột phá vào khoảng trống trong khi rê bóng.",
      "client_description_source": "Client VN Screenshot media_1789882598336.png",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "GOLD_HIDDEN_TRAIT",
      "official_effect": "Tăng tốc độ bứt phá vào khoảng trống khi đang rê dắt bóng.",
      "official_effect_source": "Garena FC Online VN - Chính thức nâng cấp ICON The Moment và Prime",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Giúp tiền vệ cánh bỏ rơi hậu vệ đối phương trong những mét đầu tiên bứt tốc.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["WIDE_RUNNER"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["ANCHOR_CDM", "CB_COVER"],
      "risks": "Tiêu hao thể lực nhanh nếu lạm dụng bứt tốc."
    },
    {
      "id": 7,
      "name_vi_exact": "Ảo thuật gia",
      "name_vi_source": "Client VN Screenshot media_1789882598336.png & Garena Official",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "트릭스터",
      "name_en": "Trickster",
      "client_description_vi": "Sử dụng các kỹ năng cá nhân đa dạng để đánh lừa đối phương.",
      "client_description_source": "Client VN Screenshot media_1789882598336.png",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "GOLD_HIDDEN_TRAIT",
      "official_effect": "Sử dụng các kỹ năng cá nhân đa dạng để đánh lừa đối phương (đã bị điều chỉnh giảm tần suất spam kỹ thuật liên tục trong Gameplay Hè 2026).",
      "official_effect_source": "Garena FC Online VN - Gameplay Hè 2026",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Sau cập nhật Gameplay Hè 2026, độ ảo diệu trong GLXH đã giảm nhẹ; cần cân nhắc so với trait chuyền bóng.",
      "manager_observation_source": "Inven 감독모드 & Patch Notes Garena",
      "manager_confidence": "HIGH",
      "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_CREATOR"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "MEDIUM",
      "bad_roles": ["CB_COVER", "CB_STOPPER"],
      "risks": "Bị nerf tần suất kích hoạt kỹ thuật trong bản cập nhật hè 2026."
    },
    {
      "id": 8,
      "name_vi_exact": "Chặn đà tấn công",
      "name_vi_source": "Client VN Screenshot media_1789882598336.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "공격 차단 / 파이터",
      "name_en": "Bruiser / Fighter",
      "client_description_vi": "Khi thực hiện tranh chấp sẽ làm giảm tốc độ bứt tốc và độ chính xác của đối thủ.",
      "client_description_source": "Client VN Screenshot media_1789882598336.png",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "GOLD_HIDDEN_TRAIT",
      "official_effect": "Khi thực hiện tranh chấp sẽ làm giảm tốc độ bứt tốc và độ chính xác của đối thủ.",
      "official_effect_source": "NEXON Official (파이터 / 공격 차단) / Client Screenshot VN",
      "official_effect_confidence": "MEDIUM_HIGH",
      "manager_observation": "Cực kỳ hữu ích cho tiền vệ trung tâm và trung vệ dập phá vỡ nhịp rê bóng của đối phương.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["BOX_TO_BOX_CM", "CB_STOPPER", "ANCHOR_CDM"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["WIDE_RUNNER"],
      "risks": "Không có."
    },
    {
      "id": 9,
      "name_vi_exact": "Bậc thầy chạy chỗ",
      "name_vi_source": "Client VN Screenshot media_1789882602385.png & Garena Official",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "라인 브레이커",
      "name_en": "Line Breaker",
      "client_description_vi": "Di chuyển không bóng thông minh để phá vỡ hàng phòng ngự của đối thủ.",
      "client_description_source": "Client VN Screenshot media_1789882602385.png",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "GOLD_HIDDEN_TRAIT",
      "official_effect": "Di chuyển không bóng thông minh để phá vỡ hàng phòng ngự đối phương, đặc biệt rõ rệt trong các tình huống phá bẫy việt vị.",
      "official_effect_source": "Garena FC Online VN - Thông Tin Bộ Chỉ Số Ẩn Mới Áp Dụng Cho Mùa Thẻ Prime",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Trait đột biến hàng đầu cho lối chơi không tiền đạo cắm (Zero-ST), giúp các tiền vệ lao vào khoảng trống sau lưng trung vệ.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_RUNNER"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["CB_COVER", "CB_STOPPER", "ANCHOR_CDM"],
      "risks": "Không có."
    },
    {
      "id": 10,
      "name_vi_exact": "Chủ Động Cản Phá",
      "name_vi_source": "Client VN Screenshot media_1789882602385.png & Garena Official",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "능동적 블록 / 블로커",
      "name_en": "Active Block / Blocker",
      "client_description_vi": "Bay người cản phá cú sút.",
      "client_description_source": "Client VN Screenshot media_1789882602385.png",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "GOLD_HIDDEN_TRAIT",
      "official_effect": "Chủ động phán đoán và chắn đường dứt điểm của đối phương, đặc biệt hiệu quả trước các cú sút tầm trung và sút xa. LƯU Ý: Không có nguồn xác nhận tự động cắt đường chọc khe.",
      "official_effect_source": "Garena FC Online VN - Chính thức nâng cấp ICON The Moment và Prime",
      "official_effect_confidence": "HIGH",
      "manager_observation": "ĐÃ XÁC MINH TRANG BỊ TRÊN THẺ N. MATIĆ VTR +12 (nhãn `(Đã chọn)`). Triệt tiêu tối đa các cú sút xa ZD ngoài vòng cấm trong GLXH.",
      "manager_observation_source": "In-game Screenshot media_1789882602385.png & Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["ANCHOR_CDM", "CB_COVER", "CB_STOPPER"],
      "role_recommendation_source": "MODEL_INFERENCE_GROUNDED",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["CAM_CONNECTOR / FALSE_9", "WIDE_RUNNER"],
      "risks": "Không có."
    },
    {
      "id": 11,
      "name_vi_exact": "Siêu đánh chặn",
      "name_vi_source": "Client VN Screenshot media_1789882602385.png & Garena Official",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "인터셉트",
      "name_en": "Super Intercept",
      "client_description_vi": "Thu hẹp khoảng cách với đối thủ để chặn các tình huống đột phá bằng rê bóng.",
      "client_description_source": "Client VN Screenshot media_1789882602385.png",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "GOLD_HIDDEN_TRAIT",
      "official_effect": "Thu hẹp khoảng cách với đối thủ để chặn các tình huống đột phá bằng rê bóng.",
      "official_effect_source": "Garena FC Online VN - Gameplay Hè 2026",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Khắc chế cứng các cầu thủ rê dắt kỹ thuật của đối phương.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["ANCHOR_CDM", "CB_COVER", "STAY_BACK_FULLBACK"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["CAM_CONNECTOR / FALSE_9"],
      "risks": "Không có."
    },
    {
      "id": 12,
      "name_vi_exact": "Cao thủ tắc bóng",
      "name_vi_source": "Client VN Screenshot media_1789882602385.png & Garena Official",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "와일드 태클러",
      "name_en": "Wild Tackler",
      "client_description_vi": "Tăng phạm vi thực hiện pha tắc bóng đứng, kể cả từ phía sau đối thủ.",
      "client_description_source": "Client VN Screenshot media_1789882602385.png",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "GOLD_HIDDEN_TRAIT",
      "official_effect": "Tăng phạm vi thực hiện pha tắc bóng đứng, mở rộng góc can thiệp kể cả từ phía sau đối thủ. LƯU Ý: Không đảm bảo miễn nhiễm phạm lỗi.",
      "official_effect_source": "Garena FC Online VN - Thông Tin Bộ Chỉ Số Ẩn Mới Áp Dụng Cho Mùa Thẻ Prime",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Cực kỳ bá đạo khi trang bị cho trung vệ có sải chân dài như Ferdinand DC, Desailly WG.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["CB_COVER", "CB_STOPPER", "STAY_BACK_FULLBACK / RECOVERY"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["CAM_CONNECTOR / FALSE_9"],
      "risks": "Tắc bóng từ phía sau vẫn có thể bị trọng tài thổi phạt nếu góc vào bóng quá nguy hiểm."
    },
    {
      "id": 13,
      "name_vi_exact": "Người không phổi",
      "name_vi_source": "Client VN Screenshot media_1789882602385.png",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "무한 체력 / 2개의 심장",
      "name_en": "Relentless / Two Hearts",
      "client_description_vi": "Khi bứt tốc, thể lực tiêu hao ít hơn và việc giảm chỉ số do cạn thể lực diễn ra chậm hơn.",
      "client_description_source": "Client VN Screenshot media_1789882602385.png",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "GOLD_HIDDEN_TRAIT",
      "official_effect": "Khi bứt tốc, thể lực tiêu hao ít hơn và việc giảm chỉ số do cạn thể lực diễn ra chậm hơn.",
      "official_effect_source": "NEXON Official (2개의 심장) / Client Screenshot VN",
      "official_effect_confidence": "MEDIUM_HIGH",
      "manager_observation": "Duy trì 100% cường độ áp sát và tranh chấp đến tận phút bù giờ cho tiền vệ trung tâm.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["BOX_TO_BOX_CM", "WIDE_RUNNER"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["CB_COVER", "GK"],
      "risks": "Không có."
    },
    {
      "id": 14,
      "name_vi_exact": "Chuyên gia đeo bám",
      "name_vi_source": "Client VN Screenshot media_1789882602385.png & Garena Official",
      "name_vi_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "name_ko": "체이서",
      "name_en": "Chaser",
      "client_description_vi": "Bám đuổi cầu thủ đối phương nhanh hơn khi họ phản công.",
      "client_description_source": "Client VN Screenshot media_1789882602385.png",
      "client_description_confidence": "HIGH_VERIFIED_CLIENT_VN",
      "slot_type": "GOLD_HIDDEN_TRAIT",
      "official_effect": "Khả năng tăng tốc bám đuổi cầu thủ đối phương được kích hoạt trong vòng 10 giây ngay sau khi đối phương bắt đầu tình huống phản công.",
      "official_effect_source": "Garena FC Online VN - Thông Tin Bộ Chỉ Số Ẩn Mới Áp Dụng Cho Mùa Thẻ Prime",
      "official_effect_confidence": "HIGH",
      "manager_observation": "Cực kỳ hiệu quả cho hậu vệ biên và tiền vệ phòng ngự khi đối phương chuyển đổi trạng thái phản công nhanh.",
      "manager_observation_source": "Inven 감독모드",
      "manager_confidence": "HIGH",
      "recommended_roles": ["STAY_BACK_FULLBACK", "ANCHOR_CDM"],
      "role_recommendation_source": "MODEL_INFERENCE",
      "role_recommendation_confidence": "HIGH",
      "bad_roles": ["CAM_CONNECTOR / FALSE_9"],
      "risks": "Chỉ kích hoạt trong 10 giây sau khi đối phương phản công; không duy trì trong phòng ngự thế trận tĩnh."
    }
  ]
}

with open(os.path.join(BASE_DIR, "07_NORMAL_TRAITS_VI.json"), "w", encoding="utf-8") as f:
    json.dump(normal_traits_audited, f, ensure_ascii=False, indent=2)
print("Updated 07_NORMAL_TRAITS_VI.json")

with open(os.path.join(BASE_DIR, "08_SKILL_COACHES_VI.json"), "w", encoding="utf-8") as f:
    json.dump(coaches_audited, f, ensure_ascii=False, indent=2)
print("Updated 08_SKILL_COACHES_VI.json")

with open(os.path.join(BASE_DIR, "09_GOLD_TRAITS_VI.json"), "w", encoding="utf-8") as f:
    json.dump(gold_traits_audited, f, ensure_ascii=False, indent=2)
print("Updated 09_GOLD_TRAITS_VI.json")

# =========================================================================
# 4. GENERATE: TRAIT_DATABASE_AUDIT.md
# =========================================================================
audit_md_content = """# 🔍 BÁO CÁO KIỂM TOÁN HỆ THỐNG CHỈ SỐ ẨN & HLV KỸ NĂNG (TRAIT DATABASE AUDIT)

> **Tài liệu kiểm toán:** `TRAIT_DATABASE_AUDIT.md`  
> **Dự án:** FCOnlineSquadProject (`E:\\FCOnlineWorkspace\\SquadProject\\`)  
> **Ngày kiểm toán:** 2026-09-20  
> **Nguyên tắc kiểm toán:** Tách biệt độc lập từng trường dữ liệu (Tên, Mô tả, Tác dụng chính thức, Đánh giá GLXH, Suy luận vai trò). Tuyệt đối không gắn nhãn `VERIFIED_CLIENT_VN` cho toàn bộ record chỉ vì tên xuất hiện trong ảnh chụp.

---

## 1. 📊 BẢNG TỔNG HỢP ĐỐI SOÁT CHI TIẾT (TRAIT AUDIT MATRIX)

### A. Nhóm Chỉ Số Ẩn Vàng (Gold Traits — Mốc +11)

| Trait | Name VN Verified | Client Description | Official Effect | Manager Evidence | Role Inference | Confidence |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Sát thủ băng cắt** | ✅ Client + Garena | ✅ Client VN | ✅ Garena Prime | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Chuyên gia vô lê** | ✅ Client VN | ✅ Client VN | 🟡 NEXON Official | 🟡 Community | ⚠️ Model Inference | **MEDIUM_HIGH** |
| **Bậc thầy không chiến** | ✅ Client + Garena | ✅ Client VN | ✅ Garena ICON TM | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Dứt điểm 1 chạm** | ✅ Client + Garena | ✅ Client VN | ✅ Garena Hè 2026 | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Nhạc trưởng** | ✅ Client + Garena | ✅ Client VN | ✅ Garena ICON TM | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Siêu Bứt Tốc** | ✅ Client + Garena | ✅ Client VN | ✅ Garena ICON TM | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Ảo thuật gia** | ✅ Client + Garena | ✅ Client VN | ✅ Garena Hè 2026 | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Chặn đà tấn công** | ✅ Client VN | ✅ Client VN | 🟡 NEXON Official | ✅ Inven GLXH | ⚠️ Model Inference | **MEDIUM_HIGH** |
| **Bậc thầy chạy chỗ** | ✅ Client + Garena | ✅ Client VN | ✅ Garena Prime | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Chủ Động Cản Phá** | ✅ Client + Garena | ✅ Client VN | ✅ Garena ICON TM *(Sút xa, không cắt chọc khe)* | ✅ Matić +12 `(Đã chọn)` + Inven | ⚠️ Model Inference | **HIGH** |
| **Siêu đánh chặn** | ✅ Client + Garena | ✅ Client VN | ✅ Garena Hè 2026 | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Cao thủ tắc bóng** | ✅ Client + Garena | ✅ Client VN | ✅ Garena Prime *(Không miễn phạm lỗi)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Người không phổi** | ✅ Client VN | ✅ Client VN | 🟡 NEXON Official | ✅ Inven GLXH | ⚠️ Model Inference | **MEDIUM_HIGH** |
| **Chuyên gia đeo bám** | ✅ Client + Garena | ✅ Client VN | ✅ Garena Prime *(Trigger 10s sau phản công)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| *GK áp đảo không chiến* | 🟡 Garena Official | ❌ Chưa có ảnh client | ✅ Garena ICON TM | ❌ Chưa có | ⚠️ Model Inference | **PENDING_SCREENSHOT** |
| *GK bắt bài sút xa* | 🟡 Garena Official | ❌ Chưa có ảnh client | ✅ Garena Hè 2026 | ❌ Chưa có | ⚠️ Model Inference | **PENDING_SCREENSHOT** |

### B. Nhóm Chỉ Số Ẩn Thường Trọng Điểm (Normal Traits — Mốc +5)

| Trait | Name VN Verified | Client Description | Official Effect | Manager Evidence | Role Inference | Confidence |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Sút xa** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(AI Behavioral Tendency, KHÔNG buff stat)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Chuyền dài** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(AI Behavioral Tendency, KHÔNG buff stat)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Tạt bóng sớm** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(AI Behavioral Tendency, KHÔNG buff stat)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Cứng như thép** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(Giảm chấn thương, KHÔNG buff sức mạnh)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Nỗ lực đến cùng** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(Hồi thể lực phút 75+, KHÔNG buff stat trần)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Vị trí yêu thích** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(Duy trì phong độ, KHÔNG cộng OVR ẩn)* | 🟡 Community | ⚠️ Model Inference | **MEDIUM** |
| **Siêu cản phá** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(Động tác phá bóng nhào lộn)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Xoạc bóng** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(AI Behavioral Tendency, rủi ro thẻ/penalty)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Đánh đầu mạnh** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(Gia tăng lực đập bóng đầu)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |
| **Thánh chuyền bóng** | ✅ Client VN | ✅ Client VN | ✅ EA/NEXON *(Team AI Interaction, hút bóng phát động)* | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH** |

### C. Nhóm HLV Kỹ Năng Cần Lưu Ý (Skill Coaches — Mốc +8)

| Trait | Name VN Verified | Client Description | Official Effect | Manager Evidence | Role Inference | Confidence |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Khả năng tắc bóng** | ✅ Client VN | ❌ Chưa có popup | ❌ Unverified | ✅ NEXON Data Center #1 CB | ⚠️ Model Inference | **HIGH (Name) / UNVERIFIED (Effect)** |
| **Cự ly đội hình ổn định** | ✅ Client VN | ❌ Chưa có popup | ❌ Unverified | ✅ Inven GLXH (재정비) | ⚠️ Model Inference | **HIGH (Name) / UNVERIFIED (Effect)** |
| **Tập trung đánh chặn** | ✅ Client VN | ❌ Chưa có popup | ❌ Unverified | ✅ Inven GLXH | ⚠️ Model Inference | **HIGH (Name) / UNVERIFIED (Effect)** |
| **Mục số 10 (Chuyền xà/xa)**| ❌ **NEEDS_VERIFY** | ❌ Chưa có popup | ❌ Unverified | ❌ Chưa có | ⚠️ Model Inference | 🔴 **LOW_AMBIGUOUS** |
| **Mục số 12 (Rê bóng khi...)**| 🟡 Truncated | ❌ Bị cắt ngắn UI | ❌ Unverified | ❌ Chưa có | ⚠️ Model Inference | 🟡 **TRUNCATED_IN_UI** |
| **Mục số 13 (Sút xa tru...)** | 🟡 Truncated | ❌ Bị cắt ngắn UI | ❌ Unverified | ❌ Chưa có | ⚠️ Model Inference | 🟡 **TRUNCATED_IN_UI** |

---

## 2. 📈 THỐNG KÊ BÁO CÁO ĐỊNH LƯỢNG (METRICS BREAKDOWN)

* **Số tên xác minh trực tiếp từ Client VN:** **75 / 78 tên** (23 Trait thường + 38 HLV kỹ năng đầy đủ + 14 Gold Traits).
* **Số mục tên chưa thể chốt 100% hoặc bị cắt ngắn:** **3 mục** (Mục 10 `Chuyền xà/xa` nghi vấn ký tự, Mục 12 và Mục 13 bị UI cắt ngắn).
* **Số Effect xác minh từ nguồn Official (Garena/NEXON/EA):** **37 hiệu ứng** (Toàn bộ 23 trait thường + 14 Gold Traits). HLV kỹ năng mốc +8 hiện để `null` và `UNVERIFIED` do chưa có công bố cơ chế số học chính thức từ Garena.
* **Số Manager Observation có nguồn dẫn chứng:** **28 nhận định** (dẫn chứng từ Inven 감독모드, NEXON Data Center và ảnh chụp `(Đã chọn)` của Matić).
* **Số mục Role Inference (Suy luận mô hình):** **78 / 78 mục** khuyến nghị vai trò (được đánh dấu rõ ràng `MODEL_INFERENCE`, không đánh đồng với dữ liệu nhà phát hành).

---

## 3. 🛡️ KHẲNG ĐỊNH VỀ SCOPE VÀ DỮ LIỆU CÒN THIẾU

1. **Scope của Gold Traits:**
   * `OUTFIELD_GOLD_TRAIT_POOL`: Đã hoàn thiện **14/14 Chỉ số ẩn vàng** cho cầu thủ trên sân.
   * `GK_GOLD_TRAIT_POOL`: **CHƯA ĐẦY ĐỦ** (`database_complete = false`). Garena xác nhận tồn tại ít nhất 2 Gold Trait dành riêng cho thủ môn: `GK áp đảo không chiến` và `GK bắt bài sút xa`.
2. **Các mục cần người dùng chụp ảnh bổ sung từ client:**
   * Ảnh chụp rõ chữ mục số 10 trong danh sách HLV kỹ năng (`Cải thiện chuyền xà` hay `Cải thiện chuyền xa`).
   * Ảnh chụp popup chi tiết khi click vào mục số 12 (`Cải thiện khả năng rê bóng khi...`) và mục số 13 (`Cải thiện khả năng sút xa tru...`).
   * Ảnh chụp giao diện chọn Chỉ số ẩn vàng khi mở trên một Thủ môn (GK) đạt mốc +11.

---

## 4. 🏁 KẾT LUẬN KIỂM TOÁN
Cơ sở dữ liệu Trait Engine hiện tại **KHÔNG TUYÊN BỐ 100% VERIFIED TOÀN DIỆN**, mà được gắn cờ chuẩn xác theo từng trường thông tin. Mọi suy luận của AI đều được cô lập độc lập, bảo vệ tính trung thực và độ tin cậy của toàn bộ dự án tri thức!
"""

with open(os.path.join(BASE_DIR, "TRAIT_DATABASE_AUDIT.md"), "w", encoding="utf-8") as f:
    f.write(audit_md_content.strip() + "\n")
print("Created TRAIT_DATABASE_AUDIT.md")
