#!/usr/bin/env python3
""" Flask app
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Base route."""
    return render_template(('0-index.html'),
                           title="Welcome to Holberton",
                           h1="Hello world"
                           )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
