#!/usr/bin/env python3
""" Route module for the API """
from flask import Flask, request, render_template
from os import getenv

app = Flask(__name__, static_url_path='')


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ GET /
    Return:
      - 0-index.html
    """
    return render_template('0-index.html')
