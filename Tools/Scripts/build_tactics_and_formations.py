import os
import json

BASE_DIR = r"E:\FCOnlineWorkspace\Research\knowledge"

# 1. INDIVIDUAL TACTICS REGISTRY
ind_tactics = {
    "ST_CF": {
        "AR": {
            "name": "Hỗ trợ tấn công (Attacking Runs)",
            "options": {
                "AR1": {
                    "ui_label_vn": "Xẻ nách / Chạy chỗ phá bẫy việt vị",
                    "description_official": "Cầu thủ chủ động di chuyển chéo vào khoảng trống giữa trung vệ và hậu vệ cánh đối phương.",
                    "effect_glxh": "Rất hiệu quả khi đối thủ dâng cao; tận dụng tốc độ và chỉ số Chọn vị trí để đón chọc khe QW/ZW.",
                    "patch": "GAMEPLAY_12TH_2026",
                    "source": "OFFICIAL_GARENA",
                    "evidence_tier": "A"
                },
                "AR2": {
                    "ui_label_vn": "Mục tiêu / Tiền đạo cắm làm tường",
                    "description_official": "Cầu thủ giữ vị trí trung tâm, quay lưng về phía khung thành để nhận bóng và phân phối cho tuyến 2.",
                    "effect_glxh": "Cực kỳ hợp với tiền đạo to con (Boniface, Haaland); giữ bóng chắc, thu hút trung vệ mở khoảng trống cho CAM/Winger.",
                    "patch": "GAMEPLAY_12TH_2026",
                    "source": "OFFICIAL_GARENA",
                    "evidence_tier": "A"
                },
                "AR3": {
                    "ui_label_vn": "Dạt biên / Mở rộng không gian",
                    "description_official": "Cầu thủ dạt hẳn sang cánh để kéo giãn cự ly phòng ngự đối phương.",
                    "effect_glxh": "Hiếm khi dùng trong sơ đồ 1 tiền đạo cắm; thường chỉ dùng cho CF trong hệ thống biến ảo.",
                    "patch": "GAMEPLAY_12TH_2026",
                    "source": "COMMUNITY_OBSERVED",
                    "evidence_tier": "C"
                }
            }
        },
        "DP": {
            "name": "Hỗ trợ phòng ngự (Defensive Pressing)",
            "options": {
                "DP1": {
                    "ui_label_vn": "Tập trung trung lộ / Giữ vị trí trung tâm",
                    "description_official": "Tiền đạo không lùi sâu về phòng ngự, luôn sẵn sàng đón đường bóng phản công tại trung lộ.",
                    "effect_glxh": "Tiết kiệm thể lực tối đa cho ST; giữ vững cự ly để làm điểm kết nối phản công.",
                    "patch": "GAMEPLAY_12TH_2026",
                    "source": "OFFICIAL_GARENA",
                    "evidence_tier": "A"
                },
                "DP2": {
                    "ui_label_vn": "Hỗ trợ phòng ngự",
                    "description_official": "Tiền đạo lùi về quấy rối tiền vệ phòng ngự đối phương khi mất bóng.",
                    "effect_glxh": "Làm hao mòn thể lực ST rất nhanh; chỉ nên dùng cho các ST có thể lực dồi dào (>110).",
                    "patch": "GAMEPLAY_12TH_2026",
                    "source": "OFFICIAL_GARENA",
                    "evidence_tier": "A"
                }
            }
        },
        "IN": {
            "name": "Đánh chặn (Interceptions)",
            "options": {
                "IN1": {"ui_label_vn": "Đánh chặn chủ động / Gắt gao", "effect_glxh": "Áp sát hậu vệ đối phương ngay khi họ có bóng; dễ bị vượt qua nếu đối thủ chuyền nhanh.", "evidence_tier": "A"},
                "IN2": {"ui_label_vn": "Đánh chặn thận trọng", "effect_glxh": "Giữ cự ly che chắn góc chuyền, tránh bị bắt bài.", "evidence_tier": "A"}
            }
        },
        "SR": {
            "name": "Chạy chỗ hỗ trợ (Support Runs)",
            "options": {
                "SR1": {"ui_label_vn": "Chạy chỗ áp sát hàng thủ", "effect_glxh": "ST liên tục đứng trên mép việt vị đè mặt trung vệ đối phương.", "evidence_tier": "B"},
                "SR2": {"ui_label_vn": "Đợi bóng / Lùi lại hỗ trợ", "effect_glxh": "ST chủ động giật lùi 2-3 nhịp nhận bóng phối hợp.", "evidence_tier": "B"}
            }
        }
    },
    "CAM": {
        "DS": {
            "name": "Hỗ trợ phòng thủ (Defensive Support)",
            "options": {
                "DS1": {"ui_label_vn": "Luôn ở phía trên", "effect_glxh": "CAM luôn túc trực ở 1/3 sân đối phương, sẵn sàng chọc khe hoặc đón bóng 2.", "evidence_tier": "A"},
                "DS2": {"ui_label_vn": "Hỗ trợ phòng ngự cơ bản", "effect_glxh": "Lùi về tạo khối 3 tiền vệ trung tâm che chắn tuyến giữa.", "evidence_tier": "A"}
            }
        },
        "SC": {
            "name": "Xâm nhập vòng cấm (Cross Support)",
            "options": {
                "SC1": {"ui_label_vn": "Xâm nhập vòng cấm khi tạt bóng", "effect_glxh": "Lao vào điểm mù trung vệ để đánh đầu hoặc đệm bóng cận thành (rất hợp Lampard, Ballack).", "evidence_tier": "A"},
                "SC2": {"ui_label_vn": "Đợi bóng ở rìa vòng cấm", "effect_glxh": "Dừng lại tuyến 2 đón bóng nảy ra để sút xa ZD/D căng.", "evidence_tier": "A"}
            }
        },
        "PF": {
            "name": "Tự do di chuyển (Positioning Freedom)",
            "options": {
                "PF1": {"ui_label_vn": "Di chuyển tự do (Free Roam)", "effect_glxh": "CAM di chuyển khắp trục ngang tìm bóng; biến hóa nhưng dễ làm xáo trộn cự ly đội hình.", "evidence_tier": "B"},
                "PF2": {"ui_label_vn": "Giữ vị trí kỷ luật (Stick to Position)", "effect_glxh": "Đảm bảo đúng trục dọc liên kết ST và CDM.", "evidence_tier": "B"}
            }
        },
        "IN": {
            "name": "Đánh chặn (Interceptions)",
            "options": {
                "IN1": {"ui_label_vn": "Chủ động", "evidence_tier": "A"},
                "IN2": {"ui_label_vn": "Thận trọng", "evidence_tier": "A"}
            }
        }
    },
    "LDM_RDM_CDM": {
        "AS": {
            "name": "Hỗ trợ tấn công (Attacking Support)",
            "options": {
                "AS1": {"ui_label_vn": "Ở lại phía sau khi tấn công (Stay Back)", "effect_glxh": "BẮT BUỘC cho vị trí Anchor; không dâng quá vòng tròn giữa sân, chống phản công cực tốt.", "evidence_tier": "A"},
                "AS2": {"ui_label_vn": "Tham gia tấn công (Join the Attack)", "effect_glxh": "Dâng lên tiếp ứng tuyến 2; hợp với Ball-Winner hoặc Box-to-Box sút xa tốt.", "evidence_tier": "A"}
            }
        },
        "DB": {
            "name": "Hỗ trợ phòng thủ (Defensive Behavior)",
            "options": {
                "DB1": {"ui_label_vn": "Cắt đường chuyền (Cut Passing Lanes)", "effect_glxh": "AI ưu tiên đứng chắn các khe chuyền bóng sệt của đối thủ.", "evidence_tier": "A"},
                "DB2": {"ui_label_vn": "Kèm chặt người (Man Mark)", "effect_glxh": "Bám sát CAM đối phương; dễ bị hút người kéo giãn khoảng trống nếu đối thủ rê bóng dắt.", "evidence_tier": "A"}
            }
        },
        "DP": {
            "name": "Định vị trung tuyến (Defensive Position)",
            "options": {
                "DP1": {"ui_label_vn": "Bao quát cánh (Cover Wing)", "effect_glxh": "Dạt ra hỗ trợ hậu vệ biên khi đối thủ khoét cánh.", "evidence_tier": "A"},
                "DP2": {"ui_label_vn": "Bảo vệ trung lộ (Cover Center)", "effect_glxh": "CỰC KỲ QUAN TRỌNG trong GLXH; khóa chặt hành lang trung tâm trước mặt 2 CB.", "evidence_tier": "A"}
            }
        },
        "IN": {
            "name": "Đánh chặn (Interceptions)",
            "options": {
                "IN1": {"ui_label_vn": "Đánh chặn chủ động", "effect_glxh": "Lao lên tranh cướp bóng sớm; cần chỉ số Quyết đoán và Thể hình cao.", "evidence_tier": "A"},
                "IN2": {"ui_label_vn": "Đánh chặn thận trọng", "effect_glxh": "Lùi bước giữ cự ly che chắn.", "evidence_tier": "A"}
            }
        }
    },
    "LB_RB": {
        "AR": {
            "name": "Tấn công biên (Attacking Runs)",
            "options": {
                "AR1": {"ui_label_vn": "Chồng biên / Tham gia tấn công (Overlap)", "effect_glxh": "Dâng cao tạo lợi thế quân số ở cánh nhưng để lộ khoảng trống cực lớn sau lưng.", "evidence_tier": "A"},
                "AR2": {"ui_label_vn": "Ở lại phía sau khi tấn công (Stay Back)", "effect_glxh": "Tạo bức tường 4 hậu vệ kiên cố, vô hiệu hóa các bài phản công cánh tốc độ của đối thủ.", "evidence_tier": "A"}
            }
        },
        "IN": {
            "name": "Đánh chặn (Interceptions)",
            "options": {
                "IN1": {"ui_label_vn": "Chủ động", "evidence_tier": "A"},
                "IN2": {"ui_label_vn": "Thận trọng", "evidence_tier": "A"}
            }
        },
        "SR": {
            "name": "Khuynh hướng di chuyển (Support Runs)",
            "options": {
                "SR1": {"ui_label_vn": "Bó vào trong (Inverted)", "effect_glxh": "Bó vào giữa như một tiền vệ mỏ neo phụ khi đội nhà cầm bóng.", "evidence_tier": "B"},
                "SR2": {"ui_label_vn": "Bám biên (Overlap wide)", "effect_glxh": "Luôn mở rộng biên độ đội hình.", "evidence_tier": "B"}
            }
        }
    },
    "CB": {
        "IN": {
            "name": "Đánh chặn (Interceptions)",
            "options": {
                "IN1": {"ui_label_vn": "Đánh chặn chủ động / Dập gắt", "effect_glxh": "Trung vệ dập lao lên chặn bóng ngay khi đối thủ chạm bước một (hợp Desailly, Ramos).", "evidence_tier": "A"},
                "IN2": {"ui_label_vn": "Đánh chặn thận trọng / Thòng bọc lót", "effect_glxh": "Lùi sâu giữ cự ly, bọc lót khi trung vệ dập lỡ trớn (hợp Schär, Van Dijk).", "evidence_tier": "A"}
            }
        }
    }
}

