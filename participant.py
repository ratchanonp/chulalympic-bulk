import csv
import json
import requests

game = "fb"
file_path = f"data/{game}/{game}-par.csv"
url = "http://localhost:3333/api/participants"

# Read csv file
with open(file_path, "r") as f:

    reader = csv.reader(f)

    data = []
    # header as key
    header = next(reader)
    for row in reader:
        # convert string to int for familyId
        row[1] = int(row[1])

        # convert string to int for value
        row[3] = int(row[3])

        # if string is empty, convert to null
        if row[4] == "":
            row[4] = None

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
    with open(f"data/{game}/{game}-par-res.json", "w") as f:
        json.dump(res, f, ensure_ascii=False, indent=4)
