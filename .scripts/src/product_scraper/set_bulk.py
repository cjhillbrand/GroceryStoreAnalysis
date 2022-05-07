from utils.DataManager import DataManager
import pandas as pd;
pd.options.mode.chained_assignment = None  # default='warn'

data_manager:DataManager = DataManager("../../.data/grocery_store_analysis.db")
products = pd.DataFrame.from_records(data_manager.get_mapped_products(), columns=["id", "name", "quantity", "price", "store", "organic", "unit", "bulk", "gpid", "pid"])

pids = products.pid.unique()
for pid in pids:
    current_products = products.loc[products.pid == pid].copy()
    current_products = current_products.reindex()
    # print(current_products)
    try:
        avg_quantity = current_products["quantity"].mean()
        non_bulk_products = current_products.loc[current_products.quantity <= avg_quantity]
        for i, non_bulk in non_bulk_products.iterrows():
            gpid = non_bulk["id"]
            print(gpid)
            data_manager.set_bulk(gpid, 0)
        for i, non_bulk in current_products.loc[current_products.quantity > avg_quantity].iterrows():
            gpid = non_bulk["id"]
            data_manager.set_bulk(gpid, 1)
    except:
        continue
    