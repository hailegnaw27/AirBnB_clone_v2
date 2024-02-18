#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!" when accessing the root route.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays "HBNB" when accessing the /hbnb route.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays "C " followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Displays "Python " followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Displays "<n> is a number" only if n is an integer.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page with the value of n inside an H1 tag.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Displays an HTML page with the value of n and whether it's even or odd.
    """
    return render_template('6-number_odd_or_even.html', n=n, odd_or_even='odd' if n % 2 != 0 else 'even')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
