SELECT product_id, new_price AS price
FROM Products p1
WHERE change_date <= "2019-08-16"
AND change_date = (
    SELECT MAX(p2.change_date)
    FROM Products p2
    WHERE p2.product_id = p1.product_id
    AND p2.change_date <= "2019-08-16"
)
UNION
SELECT product_id, 10 AS price
FROM Products
GROUP BY product_id
HAVING MAX(
    CASE 
        WHEN change_date <= '2019-08-16' 
        THEN 1 
        ELSE 0 
    END
) = 0