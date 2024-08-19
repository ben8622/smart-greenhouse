import json

CONFIG_FILE_PATH="/home/pi/smart-greenhouse/src/config/config.json"

def get_config_file():
    with open(CONFIG_FILE_PATH, "r") as config_file:
        data = json.load(config_file)
        config_file.close()
        return data

def update_config_file(json):
    with open(CONFIG_FILE_PATH, "w") as config_file:
        config_file.write(str(json))
        return True