import string
import recipe_login
from RecipeClient import RecipeClient
from ..DataManager import DataManager

meals = [
    {
        "type": "breakfast",
        "minProtein": 8,
        "maxProtein": 12,
        "minCarbs": 36,
        "maxCarbs": 54,
        "minFat": 16,
        "maxFat": 24,
        "count": 25
    },
    {
        "type": "main course",
        "minProtein": 24,
        "maxProtein": 36,
        "minCarbs": 66,
        "maxCarbs": 99,
        "minFat": 14,
        "maxFat": 20,
        "count": 50
    }
]

def load_recipe(data_manager:DataManager, recipe:object, type:string):
    recipe_id = recipe["id"]
    servings = recipe["servings"]
    veg = recipe["vegetarian"]
    score = recipe["healthScore"]
    name = recipe["title"]
    servings = recipe["servings"]
    print(f"id: {recipe_id} veg: {veg} score: {score} name: {name} servings: {servings}")
    data_manager.add_recipe((recipe_id, name, score, servings, veg, type))


client: RecipeClient = RecipeClient(recipe_login.host, recipe_login.key)
data_manager: DataManager = DataManager("../../.data/grocery_store_analysis.db")
for meal in meals:
    response = client.get_random_recipe(meal, meal["count"], True)
    for recipe in response["results"]:
        load_recipe(data_manager, recipe, meal["type"])