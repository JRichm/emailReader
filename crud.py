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


def assign_job_to_link(link, job):
    print("assign_job_to_link called")

def save_application_data():
    print("save_application_data called")

def save_response_details():
    print("save_response_details called")

def get_relevant_job_links():
    print("get_relevant_job_links called")

def get_relevant_applications():
    print("get_relevant_applications called")

def get_relevant_responses():
    print("get_relevant_responses called")