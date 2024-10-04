SELECT course_name FROM courses WHERE teacher_id = (SELECT teacher_id FROM teachers WHERE last_name = 'Smith');
