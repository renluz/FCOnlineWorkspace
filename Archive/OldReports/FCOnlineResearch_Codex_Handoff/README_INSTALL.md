# Codex Handoff — FCOnlineResearch

Gói này được tạo để đưa context của project GLXH vào Codex mà không cần copy lại toàn bộ chat.

## Cách cài vào project local
Project đích:

`E:\FCOnlineWorkspace\Research`

### Cách 1 — thủ công
Copy:
- `AGENTS.md`
- thư mục `docs\codex\`

vào root project.

Nếu project đã có `AGENTS.md`, hãy **merge**, không ghi đè mù quáng.

### Cách 2 — PowerShell
Chạy `Install-Codex-Handoff.ps1`.
Script sẽ:
- backup file trùng tên vào `_codex_handoff_backup\<timestamp>\`
- copy handoff vào project.

## Sau đó mở Codex
Trong PowerShell:

```powershell
cd "E:\FCOnlineWorkspace\Research"
codex
```

Prompt đầu tiên gợi ý:

```text
Đọc AGENTS.md và toàn bộ docs/codex trước.
Sau đó audit repo hiện tại so với CURRENT_STATE.md.
Không sửa gì cho tới khi báo cho tôi:
1) current project structure,
2) file nào đang mâu thuẫn với handoff,
3) tactic codes nào invalid/unsupported,
4) next 5 actions theo priority.
```

## Lưu ý
`AGENTS.md` được giữ ngắn và đóng vai trò bản đồ. Context chi tiết nằm trong `docs/codex/`.
