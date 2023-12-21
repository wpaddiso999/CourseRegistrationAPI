# tests/test_student.py
import pytest
from student import Student

@pytest.fixture
def student_instance():
    # You can customize the parameters based on your Student class constructor
    return Student(eid="123")

def test_register_course_valid(student_instance, mocker):
    # Mocking is_valid_course method to return True
    mocker.patch.object(student_instance, 'is_valid_course', return_value=True)

    result = student_instance.register_course("CSE", "101")
    assert result == ["CSE-101"]

def test_register_course_invalid(student_instance, mocker):
    # Mocking is_valid_course method to return False
    mocker.patch.object(student_instance, 'is_valid_course', return_value=False)

    result = student_instance.register_course("Invalid", "Course")
    assert result == {"error": "Invalid course"}
