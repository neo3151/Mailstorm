# Repository Backup Script (Abyssal Standard)
# PURPOSE: Mirror key projects from C:\Users\neo31 to D:\repo-backups

$LogDir = "C:\Users\neo31\Mailstorm\scripts\logs"
if (-not (Test-Path $LogDir)) { New-Item -ItemType Directory -Path $LogDir -Force | Out-Null }
$LogFile = Join-Path $LogDir "backup_$(Get-Date -Format 'yyyyMMdd_HHmmss').log"
Start-Transcript -Path $LogFile -Append

$SourceRoot = "C:\Users\neo31"
$DestRoot = "D:\repo-backups\Backup_$(Get-Date -Format 'yyyyMMdd')"

# List of folders to back up
$Projects = @(
    "Mailstorm",
    "Hunting_Call",
    "Hunting_Call_AI_Backend",
    "Playground",
    "Sentinel_Orchastrator",
    "dmca-monitor",
    "electronic_pet_game",
    "shadow-ring",
    "antigravity-book",
    "Gobo",
    "NotebookLM"
)

# Shared Exclusions (folders to NOT copy)
$Exclusions = @(
    "node_modules",
    ".cache",
    "bin",
    "obj",
    ".venv",
    ".next",
    "dist",
    "build",
    ".gradle",
    ".idea"
)

Write-Host "--- BEGINNING REPOSITORY BACKUP TO D: DRIVE ---" -ForegroundColor Green
Write-Host "Destination: $DestRoot" -ForegroundColor Cyan
Write-Host "Excluding: $($Exclusions -join ', ')" -ForegroundColor Yellow
Write-Host "------------------------------------------------"

# Create destination root if it doesn't exist
if (-not (Test-Path $DestRoot)) {
    New-Item -ItemType Directory -Path $DestRoot -Force | Out-Null
}

foreach ($Project in $Projects) {
    $SourcePath = Join-Path $SourceRoot $Project
    $DestPath = Join-Path $DestRoot $Project

    if (Test-Path $SourcePath) {
        Write-Host "➤ Backing up: $Project..." -NoNewline
        
        # Use Robocopy for industrial-strength mirroring
        # /MIR: Mirror directory tree
        # /XD: Exclude specific directories
        # /R:0 /W:0: Skip retries for locked files (to prevent hanging)
        # /NDL: No Directory List (less verbose)
        # /NFL: No File List (less verbose)
        robocopy $SourcePath $DestPath /MIR /XD $Exclusions /R:0 /W:0 /NDL /NFL /NJH /NJS
        
        Write-Host " DONE." -ForegroundColor Green
    } else {
        Write-Host "⚠ Skipping: $Project (Not Found at $SourcePath)" -ForegroundColor Red
    }
}

# --- DEDICATED PLAYGROUND SYNC ---
$DedicatedPlayground = "D:\Playground_Backup"
Write-Host "------------------------------------------------"
Write-Host "➤ Syncing Entire Playground to Dedicated Folder ($DedicatedPlayground)..." -NoNewline
robocopy "C:\Users\neo31\Playground" $DedicatedPlayground /MIR /XD $Exclusions /R:0 /W:0 /NDL /NFL /NJH /NJS
Write-Host " DONE." -ForegroundColor Green

Write-Host "------------------------------------------------"
Write-Host "BACKUP COMPLETE. Please verify D: drive contents." -ForegroundColor Green
Stop-Transcript
