# create_db.py
import json
import sys
import uuid

with open("db.json", "w") as out:
    with open("events.json") as in_:
        myDict = {}
        for line in in_:
            record = json.loads(line)
            key = record["key"]
            value = record["value"]

            if key in myDict:
                myDict[key].append(value)
            else:
                myDict[key] = [value]

        json.dump(myDict, out)
