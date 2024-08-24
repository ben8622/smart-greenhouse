from flask import Flask, request, render_template
from services.config_service import get_config_file, update_config_file
from services.metrics_service import get_metrics_file, update_metrics_file

# Dynamically grab the file path, works on both Linux and Windows
INDEX_HTML_FILE_PATH = "index.html"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(INDEX_HTML_FILE_PATH, metrics=get_metrics(), config=get_config())

@app.route("/config", methods=['GET'])
def get_config():
    return get_config_file()

@app.route("/config", methods=['POST'])
def update_config():
    if (update_config_file(request.get_json())):
        return 'SUCCESS', 200
    else:
        return 'INTERNAL SERVER ERROR', 500

@app.route("/metrics", methods=['GET'])
def get_metrics():
    return get_metrics_file()

@app.route("/metrics", methods=['POST'])
def update_metrics():
    if (update_metrics_file(request.get_json())):
        return 'SUCCESS', 200
    else:
        return 'INTERNAL SERVER ERROR', 500
