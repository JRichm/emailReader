from model import db
from datetime import datetime
from flask import jsonify
from model import JobLink
from sqlalchemy import func
from sqlalchemy.orm import aliased

# called from mailReader.py for each link grabbed from email
def add_new_job_link(link, external_id):
    # Check if the entry already exists
    existing_link = JobLink.query.filter_by(external_id=external_id, link=link).first()

    if existing_link:
        # Entry already exists, update the timestamp or handle it as needed
        existing_link.updated = datetime.now()
        db.session.commit()
        return existing_link.link_id
    else:
        # Entry does not exist, add a new one
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

def clear_joblink_dupes():
    duplicates_info = {'found': 0, 'deleted': 0}

    # Use an alias to join the table with itself
    j1 = aliased(JobLink)
    j2 = aliased(JobLink)

    # Specify the columns you need in the select statement and the group_by clause
    duplicates_query = (
        db.session.query(
            j1.external_id,
            func.min(j1.created).label('min_created'),
            func.max(j1.updated).label('max_updated'),
        )
        .join(
            j2,
            (j1.external_id == j2.external_id) & (j1.link == j2.link) & (j1.link_id != j2.link_id)
        )
        .group_by(j1.external_id)
        .having(func.count().label('count') > 1)
    )

    # Iterate through duplicates and decide whether to delete or merge
    for duplicate in duplicates_query:
        duplicate_entries = JobLink.query.filter(
            JobLink.external_id == duplicate.external_id
        ).order_by(JobLink.created).all()

        # Decide how to handle duplicates
        # For example, you can merge them by updating one entry and deleting the others
        if len(duplicate_entries) > 1:
            # Update the first entry with combined information
            first_entry = duplicate_entries[0]
            first_entry.created = duplicate.min_created
            first_entry.updated = duplicate.max_updated

            # Delete the other duplicate entries
            for entry in duplicate_entries[1:]:
                db.session.delete(entry)
                duplicates_info['deleted'] += 1

            duplicates_info['found'] += 1

    # Commit the changes to the database
    db.session.commit()

    return duplicates_info