SELECT query_name,
ROUND(SUM(rating/position) / COUNT(query_name), 2) AS quality,
ROUND((SUM(rating < 3) / COUNT(query_name)) * 100, 2) AS poor_query_percentage 
FROM queries
WHERE ISNULL(query_name) = 0
GROUP BY query_name 