SELECT bulk_price - non_bulk_price as price_diff, bp.pid
FROM (
    SELECT avg(price) as bulk_price, product_id as pid
    FROM (
        SELECT *
        FROM store_products
        WHERE bulk == 1
    ) as sp
    INNER JOIN products_mapping as pm on pm.grocery_product_id == sp.gpid
    GROUP BY product_id
) as bp
INNER JOIN (
    SELECT avg(price) as non_bulk_price, product_id as pid
    FROM (
        SELECT *
        FROM store_products
        WHERE bulk == 0
    ) as sp
    INNER JOIN products_mapping as pm on pm.grocery_product_id == sp.gpid
    GROUP BY product_id
) as nbp on bp.pid == nbp.pid
