from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_course():

    response = client.post("/register_course", json={
        "student_eid": "123456",
        "course_prefix": "COSC",
        "course_number": "111"
    })

    assert response.status_code == 200
    assert response.json() == {"registered_courses": ["COSC 111"]}
