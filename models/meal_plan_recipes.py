# models/meal_plan_recipes.py
from sqlalchemy import Table, Column, Integer, ForeignKey
from database.setup import Base

# Association table for many-to-many relationship
meal_plan_recipes = Table(
    'meal_plan_recipes', Base.metadata,
    Column('meal_plan_id', Integer, ForeignKey('meal_plans.id')),
    Column('recipe_id', Integer, ForeignKey('recipes.id'))
)
