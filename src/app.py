from flask import Flask, request, render_template
import pathlib
import json
from .config.config_utils import get_config_file, update_config_file

# Dynamically grab the file path, works on both Linux and Windows
INDEX_HTML_FILE_PATH = pathlib.Path("src/html/") / "index.html"

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/config", methods=['GET'])
def get_config():
    return get_config_file()

@app.route("/config", methods=['POST'])
def update_config():
    if (update_config_file(request.get_json())):
        return 'SUCCESS', 200
    else:
        return 'INTERNAL SERVER ERROR', 500
