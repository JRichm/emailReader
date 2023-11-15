from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from model import connect_to_db
from dotenv import load_dotenv
import subprocess
import os
import crud

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



@app.route('/addLinks', methods=["POST"])
def add_links():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    link_ids = []

    for entry in data:
        link_id = crud.add_new_job_link(entry.get('link'), entry.get('id'))
        link_ids.append(link_id)

    return jsonify({"link_ids": link_ids}), 200
    # called from mailReader.py

    # this function will receive a json object with multiple or single links

    # want to loop through all of the links through the object and call the add_new_job_link crud function to add each link to the database

@app.route('/get_overview_data', methods=["GET"])
def get_overview_data():

    print('get_overview_data\n')

    return jsonify([
        {
            "tableName": "JobLinks",
            "columnNames": [
                "Link",
                "Job",
                "Board",
                "External",
                "Link",
                "Created",
                "Updated"
            ],
            "data": {

            }
        },
        {
            "tableName": "AppliedJobs",
            "columnNames": [
                "Job",
                "Job Name",
                "Job Board",
                "Job Salary",
                "Date",
                "Applied",
                "Updated"
            ],
            "data": {
                
            }
        },
        {
            "tableName": "Responses",
            "columnNames": [
                "Response",
                "Job",
                "Contact Method",
                "Response",
                "Length",
                "Responded",
                "Updated"
            ],
            "data": {
                
            }
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