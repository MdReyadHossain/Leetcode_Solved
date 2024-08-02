SELECT customer_id, COUNT(customer_id) as count_no_trans
FROM visits AS v
LEFT JOIN transactions AS t 
ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY customer_id


SELECT customer_id, COUNT(customer_id) as count_no_trans
FROM (
    SELECT v.visit_id as v_id, t.visit_id as t_id, v.customer_id
    FROM visits AS v
    LEFT JOIN transactions AS t 
    ON v.visit_id = t.visit_id
) as compare
WHERE t_id IS NULL
GROUP BY customer_id
