"""
Tests for Vienna Live MCP Server

Tests basic server functionality, tool registration, and portmanteau integration.
"""

import pytest
import asyncio
from unittest.mock import patch, AsyncMock

from vienna_live_mcp.server import app, register_all_tools, get_server_status, get_portmanteau_info


class TestServer:
    """Test server initialization and basic functionality."""

    def test_app_creation(self):
        """Test that FastMCP app is created correctly."""
        assert app is not None
        assert app.name == "vienna-live-mcp"
        assert app.version == "0.1.0"

    def test_server_status_tool(self):
        """Test the get_server_status tool."""
        result = asyncio.run(get_server_status())

        assert "server" in result
        assert result["server"]["name"] == "vienna-live-mcp"
        assert result["server"]["version"] == "0.1.0"
        assert result["server"]["status"] == "healthy"

        assert "portmanteaus" in result
        expected_portmanteaus = [
            "shopping_manager",
            "travel_manager",
            "expenses_manager",
            "media_manager",
            "planning_manager"
        ]
        assert result["portmanteaus"] == expected_portmanteaus
        assert result["tools_count"] == 60

    def test_portmanteau_info_valid(self):
        """Test get_portmanteau_info with valid portmanteau."""
        result = asyncio.run(get_portmanteau_info("shopping_manager"))

        assert "description" in result
        assert "tools_count" in result
        assert "tools" in result
        assert result["tools_count"] == 12
        assert "get_store_offers" in result["tools"]

    def test_portmanteau_info_invalid(self):
        """Test get_portmanteau_info with invalid portmanteau."""
        result = asyncio.run(get_portmanteau_info("invalid_portmanteau"))

        assert "error" in result
        assert "available_portmanteaus" in result
        assert len(result["available_portmanteaus"]) == 5

    @patch('vienna_live_mcp.portmanteaus.shopping_manager.register_shopping_tools')
    @patch('vienna_live_mcp.portmanteaus.travel_manager.register_travel_tools')
    @patch('vienna_live_mcp.portmanteaus.expenses_manager.register_expenses_tools')
    @patch('vienna_live_mcp.portmanteaus.media_manager.register_media_tools')
    @patch('vienna_live_mcp.portmanteaus.planning_manager.register_planning_tools')
    def test_register_all_tools(self, mock_planning, mock_media, mock_expenses, mock_travel, mock_shopping):
        """Test that all portmanteau tools are registered."""
        register_all_tools()

        # Verify all portmanteau registration functions were called
        mock_shopping.assert_called_once_with(app)
        mock_travel.assert_called_once_with(app)
        mock_expenses.assert_called_once_with(app)
        mock_media.assert_called_once_with(app)
        mock_planning.assert_called_once_with(app)


class TestPortmanteauInfo:
    """Test portmanteau information retrieval."""

    @pytest.mark.parametrize("portmanteau,expected_tools", [
        ("shopping_manager", 12),
        ("travel_manager", 15),
        ("expenses_manager", 14),
        ("media_manager", 16),
        ("planning_manager", 13),
    ])
    def test_portmanteau_tool_counts(self, portmanteau, expected_tools):
        """Test that each portmanteau has the correct number of tools."""
        result = asyncio.run(get_portmanteau_info(portmanteau))

        assert result["tools_count"] == expected_tools
        assert len(result["tools"]) == expected_tools
        assert "description" in result
        assert "categories" in result


class TestServerConfiguration:
    """Test server configuration and metadata."""

    def test_app_metadata(self):
        """Test that app has correct metadata for Glama registry."""
        assert app.name == "vienna-live-mcp"
        assert app.version == "0.1.0"
        assert "productivity" in app.tags
        assert "personal-management" in app.tags
        assert app.author == "Sandra Schi"
        assert app.license == "MIT"

    def test_app_dependencies(self):
        """Test that app has correct dependencies listed."""
        expected_deps = [
            "fastmcp>=2.13.0,<2.14.0",
            "httpx>=0.28.1,<0.29.0",
            "pydantic>=2.5.3,<3.0.0",
            "sqlalchemy>=2.0.25,<3.0.0",
            "psycopg2-binary>=2.9.9",
            "asyncpg>=0.29.0"
        ]

        assert app.dependencies == expected_deps
