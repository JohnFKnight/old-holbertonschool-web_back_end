#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)
session = auth.create_session(email)

print(auth.destroy_session(1))


# print(auth.get_user_from_session_id(None))
# print(auth.get_user_from_session_id(""))


# print(auth.create_session("unknown@email.com"))
