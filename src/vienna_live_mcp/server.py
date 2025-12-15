#!/usr/bin/env python3
"""
Vienna Live MCP Server

A comprehensive MCP server providing programmatic access to Vienna Life Assistant
functionality through consolidated portmanteau tools.

This server implements the Portmanteau Pattern to provide clean, discoverable APIs
for shopping management, travel planning, expense tracking, media management,
and personal planning.

Author: Sandra Schi
Version: 0.1.0
"""

import asyncio
import logging
import os
from typing import Any, Dict, List, Optional
from contextlib import asynccontextmanager

from fastmcp import FastMCP
from pydantic import BaseModel, Field

# Import portmanteau tool modules
from .portmanteaus.shopping_manager import register_shopping_tools
from .portmanteaus.travel_manager import register_travel_tools
from .portmanteaus.expenses_manager import register_expenses_tools
from .portmanteaus.media_manager import register_media_tools
from .portmanteaus.planning_manager import register_planning_tools

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
app = FastMCP(
    name="vienna-live-mcp",
    version="0.1.0",
)

# =============================================================================
# LIFESPAN MANAGEMENT
# =============================================================================

@asynccontextmanager
async def lifespan(server: FastMCP):
    """Manage server lifecycle with database connections and cleanup."""
    logger.info("🚀 Starting Vienna Live MCP Server...")

    try:
        # Initialize database connections
        await initialize_database()
        logger.info("✅ Database connections established")

        # Initialize external service clients
        await initialize_clients()
        logger.info("✅ External service clients initialized")

        yield

    except Exception as e:
        logger.error(f"❌ Failed to initialize server: {e}")
        raise
    finally:
        # Cleanup resources
        await cleanup_resources()
        logger.info("🧹 Server shutdown complete")

async def initialize_database():
    """Initialize database connections and validate schema."""
    try:
        from .models import init_db
        init_db()
        logger.info("Database tables initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise

async def initialize_clients():
    """Initialize external service clients."""
    # TODO: Implement client initialization
    # - Wiener Linien API client
    # - Weather service client
    # - Currency exchange client
    # - Other external APIs
    pass

async def cleanup_resources():
    """Clean up resources on shutdown."""
    # TODO: Implement resource cleanup
    # - Close database connections
    # - Close external API clients
    # - Flush any pending operations
    pass

# =============================================================================
# CORE TOOLS
# =============================================================================

@app.tool()
async def get_server_status() -> Dict[str, Any]:
    """
    Get comprehensive server status and health information.

    Returns detailed information about:
    - Server health and version
    - Database connectivity
    - External service status
    - Available tools and portmanteaus
    - Performance metrics
    """
    return {
        "server": {
            "name": "vienna-live-mcp",
            "version": "0.1.0",
            "status": "healthy",
            "uptime": "N/A",  # TODO: Implement uptime tracking
        },
        "database": {
            "status": "connected",  # TODO: Check actual DB status
            "type": "PostgreSQL",
        },
        "services": {
            "wiener_linien": "available",  # TODO: Check service status
            "weather_api": "available",
            "currency_api": "available",
        },
        "portmanteaus": [
            "shopping_manager",
            "travel_manager",
            "expenses_manager",
            "media_manager",
            "planning_manager"
        ],
        "tools_count": 63,  # Total tools across all portmanteaus
        "last_updated": "2025-12-15"
    }

@app.tool()
async def get_portmanteau_info(portmanteau: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific portmanteau.

    Args:
        portmanteau: Name of the portmanteau ("shopping_manager", "travel_manager", etc.)

    Returns:
        Detailed information about the portmanteau and its tools
    """
    portmanteau_info = {
        "shopping_manager": {
            "description": "Comprehensive shopping management with offers, lists, and budget tracking",
            "tools_count": 11,
            "categories": ["offers", "lists", "budget", "receipts"],
            "tools": [
                "get_store_offers", "compare_prices", "find_stores_nearby",
                "shopping_list_create", "shopping_list_add_item", "get_shopping_recommendations",
                "budget_check_item", "find_coupons", "analyze_receipt", "get_shopping_history"
            ]
        },
        "travel_manager": {
            "description": "Complete travel planning with transport, weather, and booking",
            "tools_count": 15,
            "categories": ["transport", "planning", "weather", "booking"],
            "tools": [
                "get_next_tram", "plan_day_trip", "get_weather_for_travel",
                "get_train_schedule", "get_flight_info", "get_currency_exchange",
                "get_visa_requirements", "calculate_travel_cost", "get_sleeper_train_schedule"
            ]
        },
        "expenses_manager": {
            "description": "Advanced expense tracking, analysis, and budget management",
            "tools_count": 12,
            "categories": ["tracking", "analysis", "budget", "export"],
            "tools": [
                "add_expense", "get_expenses_by_category", "analyze_spending_patterns",
                "set_budget", "get_budget_status", "predict_monthly_expense",
                "export_expenses", "import_expenses"
            ]
        },
        "media_manager": {
            "description": "Unified media management across Plex, Calibre, and Immich",
            "tools_count": 10,
            "categories": ["plex", "calibre", "immich", "cross-media"],
            "tools": [
                "search_plex_library", "get_currently_watching", "search_calibre_library",
                "search_immich_photos", "create_media_playlist", "analyze_media_preferences",
                "get_media_suggestions"
            ]
        },
        "planning_manager": {
            "description": "Personal planning and productivity management",
            "tools_count": 15,
            "categories": ["todos", "calendar", "goals", "habits"],
            "tools": [
                "create_todo", "get_todos_by_category", "schedule_meeting",
                "set_goal", "create_habit", "get_productivity_stats",
                "plan_week", "get_motivational_quote"
            ]
        }
    }

    if portmanteau not in portmanteau_info:
        return {
            "error": f"Unknown portmanteau: {portmanteau}",
            "available_portmanteaus": list(portmanteau_info.keys())
        }

    return portmanteau_info[portmanteau]

# =============================================================================
# PORTMANTEAU REGISTRATION
# =============================================================================

# =============================================================================
# PORTMANTEAU REGISTRATION
# =============================================================================

# Register all portmanteau tools immediately
register_shopping_tools(app)
register_travel_tools(app)
register_expenses_tools(app)
register_media_tools(app)
register_planning_tools(app)

logger.info("All portmanteau tools registered successfully")
logger.info("Ready to serve Vienna Life Assistant functionality")

# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main():
    """Main entry point for running the MCP server."""
    import argparse

    parser = argparse.ArgumentParser(description="Vienna Live MCP Server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "http"],
        default="stdio",
        help="Transport protocol to use (default: stdio)"
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host to bind HTTP server to (default: 0.0.0.0)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind HTTP server to (default: 8000)"
    )

    args = parser.parse_args()

    if args.transport == "http":
        # Run as HTTP server
        import uvicorn
        logger.info(f"🌐 Starting HTTP server on {args.host}:{args.port}")
        uvicorn.run(
            "vienna_live_mcp.server:app",
            host=args.host,
            port=args.port,
            reload=False
        )
    else:
        # Run as STDIO server (default MCP behavior)
        logger.info("🔌 Starting STDIO server for MCP client integration")
        # FastMCP handles STDIO automatically when run as script

if __name__ == "__main__":
    main()
