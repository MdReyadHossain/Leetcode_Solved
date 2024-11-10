SELECT person_name
FROM (
    SELECT person_name, turn, 
    SUM(weight) OVER (ORDER BY turn) AS weight_sum
    FROM Queue 
) AS Q
WHERE weight_sum <= 1000
ORDER BY turn DESC
LIMIT 1