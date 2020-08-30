#!/usr/bin/env python3
""" Flask app
"""

from flask import Flask, render_template, g, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config class for app/babel config."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Base route."""
    return render_template('2-index.html')


@babel.localeselector
def get_locale() -> str:
    """ Babel get locale decorator, function."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# app.config['BABEL_DEFAULT_LOCALE'])

# @babel.timezoneselector
# def get_timezone():
#     """ Bable get timezone decorator, function."""
#     user = g.get('user', None)
#     if user is not None:
#         return user.timezone


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
