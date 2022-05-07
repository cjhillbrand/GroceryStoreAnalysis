import json
import RecipeClientInterface

class FileRecipeClient(RecipeClientInterface):
    def __init__(self, directory):
        self.directory = directory

    def get_nutrition(self, recipe_id):
        return self.__get("nutritionWidget.json")
    
    def get_recipe(self, recipe_id:int):
        return self.__get("information.json")

    def __get(self, file):
        f = open(f"{self.directory}{file}", "r")
        return json.loads(f.read())
