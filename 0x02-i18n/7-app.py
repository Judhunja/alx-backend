#!/usr/bin/env python3
"""This module contains a basic flask app that parametrizes a html template
with the correct translation based on the client supplied language"""

from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import List, Optional

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config for this flask app: supported languages
    and timezone and locale"""
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)


@app.route('/')
def home() -> str:
    """Route for the home page
    locale is passed to determine language"""
    return render_template('4-index.html',
                           locale=get_locale())


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
    timez = request.args.get('timezone')
    # check if its in the supported timezone,
    # otherwise default to the previous behaviour
    if timez in Config.BABEL_DEFAULT_TIMEZONE:
        return timez
    return 'UTC'



if __name__ == '__main__':
    """Run app in debug mode"""
    app.run()
