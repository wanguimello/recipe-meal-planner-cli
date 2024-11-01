from database.setup import engine, Base
#from models.recipe import Recipe
#from models.ingredient import Ingredient
#from models.meal_plan import MealPlan
#from models.association import recipes_meal_plans

def initialize_database():
    # Drop all tables (optional; be careful with this in production)
    Base.metadata.drop_all(engine)
    
    # Create all tables defined by the models
    Base.metadata.create_all(engine)
    print("Database initialized successfully, tables created.")

if __name__ == "__main__":
    initialize_database()
