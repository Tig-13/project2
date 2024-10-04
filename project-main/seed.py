from faker import Faker
from sqlalchemy.orm import Session
from models import Student, Group, Teacher, Subject, Grade, Base
from sqlalchemy import create_engine
from datetime import datetime
import random

fake = Faker()
engine = create_engine('postgresql://user:password@localhost/dbname')
Base.metadata.create_all(engine)
session = Session(engine)

groups = [Group(name=f'Group {i}') for i in range(1, 4)]
teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
subjects = [Subject(name=f'Subject {i}', teacher=random.choice(teachers)) for i in range(1, 8)]
students = [Student(fullname=fake.name(), group=random.choice(groups)) for _ in range(50)]

session.add_all(groups + teachers + subjects + students)
session.commit()

for student in students:
    for subject in subjects:
        for _ in range(random.randint(5, 10)):
            grade = Grade(grade=random.randint(60, 100), date_received=fake.date_this_year(), student=student, subject=subject)
            session.add(grade)

session.commit()
