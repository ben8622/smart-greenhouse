# Smart Greenhouse
## How to Run

1. Go to the projects root directory `cd ~/smart-greenhouse`
2. Create a virtual environment  `python -m venv venv`
3. Activate the virtual environment `source venv/bin/activate` for Linux or `venv\Scripts\activate.bat` for Windows
4. Install required libraries `pip install -r requirements.txt`
5. Run the flask app in develop mode on the local network `flask --app src/app.py run --debug --host=0.0.0.0`