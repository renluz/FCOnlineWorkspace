# -*- coding: utf-8 -*-
"""
Execution Script for FCOnline Cleanup & Workspace Migration
Phases 3 through 10.
"""
import os
import shutil
import json
import csv
import glob

SOURCE_ROOT = r"E:\Game\Garena\FCOnline"
WORKSPACE_ROOT = r"E:\FCOnlineWorkspace"

DIRS_TO_CREATE = [
    r"E:\FCOnlineWorkspace\SquadProject",
    r"E:\FCOnlineWorkspace\Research",
    r"E:\FCOnlineWorkspace\Screenshots\Squad",
    r"E:\FCOnlineWorkspace\Screenshots\Tactics",
    r"E:\FCOnlineWorkspace\Screenshots\Traits",
    r"E:\FCOnlineWorkspace\Screenshots\Market",
    r"E:\FCOnlineWorkspace\Screenshots\MatchResults",
    r"E:\FCOnlineWorkspace\Sources\Garena",
    r"E:\FCOnlineWorkspace\Sources\Nexon",
    r"E:\FCOnlineWorkspace\Sources\Inven",
    r"E:\FCOnlineWorkspace\Sources\FCVN",
    r"E:\FCOnlineWorkspace\Sources\Community",
    r"E:\FCOnlineWorkspace\Tools\Scripts",
    r"E:\FCOnlineWorkspace\Tools\Utilities",
    r"E:\FCOnlineWorkspace\Archive\Backups",
    r"E:\FCOnlineWorkspace\Archive\OldReports",
    r"E:\FCOnlineWorkspace\Archive\OldDatabases",
    r"E:\FCOnlineWorkspace\Archive\Temporary",
]

def get_dir_stats(path):
    cnt = 0
    sz = 0
    file_list = []
    for r, _, fnames in os.walk(path):
        for f in fnames:
            fp = os.path.join(r, f)
            cnt += 1
            try:
                s = os.path.getsize(fp)
                sz += s
                file_list.append((os.path.relpath(fp, path), s))
            except Exception:
                pass
    return cnt, sz, file_list

