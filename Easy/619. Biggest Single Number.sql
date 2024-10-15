SELECT MAX(num) as num
FROM (
    SELECT num, COUNT(num) as cnt
    FROM MyNumbers
    GROUP BY num
    HAVING cnt = 1
) as SingleNumbers