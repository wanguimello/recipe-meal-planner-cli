# models/ingredient.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.setup import Base

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(String, nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    # Link to Recipe
    recipe = relationship("Recipe", back_populates="ingredients")

    def __repr__(self):
        return f"<Ingredient(name='{self.name}', quantity='{self.quantity}')>"
