from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL (adjust if you are using a different database)
DATABASE_URL = "sqlite:///recipes.db"

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)  # Set echo=False to disable SQL query logging

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session instance
session = Session()

# Base class for models to inherit
Base = declarative_base()
