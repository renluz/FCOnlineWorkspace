# -*- coding: utf-8 -*-
"""
Phase 1: Generate E:\\FCOnline_CLEANUP_INVENTORY.csv
Recursively scans E:\\Game\\Garena\\FCOnline and classifies all files.
"""
import os
import csv
import datetime

SCAN_DIR = r"E:\Game\Garena\FCOnline"
OUTPUT_CSV = r"E:\FCOnline_CLEANUP_INVENTORY.csv"

def classify_file(full_path, rel_path):
    parts = rel_path.split(os.sep)
    top_item = parts[0]
    ext = os.path.splitext(full_path)[1].lower()
    
    # 1. FFZik
    if top_item == "FFZik":
        return {
            "classification": "UNKNOWN",
            "confidence": "HIGH",
            "reason": "Ứng dụng hỗ trợ auto GLXH (FFZik.exe) & tài nguyên liên quan, bảo toàn nguyên vẹn",
            "proposed_action": "LEAVE_UNTOUCHED"
        }
        
    # 2. GEMINI.md at root
    if rel_path == "GEMINI.md":
        return {
            "classification": "GAME_CONFIG",
            "confidence": "HIGH",
            "reason": "Bộ nhớ ngữ cảnh phân tán cục bộ tại thư mục game, cập nhật để trỏ sang workspace mới",
            "proposed_action": "LEAVE_UNTOUCHED"
        }
        
    # 3. Facebook source files
    if "CỘNG ĐỒNG GIẢ LẬP XẾP HẠNG FC ONLINE _ Facebook" in top_item or rel_path == "extracted_posts.txt":
        return {
            "classification": "RESEARCH_SOURCE",
            "confidence": "ABSOLUTE",
            "reason": "Tài liệu và hình ảnh lưu trữ từ nhóm Facebook Cộng Đồng GLXH phục vụ nghiên cứu",
            "proposed_action": "MOVE_TO_WORKSPACE_SOURCES_FCVN"
        }
        
    # 4. FCOnlineSquadProject
    if top_item == "FCOnlineSquadProject":
        if ext in [".bak", ".old", ".backup"]:
            cls = "BACKUP"
            act = "MOVE_TO_WORKSPACE_ARCHIVE_BACKUPS"
        elif ext == ".csv" or ext == ".json":
            cls = "DATABASE"
            act = "MOVE_TO_WORKSPACE_SQUADPROJECT"
        elif ext == ".md":
            cls = "GENERATED_REPORT"
            act = "MOVE_TO_WORKSPACE_SQUADPROJECT"
        elif ext in [".py", ".ps1", ".bat", ".cmd"]:
            cls = "TEMP_SCRIPT"
            act = "MOVE_TO_WORKSPACE_TOOLS_SCRIPTS"
        else:
            cls = "RESEARCH_PROJECT"
            act = "MOVE_TO_WORKSPACE_SQUADPROJECT"
        return {
            "classification": cls,
            "confidence": "ABSOLUTE",
            "reason": "Tệp thuộc dự án nghiên cứu và cấu hình đội hình FCOnlineSquadProject do AI tạo",
            "proposed_action": act
        }

    # 5. FCOnlineResearch_Codex_Handoff
    if top_item == "FCOnlineResearch_Codex_Handoff":
        return {
            "classification": "RESEARCH_PROJECT",
            "confidence": "ABSOLUTE",
            "reason": "Tài liệu chuyển giao và cài đặt research giữa AI Agent Codex & Gemini",
            "proposed_action": "MOVE_TO_WORKSPACE_ARCHIVE_OLDREPORTS"
        }

    # 6. FCOnlineResearch
    if top_item == "FCOnlineResearch":
        if ext in [".bak", ".old", ".backup"]:
            cls = "BACKUP"
            act = "MOVE_TO_WORKSPACE_ARCHIVE_BACKUPS"
        elif ext in [".csv", ".json", ".sqlite", ".db"]:
            cls = "DATABASE"
            act = "MOVE_TO_WORKSPACE_RESEARCH"
        elif ext == ".md":
            cls = "GENERATED_REPORT"
            act = "MOVE_TO_WORKSPACE_RESEARCH"
        elif ext in [".py", ".ps1", ".bat", ".cmd", ".sh", ".js", ".ts"]:
            cls = "TEMP_SCRIPT"
            act = "MOVE_TO_WORKSPACE_RESEARCH"
        else:
            cls = "RESEARCH_PROJECT"
            act = "MOVE_TO_WORKSPACE_RESEARCH"
        return {
            "classification": cls,
            "confidence": "ABSOLUTE",
            "reason": "Dữ liệu, scraper và tài liệu nghiên cứu GLXH FCOnline tạo trong các phiên trước",
            "proposed_action": act
        }

    # Default fallback for any unexpected file
    return {
        "classification": "UNKNOWN",
        "confidence": "LOW",
        "reason": "Tệp không xác định rõ ràng nguồn gốc trong thư mục game",
        "proposed_action": "LEAVE_UNTOUCHED"
    }

def main():
    rows = []
    print(f"Scanning {SCAN_DIR}...")
    for root, dirs, files in os.walk(SCAN_DIR):
        for f in files:
            full_p = os.path.join(root, f)
            rel_p = os.path.relpath(full_p, SCAN_DIR)
            ext = os.path.splitext(f)[1]
            try:
                st = os.stat(full_p)
                sz = st.st_size
                ct = datetime.datetime.fromtimestamp(st.st_ctime).strftime("%Y-%m-%d %H:%M:%S")
                mt = datetime.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            except Exception:
                sz = 0
                ct = ""
                mt = ""
            
            c_info = classify_file(full_p, rel_p)
            rows.append({
                "full_path": full_p,
                "relative_path": rel_p,
                "type": "file",
                "extension": ext,
                "size_bytes": sz,
                "created_time": ct,
                "modified_time": mt,
                "classification": c_info["classification"],
                "confidence": c_info["confidence"],
                "reason": c_info["reason"],
                "proposed_action": c_info["proposed_action"]
            })

    print(f"Total files scanned: {len(rows)}")
    with open(OUTPUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "full_path", "relative_path", "type", "extension", "size_bytes",
            "created_time", "modified_time", "classification", "confidence",
            "reason", "proposed_action"
        ])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Successfully generated {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
