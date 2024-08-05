SELECT e.name, b.bonus 
FROM employee as e
LEFT JOIN bonus as b
ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL