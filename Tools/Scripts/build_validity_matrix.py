import os
import csv

BASE_DIR = r"E:\FCOnlineWorkspace\Research\knowledge\tactics"
out_csv = os.path.join(BASE_DIR, "TACTIC_VALIDITY_MATRIX.csv")

rows = [
    # ST / CF
    {"position": "ST", "group": "AR", "variant": "AR", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Hỗ trợ tấn công cân bằng (mặc định)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "ST", "group": "AR", "variant": "AR1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Xẻ nách / Chạy chỗ phá bẫy việt vị", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "ST", "group": "AR", "variant": "AR2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Mục tiêu / Tiền đạo cắm làm tường", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "ST", "group": "AR", "variant": "AR3", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Dạt biên / Mở rộng không gian", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    
    {"position": "ST", "group": "DP", "variant": "DP", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Hỗ trợ phòng ngự cân bằng (mặc định)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "ST", "group": "DP", "variant": "DP1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Luôn luôn hỗ trợ phòng thủ (tích cực lùi về)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "ST", "group": "DP", "variant": "DP2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Luôn ở trên (không lùi về, chờ bóng phản công)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "ST", "group": "IN", "variant": "IN", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn thông thường", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "ST", "group": "IN", "variant": "IN1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn chủ động / Gắt gao", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "ST", "group": "IN", "variant": "IN2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn thận trọng", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "ST", "group": "SR", "variant": "SR", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Chạy chỗ cân bằng", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "ST", "group": "SR", "variant": "SR1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Chạy chỗ áp sát hàng thủ (đè mặt mép việt vị)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "ST", "group": "SR", "variant": "SR2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đợi bóng / Lùi lại hỗ trợ nhận bóng", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    # CAM / LAM / RAM
    {"position": "CAM", "group": "DS", "variant": "DS", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Hỗ trợ phòng thủ cơ bản (mặc định)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "CAM", "group": "DS", "variant": "DS1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Luôn ở phía trên (chờ bóng phản công)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "CAM", "group": "DS", "variant": "DS2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Hỗ trợ phòng ngự tích cực", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "CAM", "group": "IN", "variant": "IN", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn thông thường", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "CAM", "group": "IN", "variant": "IN1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn chủ động", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "CAM", "group": "IN", "variant": "IN2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn thận trọng", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "CAM", "group": "PF", "variant": "PF", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Kỷ luật vị trí (mặc định)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "CAM", "group": "PF", "variant": "PF1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Di chuyển tự do (Free Roam)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "CAM", "group": "PF", "variant": "PF2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Di chuyển rộng (chỉ áp dụng CAM; LAM/RAM KHÔNG sử dụng được)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "LAM", "group": "PF", "variant": "PF2", "ui_confirmed": "FALSE", "garena_confirmed": "EXCLUDED", "nexon_confirmed": "EXCLUDED", "community_only": "FALSE", "meaning": "INVALID_FOR_LAM: Garena quy định LAM/RAM không sử dụng được PF2", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RAM", "group": "PF", "variant": "PF2", "ui_confirmed": "FALSE", "garena_confirmed": "EXCLUDED", "nexon_confirmed": "EXCLUDED", "community_only": "FALSE", "meaning": "INVALID_FOR_RAM: Garena quy định LAM/RAM không sử dụng được PF2", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "LAM", "group": "CC", "variant": "CC1", "ui_confirmed": "FALSE", "garena_confirmed": "FALSE", "nexon_confirmed": "FALSE", "community_only": "FALSE", "meaning": "INVALID_FOR_LAM: Nhóm CC chỉ thuộc về LW/RW, không tồn tại trên LAM", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RAM", "group": "CC", "variant": "CC1", "ui_confirmed": "FALSE", "garena_confirmed": "FALSE", "nexon_confirmed": "FALSE", "community_only": "FALSE", "meaning": "INVALID_FOR_RAM: Nhóm CC chỉ thuộc về LW/RW, không tồn tại trên RAM", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "CAM", "group": "SC", "variant": "SC", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Hỗ trợ tạt bóng cân bằng", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "CAM", "group": "SC", "variant": "SC1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Xâm nhập vòng cấm khi tạt bóng", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "CAM", "group": "SC", "variant": "SC2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đợi bóng ở rìa vòng cấm (tuyến 2)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    # CDM / LDM / RDM
    {"position": "LDM", "group": "AS", "variant": "AS", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Hỗ trợ tấn công cân bằng (mặc định)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LDM", "group": "AS", "variant": "AS1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Ở lại phía sau khi tấn công (Stay Back)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LDM", "group": "AS", "variant": "AS2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Tham gia tấn công", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LDM", "group": "AS", "variant": "AS3", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Vị trí giữa các hậu vệ (chỉ áp dụng cho đội hình 4 hậu vệ)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "RDM", "group": "AS", "variant": "AS", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Hỗ trợ tấn công cân bằng (mặc định)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RDM", "group": "AS", "variant": "AS1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Ở lại phía sau khi tấn công (Stay Back)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RDM", "group": "AS", "variant": "AS2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Tham gia tấn công", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RDM", "group": "AS", "variant": "AS3", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Vị trí giữa các hậu vệ (chỉ áp dụng cho đội hình 4 hậu vệ)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "LDM", "group": "DB", "variant": "DB", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Hỗ trợ phòng thủ cân bằng", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LDM", "group": "DB", "variant": "DB1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Cắt đường chuyền (Cut Passing Lanes)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LDM", "group": "DB", "variant": "DB2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Kèm chặt người (Man Mark)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "RDM", "group": "DB", "variant": "DB", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Hỗ trợ phòng thủ cân bằng", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RDM", "group": "DB", "variant": "DB1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Cắt đường chuyền (Cut Passing Lanes)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RDM", "group": "DB", "variant": "DB2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Kèm chặt người (Man Mark)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "LDM", "group": "DP", "variant": "DP", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Phòng thủ ở biên (bọc lót khi hậu vệ cánh dâng)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LDM", "group": "DP", "variant": "DP1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Tập trung ở trung lộ (bảo vệ trung tâm)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LDM", "group": "DP", "variant": "DP2", "ui_confirmed": "FALSE", "garena_confirmed": "FALSE", "nexon_confirmed": "FALSE", "community_only": "FALSE", "meaning": "INVALID_CODE: Nhóm DP trên tiền vệ trụ KHÔNG có DP2", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "RDM", "group": "DP", "variant": "DP", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Phòng thủ ở biên (bọc lót khi hậu vệ cánh dâng)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RDM", "group": "DP", "variant": "DP1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Tập trung ở trung lộ (bảo vệ trung tâm)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RDM", "group": "DP", "variant": "DP2", "ui_confirmed": "FALSE", "garena_confirmed": "FALSE", "nexon_confirmed": "FALSE", "community_only": "FALSE", "meaning": "INVALID_CODE: Nhóm DP trên tiền vệ trụ KHÔNG có DP2", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "LDM", "group": "IN", "variant": "IN", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn thông thường", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LDM", "group": "IN", "variant": "IN1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn chủ động", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LDM", "group": "IN", "variant": "IN2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn thận trọng", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "RDM", "group": "IN", "variant": "IN", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn thông thường", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RDM", "group": "IN", "variant": "IN1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn chủ động", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RDM", "group": "IN", "variant": "IN2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn thận trọng", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    # LB / RB
    {"position": "LB", "group": "AR", "variant": "AR", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Tấn công cân bằng (mặc định)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LB", "group": "AR", "variant": "AR1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Chồng biên / Tham gia tấn công", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LB", "group": "AR", "variant": "AR2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Ở lại phía sau khi tấn công (Stay Back)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "RB", "group": "AR", "variant": "AR", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Tấn công cân bằng (mặc định)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RB", "group": "AR", "variant": "AR1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Chồng biên / Tham gia tấn công", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RB", "group": "AR", "variant": "AR2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Ở lại phía sau khi tấn công (Stay Back)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "LB", "group": "IN", "variant": "IN", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn thông thường", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LB", "group": "IN", "variant": "IN1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn chủ động", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LB", "group": "IN", "variant": "IN2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn thận trọng", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "RB", "group": "IN", "variant": "IN", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn thông thường", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RB", "group": "IN", "variant": "IN1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn chủ động", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RB", "group": "IN", "variant": "IN2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn thận trọng", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "LB", "group": "SR", "variant": "SR", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Hỗ trợ xâm nhập cân bằng (tùy tình hình)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LB", "group": "SR", "variant": "SR1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Di chuyển từ cánh vào trung tâm (làm tường hỗ trợ tuyến giữa)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LB", "group": "SR", "variant": "SR2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Phối hợp chồng cánh (lên công về thủ dọc biên)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    {"position": "RB", "group": "SR", "variant": "SR", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Hỗ trợ xâm nhập cân bằng (tùy tình hình)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RB", "group": "SR", "variant": "SR1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Di chuyển từ cánh vào trung tâm (làm tường hỗ trợ tuyến giữa)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RB", "group": "SR", "variant": "SR2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Phối hợp chồng cánh (lên công về thủ dọc biên)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    # CB
    {"position": "CB", "group": "IN", "variant": "IN", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn thông thường", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "CB", "group": "IN", "variant": "IN1", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn chủ động / Dập gắt", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "CB", "group": "IN", "variant": "IN2", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Đánh chặn thận trọng / Thòng bọc lót", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},

    # LW / RW
    {"position": "LW", "group": "CC", "variant": "CC3", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Vai trò tự do (di chuyển xung quanh nhiều hơn gần biên)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RW", "group": "CC", "variant": "CC3", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Vai trò tự do (di chuyển xung quanh nhiều hơn gần biên)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "LW", "group": "SR", "variant": "SR3", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Tiền đạo mục tiêu (luôn xuất hiện trong vòng cấm gần hậu vệ cuối)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"},
    {"position": "RW", "group": "SR", "variant": "SR3", "ui_confirmed": "TRUE", "garena_confirmed": "TRUE", "nexon_confirmed": "TRUE", "community_only": "FALSE", "meaning": "Tiền đạo mục tiêu (luôn xuất hiện trong vòng cấm gần hậu vệ cuối)", "source": "OFFICIAL_GARENA", "confidence": "HIGH"}
]

fieldnames = ["position", "group", "variant", "ui_confirmed", "garena_confirmed", "nexon_confirmed", "community_only", "meaning", "source", "confidence"]

with open(out_csv, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for r in rows:
        writer.writerow(r)

print(f"Created {out_csv} with {len(rows)} entries.")
