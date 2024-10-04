SELECT c.course_name
FROM courses c
JOIN grades g ON c.course_id = g.course_id
WHERE g.student_id = (SELECT student_id FROM students WHERE last_name = 'Doe');
