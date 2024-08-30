SELECT machine_id, 
ROUND(SUM(time) / COUNT(machine_id), 3) AS processing_time
FROM (
    SELECT machine_id, process_id, 
    MAX(timestamp) - MIN(timestamp)  AS time 
    FROM activity
    GROUP BY machine_id, process_id
) AS process_activity
GROUP BY machine_id