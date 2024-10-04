SELECT gr.group_name, AVG(g.grade) AS avg_grade
FROM groups gr
JOIN students s ON gr.group_id = s.group_id
JOIN grades g ON s.student_id = g.student_id
WHERE g.course_id = (SELECT course_id FROM courses WHERE course_name = 'History')
GROUP BY gr.group_name;
