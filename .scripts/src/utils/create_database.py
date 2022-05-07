import sqlite3
from sqlite3 import Error

create_grocery_store_products = """ CREATE TABLE if NOT EXISTS store_products (
        gpid integer PRIMARY KEY NOT NULL,
        name text NOT NULL,
        quantity real NOT NULL,
        price real NOT NULL,
        store text NOT NULL,
        organic integer NOT NULL,
        unit text NOT NULL,
        bulk intger,
        UNIQUE(name,store,organic)
    );"""

create_recipes_table = """ CREATE TABLE IF NOT EXISTS recipes (
        rid integer PRIMARY KEY NOT NULL,
        name text NOT NULL,
        servings integer NOT NULL,
        health_score integer NOT NULL,
        vegetarian integer NOT NULL,
        type text NOT NULL
    );"""

create_ingredients = """ CREATE TABLE if NOT EXISTS ingredients (
        pid integer NOT NULL PRIMARY KEY,
        name text NOT NULL,
        amount real NOT NULL,
        unit text NOT NULL,
        recipe_id integer NOT NULL,
        FOREIGN KEY (recipe_id) REFERENCES recipes(rid)
    );"""

create_nutrtion_table = """ CREATE TABLE IF NOT EXISTS nutrition (
        recipe_id integer NOT NULL,
        protein real NOT NULL,
        fat real NOT NULL,
        carb real NOT NULL,
        calories real NOT NULL
    );"""

create_products_mapping = """ CREATE TABLE if NOT EXISTS products_mapping (
        grocery_product_id integer NOT NULL,
        product_id integer NOT NULL,
        FOREIGN KEY (grocery_product_id) REFERENCES store_products(gpid),
        FOREIGN KEY (product_id) REFERENCES ingredients(pid),
        UNIQUE(grocery_product_id,product_id)
    );"""

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)      
        return conn  
    except Error as e:
        print(e)
    
    
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

if __name__ == '__main__':
    conn = create_connection(r"../.data/grocery_store_analysis.db")
    if conn is not None:
        create_table(conn, create_grocery_store_products)
        create_table(conn, create_recipes_table)
        create_table(conn, create_ingredients)
        create_table(conn, create_nutrtion_table)
        create_table(conn, create_products_mapping)
        conn.close()

