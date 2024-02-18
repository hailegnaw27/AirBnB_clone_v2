#!/usr/bin/python3
"""
This module starts a Flask web application.
"""

from flask import Flask

app = Flask(__name__)
app.config["ENV"] = "development"

@app.route('/', strict_slashes=False)
def hello():
    """
    This function handles the root route and returns 'Hello HBNB!'
    """
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
