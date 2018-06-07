# Cobalt take-home challenge recieved on May 29, 2018

from flask import Flask, Response, render_template, request, jsonify, json
# I am using BeautifulSoup to parse the HTML from the website
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
    """First endpoint returns web content that matches user input"""

    # Get input from user
    tag_value = "h1"
    endpoint = "http://www.cobalt.io"

    # Key/value pair of what HTML tag the user entered
    parameters = {"tag": tag_value}

    # Make request for the HTML of the website user enters
    response = requests.get(url=endpoint, params=parameters)

    # We want the data from the object that is returned
    data = response.text

    # Here is where we use BeauitfulSoup to parse the data
    soup = BeautifulSoup(data, "html.parser")

    # Sift out just the tags we want
    tag_html = soup.find(tag_value)

    please_work = tag_html.get_text()

    return jsonify(please_work)

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
