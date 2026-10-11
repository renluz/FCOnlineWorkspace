import urllib.request
import json
import os
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = "https://dc.fconline.garena.vn/api/app"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://dc.fconline.garena.vn/lineup"
}

def fetch_json(endpoint):
    url = f"{BASE_URL}{endpoint}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching {endpoint}: {e}")
        return None

def main():
    print("=== BẮT ĐẦU TẢI DỮ LIỆU TỪ GARENA FC ONLINE DATA CENTER ===")
    
    # 1. Fetch Formations Meta
    print("\n1. Đang tải dữ liệu Meta Formations...")
    formations_meta = fetch_json("/meta/formations")
    formations_4141_matchups = fetch_json("/meta/formations/4-1-4-1/matchups")
    
    # 2. Fetch Team Color Meta (Real Madrid: 1018)
    print("2. Đang tải dữ liệu Meta Team Color Real Madrid (1018)...")
    teamcolors_meta = fetch_json("/meta/teamcolors")
    rm_matchups = fetch_json("/meta/teamcolors/1018/matchups")
    
    # 3. Fetch Top 5 Rankers 4-1-4-1
    print("3. Đang tải danh sách Top 5 Ranker sử dụng sơ đồ 4-1-4-1...")
    rankers_4141_list = fetch_json("/meta/mastery?dimension=formation&key=4-1-4-1&rank=legend_up&window=30d")
    top5_4141_details = []
    
    if rankers_4141_list and 'items' in rankers_4141_list:
        items = rankers_4141_list['items'][:5]
        for idx, r in enumerate(items, 1):
            acc_id = r.get('accountId')
            nick = r.get('nickname')
            print(f"   [{idx}/5] Đang tải chi tiết Ranker 4-1-4-1: {nick} ({acc_id})...")
            detail = fetch_json(f"/meta/mastery/{acc_id}?dimension=formation&key=4-1-4-1&rank=legend_up&window=30d")
            top5_4141_details.append({
                "summary": r,
                "detail": detail.get('data') if detail else None
            })
            time.sleep(0.3)
            
    # 4. Fetch Top 5 Rankers Real Madrid
    print("4. Đang tải danh sách Top 5 Ranker sử dụng Team Color Real Madrid (1018)...")
    rankers_rm_list = fetch_json("/meta/mastery?dimension=teamcolor&key=1018&rank=legend_up&window=30d")
    top5_rm_details = []
    
    if rankers_rm_list and 'items' in rankers_rm_list:
        items = rankers_rm_list['items'][:5]
        for idx, r in enumerate(items, 1):
            acc_id = r.get('accountId')
            nick = r.get('nickname')
            print(f"   [{idx}/5] Đang tải chi tiết Ranker Real Madrid: {nick} ({acc_id})...")
            detail = fetch_json(f"/meta/mastery/{acc_id}?dimension=teamcolor&key=1018&rank=legend_up&window=30d")
            top5_rm_details.append({
                "summary": r,
                "detail": detail.get('data') if detail else None
            })
            time.sleep(0.3)
            
    # Combine into result structure
    result = {
        "_metadata": {
            "source": "https://dc.fconline.garena.vn/lineup",
            "crawled_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "data_as_of": formations_meta.get('meta', {}).get('asOfDate') if formations_meta else None,
            "sample_size": formations_meta.get('meta', {}).get('sampleSize') if formations_meta else None
        },
        "formations_overview": formations_meta,
        "formation_4141_matchups": formations_4141_matchups,
        "teamcolors_overview": teamcolors_meta,
        "real_madrid_matchups": rm_matchups,
        "top5_rankers_4141": top5_4141_details,
        "top5_rankers_real_madrid": top5_rm_details
    }
    
    # Save to JSON
    os.makedirs("Research", exist_ok=True)
    json_path = os.path.join("Research", "GARENA_DC_TOP_RANKERS_4141_AND_REAL_MADRID.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Đã lưu file raw JSON: {json_path}")
    
    # Generate Markdown Report
    md_path = os.path.join("Research", "GARENA_DC_TOP_RANKERS_ANALYSIS.md")
    generate_markdown_report(result, md_path)
    print(f"✅ Đã tạo báo cáo phân tích Markdown: {md_path}")
    print("\n=== HOÀN TẤT THÀNH CÔNG ===")

