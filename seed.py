# seed.py
from models.recipe import Recipe
from models.meal_plan_recipes import MealPlanRecipes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URI
DATABASE_URI = 'sqlite:///recipe.db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def seed_database():
    # Create a session
    session = Session()

    # Clear existing data (optional)
    session.query(Recipe).delete()
    session.query(MealPlanRecipes).delete()

    # Sample recipes
    sample_recipes = [
        Recipe(name="Margherita Pizza", ingredients="Flour, Water, Tomato Sauce, Mozzarella, Basil", instructions="Mix ingredients, bake for 20 minutes at 220°C."),
        Recipe(name="Pasta Carbonara", ingredients="Pasta, Eggs, Parmesan Cheese, Pancetta, Black Pepper", instructions="Cook pasta, mix with beaten eggs and cheese, add pancetta."),
        Recipe(name="Caesar Salad", ingredients="Lettuce, Croutons, Caesar Dressing, Parmesan Cheese", instructions="Toss ingredients together in a bowl."),
    ]

    # Add sample recipes to the session
    session.add_all(sample_recipes)

    # Sample meal plans
    sample_meal_plans = [
        MealPlanRecipes(meal_name="Weekly Dinner Plan", recipes=[sample_recipes[0], sample_recipes[1]]),
        MealPlanRecipes(meal_name="Healthy Meal Plan", recipes=[sample_recipes[2]]),
    ]

    # Add sample meal plans to the session
    session.add_all(sample_meal_plans)

    # Commit the session
    session.commit()
    session.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()
