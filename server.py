from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from model import connect_to_db
from dotenv import load_dotenv
from datetime import datetime
import subprocess
import os
from crud import add_new_job_link, get_relevant_job_links, get_relevant_applications, get_relevant_responses, clear_joblink_dupes, create_new_job, assign_job_to_link, get_links_without_job

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
        link_id = add_new_job_link(entry.get('link'), entry.get('id'))
        link_ids.append(link_id)

    return jsonify({"link_ids": link_ids}), 200
    # called from mailReader.py

    # this function will receive a json object with multiple or single links

    # want to loop through all of the links through the object and call the add_new_job_link crud function to add each link to the database

@app.route('/get_overview_data', methods=["GET"])
def get_overview_data():
    print('get_overview_data\n')

    job_links_data = get_relevant_job_links()
    applications_data = get_relevant_applications()
    responses_data = get_relevant_responses()

    returnData = jsonify([
        job_links_data,
        applications_data,
        responses_data
    ])

    print('returnData')
    print(returnData)

    return returnData

@app.route('/get_new_links', methods=['GET'])
def get_new_links():
    try:
        new_links = get_links_without_job()
        links_data = [
            {
                "link_id": link.link_id,
                "job_id": link.job_id,
                "external_id": link.external_id,
                "link": link.link,
                "created": link.created,
                "updated": link.updated
            }
            for link in new_links
        ]
        return jsonify({"new_links": links_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/create_job', methods=['POST'])
def create_job():
    try:
        data = request.json  # Assuming the Selenium script sends data as JSON

        # Extract job information from the Selenium script
        job_link_id = data.get('job_link_id')
        job_title = data.get('job_title')
        job_description = data.get('job_description')
        job_salary = data.get('job_salary')

        new_job = create_new_job(job_title,job_description,job_salary)

        assign_job_to_link(job_link_id, new_job.job_id)

        return jsonify({"message": "Job created successfully."}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/cleardupes', methods=["GET"])
def clear_dupes():
    print('\n\nClearing duplicate entries...\n')

    print('\t - JobLinks')

    duplicates_info = clear_joblink_dupes()
    print(duplicates_info)
    
    # Return information about duplicates found and deleted
    return jsonify({'duplicates_info': duplicates_info})

# add links     -   app route that take in an array of job links in the form of json

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