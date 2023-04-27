
import csv
import json

import requests

game = "fb"
file_path = f"data/{game}/{game}-game.csv"

url = "http://localhost:3333/api/games"

with open(file_path, "r") as f:
    
    # Read csv file
    reader = csv.reader(f)

    data = []
    # header as key
    header = next(reader)
    header.append("participants")

    for row in reader:
        # convert string to int for venueId
        row[6] = int(row[6])

        # add participants to dict
        participants = []
        row.append(participants)

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

    # save to txt only id
    with open(f"data/{game}/{game}-game-res.txt", "w") as f:
        for item in res:
            f.write(f"{item['id']}\n")
    

    