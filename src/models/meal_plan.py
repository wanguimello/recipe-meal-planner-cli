from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from database.setup import Base

class MealPlan(Base):
    __tablename__ = 'meal_plans'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    meal_type = Column(String, nullable=False)  # e.g., breakfast, lunch, dinner

    def __repr__(self):
        return f"<MealPlan(date={self.date}, meal_type={self.meal_type})>"
