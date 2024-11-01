# src/cli.py
import sys
from models.base import init_db
from models.recipe import Recipe  # Example model
from models.ingredient import Ingredient  # Example model
from models.meal_plan import MealPlan  # Example model
from sqlalchemy.orm import Session
from models.base import SessionLocal

def main_menu():
    """Display the main menu and prompt the user for a choice."""
    print("Welcome to the Recipe and Meal Planner CLI!")
    print("1. Create a Recipe")
    print("2. View Recipes")
    print("3. Create a Meal Plan")
    print("4. Exit")
    choice = input("Please select an option: ")
    return choice

def run_cli():
    """Run the command line interface."""
    init_db()  # Initialize the database
    while True:
        choice = main_menu()
        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            create_meal_plan()
        elif choice == '4':
            print("Exiting the application.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def create_recipe():
    """Function to create a new recipe."""
    # Implementation for creating a recipe
    pass

def view_recipes():
    """Function to view all recipes."""
    # Implementation for viewing recipes
    pass

def create_meal_plan():
    """Function to create a meal plan."""
    # Implementation for creating a meal plan
    pass

if __name__ == "__main__":
    run_cli()
