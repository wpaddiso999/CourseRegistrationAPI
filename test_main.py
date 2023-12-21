# tests/test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_course():
    response = client.post("/register_course", json={"student_eid": "123", "course_prefix": "CSE", "course_number": "101"})
    assert response.status_code == 200
    assert response.json() == {"registered_courses": ["CSE-101"]}
