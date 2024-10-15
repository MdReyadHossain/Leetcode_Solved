SELECT p.product_name, SUM(o.unit) AS unit
FROM Products AS p
INNER JOIN Orders AS o
ON p.product_id = o.product_id
WHERE DATE_FORMAT(o.order_date, "%Y-%m") = "2020-02"
GROUP BY p.product_id
HAVING SUM(o.unit) >= 100