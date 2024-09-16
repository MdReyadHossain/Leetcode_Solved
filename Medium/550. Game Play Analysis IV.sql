SELECT 
ROUND(SUM(DATEDIFF(a.event_date, f.first_day) = 1) / COUNT(DISTINCT a.player_id), 2) AS fraction
FROM (
    SELECT player_id, min(event_date) AS first_day
    FROM activity
    GROUP BY player_id
) AS f
JOIN activity AS a
ON f.player_id = a.player_id