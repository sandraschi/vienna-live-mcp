set windows-shell := ["pwsh.exe", "-NoLogo", "-Command"]

# ── Dashboard ─────────────────────────────────────────────────────────────────

# Open the interactive recipe dashboard in the browser
default:
    @just --list

# ── Quality ───────────────────────────────────────────────────────────────────

# Execute repo-wide quality checks (Ruff)
lint:
    uv run ruff check .

# Execute repo-wide auto-fixes and formatting (Ruff)
fix:
    uv run ruff check . --fix --unsafe-fixes
    uv run ruff format .

# ── Hardening ─────────────────────────────────────────────────────────────────

# Execute Bandit security audit
check-sec:
    uv run bandit -r src/

# Execute safety audit of dependencies
audit-deps:
    uv run safety check

# ── Vienna Live Specific ───────────────────────────────────────────────────────

# DEPRECATED — forward to ViLife (vienna-life-assistant)
run:
    pwsh -NoProfile -File web_sota/start.ps1 -Headless

# DEPRECATED — forward to ViLife web_sota
web-dev:
    pwsh -NoProfile -File web_sota/start.ps1

# Clean build artifacts
clean:
    @Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
    @Write-Host "Cleaned."

