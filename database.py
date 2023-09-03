import sqlite3
import datetime
currentDateTime = datetime.datetime.now()
con = sqlite3.connect('database.db')
cur = con.cursor()

sql1 = ''' CREATE TABLE roles (
    role_id INTEGER PRIMARY KEY,
    role_name TEXT NOT NULL
)'''


sql2 = ''' CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role_id INTEGER,
    FOREIGN KEY (role_id) REFERENCES roles(role_id)
)'''

sql3 = ''' CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY,
    id INTEGER,
    subject_taught TEXT,
    FOREIGN KEY (id) REFERENCES users(id)
    
)'''


sql4 = ''' CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    id INTEGER,
    grade_level TEXT,
    FOREIGN KEY (id) REFERENCES users(id)
)'''

sql5 = ''' CREATE TABLE lessons (
    lesson_id INTEGER PRIMARY KEY,
    teacher_id INTEGER,
    lesson_title TEXT,
    lesson_content TEXT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
)'''

sql6 = ''' CREATE TABLE assessments (
    assessment_id INTEGER PRIMARY KEY,
    lesson_id INTEGER,
    date TIMESTAMP,
    assessment_title TEXT,
    max_score REAL,
    FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id)
)'''

cur.execute(sql1)
cur.execute(sql2)
cur.execute(sql3)
cur.execute(sql4)
cur.execute(sql5)
cur.execute(sql6)
con.commit()
con.close()
