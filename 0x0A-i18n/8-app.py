#!/usr/bin/env python3
""" Flask app
"""

from flask import Flask, render_template, g, request
from flask_babel import Babel
from pytz import timezone
import pytz
import datetime

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
    return render_template('8-index.html')


@babel.localeselector
def get_locale():
    """ Babel get locale decorator, function."""
    args = request.args
    if "locale" in args:
        if args["locale"] in Config.LANGUAGES:
            return args["locale"]
        elif g.user:
            return g.user.locale
        elif "locale" in request.headers:
            return request.headers.locale
        else:
            return request.accept_languages.best_match(
                app.config['BABEL_DEFAULT_LOCALE'])
    else:
        return request.accept_languages.best_match(
            app.config['BABEL_DEFAULT_LOCALE'])


@babel.timezoneselector
def get_timezone():
    """ Babel get timezone decorator, function."""
    args = request.args
    # timez = request.args.get('timezone')
    if "timezone" in args:
        print("URL TIMEZONE", tiemz )
        # if args.timezone in Config.LANGUAGES:
        try:
            tz = pytz.timezone(timez)
            return tz
        except pytz.UnknownTimeZoneError:
            return pytz.UTC
            # return args.timezone
            # raise pytz.UnknownTimeZoneError(
            #     "tzlocal() does not support non-zoneinfo timezones
            #     like %s. \n"
            #     "Please use a timezone in the form of Continent/City")
        # finally:
        #     return pytz.UTC
    if g.user.timezone:
        print("USER TIMEZONE")
        try:
            tz = pytz.timezone(g.user.timezone)
            return tz
        except pytz.UnknownTimeZoneError:
            return pytz.UTC
            # raise pytz.UnknownTimeZoneError(
            #     "tzlocal() does not support non-zoneinfo timezones
            #     like %s. \n"
            #     "Please use a timezone in the form of Continent/City")
    if "timezone" in request.headers:
        print("HEADERS TIMEZONE")
        try:
            tz = pytz.timezone(request.headers.timezone)
            return tz
        except pytz.UnknownTimeZoneError:
            return pytz.UTC
    else:
        print("DEFAULT TIME ZONE", BABEL_DEFAULT_TIMEZONE)
        return pytz.UTC


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
    return render_template('8-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
