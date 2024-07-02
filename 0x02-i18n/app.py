#!/usr/bin/env python3
"""This module contains a basic flask app that parametrizes a html template
with the correct translation based on the client supplied language"""

from datetime import datetime
import flask
from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import List, Optional, Union
import pytz

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config for this flask app: supported languages
    and timezone and locale"""
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)

def get_user() -> Union[dict, None, object]:
    """Returns a user dictionary"""
    id = request.args.get('login_as')
    if id is not None:
        id = int(id)
    if id not in users:
        return None
    return users[id]

@app.before_request
def before_request() -> None:
    """Finds a user using get_user and sets it as a global
    on flask.g.user"""
    user = get_user()
    if user is not None:
        flask.g.user = user


@app.route('/')
def home() -> str:
    """Route for the home page
    locale is passed to determine language
    and timezone is also determined and
    displayed to the user"""
    timez = get_timezone()
    fmt = '%B %d, %Y, %H:%M:%S %p'
    time_now = datetime.now(timez).strftime(fmt)
    timezone = _('current_time_is', current_time=time_now)
    selected_user = get_user()
    if selected_user is not None:
        status = _('logged_in_as', username=selected_user["name"])
    else:
        status = _('not_logged_in')
    return render_template('index.html',
                           locale=get_locale(), status=status, timezone=timezone)


def get_locale() -> Optional[str]:
    """Determines the best match of this application
    with the client requested languages"""
    # get the value of locale arg of the url
    requested_lang = request.args.get('locale')
    # check if its in the supported languages,
    # otherwise default to the previous behaviour
    if requested_lang in Config.LANGUAGES:
        return requested_lang
    return request.accept_languages.best_match(Config.LANGUAGES)


babel.init_app(app, locale_selector=get_locale)


def get_timezone() -> Optional[str]:
    """Determines the best match of this application
    with the client requested timezone"""
    # get the value of timezone arg of the url
    timez = request.args.get('timezone', 'UTC')
    try:
        return pytz.timezone(timez)
    except pytz.exceptions.UnknownTimeZoneError:
        return pytz.timezone('UTC')


babel.init_app(app, timezone_selector=get_timezone)


if __name__ == '__main__':
    """Run app in debug mode"""
    app.run()
