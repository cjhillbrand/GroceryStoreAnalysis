SELECT 
    price_one - price_two as price_diff, 
    store_one.pid, 
    store_one.store as store_one, 
    store_two.store as store_two
FROM (
    SELECT store, price as price_one, product_id as pid
    FROM (
        SELECT store, price, gpid
        FROM store_products as sp
        WHERE store = 'STORE_ONE'
    ) as store_one
    INNER JOIN products_mapping as pm on pm.grocery_product_id == store_one.gpid
) as store_one
INNER JOIN (
    SELECT store, price as price_two, product_id as pid
    FROM (
        SELECT store, price, gpid
        FROM store_products as sp
        WHERE store = 'STORE_TWO'
    ) as store_one
    INNER JOIN products_mapping as pm on pm.grocery_product_id == store_one.gpid
) as store_two on store_one.pid == store_two.pid

