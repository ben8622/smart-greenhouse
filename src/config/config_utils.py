import json

CONFIG_FILE_PATH="/home/pi/smart-greenhouse/src/config/config.json"

def get_config_file():
    config_file = open(CONFIG_FILE_PATH)
    data = json.load(config_file)
    config_file.close()
    return data