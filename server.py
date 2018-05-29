# Cobalt take-home challenge recieved on May 29, 2018

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ROUTES
@app.route("/")
def hello():
    return "Hello World!"

# DEBUGGER STUFF ##########################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

app.run(host="0.0.0.0")
