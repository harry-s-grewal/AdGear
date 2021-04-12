# query_db.py
import sys
import json
import concurrent.futures
import datetime


startTime = datetime.datetime.now()


def count_key(key):
    if key in db_json:
        return len(db_json[key])
    else:
        return 0


counts = dict((key, 0) for key in sys.argv[1:])

with open("db.json") as f:
    db_json = json.load(f)

# ThreadPoolExecuter automatically allocates future jobs to threads. The number of threads specified here is 3
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    future_count = {executor.submit(count_key, key): key for key in counts}
    for future in concurrent.futures.as_completed(future_count):
        key = future_count[future]
        counts[key] = future.result()


for key, count in counts.items():
    print("{}: {}".format(key, count))

print(datetime.datetime.now() - startTime)
