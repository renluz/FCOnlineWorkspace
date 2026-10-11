import json
import os

data = {
  "_metadata": {
    "source": "CLIENT_SCREENSHOTS_VERIFIED",
    "server": "VN_GARENA",
    "updated_at": "2026-09-20",
    "notes": "Xác minh trực tiếp từ ảnh chụp giao diện client FC Online VN. Tuyệt đối không suy đoán."
  },
  "rules": {
    "already_selected_tag": {
      "raw_text": "(Đã chọn)",
      "meaning": "Trait đó đã có sẵn trên card gốc/đã tồn tại từ trước, KHÔNG PHẢI trait mới đang chọn thêm."
    }
  },
  "matic_vtr_12_status": {
    "player": "N. Matić",
    "season": "VTR",
    "grade": 12,
    "milestone_mechanisms": {
      "plus_5": "Mở 1 Chỉ số ẩn thường (NORMAL_HIDDEN_TRAIT)",
      "plus_8": "Mở 1 HLV kỹ năng (SKILL_COACH)",
      "plus_11": "Mở 1 Chỉ số ẩn vàng (GOLD_HIDDEN_TRAIT)"
    },
    "equipped_traits_status": {
      "plus_5_trait": "UNKNOWN (Chưa có screenshot xác nhận lựa chọn cụ thể của Matić)",
      "plus_8_coach": "UNKNOWN (Chưa có screenshot xác nhận lựa chọn cụ thể của Matić)",
      "plus_11_gold_trait": "UNKNOWN (Chưa có screenshot xác nhận lựa chọn cụ thể của Matić)"
    }
  },
  "milestone_plus_5_normal_traits": {
    "type": "NORMAL_HIDDEN_TRAIT",
    "verification_status": "VERIFIED_CLIENT_VN",
    "total_count": 23,
    "pool": [
      {"id": 1, "name_vn": "Sút xoáy"},
      {"id": 2, "name_vn": "Sút và tạt má ngoài"},
      {"id": 3, "name_vn": "Đánh đầu mạnh"},
      {"id": 4, "name_vn": "Sút xa"},
      {"id": 5, "name_vn": "Bấm bóng"},
      {"id": 6, "name_vn": "Ném biên rất xa"},
      {"id": 7, "name_vn": "Ném biên xa"},
      {"id": 8, "name_vn": "Thánh chuyền bóng"},
      {"id": 9, "name_vn": "Chuyền dài"},
      {"id": 10, "name_vn": "Tạt bóng sớm"},
      {"id": 11, "name_vn": "Tinh tế"},
      {"id": 12, "name_vn": "Ma tốc độ"},
      {"id": 13, "name_vn": "Qua người"},
      {"id": 14, "name_vn": "Cá nhân"},
      {"id": 15, "name_vn": "Siêu cản phá"},
      {"id": 16, "name_vn": "Xoạc bóng"},
      {"id": 17, "name_vn": "Ăn vạ"},
      {"id": 18, "name_vn": "Cứng như thép"},
      {"id": 19, "name_vn": "Nỗ lực đến cùng"},
      {"id": 20, "name_vn": "Tranh cãi"},
      {"id": 21, "name_vn": "Kiến tạo"},
      {"id": 22, "name_vn": "Tránh sai chân thuận"},
      {"id": 23, "name_vn": "Vị trí yêu thích"}
    ]
  },
  "milestone_plus_8_skill_coaches": {
    "type": "SKILL_COACH",
    "verification_status": "VERIFIED_CLIENT_VN",
    "total_count": 41,
    "pool": [
      {"id": 1, "name_vn": "Bậc thầy tốc độ"},
      {"id": 2, "name_vn": "Chiến thuật chuyền Tiki-Taka"},
      {"id": 3, "name_vn": "Chiến thuật chuyền trực tiếp"},
      {"id": 4, "name_vn": "Chiến thuật tiền đạo áp lực"},
      {"id": 5, "name_vn": "Cải thiện chuyền chọc khe"},
      {"id": 6, "name_vn": "Chuyền chọc khe vượt tuyến"},
      {"id": 7, "name_vn": "Cải thiện chuyền kỹ thuật"},
      {"id": 8, "name_vn": "Cải thiện chuyền vượt tuyến"},
      {"id": 9, "name_vn": "Cải thiện chuyền xuyên phá"},
      {"id": 10, "name_vn": "Cải thiện chuyền xà"},
      {"id": 11, "name_vn": "Cải thiện căng ngang"},
      {"id": 12, "name_vn": "Cải thiện khả năng rê bóng khi…", "truncated_in_ui": True},
      {"id": 13, "name_vn": "Cải thiện khả năng sút xa tru…", "truncated_in_ui": True},
      {"id": 14, "name_vn": "Cải thiện phòng thủ bên phải"},
      {"id": 15, "name_vn": "Cải thiện phòng thủ bên trái"},
      {"id": 16, "name_vn": "Cải thiện sút tầm thấp"},
      {"id": 17, "name_vn": "Cải thiện sút xoáy"},
      {"id": 18, "name_vn": "Cải thiện tạt bóng"},
      {"id": 19, "name_vn": "Cải thiện tạt bóng cao"},
      {"id": 20, "name_vn": "Cải thiện đá phạt"},
      {"id": 21, "name_vn": "Cự ly đội hình ổn định"},
      {"id": 22, "name_vn": "Di chuyển ngay khi đỡ bước 1"},
      {"id": 23, "name_vn": "Khả năng khéo léo"},
      {"id": 24, "name_vn": "Khả năng tắc bóng"},
      {"id": 25, "name_vn": "Khả năng xoạc bóng"},
      {"id": 26, "name_vn": "Phản công khi đang phòng thủ"},
      {"id": 27, "name_vn": "Xâm nhập ngay khi kêu gọi xâm nhập"},
      {"id": 28, "name_vn": "Sút cự ly gần"},
      {"id": 29, "name_vn": "Tránh tắc bóng"},
      {"id": 30, "name_vn": "Tránh xoạc bóng"},
      {"id": 31, "name_vn": "Khả năng phòng thủ Pressing"},
      {"id": 32, "name_vn": "TD mục tiêu đặc biệt"},
      {"id": 33, "name_vn": "Tạo cơ hội ghi bàn"},
      {"id": 34, "name_vn": "Tấn công với nhịp độ nhanh"},
      {"id": 35, "name_vn": "Tập trung vào bên phải"},
      {"id": 36, "name_vn": "Tập trung vào bên trái"},
      {"id": 37, "name_vn": "Tập trung đánh chặn"},
      {"id": 38, "name_vn": "Tổ chức"},
      {"id": 39, "name_vn": "Xâm nhập vòng cấm"},
      {"id": 40, "name_vn": "Áp lực"},
      {"id": 41, "name_vn": "Áp đảo toàn sân"}
    ]
  },
  "milestone_plus_11_gold_traits": {
    "type": "GOLD_HIDDEN_TRAIT",
    "verification_status": "MECHANISM_CONFIRMED_POOL_UNRECOVERED",
    "notes": "Cơ chế mở 1 Chỉ số ẩn vàng đã xác minh. Pool cụ thể cho Matić VTR chưa phục hồi được từ lưu trữ. Tuyệt đối không tự suy đoán."
  }
}

target_file = 'E:/FCOnlineWorkspace/Research/knowledge/entities/enhancement_milestones_vn.json'
with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Saved enhancement_milestones_vn.json successfully.')
