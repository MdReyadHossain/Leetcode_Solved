(SELECT name AS results
FROM users AS u
JOIN MovieRating AS mr
ON u.user_id = mr.user_id
GROUP BY u.user_id
ORDER BY COUNT(rating) DESC, u.name ASC
LIMIT 1)
UNION ALL
(SELECT title AS results
FROM movies AS m
JOIN MovieRating AS mr
ON m.movie_id = mr.movie_id
WHERE DATE_FORMAT(created_at,'%Y-%m') = '2020-02'
GROUP BY m.movie_id
ORDER BY AVG(rating) DESC, title ASC
LIMIT 1)