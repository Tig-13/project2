from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    grades = relationship('Grade', back_populates='student')

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship('Student', back_populates='group')

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date_received = Column(DateTime, nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    student = relationship('Student', back_populates='grades')
    subject = relationship('Subject', back_populates='grades')

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    grades = relationship('Grade', back_populates='subject')
    teacher = relationship('Teacher', back_populates='subjects')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)
    subjects = relationship('Subject', back_populates='teacher')
