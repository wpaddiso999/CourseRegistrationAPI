# main.py
from fastapi import FastAPI
from student import Student

app = FastAPI()

@app.post("/register_course")
def register_course(student_eid: str, course_prefix: str, course_number: str):
    student = Student(eid=student_eid)
    result = student.register_course(course_prefix, course_number)
    return {"registered_courses": result}
