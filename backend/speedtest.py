import json
import time
import orjson
import pandas
import ujson

# Define the JSON file to parse
analytics_path = "package_2023/activity/analytics/events-2023-00000-of-00001.json"

# JSON Library Line By Line
def json_lbl():
    start_time = time.time()

    with open(analytics_path) as file:
        for line in file:
            data = json.loads(line)

    print(f"JSON Line By Line: {(time.time() - start_time):.4f}s")

# UJSON Library Line By Line
def ujson_lbl():
    start_time = time.time()

    with open(analytics_path) as file:
        for line in file:
            data = ujson.loads(line)

    print(f"UJSON Line By Line: {(time.time() - start_time):.4f}s")

# ORJSON Library Line By Line
def orjson_lbl():
    start_time = time.time()

    # Read as bytes
    with open(analytics_path, "rb") as file:
        for line in file:
            data = orjson.loads(line)

    print(f"ORJSON Line By Line: {(time.time() - start_time):.4f}s")

# Pandas load to mem
def pandas_mem():
    start_time = time.time()

    data = pandas.read_json(analytics_path, lines=True)

    print(f"Pandas load into mem: {(time.time() - start_time):.4f}s")

# Json load to mem
def json_mem():
    start_time = time.time()

    with open(analytics_path) as file:
        data = json.load(file)
        
    print(f"Pandas load into mem: {(time.time() - start_time):.4f}s")


if __name__ == "__main__":
    json_lbl()
    ujson_lbl()
    orjson_lbl()
    # pandas_mem()
    # json_mem()