SELECT customer_id
FROM customer
GROUP BY customer_id
HAVING COUNT(distinct product_key) = (
    SELECT COUNT(product_key)
    FROM product
)