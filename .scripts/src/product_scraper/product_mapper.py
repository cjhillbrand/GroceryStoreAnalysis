from stringprep import b1_set
from utils.DataManager import DataManager
from difflib import SequenceMatcher
from fuzzywuzzy import fuzz
import pandas as pd;
pd.options.mode.chained_assignment = None  # default='warn'

TOPN = 15

def similar(a, b):
    return fuzz.token_set_ratio(a,b)

def similar_2(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_top_n(products, ingredient, store, n):
    store_products = products.loc[(products["store"] == store)]
    store_products["score"] = store_products.apply(lambda row : similar(row["name"], ingredient), axis = 1)
    store_products["score2"] = store_products.apply(lambda row : similar_2(row["name"], ingredient), axis = 1)
    return store_products.sort_values(by = ['score', 'score2'], ascending = False).head(n).copy()

def insert_all(top_n, iid):
    user_input = input()
    if user_input:
        indices = []
        for val in str(user_input).split(' '):
            print(val == '' or val == ' ')
            print(val)
            if val != '' and val != ' ':
                val = val.strip(' ')
                print(f"val: {val}")
                indices.append(int(val))
        for index in indices:
            gpid = int(top_n.iloc[index]["id"])
            tup = (gpid, iid)
            data_manager.add_product_mapping(tup)

data_manager:DataManager = DataManager("../../.data/grocery_store_analysis.db")

stores = pd.DataFrame.from_records(data_manager.get_stores(), columns=["name"])
products = pd.DataFrame.from_records(data_manager.get_products(), columns=["id", "name", "quantity", "price", "store", "organic", "unit", "bulk"])
ingredients = pd.DataFrame.from_records(data_manager.get_ingredients(), columns=["id", "name", "amount", "unit", "recipe_id"])

for i, row in ingredients.iterrows():
    for store in ["Safeway", "Trader Joe's"]:
        ingredient_name = row["name"]
        print(f"Ingredient: {ingredient_name}")
        top_n = get_top_n(products, row["name"], store, TOPN)
        top_n = top_n.reset_index()
        print(top_n)
        insert_all(top_n, row["id"])
