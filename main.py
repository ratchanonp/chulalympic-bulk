import requests
import json

file_path = 'chulalympic-bs.csv'
url = 'http://localhost:3333/api/games'

# read csv file and print it
with open(file_path, 'r') as f:

    headers = f.readline().strip().split(',')

    for line in f:
        # Make field venueId, facultyId to int
        # Remove date and time
        # Parse to json

        data = {}

       def is_single_participant(line):
    return line.strip().split(',')[7] == ''

def is_double_participant(line):
    return line.strip().split(',')[8] == ''

def get_data(line):
    if is_single_participant(line):
        data = {
            'sportCode': line.strip().split(',')[0],
            'sportCategoryCode': line.strip().split(',')[1],
            'start': line.strip().split(',')[4],
            'venueId': int(line.strip().split(',')[5]),
            'participants': [],
            'status': 'SCHEDULED',
            'type': 'REGULAR'
        }
    elif is_double_participant(line):
        data = {
            'sportCode': line.strip().split(',')[0],
            'sportCategoryCode': line.strip().split(',')[1],
            'start': line.strip().split(',')[4],
            'venueId': int(line.strip().split(',')[5]),
            'participants': [
                {
                    'facultyId': int(line.strip().split(',')[7]),
                    'scoreType':line.strip().split(',')[6]
                }
            ],
            'status': 'SCHEDULED',
            'type': 'REGULAR'
        }
    else:
        data = {
            'sportCode': line.strip().split(',')[0],
            'sportCategoryCode': line.strip().split(',')[1],
            'start': line.strip().split(',')[4],
            'venueId': int(line.strip().split(',')[5]),
            'participants': [
                {
                    'facultyId': int(line.strip().split(',')[7]),
                    'scoreType':line.strip().split(',')[6]
                },
                {
                    'facultyId': int(line.strip().split(',')[8]),
                    'scoreType':line.strip().split(',')[6]
                }
            ],
            'status': 'SCHEDULED',
            'type': 'REGULAR'
        }

        # Print json
        # print(json.dumps(data, indent=4, sort_keys=True))

        # Send request to server
        res = requests.post(url, json=data)

        # Print response
        print(res.status_code)
        print(res.text)
