from utils.DataManager import DataManager

data_manager:DataManager = DataManager("../../.data/grocery_store_analysis.db")
products = data_manager.get_products()

for p in products:
    q = p[2]
    quantity = q
    unit = ""
    if type(q) == str:
        quantity = q.split(' ')[0]
        unit = "".join(q.split(' ')[1:])
    new_p = (p[0], p[1], quantity, p[3], p[4], p[5], unit)
    print(p)
    print(new_p)
    # data_manager.add_product(new_p)