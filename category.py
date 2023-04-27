
import csv
import json

import requests

file_path = "data/AH/ah-cat.csv"
url = "http://localhost:3333/api/sports/categories"


# Read csv file
with open(file_path, "r") as f:
    reader = csv.reader(f)

    data = []
    # header as key
    header = next(reader)
    for row in reader:
        data.append(dict(zip(header, row)))

    # print json dunp utf-8
    print(json.dumps(data, ensure_ascii=False, indent=4))

    # post to api
    res = []
    for item in data:
        respond = requests.post(url, json=item)
        res.append(respond.json())
        
        print(f"Status code: {respond.status_code}")
        print(f"Response: {respond.json()}")


    
    # save to file
    with open("data/AH/ah-cat-res.json", "w") as f:
        json.dump(res, f, ensure_ascii=False, indent=4)
        
        