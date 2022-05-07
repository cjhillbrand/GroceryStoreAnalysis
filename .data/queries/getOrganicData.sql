SELECT organic_price - non_organic_price as price_diff, op.pid
FROM (
    SELECT avg(price) as organic_price, product_id as pid
    FROM (
        SELECT *
        FROM store_products
        WHERE organic == 1
    ) as sp
    INNER JOIN products_mapping as pm on pm.grocery_product_id == sp.gpid
    GROUP BY product_id
) as op
INNER JOIN (
    SELECT avg(price) as non_organic_price, product_id as pid
    FROM (
        SELECT *
        FROM store_products
        WHERE organic == 0
    ) as sp
    INNER JOIN products_mapping as pm on pm.grocery_product_id == sp.gpid
    GROUP BY product_id
) as nop on op.pid == nop.pid

