#!/usr/bin/env python3
"""This module contains a basic flask app that parametrizes a html template
with the correct translation based on the client supplied language"""

import flask
from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import List, Optional, Union

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
    locale is passed to determine language"""
    selected_user = get_user()
    if selected_user is not None:
        status = _('logged_in_as', username=selected_user["name"])
    else:
        status = _('not_logged_in')
    return render_template('6-index.html',
                           locale=get_locale(), status=status)


def get_locale() -> Optional[str]:
    """Determines the best match of this application
    with the client requested languages"""
    # get the value of locale arg of the url
    requested_lang = request.args.get('locale')
    # check if its in the supported languages,
    # otherwise default to the previous behaviour
    if requested_lang in Config.LANGUAGES:
        return requested_lang
    try:
        user = flask.g.user
        if user is not None:
            user_locale = user["locale"]
            if user_locale in Config.LANGUAGES:
                return user_locale
    except AttributeError:
        pass

    best_locale = request.accept_languages.best_match(Config.LANGUAGES)
    if best_locale:
        return best_locale

    return Config.BABEL_DEFAULT_LOCALE


babel.init_app(app, locale_selector=get_locale)


if __name__ == '__main__':
    """Run app"""
    app.run()
