import sqlite3
from this import d

class DataManager:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)

    def add_product(self, recipe):
        insert_statement = """
            INSERT OR IGNORE INTO store_products(gpid, name, quantity, price, store, organic, unit)
            VALUES(?,?,?,?,?,?,?) 
        """
        cursor = self.conn.cursor()
        cursor.execute(insert_statement, recipe)
        self.conn.commit()

    def add_product_mapping(self, mapping):
        insert_statement = """
            INSERT or REPLACE INTO products_mapping(grocery_product_id, product_id)
            VALUES(?,?)
        """
        cursor = self.conn.cursor()
        cursor.execute(insert_statement, mapping)
        self.conn.commit()

    def add_recipe(self, recipe):
        insert_statement = """
            INSERT OR IGNORE INTO recipes(rid,name,health_score,servings,vegetarian,type)
            VALUES(?,?,?,?,?,?) 
        """
        cursor = self.conn.cursor()
        cursor.execute(insert_statement, recipe)
        self.conn.commit()

    def add_ingredient(self, ingredient):
        insert_statement = """
            INSERT OR IGNORE INTO ingredients(pid, recipe_id, name, amount, unit)
            VALUES(?,?,?,?,?)
        """
        cursor = self.conn.cursor()
        cursor.execute(insert_statement, ingredient)
        self.conn.commit()

    def add_nutrition(self, nutrition):
        insert_statement = """
            INSERT OR IGNORE INTO nutrition(recipe_id, protein, fat, carb, calories)
            VALUES(?,?,?,?,?)
        """
        cursor = self.conn.cursor()
        cursor.execute(insert_statement, nutrition)
        self.conn.commit()

    def get_ingredients(self):
        select_statement = """
            SELECT * FROM ingredients
        """
        cursor = self.conn.cursor()
        cursor.execute(select_statement)
        return cursor.fetchall()

    def get_product(self, name, store):
        name = name.replace("'", "''")
        select_statement = f"""
            SELECT * FROM store_products
            WHERE name = '{name}'
            AND store = '{store}'
        """
        cursor = self.conn.cursor()
        cursor.execute(select_statement)
        return cursor.fetchone()

    def get_products(self):
        select_statement = f"""
            SELECT * FROM store_products
        """
        cursor = self.conn.cursor()
        cursor.execute(select_statement)
        return cursor.fetchall()

    def get_mapped_products(self):
        select_statement = """
            SELECT *
            FROM store_products as sp
            INNER JOIN products_mapping as pm ON sp.gpid == pm.grocery_product_id
        """
        cursor = self.conn.cursor()
        cursor.execute(select_statement)
        return cursor.fetchall()

    def get_recipes(self):
        select_statement = """
            SELECT rid, servings FROM recipes
        """
        cursor = self.conn.cursor()
        cursor.execute(select_statement)
        return cursor.fetchall()

    def get_stores(self):
        select_statement = """
            SELECT DISTINCT store FROM store_products
        """
        cursor = self.conn.cursor()
        cursor.execute(select_statement)
        return cursor.fetchall()

    def mapping_exists(self, ingredient_id):
        select_statement = f"""
            SELECT * from products_mapping
            WHERE product_id={ingredient_id}
        """
        cursor = self.conn.cursor()
        cursor.execute(select_statement)
        item = cursor.fetchone()
        return item is not None

    def set_bulk(self, product_id, bulk):
        update_statement = f"""
        UPDATE store_products
        SET bulk={bulk}
        WHERE gpid={product_id}
        """
        cursor = self.conn.cursor()
        cursor.execute(update_statement)
        self.conn.commit()