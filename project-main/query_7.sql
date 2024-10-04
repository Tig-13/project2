SELECT s.first_name, s.last_name, g.grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
WHERE s.group_id = (SELECT group_id FROM groups WHERE group_name = 'Group B')
AND g.course_id = (SELECT course_id FROM courses WHERE course_name = 'Physics');
