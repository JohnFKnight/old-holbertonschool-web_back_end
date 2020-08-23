#!/usr/bin/env python3
""" Flask app
"""

from flask import Flask, jsonify, request, make_response
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """ Simple app
    """
    # return jsonify({"message": "Bienvenue"})
    return {"message": "Bienvenue"}


@app.route("/users", methods=['POST'], strict_slashes=False)
def auth_users() -> str:
    """ Authenticate user
    """

    try:
        user = AUTH.register_user(
            request.form['email'], request.form['password'])
        return {"email": user.email,
                "message": "user created"}
    except ValueError as err:
        # return make_response( jsonify(
        # {"message": "email already registered"}), 400)
        return {"message": "email already registered"}, 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
