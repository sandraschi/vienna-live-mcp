"""
Database models and setup for Vienna Live MCP Server

Supports both SQLite (default, no setup required) and PostgreSQL (optional, production).
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
import os
from pathlib import Path
from typing import Generator

# Database setup (similar to Vienna Life Assistant)
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "vienna_live_mcp.db"

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{DB_PATH}"
)

# SQLite-specific settings
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    echo=False  # Set to True for SQL debugging
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db() -> Generator:
    """Dependency for getting database sessions"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initialize database tables"""
    Base.metadata.create_all(bind=engine)

# =============================================================================
# DATABASE MODELS
# =============================================================================

class Expense(Base):
    """Expense tracking model"""
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    date = Column(String, nullable=False)  # YYYY-MM-DD format
    store = Column(String, nullable=True)
    payment_method = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ShoppingList(Base):
    """Shopping list model"""
    __tablename__ = "shopping_lists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    store_preference = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ShoppingItem(Base):
    """Shopping list item model"""
    __tablename__ = "shopping_items"

    id = Column(Integer, primary_key=True, index=True)
    list_id = Column(Integer, ForeignKey("shopping_lists.id"), nullable=False)
    name = Column(String, nullable=False)
    quantity = Column(Float, default=1.0)
    category = Column(String, nullable=True)
    notes = Column(Text, nullable=True)
    completed = Column(Boolean, default=False)

    list = relationship("ShoppingList")

class Todo(Base):
    """Todo item model"""
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String, default="General")
    priority = Column(String, default="medium")  # low, medium, high
    status = Column(String, default="pending")  # pending, completed
    due_date = Column(String, nullable=True)  # YYYY-MM-DD format
    estimated_time = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

class Goal(Base):
    """Goal tracking model"""
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String, nullable=False)
    target_value = Column(Float, nullable=False)
    current_value = Column(Float, default=0.0)
    target_date = Column(String, nullable=False)  # YYYY-MM-DD format
    measurement_unit = Column(String, nullable=True)
    status = Column(String, default="active")  # active, completed
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Habit(Base):
    """Habit tracking model"""
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    frequency = Column(String, default="daily")  # daily, weekly, monthly
    target_count = Column(Integer, default=1)
    reminder_time = Column(String, nullable=True)  # HH:MM format
    current_streak = Column(Integer, default=0)
    best_streak = Column(Integer, default=0)
    total_completions = Column(Integer, default=0)
    status = Column(String, default="active")  # active, paused
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_completed = Column(String, nullable=True)  # YYYY-MM-DD format

class Budget(Base):
    """Budget tracking model"""
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    period = Column(String, default="monthly")  # weekly, monthly, yearly
    alert_threshold = Column(Float, default=80.0)  # percentage
    created_at = Column(DateTime(timezone=True), server_default=func.now())
