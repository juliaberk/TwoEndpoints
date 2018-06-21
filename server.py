# Cobalt take-home challenge recieved on May 29, 2018

from flask import Flask, Response, render_template, request, jsonify, json
# I am using BeautifulSoup to parse the HTML from the website
from bs4 import BeautifulSoup
import requests
# import collections

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
    endpoint = "http://" + request.args.get("endpoint")
    # Use the Python Requests library to request the html of the input website
    response = requests.get(url=endpoint)

    # We want the content from the Response object that is returned
    # Create an instance of the BeautifulSoup class to parse out html
    soup = BeautifulSoup(response.content, "html.parser")

    # Sift out just the instances of the tag we want
    tag_html = soup.find_all(tag)

    # Here is what we will ultimately output as JSON:
    output = {tag : []}

    # You'll notice that the tag has quotes around it, for
    # example, "h1" instead of h1 (h1 without quotes is in the sample input from the prompt)
    # From my research, JSON keys should be surrounded by quotes
    #
    # Source:
    # https://stackoverflow.com/questions/949449/json-spec-does-the-key-have-to-be-surrounded-with-quotes/949476#949476
    #
    # https://news.ycombinator.com/item?id=2032729
    #

    # This list will be the value in the dictionary of results
    # Example: h1: [result list]
    result_list = []

    # For Python, I had to make a workaround for the output.
    # Each time the loop runs, a blank copy of this dictionary is made
    # for the results to be appended to.
    #
    # Source:
    # https://stackoverflow.com/questions/35830612/how-to-create-a-new-dictionary-in-for-loop
    #

    dict_template = {}

    for item in tag_html:
        # Make a copy of the empty dictionary
        new = dict_template.copy()
        new['innerText'] = (item.get_text())
        content_list = item.contents
        new['innerHtml'] = " ".join(str(content_list))
        # Add this dict to the list of dictionaries:
        result_list.append(new)

    # Once you have list of results, add it to key/value pair of tag
    output[tag] = result_list

    return jsonify(output)

@app.route('/contains.json', methods=['GET'])
def contains():
    """Second endpoint, checks data for user input, returns boolean expression"""
    # Get input from user
    tag = request.args.get("tag")
    endpoint = "http://" + request.args.get("endpoint")
    text = (request.args.get("text"))

    # Make the GET request to the website the user entered
    response = requests.get(url=endpoint)

    # This is where the boolean value will be stored
    output = {'exists' : ""}

    soup = BeautifulSoup(response.content, "html.parser")


    if text in soup.find_all(string=text):
        output['exists'] = "true"
    else:
        output['exists'] = "false"

    return jsonify(output)

# DEBUGGER STUFF ##########################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

app.run(host="0.0.0.0")
