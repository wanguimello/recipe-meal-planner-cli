from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    instructions = Column(String)
    cooking_time = Column(Integer)
    difficulty = Column(String)

    ingredients = relationship("Ingredient", secondary="recipe_ingredients")
