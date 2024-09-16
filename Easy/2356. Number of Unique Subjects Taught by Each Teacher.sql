SELECT teacher_id, COUNT(teacher_id) AS cnt
FROM (
    SELECT teacher_id, COUNT(subject_id) AS cnt
    FROM teacher
    GROUP BY teacher_id, subject_id
) AS sub_cnt
GROUP BY teacher_id