SELECT first_name, last_name FROM students WHERE group_id = (SELECT group_id FROM groups WHERE group_name = 'Group A');
