# Import necessary libraries
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the database connection
DATABASE_URL = 'sqlite:///recipes.db'
engine = create_engine(DATABASE_URL)

# Create a session to connect with the database
Session = sessionmaker(bind=engine)
session = Session()

# Base class for declarative class definitions
Base = declarative_base()
