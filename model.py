"""  Model for emailReader Database """

from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

""" ###     Job Board     ### """
class Job_Board(db.Model):
    board_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    board_title = db.Column(db.String(), nullable=False)
    board_link = db.Column(db.String(), nullable=False)

""" ###        Job        ### """
class Job(db.Model):
    job_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    job_title = db.Column(db.String(), nullable=True)
    job_description = db.Column(db.String(), nullable=True)
    job_salary = db.Column(db.String(), nullable=True)
    job_board = db.Column(db.Integer(), nullable=True)
    board_job_id = db.Column(db.Integer(), nullable=True)
    applied = db.Column(db.Boolean())
    responded = db.Column(db.Boolean())

""" ###     Job Links     ### """
class Job_Links(db.Model):
    link_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    job_id = db.Column(db.String(), nullable=False)
    link = db.Column(db.String(), nullable=False)

