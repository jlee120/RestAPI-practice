import requests, json, os


def test_verify_updated_student_info():
    # Getting student info from file
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_name = os.path.join(project_path, 'resources/updated_student_info.json')
    with open(file_name, 'r') as infile:
        expected_data = json.load(infile)

    # Getting student id from file
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_name = os.path.join(project_path, 'resources/student_id.txt')
    with open(file_name, 'r') as infile:
        student_id = infile.read()

    api_url = 'http://thetestingworldapi.com/api/studentDetails/{}'.format(student_id)

    response = requests.get(api_url)
    assert response.status_code == 200

    response_json = json.loads(response.text)

    status = response_json['status']
    response_id = response_json['data']['id']
    first_name = response_json['data']['first_name']
    middle_name = response_json['data']['middle_name']
    last_name = response_json['data']['last_name']
    dob = response_json['data']['date_of_birth']

    assert status == "true"
    assert str(response_id) == student_id
    assert first_name == expected_data['data']['first_name']
    assert middle_name == expected_data['data']['middle_name']
    assert last_name == expected_data['data']['last_name']
    assert dob == expected_data['data']['date_of_birth']
