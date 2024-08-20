import json
import pathlib

# Dynamically grab the file path, works on both Linux and Windows
CONFIG_FILE_PATH = pathlib.Path("src/resources/") / "config.json"

def get_config_file():
    with open(CONFIG_FILE_PATH, "r") as config_file:
        data = json.load(config_file)
        config_file.close()
        return data

def update_config_file(json_dict):
    with open(CONFIG_FILE_PATH, "w") as config_file:
        json.dump(json_dict, config_file)
        return True
    return False