with open(os.path.join(BASE_DIR, "tactics", "individual_tactics_registry.json"), "w", encoding="utf-8") as f:
    json.dump(ind_tactics, f, ensure_ascii=False, indent=2)

# 2. TEAM TACTICS REGISTRY
team_tactics = {
    "speed": {"min": 1, "max": 99, "glxh_optimal_range": [45, 60], "effect": "Kiểm soát nhịp độ triển khai bóng từ sân nhà. <40 quá chậm dễ bị quây, >70 bóng đi vội dễ chuyền hỏng."},
    "passing_buildup": {"min": 1, "max": 99, "glxh_optimal_range": [35, 55], "effect": "Cự ly cự ly chuyền bóng trong triển khai. Giá trị thấp giữ cự ly cự ly gần phối hợp 1-2."},
    "positioning_buildup": {"options": ["Tổ chức (Organised)", "Tự do (Free Form)"], "glxh_recommendation": "Tổ chức để giữ nguyên khối đội hình hình học."},
    "crossing": {"min": 1, "max": 99, "glxh_optimal_range": [40, 65], "effect": "Tần suất và vị trí cầu thủ chờ đón bóng tạt bổng vào vòng cấm."},
    "shooting": {"min": 1, "max": 99, "glxh_optimal_range": [40, 65], "effect": "Mức độ sẵn sàng vung chân sút xa khi có khoảng trống ở tuyến 2."},
    "pressure": {"min": 1, "max": 99, "glxh_optimal_range": [35, 55], "effect": "Độ cao của khối đội hình phòng ngự. >65 dâng cao bắt việt vị nhưng rất dễ bị QW."},
    "aggression": {"min": 1, "max": 99, "glxh_optimal_range": [40, 55], "effect": "Mức độ quyết liệt khi áp sát tranh cướp bóng. >60 dễ ăn thẻ phạt hoặc bị qua người."},
    "team_width": {"min": 1, "max": 99, "glxh_optimal_range": [40, 52], "effect": "Bề ngang của hàng thủ. Giữ 45-50 để bảo vệ trung lộ và nách trung vệ."}
}

