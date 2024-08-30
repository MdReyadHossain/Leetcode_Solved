SELECT p.project_id, ROUND(SUM(e.experience_years) / COUNT(p.project_id), 2) AS average_years 
FROM project AS p
INNER JOIN employee AS e
ON p.employee_id = e.employee_id 
GROUP BY p.project_id