def generate_markdown_report(data, out_path):
    lines = []
    meta = data.get('_metadata', {})
    lines.append("# 📊 BÁO CÁO PHÂN TÍCH: TOP RANKER SƠ ĐỒ 4-1-4-1 & REAL MADRID (GARENA DATA CENTER)")
    lines.append(f"**Nguồn dữ liệu:** [Garena FC Online Data Center Lineup](https://dc.fconline.garena.vn/lineup)  ")
    lines.append(f"**Ngày cập nhật dữ liệu của Garena:** `{meta.get('data_as_of')}`  ")
    lines.append(f"**Mẫu số thống kê:** `{meta.get('sample_size'):,}` trận đấu Rank cao  ")
    lines.append(f"**Thời điểm trích xuất:** `{meta.get('crawled_at')}`  \n")
    lines.append("---\n")
    
    # Section 1: Overview Formations & Real Madrid
    lines.append("## 1. 📈 TỔNG QUAN META SƠ ĐỒ 4-1-4-1 & TEAM COLOR REAL MADRID\n")
    
    # Find 4-1-4-1 in formations
    f_items = data.get('formations_overview', {}).get('items', [])
    f_4141 = next((f for f in f_items if f.get('formation') == '4-1-4-1'), None)
    if f_4141:
        lines.append(f"* **Sơ đồ 4-1-4-1:** Tỷ lệ sử dụng **{f_4141.get('usagePct')}%** ({f_4141.get('sides'):,} trận), Tỷ lệ thắng trung bình: **{f_4141.get('winratePct')}%**.")
        
    tc_items = data.get('teamcolors_overview', {}).get('items', [])
    tc_rm = next((t for t in tc_items if t.get('teamColorId') == 1018), None)
    if tc_rm:
        lines.append(f"* **Team Color Real Madrid:** Tỷ lệ sử dụng đứng TOP 1 toàn server: **{tc_rm.get('usagePct')}%** ({tc_rm.get('sides'):,} trận), Tỷ lệ thắng: **{tc_rm.get('winratePct')}%**.\n")
        
    lines.append("### Khắc chế của 4-1-4-1 khi gặp các sơ đồ phổ biến:")
    lines.append("| Sơ đồ đối thủ | Số trận đối đầu | Thắng | Hòa | Thua | Tỷ lệ thắng |")
    lines.append("| :--- | :---: | :---: | :---: | :---: | :---: |")
    matchups_4141 = data.get('formation_4141_matchups', {}).get('items', [])[:8]
    for m in matchups_4141:
        lines.append(f"| **{m.get('opponent')}** | {m.get('matches'):,} | {m.get('wins'):,} | {m.get('draws'):,} | {m.get('losses'):,} | **{m.get('winratePct')}%** |")
    lines.append("\n---\n")
    
    # Section 2: Top 5 Rankers 4-1-4-1
    lines.append("## 2. 🛡️ TOP 5 RANKER SỬ DỤNG SƠ ĐỒ 4-1-4-1 HIỆU QUẢ NHẤT\n")
    for idx, r in enumerate(data.get('top5_rankers_4141', []), 1):
        s = r.get('summary', {})
        d = r.get('detail', {})
        lines.append(f"### #{idx}. HLV {s.get('nickname')} ({s.get('divisionName')})")
        lines.append(f"* **Thống kê:** `{s.get('matches')}` trận | **Thắng {s.get('wins')}** | Tỷ lệ thắng: **`{s.get('winratePct')}%`** | ELO: `{s.get('elo')}`")
        if d:
            # Tactics
            tactics = d.get('tactics', [])
            t_str = " | ".join([f"**{t.get('label')}:** {t.get('display')}" for t in tactics if t.get('key') in ['defensive_style', 'defensive_width', 'defensive_depth', 'offensive_style_buildup', 'offensive_style_chancecreation', 'offensive_width', 'offensive_player_in_box', 'teammentality']])
            lines.append(f"* **Chiến thuật đội:** {t_str}")
            
            # Squad
            lines.append("* **11 Cầu thủ xuất phát & Chiến thuật đơn (CTĐ):**")
            lines.append("| Vị trí | Tên cầu thủ | Thẻ cộng | Lệnh CTĐ đã cài đặt |")
            lines.append("| :---: | :--- | :---: | :--- |")
            for p in d.get('squad', []):
                inst = [f"`{i.get('code')}` ({i.get('label')})" for i in p.get('instructions', [])]
                inst_str = ", ".join(inst) if inst else "Mặc định"
                lines.append(f"| **{p.get('positionName')}** | {p.get('name')} | +{p.get('grade')} | {inst_str} |")
        lines.append("")
        
    lines.append("\n---\n")
    
    # Section 3: Top 5 Rankers Real Madrid
    lines.append("## 3. 👑 TOP 5 RANKER SỬ DỤNG TEAM COLOR REAL MADRID HIỆU QUẢ NHẤT\n")
    for idx, r in enumerate(data.get('top5_rankers_real_madrid', []), 1):
        s = r.get('summary', {})
        d = r.get('detail', {})
        lines.append(f"### #{idx}. HLV {s.get('nickname')} ({s.get('divisionName')})")
        lines.append(f"* **Thống kê:** `{s.get('matches')}` trận | **Thắng {s.get('wins')}** | Tỷ lệ thắng: **`{s.get('winratePct')}%`** | ELO: `{s.get('elo')}`")
        if d:
            lines.append(f"* **Sơ đồ vận hành:** `{d.get('formation')}`")
            # Tactics
            tactics = d.get('tactics', [])
            t_str = " | ".join([f"**{t.get('label')}:** {t.get('display')}" for t in tactics if t.get('key') in ['defensive_style', 'defensive_width', 'defensive_depth', 'offensive_style_buildup', 'offensive_style_chancecreation', 'offensive_width', 'offensive_player_in_box', 'teammentality']])
            lines.append(f"* **Chiến thuật đội:** {t_str}")
            
            # Squad
            lines.append("* **11 Cầu thủ xuất phát & Chiến thuật đơn (CTĐ):**")
            lines.append("| Vị trí | Tên cầu thủ | Thẻ cộng | Lệnh CTĐ đã cài đặt |")
            lines.append("| :---: | :--- | :---: | :--- |")
            for p in d.get('squad', []):
                inst = [f"`{i.get('code')}` ({i.get('label')})" for i in p.get('instructions', [])]
                inst_str = ", ".join(inst) if inst else "Mặc định"
                lines.append(f"| **{p.get('positionName')}** | {p.get('name')} | +{p.get('grade')} | {inst_str} |")
        lines.append("")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    main()
