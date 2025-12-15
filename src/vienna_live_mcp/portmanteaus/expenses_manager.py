"""
Expenses Manager Portmanteau

Advanced expense tracking, analysis, and budget management including:
- Expense entry and categorization
- Budget setting and monitoring
- Spending pattern analysis
- Financial reporting and export
- Predictive expense analysis

This portmanteau provides comprehensive financial management tools.
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

# Mock data for development
MOCK_EXPENSES = []
MOCK_BUDGETS = {}

def register_expenses_tools(app):
    """Register all expenses manager tools with the MCP server."""

    @app.tool()
    async def add_expense(
        amount: float,
        description: str,
        category: str,
        date: Optional[str] = None,
        store: Optional[str] = None,
        payment_method: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Add a new expense entry.

        Args:
            amount: Expense amount in EUR
            description: Description of the expense
            category: Expense category (e.g., "Food", "Transport", "Entertainment")
            date: Expense date (default: today)
            store: Store/business name (optional)
            payment_method: Payment method (optional)

        Returns:
            Expense creation confirmation with ID
        """
        try:
            expense_date = date or datetime.now().strftime("%Y-%m-%d")
            expense = {
                "id": f"exp_{len(MOCK_EXPENSES) + 1}",
                "amount": amount,
                "description": description,
                "category": category,
                "date": expense_date,
                "store": store,
                "payment_method": payment_method,
                "created_at": datetime.now().isoformat()
            }

            MOCK_EXPENSES.append(expense)

            logger.info(f"Added expense: €{amount} for {description} in category {category}")
            return {
                "success": True,
                "expense": expense,
                "message": f"Expense of €{amount} added successfully"
            }

        except Exception as e:
            logger.error(f"Failed to add expense: {e}")
            return {"error": str(e)}

    @app.tool()
    async def update_expense(
        expense_id: str,
        updates: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Update an existing expense entry.

        Args:
            expense_id: ID of the expense to update
            updates: Dictionary of fields to update

        Returns:
            Updated expense information
        """
        try:
            expense = next((exp for exp in MOCK_EXPENSES if exp["id"] == expense_id), None)
            if not expense:
                return {"error": f"Expense {expense_id} not found"}

            # Update allowed fields
            allowed_fields = ["amount", "description", "category", "date", "store", "payment_method"]
            for field, value in updates.items():
                if field in allowed_fields:
                    expense[field] = value

            expense["updated_at"] = datetime.now().isoformat()

            logger.info(f"Updated expense {expense_id}")
            return {
                "success": True,
                "expense": expense,
                "message": f"Expense {expense_id} updated successfully"
            }

        except Exception as e:
            logger.error(f"Failed to update expense {expense_id}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def delete_expense(expense_id: str, confirm: bool = False) -> Dict[str, Any]:
        """
        Delete an expense entry.

        Args:
            expense_id: ID of the expense to delete
            confirm: Safety confirmation (must be True)

        Returns:
            Deletion confirmation
        """
        try:
            if not confirm:
                return {"error": "Deletion requires confirmation. Set confirm=true"}

            expense = next((exp for exp in MOCK_EXPENSES if exp["id"] == expense_id), None)
            if not expense:
                return {"error": f"Expense {expense_id} not found"}

            MOCK_EXPENSES.remove(expense)

            logger.info(f"Deleted expense {expense_id}: €{expense['amount']} for {expense['description']}")
            return {
                "success": True,
                "message": f"Expense {expense_id} deleted successfully",
                "deleted_expense": {
                    "id": expense_id,
                    "amount": expense["amount"],
                    "description": expense["description"]
                }
            }

        except Exception as e:
            logger.error(f"Failed to delete expense {expense_id}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_expenses_by_category(
        category: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        group_by: str = "month"
    ) -> Dict[str, Any]:
        """
        Get expenses grouped by category with date filtering.

        Args:
            category: Filter by specific category (optional)
            date_from: Start date (optional)
            date_to: End date (optional)
            group_by: Grouping period ("day", "week", "month")

        Returns:
            Categorized expense data with totals
        """
        try:
            # Filter expenses
            filtered_expenses = MOCK_EXPENSES.copy()

            if category:
                filtered_expenses = [exp for exp in filtered_expenses if exp["category"].lower() == category.lower()]

            if date_from:
                filtered_expenses = [exp for exp in filtered_expenses if exp["date"] >= date_from]
            if date_to:
                filtered_expenses = [exp for exp in filtered_expenses if exp["date"] <= date_to]

            # Group by category
            category_totals = {}
            for exp in filtered_expenses:
                cat = exp["category"]
                if cat not in category_totals:
                    category_totals[cat] = {"count": 0, "total": 0.0, "expenses": []}
                category_totals[cat]["count"] += 1
                category_totals[cat]["total"] += exp["amount"]
                category_totals[cat]["expenses"].append({
                    "id": exp["id"],
                    "amount": exp["amount"],
                    "description": exp["description"],
                    "date": exp["date"]
                })

            # Sort categories by total spending
            sorted_categories = sorted(
                category_totals.items(),
                key=lambda x: x[1]["total"],
                reverse=True
            )

            result = {
                "period": {
                    "from": date_from or "all",
                    "to": date_to or "all"
                },
                "total_expenses": len(filtered_expenses),
                "total_amount": sum(exp["amount"] for exp in filtered_expenses),
                "categories": dict(sorted_categories),
                "top_category": sorted_categories[0][0] if sorted_categories else None
            }

            logger.info(f"Retrieved expenses by category: {len(result['categories'])} categories, €{result['total_amount']}")
            return result

        except Exception as e:
            logger.error(f"Failed to get expenses by category: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_expenses_by_date_range(
        date_from: str,
        date_to: str,
        category: Optional[str] = None,
        min_amount: Optional[float] = None,
        max_amount: Optional[float] = None
    ) -> List[Dict[str, Any]]:
        """
        Get expenses within a specific date range with optional filters.

        Args:
            date_from: Start date (YYYY-MM-DD)
            date_to: End date (YYYY-MM-DD)
            category: Filter by category (optional)
            min_amount: Minimum expense amount (optional)
            max_amount: Maximum expense amount (optional)

        Returns:
            Filtered list of expenses
        """
        try:
            filtered_expenses = [
                exp for exp in MOCK_EXPENSES
                if date_from <= exp["date"] <= date_to
            ]

            if category:
                filtered_expenses = [exp for exp in filtered_expenses if exp["category"].lower() == category.lower()]

            if min_amount is not None:
                filtered_expenses = [exp for exp in filtered_expenses if exp["amount"] >= min_amount]

            if max_amount is not None:
                filtered_expenses = [exp for exp in filtered_expenses if exp["amount"] <= max_amount]

            # Sort by date (newest first)
            filtered_expenses.sort(key=lambda x: x["date"], reverse=True)

            total_amount = sum(exp["amount"] for exp in filtered_expenses)

            result = {
                "period": {"from": date_from, "to": date_to},
                "count": len(filtered_expenses),
                "total_amount": total_amount,
                "average_amount": total_amount / len(filtered_expenses) if filtered_expenses else 0,
                "expenses": filtered_expenses
            }

            logger.info(f"Retrieved {len(filtered_expenses)} expenses from {date_from} to {date_to}")
            return result

        except Exception as e:
            logger.error(f"Failed to get expenses by date range: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_top_spending_categories(
        period: str = "month",
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Get highest spending categories for a time period.

        Args:
            period: Time period ("week", "month", "quarter", "year")
            limit: Maximum categories to return

        Returns:
            Top spending categories with amounts and percentages
        """
        try:
            # Calculate date range based on period
            now = datetime.now()
            if period == "week":
                date_from = (now - timedelta(days=7)).strftime("%Y-%m-%d")
            elif period == "month":
                date_from = (now - timedelta(days=30)).strftime("%Y-%m-%d")
            elif period == "quarter":
                date_from = (now - timedelta(days=90)).strftime("%Y-%m-%d")
            elif period == "year":
                date_from = (now - timedelta(days=365)).strftime("%Y-%m-%d")
            else:
                date_from = (now - timedelta(days=30)).strftime("%Y-%m-%d")

            date_to = now.strftime("%Y-%m-%d")

            # Filter expenses by date
            period_expenses = [
                exp for exp in MOCK_EXPENSES
                if date_from <= exp["date"] <= date_to
            ]

            # Group by category
            category_totals = {}
            total_spent = 0

            for exp in period_expenses:
                cat = exp["category"]
                amount = exp["amount"]
                total_spent += amount

                if cat not in category_totals:
                    category_totals[cat] = 0
                category_totals[cat] += amount

            # Create result with percentages
            top_categories = []
            for category, amount in sorted(category_totals.items(), key=lambda x: x[1], reverse=True)[:limit]:
                percentage = (amount / total_spent * 100) if total_spent > 0 else 0
                top_categories.append({
                    "category": category,
                    "amount": amount,
                    "percentage": round(percentage, 1),
                    "expense_count": len([exp for exp in period_expenses if exp["category"] == category])
                })

            result = {
                "period": period,
                "date_range": {"from": date_from, "to": date_to},
                "total_spent": total_spent,
                "categories": top_categories
            }

            logger.info(f"Retrieved top {len(top_categories)} spending categories for {period}")
            return result

        except Exception as e:
            logger.error(f"Failed to get top spending categories: {e}")
            return {"error": str(e)}

    @app.tool()
    async def analyze_spending_patterns(
        period: str = "month",
        focus: str = "trends"
    ) -> Dict[str, Any]:
        """
        AI-powered spending pattern analysis.

        Args:
            period: Analysis period ("month", "quarter", "year")
            focus: Analysis focus ("trends", "anomalies", "savings")

        Returns:
            Detailed spending analysis with insights and recommendations
        """
        try:
            # Calculate date range
            now = datetime.now()
            if period == "month":
                date_from = (now - timedelta(days=30)).strftime("%Y-%m-%d")
            elif period == "quarter":
                date_from = (now - timedelta(days=90)).strftime("%Y-%m-%d")
            elif period == "year":
                date_from = (now - timedelta(days=365)).strftime("%Y-%m-%d")

            date_to = now.strftime("%Y-%m-%d")

            # Analyze spending patterns (mock AI analysis)
            period_expenses = [
                exp for exp in MOCK_EXPENSES
                if date_from <= exp["date"] <= date_to
            ]

            analysis = {
                "period": {"from": date_from, "to": date_to},
                "total_expenses": len(period_expenses),
                "total_spent": sum(exp["amount"] for exp in period_expenses),
                "average_daily": 0,
                "insights": [],
                "recommendations": []
            }

            if period_expenses:
                days_in_period = (datetime.strptime(date_to, "%Y-%m-%d") - datetime.strptime(date_from, "%Y-%m-%d")).days + 1
                analysis["average_daily"] = analysis["total_spent"] / days_in_period

                # Generate mock insights based on focus
                if focus == "trends":
                    analysis["insights"] = [
                        "Spending increased by 15% compared to previous period",
                        "Food category represents 35% of total expenses",
                        "Weekend spending is 40% higher than weekdays"
                    ]
                    analysis["recommendations"] = [
                        "Consider meal planning to reduce food expenses",
                        "Look for grocery delivery discounts",
                        "Set weekly spending limits for entertainment"
                    ]
                elif focus == "anomalies":
                    analysis["insights"] = [
                        "Unusual spending spike on groceries last Tuesday",
                        "Higher than average transport costs this week",
                        "Multiple small purchases suggesting impulse buying"
                    ]
                    analysis["recommendations"] = [
                        "Review grocery purchases for bulk buying opportunities",
                        "Check public transport subscriptions for savings",
                        "Set daily spending alerts to curb impulse purchases"
                    ]
                elif focus == "savings":
                    analysis["insights"] = [
                        "Potential savings of €120/month through bulk purchasing",
                        "€85/month savings possible with subscription optimization",
                        "€45/month savings from reduced dining out"
                    ]
                    analysis["recommendations"] = [
                        "Start a grocery bulk buying program",
                        "Audit and cancel unused subscriptions",
                        "Cook at home more frequently"
                    ]

            logger.info(f"Generated {focus} analysis for {period} period")
            return analysis

        except Exception as e:
            logger.error(f"Failed to analyze spending patterns: {e}")
            return {"error": str(e)}

    @app.tool()
    async def set_budget(
        category: str,
        amount: float,
        period: str = "monthly",
        alert_threshold: float = 80.0
    ) -> Dict[str, Any]:
        """
        Set budget for a category and time period.

        Args:
            category: Budget category
            amount: Budget amount in EUR
            period: Budget period ("weekly", "monthly", "yearly")
            alert_threshold: Alert when spending reaches this percentage (default: 80%)

        Returns:
            Budget creation confirmation
        """
        try:
            budget_key = f"{category}_{period}"
            budget = {
                "id": budget_key,
                "category": category,
                "amount": amount,
                "period": period,
                "alert_threshold": alert_threshold,
                "created_at": datetime.now().isoformat(),
                "spent_this_period": 0.0,  # Would be calculated from actual expenses
                "remaining": amount
            }

            MOCK_BUDGETS[budget_key] = budget

            logger.info(f"Set {period} budget of €{amount} for category {category}")
            return {
                "success": True,
                "budget": budget,
                "message": f"Budget of €{amount} set for {category} ({period})"
            }

        except Exception as e:
            logger.error(f"Failed to set budget for {category}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_budget_status(
        category: Optional[str] = None,
        period: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get current budget status and alerts.

        Args:
            category: Filter by category (optional)
            period: Filter by period (optional)

        Returns:
            Budget status with alerts and remaining amounts
        """
        try:
            budgets = MOCK_BUDGETS.copy()

            # Filter budgets
            if category:
                budgets = {k: v for k, v in budgets.items() if v["category"].lower() == category.lower()}
            if period:
                budgets = {k: v for k, v in budgets.items() if v["period"] == period}

            # Calculate current spending (mock)
            for budget_key, budget in budgets.items():
                # In real implementation, calculate from actual expenses
                budget["spent_this_period"] = budget["amount"] * 0.6  # Mock 60% spent
                budget["remaining"] = budget["amount"] - budget["spent_this_period"]
                budget["percentage_used"] = (budget["spent_this_period"] / budget["amount"]) * 100

                # Check for alerts
                if budget["percentage_used"] >= budget["alert_threshold"]:
                    budget["alert"] = {
                        "level": "warning" if budget["percentage_used"] < 100 else "danger",
                        "message": f"Budget {budget['percentage_used']:.1f}% used"
                    }

            result = {
                "budgets": list(budgets.values()),
                "summary": {
                    "total_budgets": len(budgets),
                    "alerts": len([b for b in budgets.values() if "alert" in b]),
                    "total_allocated": sum(b["amount"] for b in budgets.values()),
                    "total_remaining": sum(b["remaining"] for b in budgets.values())
                }
            }

            logger.info(f"Retrieved budget status for {len(budgets)} budgets")
            return result

        except Exception as e:
            logger.error(f"Failed to get budget status: {e}")
            return {"error": str(e)}

    @app.tool()
    async def predict_monthly_expense(based_on_months: int = 3, include_trends: bool = True) -> Dict[str, Any]:
        """
        Predict next month's expenses based on historical data.

        Args:
            based_on_months: Number of months to analyze (default: 3)
            include_trends: Include trend analysis (default: true)

        Returns:
            Expense prediction with confidence levels and trends
        """
        try:
            # Mock prediction based on historical data
            prediction = {
                "prediction_for": (datetime.now() + timedelta(days=30)).strftime("%Y-%m"),
                "predicted_amount": 1250.00,
                "confidence_level": 0.78,
                "based_on_months": based_on_months,
                "historical_average": 1180.50,
                "change_percentage": 5.9,
                "category_predictions": {
                    "Food": {"predicted": 380.00, "trend": "increasing"},
                    "Transport": {"predicted": 180.00, "trend": "stable"},
                    "Entertainment": {"predicted": 120.00, "trend": "decreasing"},
                    "Utilities": {"predicted": 250.00, "trend": "stable"},
                    "Other": {"predicted": 320.00, "trend": "increasing"}
                },
                "factors": [
                    "Seasonal increase in utility costs",
                    "Upcoming holiday spending",
                    "Regular subscription renewals"
                ]
            }

            if include_trends:
                prediction["trends"] = {
                    "overall_trend": "increasing",
                    "volatility": "medium",
                    "seasonal_pattern": "end-of-month spending spike",
                    "recommendations": [
                        "Build emergency fund buffer",
                        "Review entertainment subscriptions",
                        "Plan for holiday expenses"
                    ]
                }

            logger.info(f"Generated expense prediction with {prediction['confidence_level']*100:.0f}% confidence")
            return prediction

        except Exception as e:
            logger.error(f"Failed to predict monthly expenses: {e}")
            return {"error": str(e)}

    @app.tool()
    async def export_expenses(
        format: str = "csv",
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        category: Optional[str] = None,
        include_summary: bool = True
    ) -> Dict[str, Any]:
        """
        Export expenses in various formats.

        Args:
            format: Export format ("csv", "json", "pdf")
            date_from: Start date filter (optional)
            date_to: End date filter (optional)
            category: Category filter (optional)
            include_summary: Include summary statistics (default: true)

        Returns:
            Export result with file information or data
        """
        try:
            # Filter expenses
            filtered_expenses = MOCK_EXPENSES.copy()

            if date_from:
                filtered_expenses = [exp for exp in filtered_expenses if exp["date"] >= date_from]
            if date_to:
                filtered_expenses = [exp for exp in filtered_expenses if exp["date"] <= date_to]
            if category:
                filtered_expenses = [exp for exp in filtered_expenses if exp["category"].lower() == category.lower()]

            # Generate export data
            export_data = {
                "metadata": {
                    "export_date": datetime.now().isoformat(),
                    "format": format,
                    "total_expenses": len(filtered_expenses),
                    "date_range": {"from": date_from, "to": date_to},
                    "filters": {"category": category}
                },
                "expenses": filtered_expenses
            }

            if include_summary:
                total_amount = sum(exp["amount"] for exp in filtered_expenses)
                export_data["summary"] = {
                    "total_amount": total_amount,
                    "average_amount": total_amount / len(filtered_expenses) if filtered_expenses else 0,
                    "categories": {},
                    "date_range": {
                        "earliest": min((exp["date"] for exp in filtered_expenses), default=None),
                        "latest": max((exp["date"] for exp in filtered_expenses), default=None)
                    }
                }

                # Category breakdown
                for exp in filtered_expenses:
                    cat = exp["category"]
                    if cat not in export_data["summary"]["categories"]:
                        export_data["summary"]["categories"][cat] = {"count": 0, "total": 0.0}
                    export_data["summary"]["categories"][cat]["count"] += 1
                    export_data["summary"]["categories"][cat]["total"] += exp["amount"]

            # Format-specific handling
            if format == "csv":
                # In real implementation, generate CSV content
                export_data["download_url"] = "expenses_export.csv"
            elif format == "pdf":
                export_data["download_url"] = "expenses_report.pdf"
            # JSON is returned directly

            logger.info(f"Exported {len(filtered_expenses)} expenses in {format} format")
            return export_data

        except Exception as e:
            logger.error(f"Failed to export expenses: {e}")
            return {"error": str(e)}

    logger.info("[OK] Expenses Manager portmanteau tools registered")
