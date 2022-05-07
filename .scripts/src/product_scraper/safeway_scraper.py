import time
import re
from unicodedata import category
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from DataManager import DataManager
from safeway_pages import PAGES

NAME_INDEX = 1
PRICE_PARTS_INDEX = 2
PRICE_INDEX = 0
UNIT_INDEX = 1
CATEGORY_INDEX = 0
STORE = "Safeway"

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

data_manager:DataManager = DataManager("../../.data/grocery_store_analysis.db")

URL = "https://www.safeway.com/shop/aisles"
for page in PAGES:
    for sub_category in page["sub_categories"]:
        for page_num in range(1, sub_category["pages"]):
            category = page["category"]
            sub_category_name = sub_category["name"]
            driver.get(f"{URL}/{category}/{sub_category_name}.3132.html?page={page_num}")
            time.sleep(1)
            product_list = driver.find_elements(by=By.TAG_NAME, value="product-item-v2")
            for product in product_list:
                title = product.find_elements(by=By.CLASS_NAME, value="product-item-title-tooltip")
                if (len(title) == 0):
                    # tool tip not present - title wont have ellipses.
                    title = product.find_element(by=By.CLASS_NAME, value="product-title__name").get_attribute("innerText")
                else:
                    # tool tip present - grab title from tooltip since it wont have ellipses.
                    title = title[0].get_attribute("innerText")

                price = product.find_element(by=By.CLASS_NAME, value="product-price").get_attribute("innerText")
                title_parts = title.split('-')
                name = title_parts[0].strip()
                if len(title_parts) < 2:
                    quantity = 1
                else:
                    quantity = title_parts[1].strip()

                isOrganic = re.match(".*[oO]rganic.*", name) != None

                price_parts = price.split('\n')
                your_price = float(price_parts[1].split('/')[0].replace("$", ""))

                print(f"name: {name} price: {your_price} unit: {quantity} organic: {isOrganic} store: {STORE}")
                data_manager.add_product((name, quantity, your_price, STORE, isOrganic))