#!/usr/bin/env python3
"""
Flask application to serve a basic HTML page.

This script initializes a Flask application and defines a route
to render an HTML template.
"""

from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)


@app.route('/')
def home():
    """
    Home route that renders the '0-index.html' template.

    Returns:
        str: Rendered HTML content of the '0-index.html' template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    """
    Run the Flask application in debug mode when the script is executed.
    """
    app.run(debug=True)
