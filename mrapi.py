from flask import Flask, request, render_template
from model import connect_to_db
import subprocess

app = Flask(__name__)
app.secret_key = 'mail'

# Build Tailwind CSS during Flask application startup
subprocess.run(["npx.cmd", "postcss", "static/css/global.css", "-o", "static/css/output.css"])


@app.route("/")
def index():

    text = 1000

    return render_template('index.html')

# add new link to db
@app.route('/addLink', methods=["POST"])
def add_link():
    if request.method == 'POST':
        data = request.json  # Access the JSON data sent in the POST request
        print('post request data:', data)
    else:
        print('other request')
    return {"response": "success"}

# save application details

# save response details

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)