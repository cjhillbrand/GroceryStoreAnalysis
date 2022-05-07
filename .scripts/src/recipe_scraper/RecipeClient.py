import http.client
import json
from RecipeClientInterface import RecipeClientInterface

class RecipeClient(RecipeClientInterface):
    def __init__(self, host, key):
        self.conn = http.client.HTTPSConnection(host)
        self.headers = {
            'X-RapidAPI-Host': host,
            'X-RapidAPI-Key': key
        }

    def get_recipe(self, recipe_id:int):
        return self.__get(f"/recipes/{recipe_id}/information")

    def get_nutrition(self, recipe_id:int):
        return self.__get(f"/recipes/{recipe_id}/nutritionWidget.json", )

    def get_random_recipe(self, nutrition:object, count:int, isVegetarion=True):
        type = nutrition["type"]
        minProtein = nutrition["minProtein"]
        maxProtein = nutrition["maxProtein"]
        minCarbs = nutrition["minCarbs"]
        maxCarbs= nutrition["maxCarbs"]
        minFat = nutrition["minFat"]
        maxFat = nutrition["maxFat"]
        vegetarian_option = "&diet=vegetarian" if isVegetarion else ""
        return self.__get(
            f"/recipes/searchComplex?limitLicense=false&number={count}" \
            f"&minProtein={minProtein}&maxProtein={maxProtein}" \
            f"&minCarbs={minCarbs}&maxCarbs={maxCarbs}" \
            f"&minFat={minFat}&maxFat={maxFat}" \
            f"&type={type}&addRecipeInformation=true{vegetarian_option}")

    def __get(self, url):
        url = url.replace(" ", "%20")
        self.conn.request("GET", url, headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        return json.loads(data.decode("utf-8"))