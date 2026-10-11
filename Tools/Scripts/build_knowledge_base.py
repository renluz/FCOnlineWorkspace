import os
import sys
import json

BASE_DIR = r"E:\FCOnlineWorkspace\Research\knowledge"

def ensure_dir(d):
    os.makedirs(d, exist_ok=True)

# 1. SOURCES REGISTRY
sources = {
    "SRC_GARENA_OFFICIAL": {
        "source_id": "SRC_GARENA_OFFICIAL",
        "name": "Garena FC Online Vietnam Official Announcements & Patch Notes",
        "url": "https://fconline.garena.vn",
        "type": "OFFICIAL_GARENA",
        "server": "VN_GARENA",
        "reliability_tier": "A",
        "description": "Thông báo bản cập nhật, gameplay patch notes, cơ chế tính năng và thông số chính thức từ Garena VN."
    },
    "SRC_NEXON_OFFICIAL": {
        "source_id": "SRC_NEXON_OFFICIAL",
        "name": "Nexon FC Online Korea Official Data Center & Open API",
        "url": "https://open.api.nexon.com",
        "type": "OFFICIAL_NEXON",
        "server": "KR_NEXON",
        "reliability_tier": "A",
        "description": "Metadata API chuẩn, cấu trúc match-detail, ranker stats và định nghĩa hệ thống từ Nexon."
    },
    "SRC_INVEN_GLXH": {
        "source_id": "SRC_INVEN_GLXH",
        "name": "Inven FC Online Korea - Manager Mode Community (감독모드)",
        "url": "https://fconline.inven.co.kr",
        "type": "COMMUNITY_HIGH_RANK",
        "server": "KR_NEXON",
        "reliability_tier": "B",
        "description": "Chiến thuật, sơ đồ, phân tích AI cầu thủ và thống kê từ các Ranker Super Champions / Champions."
    },
    "SRC_FCVN": {
        "source_id": "SRC_FCVN",
        "name": "FCVN - Cộng Đồng FC Online Việt Nam",
        "url": "https://fcvn.net",
        "type": "COMMUNITY_VERIFIED",
        "server": "VN_GARENA",
        "reliability_tier": "C",
        "description": "Phân tích meta Việt Nam, đánh giá mùa thẻ, kinh nghiệm build team color và vận hành giải đấu."
    },
    "SRC_FB_GLXH_VN": {
        "source_id": "SRC_FB_GLXH_VN",
        "name": "Cộng Đồng Giả Lập Xếp Hạng FC Online Việt Nam (Facebook)",
        "url": "https://www.facebook.com/groups/glxhfconlinevn",
        "type": "COMMUNITY_OBSERVED",
        "server": "VN_GARENA",
        "reliability_tier": "C",
        "description": "Dữ liệu người dùng Việt Nam chia sẻ thực tế về leo rank Thách Đấu / Siêu Sao GLXH."
    },
    "SRC_FIFAADDICT": {
        "source_id": "SRC_FIFAADDICT",
        "name": "FIFAAddict Global Database",
        "url": "https://fifaaddict.com",
        "type": "DATABASE_PUBLIC",
        "server": "GLOBAL_GENERIC",
        "reliability_tier": "B",
        "description": "Cơ sở dữ liệu thẻ, natural positions, body type, work rate và traits cầu thủ toàn cầu."
    },
    "SRC_YOUTUBE_VN": {
        "source_id": "SRC_YOUTUBE_VN",
        "name": "Kênh Chuyên Sâu GLXH / Review Chiến Thuật VN",
        "url": "https://youtube.com",
        "type": "COMMUNITY_MEDIA",
        "server": "VN_GARENA",
        "reliability_tier": "C",
        "description": "Video thực chiến, phân tích góc nhìn trận đấu và kiểm chứng phôi chiến thuật trong GLXH."
    }
}

