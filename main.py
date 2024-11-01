import sys
from models.recipe import Recipe
#from models.ingredient import Ingredient
#from models.meal_plan import MealPlan
from database.setup import session


def main_menu():
    while True:
        print("Welcome to the Recipe and Meal Planner CLI!")
        print("1. Add a Recipe")
        print("2. View Recipes")
        print("3. Create a Meal Plan")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            create_meal_plan()
        elif choice == '4':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def add_recipe():
    name = input("Enter recipe name: ")
    instructions = input("Enter instructions: ")
    category = input("Enter category (e.g., breakfast, lunch): ")
    
    # Create a new recipe instance
    new_recipe = Recipe(name=name, instructions=instructions, category=category)
    session.add(new_recipe)
    session.commit()
    print(f"Recipe '{name}' added successfully.")

def view_recipes():
    recipes = session.query(Recipe).all()
    for recipe in recipes:
        print(recipe)

def create_meal_plan():
    print("Feature to create a meal plan coming soon...")

if __name__ == "__main__":
     main_menu()                                                        