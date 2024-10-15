SELECT e1.employee_id, e1.name, 
COUNT(e2.employee_id) AS reports_count, 
ROUND(AVG(e2.age)) AS average_age
FROM Employees AS e1, Employees AS e2
WHERE e1.employee_id = e2.reports_to
GROUP BY 1
HAVING reports_count > 0
ORDER BY 1