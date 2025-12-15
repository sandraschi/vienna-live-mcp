"""
Shopping Manager Portmanteau

Consolidated tools for comprehensive shopping management including:
- Store offers and price comparisons
- Shopping list management
- Budget checking and recommendations
- Receipt analysis and history

This portmanteau follows the Portmanteau Pattern to provide a clean,
discoverable API for all shopping-related functionality.
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

# Mock data for development - will be replaced with actual database queries
MOCK_STORE_OFFERS = {
    "spar": [
        {"item": "Bananas", "price": 1.99, "discount": 0.50, "valid_until": "2025-12-20"},
        {"item": "Milk", "price": 1.29, "discount": 0.20, "valid_until": "2025-12-18"},
    ],
    "billa": [
        {"item": "Apples", "price": 2.49, "discount": 0.30, "valid_until": "2025-12-19"},
        {"item": "Bread", "price": 1.89, "discount": 0.40, "valid_until": "2025-12-17"},
    ]
}

MOCK_SHOPPING_LISTS = {}

def register_shopping_tools(app):
    """Register all shopping manager tools with the MCP server."""

    @app.tool()
    async def get_store_offers(store_name: Optional[str] = None, category: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get current offers from stores (Spar, Billa, Hofer, etc.)

        Args:
            store_name: Specific store to check (optional)
            category: Product category filter (optional)
            limit: Maximum offers to return (default: 10)

        Returns:
            List of current offers with prices, discounts, and validity
        """
        try:
            # TODO: Replace with actual API calls to store services
            offers = []

            if store_name and store_name.lower() in MOCK_STORE_OFFERS:
                offers.extend(MOCK_STORE_OFFERS[store_name.lower()])
            else:
                # Return offers from all stores
                for store_offers in MOCK_STORE_OFFERS.values():
                    offers.extend(store_offers)

            # Apply category filter if specified
            if category:
                # TODO: Implement category filtering
                pass

            # Limit results
            offers = offers[:limit]

            logger.info(f"Retrieved {len(offers)} store offers")
            return offers

        except Exception as e:
            logger.error(f"Failed to get store offers: {e}")
            return []

    @app.tool()
    async def compare_prices(item_name: str, stores: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Compare prices for a specific item across different stores.

        Args:
            item_name: Name of the item to compare
            stores: List of stores to check (optional, defaults to all)

        Returns:
            Price comparison data with best deals highlighted
        """
        try:
            # TODO: Implement actual price comparison logic
            mock_comparison = {
                "item": item_name,
                "comparisons": [
                    {"store": "Spar", "price": 2.99, "discount": 0.50, "best_deal": True},
                    {"store": "Billa", "price": 3.29, "discount": 0.20, "best_deal": False},
                    {"store": "Hofer", "price": 3.49, "discount": 0.10, "best_deal": False},
                ],
                "best_price": 2.49,
                "potential_savings": 1.00,
                "last_updated": datetime.now().isoformat()
            }

            logger.info(f"Price comparison completed for {item_name}")
            return mock_comparison

        except Exception as e:
            logger.error(f"Failed to compare prices for {item_name}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def find_stores_nearby(location: str, store_chain: Optional[str] = None, radius_km: float = 2.0) -> List[Dict[str, Any]]:
        """
        Find stores near a specific location.

        Args:
            location: Address or location name
            store_chain: Specific store chain to find (optional)
            radius_km: Search radius in kilometers (default: 2.0)

        Returns:
            List of nearby stores with addresses, hours, and distance
        """
        try:
            # TODO: Implement actual location-based search
            mock_stores = [
                {
                    "name": "Spar City",
                    "chain": "Spar",
                    "address": "Stephansplatz 1, 1010 Vienna",
                    "distance_km": 0.5,
                    "opening_hours": "06:00-22:00",
                    "phone": "+43 1 1234567"
                },
                {
                    "name": "Billa Plus",
                    "chain": "Billa",
                    "address": "Kärntner Straße 12, 1010 Vienna",
                    "distance_km": 0.8,
                    "opening_hours": "07:00-20:00",
                    "phone": "+43 1 2345678"
                }
            ]

            # Filter by chain if specified
            if store_chain:
                mock_stores = [store for store in mock_stores if store["chain"].lower() == store_chain.lower()]

            # Filter by radius
            mock_stores = [store for store in mock_stores if store["distance_km"] <= radius_km]

            logger.info(f"Found {len(mock_stores)} stores near {location}")
            return mock_stores

        except Exception as e:
            logger.error(f"Failed to find stores near {location}: {e}")
            return []

    @app.tool()
    async def shopping_list_create(name: str, description: Optional[str] = None, store_preference: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new shopping list.

        Args:
            name: Name of the shopping list
            description: Optional description
            store_preference: Preferred store for this list

        Returns:
            Created shopping list information
        """
        try:
            list_id = f"list_{len(MOCK_SHOPPING_LISTS) + 1}"
            shopping_list = {
                "id": list_id,
                "name": name,
                "description": description,
                "store_preference": store_preference,
                "items": [],
                "created_at": datetime.now().isoformat(),
                "total_estimated": 0.0
            }

            MOCK_SHOPPING_LISTS[list_id] = shopping_list

            logger.info(f"Created shopping list: {name}")
            return shopping_list

        except Exception as e:
            logger.error(f"Failed to create shopping list {name}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def shopping_list_add_item(
        list_id: str,
        item_name: str,
        quantity: Optional[int] = 1,
        category: Optional[str] = None,
        notes: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Add an item to a shopping list.

        Args:
            list_id: ID of the shopping list
            item_name: Name of the item to add
            quantity: Quantity needed (default: 1)
            category: Item category (optional)
            notes: Additional notes (optional)

        Returns:
            Updated shopping list item information
        """
        try:
            if list_id not in MOCK_SHOPPING_LISTS:
                return {"error": f"Shopping list {list_id} not found"}

            item = {
                "id": f"item_{len(MOCK_SHOPPING_LISTS[list_id]['items']) + 1}",
                "name": item_name,
                "quantity": quantity,
                "category": category,
                "notes": notes,
                "completed": False,
                "added_at": datetime.now().isoformat()
            }

            MOCK_SHOPPING_LISTS[list_id]["items"].append(item)

            logger.info(f"Added item {item_name} to shopping list {list_id}")
            return item

        except Exception as e:
            logger.error(f"Failed to add item to shopping list {list_id}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def shopping_list_get(list_id: str, include_completed: bool = False) -> Dict[str, Any]:
        """
        Get shopping list contents.

        Args:
            list_id: ID of the shopping list
            include_completed: Whether to include completed items (default: false)

        Returns:
            Complete shopping list with all items
        """
        try:
            if list_id not in MOCK_SHOPPING_LISTS:
                return {"error": f"Shopping list {list_id} not found"}

            shopping_list = MOCK_SHOPPING_LISTS[list_id].copy()

            if not include_completed:
                shopping_list["items"] = [
                    item for item in shopping_list["items"]
                    if not item.get("completed", False)
                ]

            logger.info(f"Retrieved shopping list {list_id} with {len(shopping_list['items'])} items")
            return shopping_list

        except Exception as e:
            logger.error(f"Failed to get shopping list {list_id}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_shopping_recommendations(based_on: str = "recent_purchases", limit: int = 5) -> List[Dict[str, Any]]:
        """
        Get personalized shopping recommendations.

        Args:
            based_on: Basis for recommendations ("recent_purchases", "seasonal", "budget")
            limit: Maximum recommendations to return

        Returns:
            List of recommended items with reasons
        """
        try:
            # TODO: Implement AI-powered recommendations based on user history
            mock_recommendations = [
                {
                    "item": "Organic Bananas",
                    "reason": "Frequently purchased in the last month",
                    "category": "Fruits",
                    "estimated_price": 2.49,
                    "confidence": 0.85
                },
                {
                    "item": "Whole Milk",
                    "reason": "Seasonal consumption pattern detected",
                    "category": "Dairy",
                    "estimated_price": 1.29,
                    "confidence": 0.72
                },
                {
                    "item": "Fresh Bread",
                    "reason": "Complements your recent cheese purchases",
                    "category": "Bakery",
                    "estimated_price": 2.99,
                    "confidence": 0.68
                }
            ]

            recommendations = mock_recommendations[:limit]
            logger.info(f"Generated {len(recommendations)} shopping recommendations")
            return recommendations

        except Exception as e:
            logger.error(f"Failed to get shopping recommendations: {e}")
            return []

    @app.tool()
    async def budget_check_item(item_name: str, price: float, budget_category: Optional[str] = None) -> Dict[str, Any]:
        """
        Check if an item purchase fits within budget constraints.

        Args:
            item_name: Name of the item
            price: Price of the item
            budget_category: Budget category to check against (optional)

        Returns:
            Budget impact analysis and recommendations
        """
        try:
            # TODO: Implement actual budget checking against user's expense data
            mock_budget_check = {
                "item": item_name,
                "price": price,
                "budget_category": budget_category or "General",
                "remaining_budget": 150.00,  # Mock remaining budget
                "impact_percentage": (price / 200.00) * 100,  # Assuming €200 budget
                "fits_budget": price <= 150.00,
                "recommendations": [
                    "Item fits within current budget",
                    "Consider buying in bulk for better value"
                ] if price <= 150.00 else [
                    "Item exceeds current budget",
                    "Consider cheaper alternative or delay purchase"
                ]
            }

            logger.info(f"Budget check completed for {item_name} (€{price})")
            return mock_budget_check

        except Exception as e:
            logger.error(f"Failed to check budget for {item_name}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def find_coupons(store_name: Optional[str] = None, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Find available coupons and discount codes.

        Args:
            store_name: Specific store to check (optional)
            category: Product category (optional)

        Returns:
            List of available coupons with codes and expiry dates
        """
        try:
            # TODO: Integrate with actual coupon services
            mock_coupons = [
                {
                    "store": "Spar",
                    "code": "SPAR10",
                    "discount": "10% off",
                    "category": "All items",
                    "expiry_date": "2025-12-31",
                    "description": "Valid on all purchases over €20"
                },
                {
                    "store": "Billa",
                    "code": "BILLA5",
                    "discount": "€5 off",
                    "category": "Fruits & Vegetables",
                    "expiry_date": "2025-12-25",
                    "description": "Valid on seasonal produce"
                }
            ]

            # Filter by store and category if specified
            if store_name:
                mock_coupons = [c for c in mock_coupons if c["store"].lower() == store_name.lower()]

            if category:
                mock_coupons = [c for c in mock_coupons if category.lower() in c["category"].lower()]

            logger.info(f"Found {len(mock_coupons)} available coupons")
            return mock_coupons

        except Exception as e:
            logger.error(f"Failed to find coupons: {e}")
            return []

    @app.tool()
    async def analyze_receipt(image_path: Optional[str] = None, image_url: Optional[str] = None, store_name: Optional[str] = None) -> Dict[str, Any]:
        """
        Analyze receipt image using OCR and categorize items.

        Args:
            image_path: Local path to receipt image
            image_url: URL to receipt image
            store_name: Store name for better categorization (optional)

        Returns:
            Parsed receipt data with categorized items and totals
        """
        try:
            # TODO: Implement OCR receipt analysis
            mock_receipt = {
                "store": store_name or "Unknown Store",
                "date": datetime.now().strftime("%Y-%m-%d"),
                "total": 24.97,
                "items": [
                    {"name": "Bananas", "quantity": 1, "price": 2.49, "category": "Fruits"},
                    {"name": "Milk", "quantity": 1, "price": 1.29, "category": "Dairy"},
                    {"name": "Bread", "quantity": 1, "price": 1.89, "category": "Bakery"},
                    {"name": "Apples", "quantity": 2, "price": 4.98, "category": "Fruits"}
                ],
                "tax": 3.74,
                "confidence": 0.92,
                "processing_time": 2.1
            }

            logger.info(f"Receipt analysis completed for {store_name or 'unknown store'}")
            return mock_receipt

        except Exception as e:
            logger.error(f"Failed to analyze receipt: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_shopping_history(
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        store: Optional[str] = None,
        category: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get historical shopping data and patterns.

        Args:
            date_from: Start date (YYYY-MM-DD)
            date_to: End date (YYYY-MM-DD)
            store: Filter by store
            category: Filter by category

        Returns:
            Shopping history with totals and insights
        """
        try:
            # TODO: Query actual shopping history from database
            mock_history = {
                "period": {
                    "from": date_from or "2025-11-01",
                    "to": date_to or datetime.now().strftime("%Y-%m-%d")
                },
                "total_spent": 342.67,
                "total_purchases": 12,
                "average_purchase": 28.56,
                "top_stores": [
                    {"name": "Spar", "spent": 156.43, "visits": 6},
                    {"name": "Billa", "spent": 124.89, "visits": 4},
                    {"name": "Hofer", "spent": 61.35, "visits": 2}
                ],
                "top_categories": [
                    {"name": "Fruits & Vegetables", "spent": 89.23, "percentage": 26.0},
                    {"name": "Dairy", "spent": 67.45, "percentage": 19.7},
                    {"name": "Bakery", "spent": 54.12, "percentage": 15.8}
                ],
                "insights": [
                    "Average weekly spending: €48.95",
                    "Most active day: Saturday",
                    "Biggest purchase: €67.23 at Spar"
                ]
            }

            logger.info(f"Retrieved shopping history for period {mock_history['period']}")
            return mock_history

        except Exception as e:
            logger.error(f"Failed to get shopping history: {e}")
            return {"error": str(e)}

    logger.info("[OK] Shopping Manager portmanteau tools registered")
