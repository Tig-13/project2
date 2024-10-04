SELECT AVG(g.grade) AS avg_grade
FROM grades g
JOIN courses c ON g.course_id = c.course_id
WHERE c.teacher_id = (SELECT teacher_id FROM teachers WHERE last_name = 'Johnson');