with open(os.path.join(BASE_DIR, "tactics", "team_tactics_registry.json"), "w", encoding="utf-8") as f:
    json.dump(team_tactics, f, ensure_ascii=False, indent=2)

# 3. FORMATION KNOWLEDGE FILES (7 FORMATIONS)
formations = {
    "4-2-3-1": {
        "formation_code": "4-2-3-1",
        "name": "4-2-3-1 Đóng Băng Trung Tuyến (The Balanced Benchmark)",
        "structure": "4 Hậu vệ (LB-CB-CB-RB), 2 Tiền vệ trụ (LDM-RDM), 3 Tiền vệ công (LAM-CAM-RAM), 1 Tiền đạo cắm (ST)",
        "roles": {
            "ST": "Target Man hoặc Complete Forward có khả năng tì đè và dứt điểm đa dạng.",
            "CAM": "Nhạc trưởng trung lộ, tầm nhìn cao, sút xa tốt.",
            "LAM_RAM": "Cầu thủ chạy cánh hoặc Inside Forward đảo chân cắt vào trong.",
            "LDM_RDM": "Cặp bài trùng hoàn hảo: 1 Anchor giữ vị trí + 1 Box-to-Box cơ động.",
            "LB_RB": "Hậu vệ biên giữ vị trí (AR2 Stay Back) để chống phản công biên."
        },
        "strengths": ["Cực kỳ cân bằng giữa công và thủ", "Kiểm soát bóng tuyến giữa áp đảo", "Chống phản công tốt nhờ cặp Double Pivot"],
        "weaknesses": ["Nếu ST bị cô lập thì đợt tấn công dễ bế tắc", "Yêu cầu CAM và 2 Wingers có nhãn quan chuyền bóng tốt"],
        "high_rank_evidence": "Chiếm trên 45% lựa chọn của Top 100 Inven Super Champions Hàn Quốc và Rank Thách Đấu Garena VN.",
        "patch": "GAMEPLAY_12TH_2026",
        "server": "GLOBAL_GENERIC",
        "required_profiles": "ST to khỏe, CAM kiến tạo, LDM/RDM thể lực >110 và thủ >110."
    },
    "4-2-2-1-1": {
        "formation_code": "4-2-2-1-1",
        "name": "4-2-2-1-1 Chuyển Trạng Thái Siêu Tốc (Transition Master)",
        "structure": "4 Hậu vệ, 2 Tiền vệ trụ (LDM-RDM), 2 Tiền vệ cánh (LM-RM), 1 Hộ công (CF/CAM), 1 Tiền đạo cắm (ST)",
        "strengths": ["Khả năng bung tốc độ phản công biên cực nhanh", "Hộ công lùi sâu kết nối tuyến giữa rất mượt"],
        "weaknesses": ["Khoảng cách giữa LM/RM và trung lộ đôi khi bị loãng"],
        "patch": "GAMEPLAY_12TH_2026",
        "server": "GLOBAL_GENERIC",
        "required_profiles": "LM/RM có tốc độ xé gió, CF có nhãn quan và dứt điểm ZD."
    },
    "4-1-2-3": {
        "formation_code": "4-1-2-3",
        "name": "4-1-2-3 Pressing Tầm Cao (High Press Control)",
        "structure": "4 Hậu vệ, 1 Tiền vệ mỏ neo (CDM), 2 Tiền vệ trung tâm (LCM-RCM), 3 Tiền đạo (LW-ST-RW)",
        "strengths": ["Áp đặt thế trận cực mạnh trên phần sân đối phương", "Sức sát thương 3 mũi công biên và trung lộ"],
        "weaknesses": ["Rủi ro cao nhất: Single CDM bị quá tải nếu đối thủ thoát pressing phản công nhanh"],
        "patch": "GAMEPLAY_12TH_2026",
        "server": "KR_NEXON",
        "required_profiles": "CDM phải là quái vật thể hình và đánh chặn (Rodri, Vieira, Rijkaard)."
    },
    "4-1-2-3-0": {
        "formation_code": "4-1-2-3-0",
        "name": "4-1-2-3-0 Kiểm Soát Không Tiền Đạo Cắm (False 9 Total Football)",
        "structure": "4 Hậu vệ, 1 CDM, 2 CM, 2 Wingers (LW-RW), 1 CF/CAM lùi sâu không có ST cắm",
        "strengths": ["Hàng thủ đối phương mất phương hướng do không có tiền đạo để kèm", "Kiểm soát bóng 60-70%"],
        "weaknesses": ["Thiếu điểm cắt bóng trong các tình huống tạt cánh bổng"],
        "patch": "GAMEPLAY_12TH_2026",
        "server": "KR_NEXON",
        "required_profiles": "Toàn bộ tiền vệ và tiền đạo đều phải có kỹ năng chuyền bóng và rê dắt thượng thừa."
    },
    "4-1-2-1-2": {
        "formation_code": "4-1-2-1-2",
        "name": "4-1-2-1-2 Kim Cương Hẹp (Narrow Diamond Central Overload)",
        "structure": "4 Hậu vệ, 1 CDM, 2 CM (LCM-RCM), 1 CAM, 2 Tiền đạo (LS-RS)",
        "strengths": ["Hỏa lực 2 tiền đạo bổ trợ cho nhau", "Đột phá vỗ mặt trung lộ bằng bật nhả 1-2 cự ly ngắn"],
        "weaknesses": ["Hoàn toàn không có tiền vệ cánh, rất dễ bị đối thủ khoét nách biên"],
        "patch": "GAMEPLAY_12TH_2026",
        "server": "VN_GARENA",
        "required_profiles": "Cần 2 hậu vệ biên có thể lực dồi dào gánh trọn vẹn hành lang cánh."
    },
    "4-3-1-2": {
        "formation_code": "4-3-1-2",
        "name": "4-3-1-2 Tam Giác Cơ Động Tuyến Giữa",
        "structure": "4 Hậu vệ, 3 Tiền vệ trung tâm (LCM-CM-RCM), 1 CAM, 2 Tiền đạo (ST-ST)",
        "strengths": ["Khối trung tuyến 3 người che chắn cực kỳ chặt chẽ", "Phối hợp trung lộ biến hóa"],
        "weaknesses": ["Cần CM có tốc độ và khả năng dạt biên khi cần thiết"],
        "patch": "GAMEPLAY_12TH_2026",
        "server": "GLOBAL_GENERIC",
        "required_profiles": "3 tiền vệ trung tâm toàn diện cả công lẫn thủ."
    },
    "5-2-3": {
        "formation_code": "5-2-3",
        "name": "5-2-3 Khối Thấp Phản Công Thần Tốc (Low Block Counter)",
        "structure": "5 Hậu vệ (LWB-LCB-CB-RCB-RWB), 2 Tiền vệ (LCM-RCM hoặc LDM-RDM), 3 Tiền đạo (LW-ST-RW)",
        "strengths": ["Phòng ngự số đông cực kỳ khó khoan phá trong vòng cấm", "Tận dụng tốc độ 3 tiền đạo phản công chớp nhoáng"],
        "weaknesses": ["Tuyến giữa chỉ có 2 người, dễ bị đối phương ép sân và kiểm soát bóng dài hạn"],
        "patch": "GAMEPLAY_12TH_2026",
        "server": "VN_GARENA",
        "required_profiles": "3 trung vệ không chiến tốt, 2 tiền đạo cánh có tốc độ vượt trội."
    }
}

