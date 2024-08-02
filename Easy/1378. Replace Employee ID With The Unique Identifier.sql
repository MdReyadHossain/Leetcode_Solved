SELECT eun.unique_id, emp.name
FROM employees AS emp
LEFT JOIN employeeUNI AS eun 
ON emp.id = eun.id