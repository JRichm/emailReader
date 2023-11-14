"""    Script to (re)start database     """

import os
import model
import mrapi

# delete db to start fresh
os.system("dropdb -U jamcam -e mailReader")
os.system("createdb -U jamcam mailReader")

# create tables from model.py
with mrapi.app.app_context():
    model.connect_to_db(mrapi.app)
    model.db.create_all()

