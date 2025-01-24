#!/usr/bin/env python3
from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """
    Configuration for Flask application with Babel extension.

    Attributes:
        LANGUAGES (list): List of supported languages for the app.
        BABEL_DEFAULT_LOCALE (str): Default language for the app (English).
        BABEL_DEFAULT_TIMEZONE (str): Default timezone (UTC).
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Initialize Flask application
app = Flask(__name__)
# Load configuration from Config class
app.config.from_object(Config)

# Initialize Babel with the app
babel = Babel(app)

@app.route('/')
def home():
    """
    Home route that serves a simple "Hello world" message.
    Returns:
        str: HTML string with a header message.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
