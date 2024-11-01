# models/recipe.py
from sqlalchemy import Column, Integer, String
from .base import Base  

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    instructions = Column(String)

    def __repr__(self):
        return f"<Recipe(title={self.title}, instructions={self.instructions})>"