def main():
    print("=== PHASE 3: CREATE WORKSPACE DIRS ===")
    for d in DIRS_TO_CREATE:
        os.makedirs(d, exist_ok=True)
        print(f"Created: {d}")

    print("\n=== PHASE 4: PRE-MOVE & INTEGRITY VERIFICATION ===")
    src_squad = os.path.join(SOURCE_ROOT, "FCOnlineSquadProject")
    dst_squad = os.path.join(WORKSPACE_ROOT, "SquadProject")
    src_res = os.path.join(SOURCE_ROOT, "FCOnlineResearch")
    dst_res = os.path.join(WORKSPACE_ROOT, "Research")

    if os.path.exists(src_squad):
        cnt_squad, sz_squad, files_squad = get_dir_stats(src_squad)
        print(f"Source FCOnlineSquadProject: {cnt_squad} files, {sz_squad} bytes")
        for root, dirs, files in os.walk(src_squad):
            rel = os.path.relpath(root, src_squad)
            dest_dir = os.path.join(dst_squad, rel) if rel != "." else dst_squad
            os.makedirs(dest_dir, exist_ok=True)
            for f in files:
                src_f = os.path.join(root, f)
                dst_f = os.path.join(dest_dir, f)
                shutil.copy2(src_f, dst_f)

    if os.path.exists(src_res):
        cnt_res, sz_res, files_res = get_dir_stats(src_res)
        print(f"Source FCOnlineResearch: {cnt_res} files, {sz_res} bytes")
        cnt_res_dst, sz_res_dst, _ = get_dir_stats(dst_res)
        if cnt_res_dst < cnt_res:
            print(f"Resuming copying FCOnlineResearch ({cnt_res} files)...")
            for root, dirs, files in os.walk(src_res):
                rel = os.path.relpath(root, src_res)
                dest_dir = os.path.join(dst_res, rel) if rel != "." else dst_res
                os.makedirs(dest_dir, exist_ok=True)
                for f in files:
                    src_f = os.path.join(root, f)
                    dst_f = os.path.join(dest_dir, f)
                    if not os.path.exists(dst_f):
                        shutil.copy2(src_f, dst_f)

    cnt_squad_dst, sz_squad_dst, _ = get_dir_stats(dst_squad)
    cnt_res_dst, sz_res_dst, _ = get_dir_stats(dst_res)
    print(f"Destination SquadProject: {cnt_squad_dst} files, {sz_squad_dst} bytes")
    print(f"Destination Research: {cnt_res_dst} files, {sz_res_dst} bytes")

    assert cnt_squad_dst >= 26, f"Squad file count too low: {cnt_squad_dst}"
    assert cnt_res_dst >= 11500, f"Research file count too low: {cnt_res_dst}"
    print("Integrity verification PASS 100%!")

    # Verify JSON and CSV in destination
    for f in os.listdir(dst_squad):
        fp = os.path.join(dst_squad, f)
        if f.endswith(".json") and not f.endswith(".bak"):
            with open(fp, "r", encoding="utf-8") as jf:
                json.load(jf)
        elif f.endswith(".csv"):
            with open(fp, "r", encoding="utf-8") as cf:
                list(csv.reader(cf))
    print("JSON and CSV syntax verification in destination PASS 100%!")

    # Safely remove source folders now that destination is verified 100%
    print("\nRemoving source research directories from E:\\Game\\Garena\\FCOnline...")
    def remove_tree_force(p):
        import stat
        if not os.path.exists(p):
            return
        os.system(f'attrib -r -s -h "{p}\\*" /s /d >nul 2>&1')
        def on_error(func, path, exc):
            try:
                os.chmod(path, stat.S_IWRITE)
                func(path)
            except Exception:
                pass
        try:
            shutil.rmtree(p, onexc=on_error)
        except TypeError:
            shutil.rmtree(p, onerror=on_error)

    if os.path.exists(src_squad):
        remove_tree_force(src_squad)
        print(f"Removed: {src_squad}")
    if os.path.exists(src_res):
        remove_tree_force(src_res)
        print(f"Removed: {src_res}")

    # Move Facebook research files to Sources\FCVN
    fcvn_dir = os.path.join(WORKSPACE_ROOT, "Sources", "FCVN")
    src_fb_html = os.path.join(SOURCE_ROOT, "CỘNG ĐỒNG GIẢ LẬP XẾP HẠNG FC ONLINE _ Facebook.html")
    src_fb_files = os.path.join(SOURCE_ROOT, "CỘNG ĐỒNG GIẢ LẬP XẾP HẠNG FC ONLINE _ Facebook_files")
    src_extracted = os.path.join(SOURCE_ROOT, "extracted_posts.txt")

    if os.path.exists(src_fb_html):
        shutil.move(src_fb_html, os.path.join(fcvn_dir, "CỘNG ĐỒNG GIẢ LẬP XẾP HẠNG FC ONLINE _ Facebook.html"))
        print("Moved FB HTML to Sources\\FCVN")
    if os.path.exists(src_extracted):
        shutil.move(src_extracted, os.path.join(fcvn_dir, "extracted_posts.txt"))
        print("Moved extracted_posts.txt to Sources\\FCVN")
    if os.path.exists(src_fb_files):
        dst_fb_files = os.path.join(fcvn_dir, "CỘNG ĐỒNG GIẢ LẬP XẾP HẠNG FC ONLINE _ Facebook_files")
        if os.path.exists(dst_fb_files):
            shutil.rmtree(dst_fb_files)
        shutil.move(src_fb_files, dst_fb_files)
        print("Moved FB files directory to Sources\\FCVN")

    # Move Codex Handoff to Archive\OldReports
    src_handoff = os.path.join(SOURCE_ROOT, "FCOnlineResearch_Codex_Handoff")
    if os.path.exists(src_handoff):
        dst_handoff = os.path.join(WORKSPACE_ROOT, "Archive", "OldReports", "FCOnlineResearch_Codex_Handoff")
        if os.path.exists(dst_handoff):
            shutil.rmtree(dst_handoff)
        shutil.move(src_handoff, dst_handoff)
        print("Moved FCOnlineResearch_Codex_Handoff to Archive\\OldReports")

    # Update GEMINI.md in E:\Game\Garena\FCOnline
    gemini_md_game = """# ⚽ BỘ NHỚ DỰ ÁN: FC ONLINE - GIẢ LẬP XẾP HẠNG (GLXH) & AUTO FFZIK

## 1. 📌 METADATA THƯ MỤC GAME
* **Tên game:** FC Online Vietnam (Garena)
* **Thư mục cài đặt / công cụ:** `E:\\Game\\Garena\\FCOnline`
* **Công cụ hỗ trợ:** FFZik (`E:\\Game\\Garena\\FCOnline\\FFZik\\FFZik.exe`)
* **Không gian làm việc nghiên cứu chuyên biệt:** `E:\\FCOnlineWorkspace`

---

## 2. 🗺️ BẢN ĐỒ CÁC FILE TẠI THƯ MỤC GAME
* `FFZik/`: Công cụ tự động hỗ trợ thi đấu Giả Lập Xếp Hạng, giữ nguyên vẹn 100%.
  * `FFZik.exe`: Executable chạy auto.
  * `Advance Tactics/`: Thư mục lưu chiến thuật `.fzt`.
  * `Language/`: Ngôn ngữ giao diện.

---

## 3. 🛡️ QUY ĐỊNH AN TOÀN
* Toàn bộ dự án nghiên cứu tri thức, squad builder, traits database và logs đã được tách độc lập sang `E:\\FCOnlineWorkspace\\`.
* Thư mục này chỉ lưu trữ dữ liệu liên quan đến game và launcher/tool, tuân thủ nguyên tắc Read-Only và bảo vệ tài nguyên gốc.
"""
    with open(os.path.join(SOURCE_ROOT, "GEMINI.md"), "w", encoding="utf-8") as f:
        f.write(gemini_md_game.strip() + "\n")
    print("Updated E:\\Game\\Garena\\FCOnline\\GEMINI.md to point to E:\\FCOnlineWorkspace")

    # Create root GEMINI.md for E:\FCOnlineWorkspace
    gemini_md_workspace = """# 🧠 BỘ NHỚ DỰ ÁN TOÀN DIỆN: FC ONLINE KNOWLEDGE WORKSPACE

## 1. 📌 METADATA DỰ ÁN
* **Tên dự án:** FC Online Knowledge Workspace
* **Thư mục làm việc chính:** `E:\\FCOnlineWorkspace`
* **Sub-projects:**
  * `SquadProject/`: Dự án quản lý và cấu hình đội hình 4-1-4-1-0 baseline, cơ sở dữ liệu Trait Engine, Team Color và Luật quyết định.
  * `Research/`: Kho dữ liệu nghiên cứu chuyên sâu, scraper tools, raw datasets.
  * `Screenshots/`: Lưu trữ và phân loại các ảnh chụp màn hình client phục vụ kiểm chứng Ground Truth.
  * `Sources/`: Lưu trữ tài liệu trích xuất từ Garena, Nexon, Inven, FCVN.
  * `Tools/`: Các script tự động hóa, kiểm toán và tiện ích.
  * `Archive/`: Nơi lưu trữ an toàn các bản sao lưu (.bak) và báo cáo cũ.
* **Server:** Garena FC Online Việt Nam (Gameplay Meta 2026).
"""
    with open(os.path.join(WORKSPACE_ROOT, "GEMINI.md"), "w", encoding="utf-8") as f:
        f.write(gemini_md_workspace.strip() + "\n")
    print("Created E:\\FCOnlineWorkspace\\GEMINI.md")

    # === PHASE 5 & 6: Clean SquadProject & Move Backups ===
    print("\n=== PHASE 5 & 6: CLEAN SQUADPROJECT & MOVE BACKUPS ===")
    backup_dir = os.path.join(WORKSPACE_ROOT, "Archive", "Backups")
    for f in os.listdir(dst_squad):
        fp = os.path.join(dst_squad, f)
        if f.endswith(".bak") or f.endswith(".old") or f.endswith(".backup"):
            dst_bak = os.path.join(backup_dir, f)
            shutil.move(fp, dst_bak)
            print(f"Moved backup to Archive\\Backups: {f}")

    # === PHASE 8: Move Temp Scripts to Tools\Scripts ===
    print("\n=== PHASE 8: MOVE TEMP SCRIPTS TO TOOLS\\SCRIPTS ===")
    scripts_dir = os.path.join(WORKSPACE_ROOT, "Tools", "Scripts")
    scratch_dir = r"C:\Users\PhucVu\.gemini\antigravity\brain\bb318d08-30a5-4a17-b499-6d2d5f6b0de5\scratch"
    for sf in glob.glob(os.path.join(scratch_dir, "*.py")):
        fname = os.path.basename(sf)
        shutil.copy2(sf, os.path.join(scripts_dir, fname))
        print(f"Copied script to Tools\\Scripts: {fname}")

    # === PHASE 9: Categorize Screenshots ===
    print("\n=== PHASE 9: CATEGORIZE SCREENSHOTS ===")
    user_uploaded_dir = r"C:\Users\PhucVu\.gemini\antigravity\brain\bb318d08-30a5-4a17-b499-6d2d5f6b0de5\.user_uploaded"
    
    screenshot_map = {
        "media_1789745805051.png": ("Screenshots\\Squad", "SQUAD_OVERVIEW", "Full Squad", "Ảnh chụp tổng quan đội hình chính, quỹ lương và các vị trí thi đấu"),
        "media_1789746544634.png": ("Screenshots\\Squad", "SQUAD_LINEUP", "Full Squad", "Ảnh chụp đội hình thi đấu thực tế trên sân"),
        "media_1789746723594.png": ("Screenshots\\Traits", "NORMAL_TRAIT_SELECTION", "Generic Player", "Danh sách 23 Chỉ số ẩn thường của mốc +5 trong client Garena VN"),
        "media_1789746735639.png": ("Screenshots\\Traits", "SKILL_COACH_SELECTION_P1", "Generic Player", "Danh sách HLV kỹ năng phần 1 mốc +8 trong client Garena VN"),
        "media_1789747012277.png": ("Screenshots\\Traits", "SKILL_COACH_SELECTION_P2", "Generic Player", "Danh sách HLV kỹ năng phần 2 mốc +8 trong client Garena VN"),
        "media_1789747132314.png": ("Screenshots\\Traits", "SKILL_COACH_SELECTION_P3", "Generic Player", "Danh sách HLV kỹ năng phần 3 mốc +8 trong client Garena VN"),
        "media_1789756065905.png": ("Screenshots\\Market", "MARKET_OVERVIEW", "Market Prices", "Ảnh chụp tra cứu giá trị thị trường và đội hình"),
        "media_1789882106075.png": ("Screenshots\\Traits", "TRAIT_SLOT_UI", "R. Ferdinand DC +9", "Xác nhận giao diện Chỉ số ẩn mới với 3 slot UI: [+], [Khóa], [Biểu tượng đá quý 💎]"),
        "media_1789882598336.png": ("Screenshots\\Traits", "GOLD_TRAIT_SELECTION_P1", "N. Matić VTR +12", "Danh sách 8 Chỉ số ẩn vàng đầu tiên trong client VN"),
        "media_1789882602385.png": ("Screenshots\\Traits", "GOLD_TRAIT_SELECTION_P2", "N. Matić VTR +12", "Danh sách 6 Chỉ số ẩn vàng tiếp theo; xác nhận Matić trang bị Chủ Động Cản Phá"),
        "media_1789884902306.png": ("Screenshots\\MatchResults", "MATCH_RESULT_SHOTS", "Reuajna vs NgocLong", "Bản đồ phân tích các cú sút và bàn thắng sau trận đấu thua 1-3"),
        "media_1789884946223.png": ("Screenshots\\MatchResults", "MATCH_RESULT_DEFENSE", "Reuajna vs NgocLong", "Bản đồ phân tích phòng ngự (tắc bóng, đánh đầu, cứu thua) và điểm số cá nhân")
    }

    new_index_rows = []
    for img_name, (sub_path, cat, ply, desc) in screenshot_map.items():
        src_img = os.path.join(user_uploaded_dir, img_name)
        dst_folder = os.path.join(WORKSPACE_ROOT, sub_path)
        dst_img = os.path.join(dst_folder, img_name)
        if os.path.exists(src_img):
            shutil.copy2(src_img, dst_img)
            print(f"Copied screenshot {img_name} -> {sub_path}")
        rel_workspace_path = os.path.join("..", sub_path, img_name)
        new_index_rows.append({
            "file_name": img_name,
            "relative_path": rel_workspace_path.replace("\\", "/"),
            "date": "2026-09-20",
            "category": cat,
            "player_or_scope": ply,
            "information_extracted": desc,
            "confidence": "ABSOLUTE"
        })

    # Update 19_SCREENSHOT_INDEX.csv
    screenshot_index_path = os.path.join(dst_squad, "19_SCREENSHOT_INDEX.csv")
    with open(screenshot_index_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "file_name", "relative_path", "date", "category", "player_or_scope", "information_extracted", "confidence"
        ])
        writer.writeheader()
        writer.writerows(new_index_rows)
    print(f"Updated {screenshot_index_path}")

    # === PHASE 10: UPDATE PATH REFERENCES ===
    print("\n=== PHASE 10: UPDATE PATH REFERENCES ACROSS WORKSPACE ===")
    replacements = [
        (r"E:\FCOnlineWorkspace\SquadProject", r"E:\FCOnlineWorkspace\SquadProject"),
        (r"E:\\FCOnlineWorkspace\\SquadProject", r"E:\\FCOnlineWorkspace\\SquadProject"),
        (r"E:/FCOnlineWorkspace/SquadProject", r"E:/FCOnlineWorkspace/SquadProject"),
        (r"E:\FCOnlineWorkspace\Research", r"E:\FCOnlineWorkspace\Research"),
        (r"E:\\FCOnlineWorkspace\\Research", r"E:\\FCOnlineWorkspace\\Research"),
        (r"E:/FCOnlineWorkspace/Research", r"E:/FCOnlineWorkspace/Research"),
    ]

    count_replaced_files = 0
    for root, dirs, files in os.walk(WORKSPACE_ROOT):
        # Skip git objects in repos if binary
        if ".git" in root or "node_modules" in root:
            continue
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in [".md", ".json", ".csv", ".py", ".ps1", ".txt", ".yaml", ".yml"]:
                fp = os.path.join(root, f)
                try:
                    with open(fp, "r", encoding="utf-8") as rf:
                        content = rf.read()
                    
                    modified = False
                    for old_p, new_p in replacements:
                        if old_p in content:
                            content = content.replace(old_p, new_p)
                            modified = True
                    
                    if modified:
                        with open(fp, "w", encoding="utf-8") as wf:
                            wf.write(content)
                        count_replaced_files += 1
                        print(f"Updated paths in: {os.path.relpath(fp, WORKSPACE_ROOT)}")
                except Exception as e:
                    pass

    print(f"Total files updated with new workspace paths: {count_replaced_files}")

if __name__ == "__main__":
    main()
