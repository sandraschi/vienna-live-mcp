"""
Planning Manager Portmanteau

Personal planning and productivity management including:
- Todo list management and categorization
- Calendar and scheduling tools
- Goal setting and tracking
- Habit formation and monitoring
- Productivity analysis and recommendations

This portmanteau provides comprehensive personal productivity tools.
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

# Mock data for development
MOCK_TODOS = []
MOCK_GOALS = []
MOCK_HABITS = []

def register_planning_tools(app):
    """Register all planning manager tools with the MCP server."""

    @app.tool()
    async def create_todo(
        title: str,
        description: Optional[str] = None,
        category: str = "General",
        priority: str = "medium",
        due_date: Optional[str] = None,
        estimated_time: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a new todo item.

        Args:
            title: Todo title
            description: Detailed description (optional)
            category: Category for organization
            priority: Priority level ("low", "medium", "high")
            due_date: Due date (YYYY-MM-DD) (optional)
            estimated_time: Estimated time to complete (optional)

        Returns:
            Created todo item information
        """
        try:
            todo = {
                "id": f"todo_{len(MOCK_TODOS) + 1}",
                "title": title,
                "description": description,
                "category": category,
                "priority": priority,
                "due_date": due_date,
                "estimated_time": estimated_time,
                "status": "pending",
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat()
            }

            MOCK_TODOS.append(todo)

            logger.info(f"Created todo: {title} (priority: {priority})")
            return {
                "success": True,
                "todo": todo,
                "message": f"Todo '{title}' created successfully"
            }

        except Exception as e:
            logger.error(f"Failed to create todo: {e}")
            return {"error": str(e)}

    @app.tool()
    async def update_todo(
        todo_id: str,
        updates: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Update an existing todo item.

        Args:
            todo_id: ID of the todo to update
            updates: Dictionary of fields to update

        Returns:
            Updated todo information
        """
        try:
            todo = next((t for t in MOCK_TODOS if t["id"] == todo_id), None)
            if not todo:
                return {"error": f"Todo {todo_id} not found"}

            # Update allowed fields
            allowed_fields = ["title", "description", "category", "priority", "due_date", "estimated_time", "status"]
            for field, value in updates.items():
                if field in allowed_fields:
                    todo[field] = value

            todo["updated_at"] = datetime.now().isoformat()

            logger.info(f"Updated todo {todo_id}")
            return {
                "success": True,
                "todo": todo,
                "message": f"Todo {todo_id} updated successfully"
            }

        except Exception as e:
            logger.error(f"Failed to update todo {todo_id}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_todos_by_category(
        category: Optional[str] = None,
        status: str = "all",
        priority: Optional[str] = None,
        limit: int = 20
    ) -> List[Dict[str, Any]]:
        """
        Get todos filtered by category and other criteria.

        Args:
            category: Filter by specific category (optional)
            status: Filter by status ("pending", "completed", "all")
            priority: Filter by priority ("low", "medium", "high") (optional)
            limit: Maximum todos to return

        Returns:
            List of filtered todos
        """
        try:
            filtered_todos = MOCK_TODOS.copy()

            # Apply filters
            if category:
                filtered_todos = [t for t in filtered_todos if t["category"].lower() == category.lower()]
            if status != "all":
                filtered_todos = [t for t in filtered_todos if t["status"] == status]
            if priority:
                filtered_todos = [t for t in filtered_todos if t["priority"] == priority]

            # Sort by priority (high first) and due date
            priority_order = {"high": 0, "medium": 1, "low": 2}
            filtered_todos.sort(key=lambda x: (
                priority_order.get(x["priority"], 3),
                x.get("due_date") or "9999-99-99"
            ))

            results = filtered_todos[:limit]
            logger.info(f"Retrieved {len(results)} todos matching criteria")
            return results

        except Exception as e:
            logger.error(f"Failed to get todos by category: {e}")
            return []

    @app.tool()
    async def complete_todo(
        todo_id: str,
        completion_notes: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Mark a todo as completed.

        Args:
            todo_id: ID of the todo to complete
            completion_notes: Optional notes about completion

        Returns:
            Completion confirmation
        """
        try:
            todo = next((t for t in MOCK_TODOS if t["id"] == todo_id), None)
            if not todo:
                return {"error": f"Todo {todo_id} not found"}

            todo["status"] = "completed"
            todo["completed_at"] = datetime.now().isoformat()
            todo["completion_notes"] = completion_notes
            todo["updated_at"] = datetime.now().isoformat()

            logger.info(f"Completed todo {todo_id}: {todo['title']}")
            return {
                "success": True,
                "todo": todo,
                "message": f"Todo '{todo['title']}' marked as completed"
            }

        except Exception as e:
            logger.error(f"Failed to complete todo {todo_id}: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_calendar_events(
        date_from: str,
        date_to: str,
        category: Optional[str] = None,
        include_completed: bool = True
    ) -> List[Dict[str, Any]]:
        """
        Get calendar events within a date range.

        Args:
            date_from: Start date (YYYY-MM-DD)
            date_to: End date (YYYY-MM-DD)
            category: Filter by category (optional)
            include_completed: Include completed events (default: true)

        Returns:
            List of calendar events
        """
        try:
            # TODO: Integrate with actual calendar system
            mock_events = [
                {
                    "id": "event_001",
                    "title": "Vet appointment for Benny",
                    "category": "Pets",
                    "start_time": "2025-12-16T09:00:00Z",
                    "end_time": "2025-12-16T10:00:00Z",
                    "location": "Tierklinik Vienna",
                    "description": "Annual checkup and vaccinations",
                    "status": "confirmed",
                    "reminder": "15 minutes before"
                },
                {
                    "id": "event_002",
                    "title": "Grocery shopping",
                    "category": "Shopping",
                    "start_time": "2025-12-16T14:00:00Z",
                    "end_time": "2025-12-16T15:30:00Z",
                    "location": "Spar Stephansplatz",
                    "description": "Weekly grocery shopping",
                    "status": "pending",
                    "priority": "medium"
                },
                {
                    "id": "event_003",
                    "title": "Coffee with Marion",
                    "category": "Social",
                    "start_time": "2025-12-17T15:00:00Z",
                    "end_time": "2025-12-17T17:00:00Z",
                    "location": "Café Central",
                    "description": "Catch up with sister",
                    "status": "confirmed",
                    "attendees": ["Marion", "Sandra"]
                }
            ]

            # Apply filters
            filtered_events = [
                event for event in mock_events
                if date_from <= event["start_time"][:10] <= date_to
            ]

            if category:
                filtered_events = [event for event in filtered_events if event.get("category", "").lower() == category.lower()]

            if not include_completed:
                filtered_events = [event for event in filtered_events if event.get("status") != "completed"]

            # Sort by start time
            filtered_events.sort(key=lambda x: x["start_time"])

            logger.info(f"Retrieved {len(filtered_events)} calendar events")
            return filtered_events

        except Exception as e:
            logger.error(f"Failed to get calendar events: {e}")
            return []

    @app.tool()
    async def schedule_meeting(
        title: str,
        start_time: str,
        end_time: str,
        description: Optional[str] = None,
        location: Optional[str] = None,
        attendees: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Schedule a new meeting or event.

        Args:
            title: Meeting title
            description: Meeting description (optional)
            start_time: Start time (ISO format)
            end_time: End time (ISO format)
            location: Meeting location (optional)
            attendees: List of attendees (optional)

        Returns:
            Meeting scheduling confirmation
        """
        try:
            # TODO: Check for conflicts and integrate with calendar system
            meeting = {
                "id": f"meeting_{int(datetime.now().timestamp())}",
                "title": title,
                "description": description,
                "start_time": start_time,
                "end_time": end_time,
                "location": location,
                "attendees": attendees or [],
                "status": "scheduled",
                "created_at": datetime.now().isoformat(),
                "category": "Meeting"
            }

            logger.info(f"Scheduled meeting: {title} at {start_time}")
            return {
                "success": True,
                "meeting": meeting,
                "message": f"Meeting '{title}' scheduled successfully"
            }

        except Exception as e:
            logger.error(f"Failed to schedule meeting: {e}")
            return {"error": str(e)}

    @app.tool()
    async def check_schedule_conflicts(
        proposed_start: str,
        proposed_end: str,
        exclude_event_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Check for scheduling conflicts with existing events.

        Args:
            proposed_start: Proposed start time (ISO format)
            proposed_end: Proposed end time (ISO format)
            exclude_event_id: Event ID to exclude from conflict check (optional)

        Returns:
            Conflict analysis with alternatives
        """
        try:
            # TODO: Query actual calendar for conflicts
            mock_conflicts = [
                {
                    "event_id": "event_001",
                    "title": "Vet appointment for Benny",
                    "start_time": "2025-12-16T09:00:00Z",
                    "end_time": "2025-12-16T10:00:00Z",
                    "overlap_minutes": 30,
                    "conflict_level": "partial"
                }
            ]

            has_conflicts = len(mock_conflicts) > 0

            result = {
                "has_conflicts": has_conflicts,
                "conflicts": mock_conflicts,
                "proposed_time": {
                    "start": proposed_start,
                    "end": proposed_end,
                    "duration_minutes": int((datetime.fromisoformat(proposed_end.replace('Z', '+00:00')) -
                                            datetime.fromisoformat(proposed_start.replace('Z', '+00:00'))).total_seconds() / 60)
                }
            }

            if has_conflicts:
                # Suggest alternatives
                base_time = datetime.fromisoformat(proposed_start.replace('Z', '+00:00'))
                alternatives = []
                for i in range(1, 4):
                    alt_start = base_time + timedelta(hours=i)
                    alt_end = alt_start + timedelta(minutes=result["proposed_time"]["duration_minutes"])
                    alternatives.append({
                        "start": alt_start.isoformat(),
                        "end": alt_end.isoformat(),
                        "reason": f"Moved {i} hour{'s' if i > 1 else ''} later"
                    })
                result["alternatives"] = alternatives

            logger.info(f"Checked schedule conflicts: {len(mock_conflicts)} conflicts found")
            return result

        except Exception as e:
            logger.error(f"Failed to check schedule conflicts: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_productivity_stats(
        period: str = "week",
        include_goals: bool = True
    ) -> Dict[str, Any]:
        """
        Get productivity statistics and insights.

        Args:
            period: Time period ("week", "month", "quarter")
            include_goals: Include goal progress (default: true)

        Returns:
            Comprehensive productivity statistics
        """
        try:
            # Calculate date range
            now = datetime.now()
            if period == "week":
                start_date = now - timedelta(days=7)
            elif period == "month":
                start_date = now - timedelta(days=30)
            elif period == "quarter":
                start_date = now - timedelta(days=90)
            else:
                start_date = now - timedelta(days=7)

            # Mock productivity stats
            stats = {
                "period": period,
                "date_range": {
                    "from": start_date.strftime("%Y-%m-%d"),
                    "to": now.strftime("%Y-%m-%d")
                },
                "todos": {
                    "completed": 23,
                    "pending": 8,
                    "overdue": 2,
                    "completion_rate": 74.2
                },
                "time_tracking": {
                    "total_focus_time": "42h 15m",
                    "average_daily": "6h 2m",
                    "most_productive_day": "Wednesday",
                    "peak_hours": "09:00-11:00"
                },
                "habits": {
                    "tracked_habits": 5,
                    "average_streak": 12,
                    "best_streak": 28,
                    "completion_rate": 68
                },
                "goals": {
                    "active_goals": 3,
                    "completed_this_period": 1,
                    "on_track": 2,
                    "behind_schedule": 0
                },
                "insights": [
                    "Most productive during morning hours (9-11 AM)",
                    "Higher completion rates on weekdays vs weekends",
                    "Reading habit shows 85% completion rate",
                    "Consider breaking large tasks into smaller subtasks"
                ]
            }

            logger.info(f"Generated productivity stats for {period} period")
            return stats

        except Exception as e:
            logger.error(f"Failed to get productivity stats: {e}")
            return {"error": str(e)}

    @app.tool()
    async def set_goal(
        title: str,
        description: str,
        category: str,
        target_value: float,
        target_date: str,
        measurement_unit: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Set a new goal to track.

        Args:
            title: Goal title
            description: Goal description
            category: Goal category (e.g., "Health", "Career", "Personal")
            target_value: Target value to achieve
            target_date: Target completion date (YYYY-MM-DD)
            measurement_unit: Unit for measurement (optional)

        Returns:
            Goal creation confirmation
        """
        try:
            goal = {
                "id": f"goal_{len(MOCK_GOALS) + 1}",
                "title": title,
                "description": description,
                "category": category,
                "target_value": target_value,
                "current_value": 0,
                "target_date": target_date,
                "measurement_unit": measurement_unit,
                "status": "active",
                "created_at": datetime.now().isoformat(),
                "progress_percentage": 0
            }

            MOCK_GOALS.append(goal)

            logger.info(f"Set goal: {title} (target: {target_value} by {target_date})")
            return {
                "success": True,
                "goal": goal,
                "message": f"Goal '{title}' set successfully"
            }

        except Exception as e:
            logger.error(f"Failed to set goal: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_goals_progress(
        goal_id: Optional[str] = None,
        status: str = "all"
    ) -> List[Dict[str, Any]]:
        """
        Get goals progress tracking.

        Args:
            goal_id: Specific goal ID (optional)
            status: Filter by status ("active", "completed", "all")

        Returns:
            List of goals with progress information
        """
        try:
            goals = MOCK_GOALS.copy()

            # Apply filters
            if goal_id:
                goals = [g for g in goals if g["id"] == goal_id]
            if status != "all":
                goals = [g for g in goals if g["status"] == status]

            # Calculate progress (mock updates)
            for goal in goals:
                # Simulate progress updates
                if goal["status"] == "active":
                    goal["current_value"] = goal["target_value"] * 0.65  # Mock 65% progress
                    goal["progress_percentage"] = (goal["current_value"] / goal["target_value"]) * 100

                    # Check if target date is approaching
                    target_date = datetime.fromisoformat(goal["target_date"])
                    days_remaining = (target_date - datetime.now()).days
                    if days_remaining < 7:
                        goal["urgency"] = "high"
                    elif days_remaining < 14:
                        goal["urgency"] = "medium"
                    else:
                        goal["urgency"] = "low"

            logger.info(f"Retrieved progress for {len(goals)} goals")
            return goals

        except Exception as e:
            logger.error(f"Failed to get goals progress: {e}")
            return []

    @app.tool()
    async def create_habit(
        name: str,
        description: Optional[str] = None,
        frequency: str = "daily",
        target_count: int = 1,
        reminder_time: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a habit to track.

        Args:
            name: Habit name
            description: Habit description (optional)
            frequency: Frequency ("daily", "weekly", "monthly")
            target_count: Target completions per frequency period
            reminder_time: Reminder time (HH:MM) (optional)

        Returns:
            Habit creation confirmation
        """
        try:
            habit = {
                "id": f"habit_{len(MOCK_HABITS) + 1}",
                "name": name,
                "description": description,
                "frequency": frequency,
                "target_count": target_count,
                "reminder_time": reminder_time,
                "current_streak": 0,
                "best_streak": 0,
                "total_completions": 0,
                "status": "active",
                "created_at": datetime.now().isoformat()
            }

            MOCK_HABITS.append(habit)

            logger.info(f"Created habit: {name} ({frequency})")
            return {
                "success": True,
                "habit": habit,
                "message": f"Habit '{name}' created successfully"
            }

        except Exception as e:
            logger.error(f"Failed to create habit: {e}")
            return {"error": str(e)}

    @app.tool()
    async def log_habit_completion(
        habit_id: str,
        date: Optional[str] = None,
        notes: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Log habit completion for a specific date.

        Args:
            habit_id: ID of the habit
            date: Date of completion (default: today)
            notes: Optional notes about the completion

        Returns:
            Habit logging confirmation
        """
        try:
            habit = next((h for h in MOCK_HABITS if h["id"] == habit_id), None)
            if not habit:
                return {"error": f"Habit {habit_id} not found"}

            completion_date = date or datetime.now().strftime("%Y-%m-%d")

            # Update habit stats
            habit["total_completions"] += 1
            habit["current_streak"] += 1
            if habit["current_streak"] > habit["best_streak"]:
                habit["best_streak"] = habit["current_streak"]

            habit["last_completed"] = completion_date
            habit["updated_at"] = datetime.now().isoformat()

            logger.info(f"Logged completion for habit {habit_id}: streak now {habit['current_streak']}")
            return {
                "success": True,
                "habit": habit,
                "message": f"Habit '{habit['name']}' completion logged successfully"
            }

        except Exception as e:
            logger.error(f"Failed to log habit completion: {e}")
            return {"error": str(e)}

    @app.tool()
    async def get_habit_streak(
        habit_id: Optional[str] = None,
        include_broken: bool = False
    ) -> List[Dict[str, Any]]:
        """
        Get current habit streaks and statistics.

        Args:
            habit_id: Specific habit ID (optional)
            include_broken: Include habits with broken streaks (default: false)

        Returns:
            List of habits with streak information
        """
        try:
            habits = MOCK_HABITS.copy()

            if habit_id:
                habits = [h for h in habits if h["id"] == habit_id]

            if not include_broken:
                habits = [h for h in habits if h["current_streak"] > 0]

            # Sort by current streak (highest first)
            habits.sort(key=lambda x: x["current_streak"], reverse=True)

            result = []
            for habit in habits:
                habit_data = habit.copy()
                habit_data["streak_status"] = "active" if habit["current_streak"] > 0 else "broken"

                # Calculate completion rate (mock)
                days_since_creation = (datetime.now() - datetime.fromisoformat(habit["created_at"])).days
                habit_data["completion_rate"] = (habit["total_completions"] / max(days_since_creation, 1)) * 100

                result.append(habit_data)

            logger.info(f"Retrieved streak information for {len(result)} habits")
            return result

        except Exception as e:
            logger.error(f"Failed to get habit streaks: {e}")
            return []

    @app.tool()
    async def get_motivational_quote(
        category: str = "productivity",
        language: str = "en"
    ) -> Dict[str, Any]:
        """
        Get a motivational quote.

        Args:
            category: Quote category ("productivity", "health", "success", "random")
            language: Quote language ("en", "de") (default: "en")

        Returns:
            Motivational quote with author
        """
        try:
            # Mock quotes by category
            quotes = {
                "productivity": [
                    {
                        "quote": "The way to get started is to quit talking and begin doing.",
                        "author": "Walt Disney",
                        "category": "productivity"
                    },
                    {
                        "quote": "Productivity is never an accident. It is always the result of a commitment to excellence, intelligent planning, and focused effort.",
                        "author": "Paul J. Meyer",
                        "category": "productivity"
                    }
                ],
                "health": [
                    {
                        "quote": "Take care of your body. It's the only place you have to live.",
                        "author": "Jim Rohn",
                        "category": "health"
                    }
                ],
                "success": [
                    {
                        "quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.",
                        "author": "Winston Churchill",
                        "category": "success"
                    }
                ],
                "random": [
                    {
                        "quote": "The best way to predict the future is to create it.",
                        "author": "Peter Drucker",
                        "category": "motivation"
                    }
                ]
            }

            category_quotes = quotes.get(category, quotes["random"])
            selected_quote = category_quotes[0]  # Would randomly select in real implementation

            logger.info(f"Retrieved {category} quote by {selected_quote['author']}")
            return selected_quote

        except Exception as e:
            logger.error(f"Failed to get motivational quote: {e}")
            return {"error": str(e)}

    @app.tool()
    async def plan_week(
        focus_areas: Optional[List[str]] = None,
        include_habits: bool = True,
        include_goals: bool = True
    ) -> Dict[str, Any]:
        """
        Generate weekly planning suggestions.

        Args:
            focus_areas: Specific areas to focus on (optional)
            include_habits: Include habit reminders (default: true)
            include_goals: Include goal progress check (default: true)

        Returns:
            Weekly planning suggestions and priorities
        """
        try:
            # Generate week plan based on current date
            today = datetime.now()
            week_start = today - timedelta(days=today.weekday())  # Monday
            week_end = week_start + timedelta(days=6)  # Sunday

            plan = {
                "week_of": week_start.strftime("%Y-%m-%d"),
                "date_range": {
                    "from": week_start.strftime("%Y-%m-%d"),
                    "to": week_end.strftime("%Y-%m-%d")
                },
                "focus_areas": focus_areas or ["productivity", "health", "learning"],
                "daily_suggestions": {},
                "weekly_goals": [],
                "habit_reminders": [],
                "priority_tasks": []
            }

            # Generate daily suggestions
            weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            for i, day in enumerate(weekdays):
                day_date = week_start + timedelta(days=i)
                plan["daily_suggestions"][day] = {
                    "date": day_date.strftime("%Y-%m-%d"),
                    "focus": plan["focus_areas"][i % len(plan["focus_areas"])],
                    "suggested_activities": [
                        "Review and update todos",
                        "Work on habit maintenance",
                        "Plan next day"
                    ]
                }

            # Weekly goals
            if include_goals:
                plan["weekly_goals"] = [
                    "Complete 80% of scheduled todos",
                    "Maintain habit streaks",
                    "Advance personal goals by 20%",
                    "Review and adjust weekly priorities"
                ]

            # Habit reminders
            if include_habits:
                plan["habit_reminders"] = [
                    "Daily reading (20 minutes)",
                    "Exercise routine",
                    "Meditation practice",
                    "Learning session"
                ]

            # Priority tasks
            plan["priority_tasks"] = [
                "Review calendar for upcoming week",
                "Update goal progress",
                "Plan meals and grocery needs",
                "Schedule important meetings"
            ]

            logger.info(f"Generated weekly plan for {plan['week_of']}")
            return plan

        except Exception as e:
            logger.error(f"Failed to generate weekly plan: {e}")
            return {"error": str(e)}

    logger.info("[OK] Planning Manager portmanteau tools registered")
