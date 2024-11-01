from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.setup import Base

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(String, nullable=False)
    unit = Column(String, nullable=False)

    # Foreign key to reference Recipe
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship('Recipe', back_populates='ingredients')

    def __repr__(self):
        return f"<Ingredient(name={self.name}, quantity={self.quantity} {self.unit})>"
