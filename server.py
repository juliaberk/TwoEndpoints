# Cobalt take-home challenge recieved on May 29, 2018

from flask import Flask, render_template, request, jsonify

import requests

app = Flask(__name__)

# ROUTES
@app.route('/', methods=['GET'])
def index():
    """Show main page where user enters inputs & sees results"""

    return render_template("index.html")

@app.route('/parse.json', methods=['GET'])
def parse():
    """First endpoint, returns what tag the user enters"""

    url = "http://www.cobalt.io"

    # querystring = {}

    response = requests.request("GET", url)

    tag_result = response.json()

    return tag_result

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
