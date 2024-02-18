#!/usr/bin/python3
"""
    /cities_by_states: This route displays an HTML page with a list of all states and their corresponding cities.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """This function renders an HTML page that showcases a comprehensive list of states and their related cities.

    The states and cities are sorted alphabetically for better readability.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """This function closes the current SQLAlchemy session gracefully.

    It ensures proper termination and cleanup of resources.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
