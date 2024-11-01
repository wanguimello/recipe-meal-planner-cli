# Import necessary SQLAlchemy components
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.setup import Base

class Recipe(Base):
    # Define table name
    __tablename__ = 'recipes'

    # Define columns with data types
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    instructions = Column(String, nullable=False)
    category = Column(String, nullable=False)  # e.g., breakfast, lunch, dinner

    # Define relationship with Ingredient model
    ingredients = relationship('Ingredient', back_populates='recipe')

    def __repr__(self):
        # Return a readable string representation of the Recipe instance
        return f"<Recipe(name={self.name}, category={self.category})>"
