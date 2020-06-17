import requests, json, os


def test_add_user():
    api_url = 'http://thetestingworldapi.com/api/studentDetails'

    # Read student info JSON from file
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_name = os.path.join(project_path, 'resources/student_info.json')
    with open(file_name, 'r') as infile:
        request_data = json.load(infile)

    response = requests.post(api_url, request_data)
    assert response.status_code == 201

    response_json = json.loads(response.text)
    id = response_json['id']
    first_name = response_json['first_name']
    middle_name = response_json['middle_name']
    last_name = response_json['last_name']
    dob = response_json['date_of_birth']

    assert first_name == request_data['first_name']
    assert middle_name == request_data['middle_name']
    assert last_name == request_data['last_name']
    assert dob == request_data['date_of_birth']

    # Write id to file
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_name = os.path.join(project_path, 'resources/student_id.txt')
    with open(file_name, 'w') as outfile:
        outfile.write(str(id))
