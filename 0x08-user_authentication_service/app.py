#!/usr/bin/env python3
""" Flask app
"""

from flask import Flask, jsonify, request, abort, make_response
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """ Simple app
    """
    # return jsonify({"message": "Bienvenue"})
    return {"message": "Bienvenue"}


@app.route("/users", methods=['POST'], strict_slashes=False)
def auth_users() -> str:
    """ Authenticate user
    """

    try:
        user = AUTH.register_user(request.form['email'],
                                  request.form['password'])
        return jsonify({"email": user.email,
                        "message": "user created"})
    except ValueError as err:
        # return make_response( jsonify(
        # {"message": "email already registered"}), 400)
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login() -> str:
    """ Validate login
    """

    data = request.form

    # try:
    valid = AUTH.valid_login(data['email'], data['password'])
    if valid:
        sess = AUTH.create_session(data['email'])
        resp = make_response({"email": data['email'],
                              "message": "logged in"})
        resp.set_cookie("session_id", sess)
        return resp
    else:
        abort(401)
    # except NoResultFound:
    #     abort(401)


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """Log out user by destroying user session id
    """
    form = request.form
    try:
        "session id in request cookie"
        sess = request.cookies.get('session_id')
        usr = AUTH.get_user_from_session_id(sess)
        AUTH.destroy_session(usr.id)
        return redirect('/')
    except NoResultFound:
        return 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
