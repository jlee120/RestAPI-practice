import requests, json, os


def test_verify_deleted_student():
    # Getting student id from file
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_name = os.path.join(project_path, 'resources/student_id.txt')
    with open(file_name, 'r') as infile:
        student_id = infile.read()

    api_url = 'http://thetestingworldapi.com/api/studentDetails/{}'.format(student_id)

    response = requests.get(api_url)
    assert response.status_code == 200

    response_json = json.loads(response.text)
    print(response_json)
    status = response_json['status']
    msg = response_json['msg']

    assert status == "false"
    assert msg == "No data found"
