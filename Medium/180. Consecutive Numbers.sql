SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs AS l1
JOIN Logs AS l2
ON l1.id = l2.id + 1 AND l1.num = l2.num
JOIN Logs AS l3
ON l1.id = l3.id + 2 AND l1.num = l3.num
