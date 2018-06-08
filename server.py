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
    tag = request.args.get("tag")
    endpoint = request.args.get("endpoint")

    # Use the Python Requests library to request the html of the input website
    response = requests.get(url=endpoint)

    # We want the data from the Response object that is returned
    data = response.content

    # Create an instance of the BeautifulSoup class to parse our html
    soup = BeautifulSoup(data, "html.parser")

    # Sift out just the tags we want
    tag_html = soup.find_all(tag)

    # please_work = tag_html.get_text()

    # print please_work
    #
    python_set = set()

    innerHTML_dict = dict()

    for item in tag_html:
        python_set.add(item)
        innerHTML_dict['innerHTML'] = (item.get_text())

    # jsonify(python_set)

    print innerHTML_dict

    print python_set

    # Sift out just the tags we want
    # tag_html = soup.find(tag_value)
    #
    # please_work = tag_html.get_text()

@app.route('/contains', methods=['GET'])
def contains():
    """Second endpoint, checks data for user input, returns boolean expression"""

    return "containssss"

# DEBUGGER STUFF ##########################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

app.run(host="0.0.0.0")
