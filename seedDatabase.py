"""    Script to (re)start database     """

import os
import json
import mrapi
from model import connect_to_db, db, Job_Board


# Load job_boards information from JSON
def load_job_boards():
    with open("./data/job_boards.json", "r") as f:
        data = json.load(f)
        return data["jobBoards"]


# delete db to start fresh
os.system("dropdb -U jamcam -e mailReader")
os.system("createdb -U jamcam mailReader")


# create tables from model.py
with mrapi.app.app_context():
    connect_to_db(mrapi.app)
    db.create_all()

    # Load job board data from JSON file
    job_boards_data = load_job_boards()

    # Add job boards to the database
    for board_data in job_boards_data:
        board_name, board_info = list(board_data.items())[0]
        new_board = Job_Board(board_title=board_info["name"], board_link=board_info["url"])
        db.session.add(new_board)

    # Commit the changes to the database
    db.session.commit()

    print("Job boards added to the database.")