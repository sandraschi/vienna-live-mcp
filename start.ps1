Param([switch]$Headless)

Write-Host ""
Write-Host "DEPRECATED: vienna-live-mcp" -ForegroundColor Yellow
Write-Host "Superseded by vienna-life-assistant (ViLife)." -ForegroundColor White
Write-Host ""
Write-Host "  Web UI:  http://127.0.0.1:10988" -ForegroundColor Cyan
Write-Host "  MCP:     http://127.0.0.1:10922/mcp  (tool: vienna_life)" -ForegroundColor Cyan
Write-Host "  Start:   D:\Dev\repos\vienna-life-assistant\web_sota\start.ps1" -ForegroundColor Green
Write-Host ""
Write-Host "See DEPRECATED.md and mcp-central-docs/operations/planning/FLEET_NAMING.md" -ForegroundColor Gray
Write-Host ""

if (-not $Headless) {
    $open = Read-Host "Open ViLife start folder? [y/N]"
    if ($open -eq 'y') {
        Start-Process explorer.exe -ArgumentList "D:\Dev\repos\vienna-life-assistant\web_sota"
    }
}

exit 1
