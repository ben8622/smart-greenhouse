from flask import Flask
import json
from .config.config_utils import get_config_file

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/config")
def get_config():
    return get_config_file()
