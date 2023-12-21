# student.py
class Student:
    def __init__(self, eid, name=''):
        self.eid = eid
        self.name = name
        self.registered_courses = []

    def register_course(self, course_prefix, course_number):
        # Your validation logic here
        if self.is_valid_course(course_prefix, course_number):
            course = f"{course_prefix}-{course_number}"
            self.registered_courses.append(course)
            return self.registered_courses
        else:
            return {"error": "Invalid course"}

    def is_valid_course(self, course_prefix, course_number):
        # Your validation logic here
        # Example: Check if the course exists in a database or a predefined list
        return True
