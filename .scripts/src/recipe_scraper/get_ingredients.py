import recipe_login
import re
from RecipeClientInterface import RecipeClientInterface
from ..DataManager import DataManager
from RecipeClient import RecipeClient

def load_nutrition(client:RecipeClientInterface, data_manager:DataManager, recipe_id:int):
    nutrition = client.get_nutrition(recipe_id)
    calories = int(re.findall("[0-9]+", nutrition["calories"])[0])
    carbs = int(re.findall("[0-9]+", nutrition["carbs"])[0])
    fat = int(re.findall("[0-9]+", nutrition["fat"])[0])
    protein = int(re.findall("[0-9]+", nutrition["protein"])[0])
    print(f"id: {recipe_id} calories: {calories} protein: {protein} fat: {fat} carbs: {carbs}")
    data_manager.add_nutrition((recipe_id, protein, fat, carbs, calories))

def load_ingredients(client:RecipeClientInterface, data_manager:DataManager, recipe_id:int, servings:int):
    recipe = client.get_recipe(recipe_id)
    ingredients = recipe["extendedIngredients"]
    for ingredient in ingredients:
        id = ingredient["id"]
        amount = ingredient["amount"]
        name = ingredient["name"]
        unit = ingredient["unit"]
        print(f"id: {id} amount: {amount / servings} name: {name} unit: {unit}")
        data_manager.add_ingredient((id, recipe_id, name, amount, unit))

client: RecipeClientInterface = RecipeClient(recipe_login.host, recipe_login.key)
data_manager: DataManager = DataManager("../../.data/grocery_store_analysis.db")

# tuples of (recipe_id, servings)
recipes = data_manager.get_recipes()
for recipe in recipes:
    load_nutrition(client, data_manager, recipe[0])
    load_ingredients(client, data_manager, recipe[0], recipe[1])
