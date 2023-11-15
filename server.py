from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from model import connect_to_db
from dotenv import load_dotenv
import subprocess
import os

load_dotenv()

app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv('SECRET_KEY')

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

@app.route('/get_overview_data', methods=["GET"])
def get_overview_data():

    print('get_overview_data\n')

    return jsonify([
        {
            "TableName": "AppliedJobs",
            "ColumnNames": [
                "JobId",
                "JobName",
                "JobBoard",
                "JobSalary",
                "Date"
            ]
        },
        {
            "TableName": "Responses",
            "ColumnNames": [
                "ResponseId",
                "Job",
                "ContactMethod",
                "Response",
                "Length"
            ]
        }
    ])


# add links     -   app route that take in an array of job links in the form of json

# json param format :
#    [
#        {
#            "job_board": "",
#            "external_id": "",
#            "job_link": ""
#        },
#        {
#            "job_board": "",
#            "external_id": "",
#            "job_link": ""
#        }
#    ]

# loop through array of links
    # call crud function to try to add each link to job_links table


#crud.py

    # def new_job_link(job_board, external_id, job_link):

    # def seach_external_id(external_id, job_board):
        # select * from job_board
        #       where job_board.external_id = external_id


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)