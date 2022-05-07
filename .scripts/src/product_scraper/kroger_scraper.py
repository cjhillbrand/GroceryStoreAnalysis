from product_scraper.KrogerClient import KrogerClient
from utils.DataManager import DataManager
from product_scraper import kroger_login
import re


BASE_URL = "https://api.kroger.com/v1"    
STORE = kroger_login.location_name

client:KrogerClient = KrogerClient(BASE_URL)
data_manager:DataManager = DataManager("../../.data/grocery_store_analysis.db")

ingredients = data_manager.get_ingredients()
for ingredient in ingredients:
    ingredient_id = ingredient[0]
    ingredient_name = ingredient[1]
    try:
        products = client.get_products(ingredient_name, kroger_login.location)
    except:
        # best effort approach
        continue

    for product in products.get("data"):
        # Kroger stores an array of items in one product. 
        # I dont necessarily understand, although lets just take the top
        # item for simplicity.
        name = product.get("description")\
            .replace('®', '')\
            .replace('™', '')
        isOrganic = re.match(".*[oO]rganic.*", name) != None
        items = product.get("items")
        if (items is not None and len(items) > 0):
            # again best effort approach
            item = product.get("items")[0]
            quantity = item.get("size")
            price_obj = item.get("price")
            if (price_obj is not None):
                price = price_obj.get("regular")

                print(f"name: {name} price: {price} unit: {quantity} organic: {isOrganic} store: {STORE}")
                data_manager.add_product((name, quantity, price, STORE, isOrganic))
                p = data_manager.get_product(name, STORE)
                data_manager.add_product_mapping((p[0], ingredient_id))