# models/base.py
from database.setup import Base, engine
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.meal_plan import MealPlan
from models.meal_plan_recipes import meal_plan_recipes  # Import association table

def init_db():
    Base.metadata.create_all(engine)
