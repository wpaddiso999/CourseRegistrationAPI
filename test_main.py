import requests

def test_register_course():
   
    base_url = "http://localhost:8000"
    endpoint = "/register_course"

   
    data = {
        "student_eid": "123456",
        "course_prefix": "CS",
        "course_number": "101"
    }


    response = requests.post(f"{base_url}{endpoint}", json=data)

    assert response.status_code == 200

 
    print(response.json())


test_register_course()
