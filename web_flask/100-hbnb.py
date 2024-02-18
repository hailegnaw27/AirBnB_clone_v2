#!/usr/bin/python3
"""This script starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb: This route leads to the HBnB home page.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """This function displays the main HBnB filters HTML page.

    It retrieves states, amenities, and places from the storage and passes them to the template.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """This function removes the current SQLAlchemy session.

    It ensures proper termination and cleanup of resources.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
