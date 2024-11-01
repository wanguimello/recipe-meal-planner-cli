# src/models/base.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL for SQLite
DATABASE_URL = "sqlite:///recipes.db"

# Create a new SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare the base class for models
Base = declarative_base()

def init_db():
    """Initialize the database by importing models and creating tables."""
    from . import recipe  # Import the recipe model
    from . import ingredient  # Import the ingredient model
    from . import meal_plan  # Import the meal plan model
    Base.metadata.create_all(bind=engine)  # Create all tables

# Optional: Call init_db if this script is run directly
if __name__ == "__main__":
    init_db()  # Initialize the database
