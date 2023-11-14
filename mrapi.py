from flask import Flask, request

app = Flask(__name__)

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
    app.run(debug=True)