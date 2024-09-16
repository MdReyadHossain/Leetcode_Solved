SELECT DATE_FORMAT(trans_date, "%Y-%m") AS month, country,
COUNT(id) AS trans_count, 
COUNT(IF(state = "approved", state, null)) AS approved_count,
SUM(amount) AS trans_total_amount,
SUM(IF(state = "approved", amount, 0)) AS approved_total_amount
FROM transactions 
GROUP BY country, month