#!/usr/bin/env python3
""" Flask app
"""

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """ Simple app
    """
    # return jsonify({"message": "Bienvenue"})
    return {"message": "Bienvenue"}


# @app.route('/users/<email>/<password>',
#            methods=['GET', 'POST'], strict_slashes=False)
# def users(*, email, password):
# @app.route("/users", methods=['POST'], strict_slashes=False)
# def users() -> str:
#     """ Authenticate user
#     """
    # from auth import Auth

    # AUTH = Auth()

#     try:
#         user = AUTH.register_user(
#             request.form['email'], request.form['password'])
#         return {"email": user.email,
#                 "message": "user created"}
#     except ValueError as err:
#         # return make_response( jsonify(
#         # {"message": "email already registered"}), 400)
#         return {"message": "email already registered"}, 400

@app.route("/users", methods=['POST'], strict_slashes=False)
def register_route() -> str:
    """ get the register route
    """

    from auth import Auth

    AUTH = Auth()


    body = request.form

    try:
        user = AUTH.register_user(body['email'], body['password'])
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
