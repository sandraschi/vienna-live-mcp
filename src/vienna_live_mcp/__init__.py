"""
Vienna Live MCP Server

A comprehensive MCP server providing programmatic access to Vienna Life Assistant
functionality through consolidated portmanteau tools.

This package implements the Portmanteau Pattern to organize related tools into
logical categories for better discoverability and usability.

Portmanteaus:
- shopping_manager: Store offers, shopping lists, budget tracking
- travel_manager: Transport schedules, trip planning, travel utilities
- expenses_manager: Expense tracking, budget analysis, financial insights
- media_manager: Unified media access across Plex, Calibre, Immich
- planning_manager: Todo management, calendar, goals, productivity

Usage:
    # Run as STDIO server (default MCP behavior)
    python -m vienna_live_mcp.server

    # Run as HTTP server
    python -m vienna_live_mcp.server --transport http --port 8000

Author: Sandra Schi
Version: 0.1.0
License: MIT
"""

from .server import app

__version__ = "0.1.0"
__author__ = "Sandra Schi"
__license__ = "MIT"

__all__ = ["app"]