with open(os.path.join(BASE_DIR, "sources", "sources_registry.json"), "w", encoding="utf-8") as f:
    json.dump(sources, f, ensure_ascii=False, indent=2)

# 2. PATCHES HISTORY
patches = {
    "GAMEPLAY_12TH_2026": {
        "patch_id": "GAMEPLAY_12TH_2026",
        "release_date": "2026-01-15",
        "server_status": {"VN_GARENA": "ACTIVE", "KR_NEXON": "ACTIVE"},
        "key_changes": [
            "Cải thiện độ nhạy AI đánh chặn (Interception AI) cho các tiền vệ mỏ neo có chỉ số Quyết đoán và Cắt bóng cao.",
            "Nerf nhẹ độ chính xác của các đường chuyền dài QW bổng xuyên tuyến nếu cầu thủ chuyền bị áp sát.",
            "Tăng tốc độ tiêu hao thể lực khi cài đặt Chiến thuật áp lực cao (Pressing / Aggression > 70) trong Manager Mode.",
            "Điều chỉnh hành vi thủ môn: Bắt bài sút xa ZD tốt hơn ở góc gần, giảm tỷ lệ văng bóng lập bập.",
            "Tăng cường tính kỷ luật vị trí của trung vệ: Giảm hiện tượng CB tự ý dâng cao khi cài đặt IN2."
        ],
        "tactical_implication": "Lối đá 4-2-3-1 với cặp Double Pivot (1 Anchor + 1 Ball Winner) và nhịp độ kiểm soát (Speed 45-55) trở nên cực kỳ ổn định trong GLXH."
    },
    "GAMEPLAY_11TH_2025": {
        "patch_id": "GAMEPLAY_11TH_2025",
        "release_date": "2025-08-20",
        "server_status": {"VN_GARENA": "SUPERSEDED", "KR_NEXON": "SUPERSEDED"},
        "key_changes": [
            "Tối ưu AI bọc lót của cặp trung vệ khi đối phương phản công nhanh.",
            "Tăng tính hiệu quả của các quả tạt bóng sớm (Early Cross) từ hành lang cánh.",
            "Sửa lỗi Fullback bó vào trung lộ quá sâu khi đối thủ khoét nách biên."
        ],
        "tactical_implication": "Các tiền đạo mục tiêu (Target Man) có khả năng không chiến (Boniface, Haaland) bắt đầu thịnh hành trở lại."
    },
    "GAMEPLAY_10TH_2025": {
        "patch_id": "GAMEPLAY_10TH_2025",
        "release_date": "2025-03-10",
        "server_status": {"VN_GARENA": "SUPERSEDED", "KR_NEXON": "SUPERSEDED"},
        "key_changes": [
            "Cân bằng sức mạnh tranh chấp (Physical Collision): Cầu thủ có thể hình Đậm (Stocky) tì đè giữ bóng tốt hơn hẳn.",
            "Giảm hiệu ứng trượt quán tính của hậu vệ sau khi vào bóng hụt."
        ],
        "tactical_implication": "Tiền vệ thể hình nhỏ (nhỏ con) bị lép vế hoàn toàn trước các máy quét cơ bắp tuyến giữa."
    }
}

with open(os.path.join(BASE_DIR, "patches", "gameplay_patches.json"), "w", encoding="utf-8") as f:
    json.dump(patches, f, ensure_ascii=False, indent=2)

