#!/usr/bin/env python3
""" Flask app
"""

from flask import Flask, render_template, g, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Config class for app/babel config."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Base route."""
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """ Babel get locale decorator, function."""
    args = request.args
    if "locale" in args:
        if args["locale"] in Config.LANGUAGES:
            return args["locale"]
        else:
            return request.accept_languages.best_match(
                app.config['BABEL_DEFAULT_LOCALE'])
# LANGUAGES'])
    else:
        return request.accept_languages.best_match(
            app.config['BABEL_DEFAULT_LOCALE'])


def get_user():
    """ Get user id in request.
    Then return user from users mock d/b.
    """
    uid = request.args.get('login_as')
    if uid:
        uid = int(uid)
        if uid in users.keys():
            return users[uid]
        else:
            return None
    else:
        return uid


@app.before_request
def before_request():
    """ Run the following first always."""
    g.user = (get_user())
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
