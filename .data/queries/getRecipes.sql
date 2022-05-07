SELECT sum(price) / servings as price, rid, vegetarian, type
FROM recipes as r 
INNER JOIN ingredients as i on i.recipe_id == r.rid
INNER JOIN (
    SELECT pm.product_id as pid, avg(sp.price) as price
    FROM store_products as sp
    INNER JOIN products_mapping as pm on pm.grocery_product_id == sp.gpid
    GROUP BY pm.product_id
) as prices on prices.pid == i.pid
GROUP BY rid, type, vegetarian, servings
