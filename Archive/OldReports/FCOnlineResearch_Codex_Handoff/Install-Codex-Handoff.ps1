param(
  [string]$Destination = "E:\FCOnlineWorkspace\Research"
)

$ErrorActionPreference = "Stop"
$Source = Split-Path -Parent $MyInvocation.MyCommand.Path
$Stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$BackupRoot = Join-Path $Destination "_codex_handoff_backup\$Stamp"

if (-not (Test-Path $Destination)) {
    throw "Destination not found: $Destination"
}

$Files = @(
    "AGENTS.md",
    "docs\codex\CURRENT_STATE.md",
    "docs\codex\RESEARCH_RULES.md",
    "docs\codex\TACTIC_VALIDITY.md",
    "docs\codex\NEXT_TASKS.md",
    "docs\codex\DECISION_HISTORY.md",
    "docs\codex\CODEX_START_PROMPT.txt"
)

foreach ($rel in $Files) {
    $src = Join-Path $Source $rel
    $dst = Join-Path $Destination $rel

    if (-not (Test-Path $src)) {
        throw "Missing source file: $src"
    }

    if (Test-Path $dst) {
        $backup = Join-Path $BackupRoot $rel
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $backup) | Out-Null
        Copy-Item $dst $backup -Force
    }

    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
    Copy-Item $src $dst -Force
}

Write-Host ""
Write-Host "Codex handoff installed to:"
Write-Host "  $Destination"
Write-Host ""
if (Test-Path $BackupRoot) {
    Write-Host "Existing files backed up to:"
    Write-Host "  $BackupRoot"
}
Write-Host ""
Write-Host 'Next: cd "E:\FCOnlineWorkspace\Research"'
Write-Host "Then start Codex and paste docs\codex\CODEX_START_PROMPT.txt"
