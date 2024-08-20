from flask import Flask, request, render_template
from services.config_service import get_config_file, update_config_file

# Dynamically grab the file path, works on both Linux and Windows
INDEX_HTML_FILE_PATH = "index.html"

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template(INDEX_HTML_FILE_PATH)

@app.route("/config", methods=['GET'])
def get_config():
    return get_config_file()

@app.route("/config", methods=['POST'])
def update_config():
    if (update_config_file(request.get_json())):
        return 'SUCCESS', 200
    else:
        return 'INTERNAL SERVER ERROR', 500
