SELECT requester_id AS id, count(accepter_id) AS num
FROM (
    SELECT requester_id , accepter_id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id , requester_id
    FROM RequestAccepted
) AS Friends
GROUP BY id
ORDER BY num DESC
LIMIT 1