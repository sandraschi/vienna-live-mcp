param(
    [switch]$Headless,
    [switch]$BackendOnly,
    [switch]$FrontendOnly,
    [switch]$NoBrowser
)

$ProjectRoot = Split-Path -Parent $PSScriptRoot
$FleetStartPath = Join-Path $ProjectRoot "scripts\FleetStartMode.ps1"
if (-not (Test-Path -LiteralPath $FleetStartPath)) {
    Write-Host "ERROR: Missing vendored launcher helper: $FleetStartPath" -ForegroundColor Red
    exit 1
}
. $FleetStartPath
Stop-FleetPortSquatters -Ports @(10988, 10922, 10989, 10990) -Label "vienna-live-mcp"

$ViLifeStart = 'D:\Dev\repos\vienna-life-assistant\web_sota\start.ps1'

Write-Host ""
Write-Host "DEPRECATED: vienna-live-mcp/web_sota" -ForegroundColor Yellow
Write-Host "Superseded by vienna-life-assistant (ViLife)." -ForegroundColor White
Write-Host ""
Write-Host "  Web UI:  http://127.0.0.1:10988" -ForegroundColor Cyan
Write-Host "  MCP:     http://127.0.0.1:10922/mcp  (tool: vienna_life)" -ForegroundColor Cyan
Write-Host ""
Write-Host "Forwarding to ViLife start.ps1 ..." -ForegroundColor Green
Write-Host "See DEPRECATED.md" -ForegroundColor Gray
Write-Host ""

if (-not (Test-Path $ViLifeStart)) {
    Write-Host "ERROR: ViLife start script not found: $ViLifeStart" -ForegroundColor Red
    exit 1
}

& $ViLifeStart @PSBoundParameters
exit $LASTEXITCODE

