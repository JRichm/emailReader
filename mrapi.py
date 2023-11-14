from flask import Flask, request
from model import connect_to_db

app = Flask(__name__)
app.secret_key = 'mail'


@app.route("/")
def index():

    text = 1000

    return {
        "somejson" : {
            "key": text
        }
    }

# add new link to db
@app.route('/addLink', methods=["POST"])
def add_link():
    if request.method == 'POST':
        data = request.json  # Access the JSON data sent in the POST request
        print('post request data:', data)
    else:
        print('other request')
    return {"response": "success"}

# save application details

# save response details

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)