DELETE FROM person
WHERE id NOT IN (
    SELECT uid FROM (
        SELECT MIN(id) as uid
        FROM person
        GROUP BY email
    ) as u_emails
)