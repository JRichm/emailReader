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