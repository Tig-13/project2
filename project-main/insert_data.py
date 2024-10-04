import faker
import psycopg2
import random
from datetime import datetime

fake = faker.Faker()

conn = psycopg2.connect("dbname=yourdbname user=youruser password=yourpassword")
cur = conn.cursor()

groups = ['Group A', 'Group B', 'Group C']
for group in groups:
    cur.execute("INSERT INTO groups (group_name) VALUES (%s)", (group,))

for _ in range(5):
    cur.execute("INSERT INTO teachers (first_name, last_name) VALUES (%s, %s)",
                (fake.first_name(), fake.last_name()))

courses = ['Math', 'History', 'Physics', 'Literature', 'Chemistry', 'Biology', 'Art', 'Music']
for course in courses:
    cur.execute("SELECT teacher_id FROM teachers ORDER BY RANDOM() LIMIT 1")
    teacher_id = cur.fetchone()[0]
    cur.execute("INSERT INTO courses (course_name, teacher_id) VALUES (%s, %s)", (course, teacher_id))

for _ in range(30):
    group_id = random.randint(1, 3)
    cur.execute("INSERT INTO students (first_name, last_name, group_id) VALUES (%s, %s, %s)",
                (fake.first_name(), fake.last_name(), group_id))

cur.execute("SELECT student_id FROM students")
students = cur.fetchall()

cur.execute("SELECT course_id FROM courses")
courses = cur.fetchall()

for student in students:
    for _ in range(random.randint(10, 20)):
        course_id = random.choice(courses)[0]
        grade = random.randint(1, 10)
        date_assigned = fake.date_this_year()
        cur.execute("INSERT INTO grades (student_id, course_id, grade, date_assigned) VALUES (%s, %s, %s, %s)",
                    (student[0], course_id, grade, date_assigned))

conn.commit()
cur.close()
conn.close()
