"""
Portmanteaus Package

This package contains all the portmanteau tool collections for the Vienna Live MCP server.
Each portmanteau provides a cohesive set of tools for a specific domain area.

Available Portmanteaus:
- shopping_manager: Store offers, shopping lists, budget tracking
- travel_manager: Transport schedules, trip planning, travel utilities
- expenses_manager: Expense tracking, budget analysis, financial insights
- media_manager: Unified media access across Plex, Calibre, Immich
- planning_manager: Todo management, calendar, goals, productivity

Each portmanteau follows the Portmanteau Pattern for clean, discoverable APIs.
"""

from .shopping_manager import register_shopping_tools
from .travel_manager import register_travel_tools
from .expenses_manager import register_expenses_tools
from .media_manager import register_media_tools
from .planning_manager import register_planning_tools

__all__ = [
    "register_shopping_tools",
    "register_travel_tools",
    "register_expenses_tools",
    "register_media_tools",
    "register_planning_tools"
]
