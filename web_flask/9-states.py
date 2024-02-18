#!/usr/bin/python3
"""This script starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states: This route leads to an HTML page with a list of all State objects.
    /states/<id>: This route displays the HTML page for a specific state with the given <id>.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """This function displays an HTML page with a list of all States.

    The States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """This function displays an HTML page with information about a specific state.

    If the state with the given <id> exists, it is displayed on the page.
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """This function removes the current SQLAlchemy session.

    It ensures proper termination and cleanup of resources.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
