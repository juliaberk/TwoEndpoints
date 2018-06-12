# Cobalt take-home challenge recieved on May 29, 2018

from flask import Flask, Response, render_template, request, jsonify, json
# I am using BeautifulSoup to parse the HTML from the website
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# CLASSES
class ReturnedTags:
    """ The content of the given tag on a page """
    innerHTML = None
    outerHTML = None

# ROUTES
@app.route('/', methods=['GET'])
def index():
    """Show main page where user enters inputs & sees results"""

    return render_template("index.html")

@app.route('/parse.json', methods=['GET'])
def parse():
    """First endpoint returns web content that matches user input"""

    # Get input from user
    # tag = request.args.get("tag")
    # endpoint = request.args.get("endpoint")
    tag = "h1"
    url = "http://www.cobalt.io"

    # Use the Python Requests library to request the html of the input website
    response = requests.get(url="http://www.cobalt.io")

    # We want the content from the Response object that is returned
    # Create an instance of the BeautifulSoup class to parse out html
    soup = BeautifulSoup(response.content, "html.parser")

    # Sift out just the tags we want
    tag_html = soup.find_all(tag)

    # print list(tag_html)
    for item in tag_html:
        print item.get_text()
        print item

    return "ok cool"

@app.route('/contains.json', methods=['GET'])
def contains():
    """Second endpoint, checks data for user input, returns boolean expression"""
    # Get input from user
    tag = request.args.get("tag")
    endpoint = request.args.get("endpoint")
    text = request.args.get("text")

    response = requests.get(url="http://www.cobalt.io")



    return "This route works yay"

# DEBUGGER STUFF ##########################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

app.run(host="0.0.0.0")
