# generate_events.py
import json
import random
import uuid
 
# Number of events to generate
N = 100000
 
# Generate a relatively small number of keys
KEYS = [str(uuid.uuid4()) for _ in range(N // 100)]
 
with open("events.json", "w") as f:
    for _ in range(N):
        record = {
            "key": random.choice(KEYS),
            "value": str(uuid.uuid4()),
        }
        json.dump(record, f)
        f.write("\n")