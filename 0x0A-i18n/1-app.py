#!/usr/bin/env python3
""" Flask app
"""

from flask import Flask, render_template, g, request
from flask.ext.babel import Babel
# from flask_babel import Babel

app = Flask(__name__)
app.config.from_object('Config')
babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Base route."""
    return render_template('1-index.html')


class Config(object):
    """ Config class for app/babel config."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
