# DEPRECATED — vienna-live-mcp

**Status:** Quarantined 2026-06-05  
**Replacement:** `vienna-life-assistant` (ViLife)

This repo duplicated Vienna Life functionality with a broken webapp (missing FastAPI dep, stale portmanteau surface). Fleet policy P3: **one carrier** — extend ViLife, do not maintain a parallel life MCP.

## Use instead

| Need | Surface |
|------|---------|
| Human UI | `vienna-life-assistant/web_sota` → http://127.0.0.1:10988 |
| Agent MCP | http://127.0.0.1:10922/mcp — `vienna_life` portmanteau |
| Fleet bridge | `fleet_call(server="vienna-life", tool="vienna_life", ...)` |

## Do not confuse with

- **vla-mcp** — Video-Language-Action robotics (`vla-robotics`), not life admin.

See `mcp-central-docs/operations/planning/FLEET_NAMING.md`.
