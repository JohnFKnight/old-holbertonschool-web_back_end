#!/usr/bin/env python3
""" Flask app
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """ Simple app
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users/<email><password>', methods=['POST'], strict_slashes=False)
def users(email, password):
    from auth import Auth

    AUTH = Auth()

    try:
        user = auth.register_user(email, password)
        return jasonify({"email": "<registered email>",
                         "message": "user created"})
    except ValueError as err:
        return jasonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