# 3. ENTITIES (Traits, Mechanics, Body Types)
entities = {
    "traits": {
        "Finesse Shot": {
            "name_vn": "Sút xoáy",
            "code": "FINESSE_SHOT",
            "effect_glxh": "AI ưu tiên chọn phương án dứt điểm cứa lòng ZD khi nhận bóng ở góc chếch 16m50; tăng độ xoáy và tỷ lệ bóng găm vào góc chết.",
            "best_positions": ["ST", "CAM", "LW", "RW"],
            "importance": "TIER_S"
        },
        "Power Header": {
            "name_vn": "Đánh đầu mạnh",
            "code": "POWER_HEADER",
            "effect_glxh": "Tăng uy lực đập bóng bằng đầu trong các pha tạt cánh và phạt góc; bóng đi căng, khó cản phá.",
            "best_positions": ["ST", "CB"],
            "importance": "TIER_S"
        },
        "Playmaker": {
            "name_vn": "Thánh chuyền bóng / Kiến tạo",
            "code": "PLAYMAKER",
            "effect_glxh": "Tăng nhãn quan AI; các đường chọc khe QW hoặc xẻ nách có quỹ đạo chuẩn xác hơn và giảm độ trễ ra chân.",
            "best_positions": ["CAM", "CM", "CDM"],
            "importance": "TIER_A"
        },
        "Long Passer": {
            "name_vn": "Chuyền dài",
            "code": "LONG_PASSER",
            "effect_glxh": "Tự động kích hoạt các pha mở bóng đảo cánh chính xác khi phát hiện khoảng trống ở biên đối diện.",
            "best_positions": ["CDM", "CM", "CB"],
            "importance": "TIER_A"
        },
        "Speed Dribbler": {
            "name_vn": "Ma tốc độ",
            "code": "SPEED_DRIBBLER",
            "effect_glxh": "Cầu thủ đẩy bóng dài nhanh hơn khi dốc biên phản công; tận dụng tối đa chỉ số Tốc độ.",
            "best_positions": ["LW", "RW", "ST", "LB", "RB"],
            "importance": "TIER_B"
        },
        "Solid Player": {
            "name_vn": "Cứng như thép",
            "code": "SOLID_PLAYER",
            "effect_glxh": "Khó bị chấn thương khi va chạm mạnh; duy trì thể lực và độ ổn định xuyên suốt 90 phút.",
            "best_positions": ["CDM", "CB", "ST"],
            "importance": "TIER_B"
        },
        "GK Long Throw": {
            "name_vn": "Ném bóng xa (GK)",
            "code": "GK_LONG_THROW",
            "effect_glxh": "Thủ môn ném bóng phản công nhanh qua nửa sân với độ chính xác cao ngay sau khi bắt gọn bóng.",
            "best_positions": ["GK"],
            "importance": "TIER_S"
        },
        "GK 1-on-1": {
            "name_vn": "Đối mặt (GK)",
            "code": "GK_ONE_ON_ONE",
            "effect_glxh": "AI thủ môn thu hẹp góc sút và đổ người cản phá cực nhanh trong các tình huống tiền đạo đối phương thoát xuống.",
            "best_positions": ["GK"],
            "importance": "TIER_S"
        }
    },
    "body_types": {
        "Lean": {
            "name_vn": "Nhỏ / Gầy",
            "characteristics": "Xoay sở cực nhanh, thoát pressing mượt, rê bóng dính chân nhưng yếu trong tì đè tay đôi.",
            "ideal_roles": ["Winger", "Agile CAM"]
        },
        "Average": {
            "name_vn": "Chuẩn / Trung bình",
            "characteristics": "Cân bằng tối ưu giữa sức càn lướt và độ linh hoạt khi đổi hướng di chuyển.",
            "ideal_roles": ["Box-to-Box CM", "Complete Fullback", "Versatile ST"]
        },
        "Stocky": {
            "name_vn": "Đậm / To con",
            "characteristics": "Trọng tâm thấp hoặc bề ngang dày; cản phá bóng cực gắt, tì đè húc văng đối thủ, cực kỳ bá đạo trong tranh chấp GLXH.",
            "ideal_roles": ["Anchor CDM", "Stopper CB", "Target Man ST"]
        }
    }
}

with open(os.path.join(BASE_DIR, "entities", "mechanics_entities.json"), "w", encoding="utf-8") as f:
    json.dump(entities, f, ensure_ascii=False, indent=2)

print("Created sources, patches, entities.")
