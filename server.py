# Cobalt take-home challenge recieved on May 29, 2018

from flask import Flask, Response, render_template, request, jsonify, json
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# ROUTES
@app.route('/', methods=['GET'])
def index():
    """Show main page where user enters inputs & sees results"""

    return render_template("index.html")

@app.route('/parse.json', methods=['GET'])
def parse():
    """First endpoint, returns content that matches user input"""
    # First thing I did was make a GET request for the whole website
    # When that worked, I JSONified it
    # After getting the JSON response, I wittled it down to one tag

    tag_value = "h1"
    url = "http://www.cobalt.io"

    parameters = {"tag": tag_value}

    response = requests.get(url=url, params=parameters)

    # data = response.json()

    print(response.url)

    print (response.encoding)

    print(response.status_code)

    json_resp = json.dumps(response)

    # print(json_resp)

    print (json_resp.headers.get("content-type", "unknown"))

    return "testing route"

@app.route('/contains', methods=['GET'])
def contains():
    """Second endpoint, returns boolean expression"""

    return "containssss"

# DEBUGGER STUFF ##########################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

app.run(host="0.0.0.0")