for f_code, data in formations.items():
    safe_name = f_code.replace("/", "-")
    with open(os.path.join(BASE_DIR, "formations", f"{safe_name}.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 4. PLAYER ARCHETYPES REGISTRY
archetypes = {
    "RUN_BEHIND_ST": {
        "name": "Tiền đạo chạy chỗ phá bẫy việt vị",
        "core_attributes": ["Tốc độ", "Tăng tốc", "Chọn vị trí", "Phản xạ", "Khéo léo"],
        "key_traits": ["Ma tốc độ", "Phá bẫy việt vị"],
        "ideal_instructions": "AR1 (Xẻ nách), DP1 (Tập trung trung lộ)",
        "examples": ["Son Heung Min", "Aubameyang", "Mbappe", "Shevchenko"]
    },
    "TARGET_MAN_ST": {
        "name": "Tiền đạo mục tiêu làm tường / Không chiến",
        "core_attributes": ["Sức mạnh", "Chiều cao (>=188cm)", "Đánh đầu", "Nhảy", "Giữ bóng", "Dứt điểm"],
        "key_traits": ["Đánh đầu mạnh", "Cứng như thép"],
        "ideal_instructions": "AR2 (Mục tiêu), DP1 (Tập trung trung lộ)",
        "examples": ["V. Boniface", "E. Haaland", "D. Drogba", "R. van Nistelrooy"]
    },
    "BOX_TO_BOX_CM": {
        "name": "Tiền vệ con thoi toàn diện",
        "core_attributes": ["Thể lực (>=115)", "Chuyền ngắn", "Sút xa", "Cắt bóng", "Tốc độ đều"],
        "key_traits": ["Sút xa", "Thánh chuyền bóng"],
        "ideal_instructions": "AS2 hoặc AS Mặc định, DP2 (Bảo vệ trung lộ)",
        "examples": ["F. Lampard", "W. Zaïre-Emery", "R. Gullit", "M. Ballack"]
    },
    "ANCHOR_CDM": {
        "name": "Tiền vệ mỏ neo thuần túy",
        "core_attributes": ["Cắt bóng (>=115)", "Quyết đoán (>=110)", "Kèm người", "Thể hình Đậm/Chuẩn", "Bình tĩnh"],
        "key_traits": ["Cứng như thép", "Chuyền dài"],
        "ideal_instructions": "AS1 (Ở lại phía sau), DB1 (Cắt đường chuyền), DP2 (Bảo vệ trung lộ)",
        "examples": ["Rodri", "P. Vieira", "F. Rijkaard", "Casemiro"]
    },
    "STOPPER_CB": {
        "name": "Trung vệ dập áp sát quyết liệt",
        "core_attributes": ["Sức mạnh", "Quyết đoán", "Tắc bóng", "Xoạc bóng", "Thể hình Đậm"],
        "key_traits": ["Cứng như thép", "Đánh đầu mạnh"],
        "ideal_instructions": "IN1 (Đánh chặn chủ động)",
        "examples": ["M. Desailly", "Sergio Ramos", "Jaap Stam", "Vidic"]
    },
    "COVER_SWEEPER_CB": {
        "name": "Trung vệ thòng bọc lót / Phân phối bóng",
        "core_attributes": ["Tốc độ", "Phản xạ", "Chọn vị trí phòng ngự", "Bình tĩnh", "Chuyền dài"],
        "key_traits": ["Chuyền dài"],
        "ideal_instructions": "IN2 (Đánh chặn thận trọng)",
        "examples": ["F. Schär", "V. van Dijk", "F. Maldini", "F. Cannavaro"]
    },
    "COMPLETE_FULLBACK": {
        "name": "Hậu vệ biên toàn diện 2 chân",
        "core_attributes": ["Tốc độ (>=120)", "Thể lực (>=120)", "Tắc bóng", "Tạt bóng", "Chân không thuận >=4"],
        "key_traits": ["Ma tốc độ", "Tạt bóng sớm"],
        "ideal_instructions": "AR2 (Ở lại phía sau) để thủ chắc, hoặc AR1 (Chồng biên) khi cần bàn",
        "examples": ["G. Zambrotta", "J. Gvardiol", "A. Cole", "Cafu"]
    },
    "GIANT_SHOT_STOPPER_GK": {
        "name": "Thủ môn hộ pháp phản xạ",
        "core_attributes": ["Chiều cao (>=195cm)", "Phản xạ GK", "Đổ người GK", "Bắt bóng GK"],
        "key_traits": ["Ném bóng xa", "Cản phá 1-on-1"],
        "examples": ["Mailson", "W. Hennessey", "T. Courtois", "E. van der Sar"]
    }
}

with open(os.path.join(BASE_DIR, "players", "player_archetypes.json"), "w", encoding="utf-8") as f:
    json.dump(archetypes, f, ensure_ascii=False, indent=2)

print("Created tactics, formations, and player archetypes.")
