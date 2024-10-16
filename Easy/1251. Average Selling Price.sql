SELECT p.product_id, IFNULL(ROUND(SUM((us.units * p.price)) / SUM(us.units), 2), 0) AS average_price 
FROM prices AS p
LEFT JOIN unitssold AS us
ON p.product_id = us.product_id
AND us.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id 