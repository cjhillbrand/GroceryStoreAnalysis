import time
import re
from unicodedata import category
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from DataManager import DataManager

NAME_INDEX = 1
PRICE_PARTS_INDEX = 2
PRICE_INDEX = 0
UNIT_INDEX = 1
CATEGORY_INDEX = 0
STORE = "Trader Joe's"
CATEGORIES_IGNORE = [
    "entrées & sides",
    "candies & cookies",
    "wraps, burritos & sandwiches",
    "chips, crackers & crunchy bites",
    "bars, jerky &... suprises",
    "salads, soups & sides",
    "entrées & center of plate",
    "appetizers",
    "cool desserts",
    "sweet stuff",
    "dip/spread"
]

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

data_manager:DataManager = DataManager("../../.data/grocery_store_analysis.db")

URL = "https://www.traderjoes.com/home/products/category/food-8"
for i in range(1, 31):
    driver.get(f"{URL}?filters=%7B\"page\"%3A{i}%7D")
    time.sleep(2)
    product_list = driver.find_element(by=By.CLASS_NAME, value="ProductList_productList__list__3-dGs")
    products = product_list.find_elements(by=By.TAG_NAME, value="li")

    for p in products:
        product_parts = p.text.split('\n')
        if len(product_parts) != 1:
            category = product_parts[CATEGORY_INDEX]
            if (category.lower() not in CATEGORIES_IGNORE):
                name = product_parts[NAME_INDEX]
                isOrganic = re.match(".*[oO]rganic.*", name) != None
                price_parts = product_parts[PRICE_PARTS_INDEX].split('/')
                price = price_parts[PRICE_INDEX]
                unit = price_parts[UNIT_INDEX]
                print(f"category: {category} name: {name} price: {price} unit: {unit} organic: {isOrganic} store: {STORE}")
                data_manager.add_product((name, unit, price, STORE, isOrganic))