import json
import pathlib

# Dynamically grab the file path, works on both Linux and Windows
METRICS_FILE_PATH = pathlib.Path("flask-app/resources/") / "metrics.json"

def get_metrics_file():
    with open(METRICS_FILE_PATH, "r") as metrics_file:
        data = json.load(metrics_file)
        metrics_file.close()
        return data

def update_metrics_file(json_list):
    with open(METRICS_FILE_PATH, "w") as metrics_file:
        json.dump(json_list, metrics_file)
        return True
    return False