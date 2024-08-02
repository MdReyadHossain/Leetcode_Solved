SELECT w1.id
FROM weather AS w1
JOIN weather AS w2
ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature