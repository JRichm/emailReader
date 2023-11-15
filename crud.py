from model import db
from datetime import datetime
from flask import jsonify
from model import JobLink

# called from mailReader.py for each link grabbed from email
def add_new_job_link(link, external_id):
    new_link = JobLink(job_id=None, external_id=external_id, link=link, created=datetime.now(), updated=datetime.now())
    db.session.add(new_link)
    db.session.commit()
    return new_link.link_id

# update link entry and set job_id
def assign_job_to_link(link, job):
    print("assign_job_to_link called")

# record data after automatically applying for job
def save_application_data():
    print("save_application_data called")

# record data from employer responses
def save_response_details():
    print("save_response_details called")

# get top job links for front page overview
def get_relevant_job_links():
    print("get_relevant_job_links called")
    link_query = JobLink.query.order_by(JobLink.created).all()

    job_links_data = []

    for link in link_query:
        # Format created and updated datetime objects
        created_formatted = link.created.strftime('%b, %d %Y')
        updated_formatted = link.updated.strftime('%b, %d %Y')

        link_data = {
            "external_id": link.external_id,
            "link": link.link,
            "created": created_formatted,
            "updated": updated_formatted,
        }
        job_links_data.append(link_data)

    return {
        "tableName": "Unopened Job Links",
        "columnNames": ["external_id", "link", "created", "updated"],
        "data": job_links_data
    }


# get top applications for front page overview
def get_relevant_applications():
    print("get_relevant_applications called")

    return {
        "tableName": "Applications",
        "data": None
    }

# get top responses for front page overview
def get_relevant_responses():
    print("get_relevant_responses called")

    return {
        "tableName": "Responses",
        "data": None
    }