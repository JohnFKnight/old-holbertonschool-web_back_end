#!/usr/bin/env python3
""" Mask values of requested fields.
"""

import re
import logging
from typing import List, Generic, TypeVar
from os import environ as e
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Init constructor
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filter, format record.
        tried: return self.FORMAT, x (filter_datum result)
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Mask field values with redaction.
    Return message with masked field values, delimited by separator.
    """

    for field in fields:
        message = (re.sub(field + "(.+?)" + separator,
                          field + "=" + redaction + separator, message))
    return message


def get_logger() -> logging.Logger:
    """ Create log record
    """

    log = logging.getLogger("user_data")
    log.propagate = False
    log.setLevel(logging.INFO)
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    handler = logging.StreamHandler()
    # handler.setLevel(level=logging.INFO)
    handler.setFormatter(formatter)
    log.addHandler(handler)
    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Create database connector object.
    """
    uname = e['PERSONAL_DATA_DB_USERNAME']
    pwd = e['PERSONAL_DATA_DB_PASSWORD']
    host = e['PERSONAL_DATA_DB_HOST']
    db = e['PERSONAL_DATA_DB_NAME']

    return mysql.connector.connect(database=db,
                                   host=host, user=uname, password=pwd)


def main():
    """ Main. Get and display all users with
    redacted fields.
    """
    db = get_db()
    log = get_logger()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    names = []
    for j, row in enumerate(cursor):
        message = ""
        for i, col in enumerate(cursor.description):
            message += "{}={}; ".format(col[0], row[i])

        # log.info(message)  # Wills way! Much better! READ THE DOC!
    log_record = logging.LogRecord("user_data", logging.INFO,
                                   None, None, message, None, None)
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    for k in range(j + 1):
        print(formatter.format(log_record))
    cursor.close()
    db.close()


def hash_password(pwd: str): -> bytes:
    """ Create salt-ed, hash-ed pwd
    """
    import bcrypt

    # salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes(pwd, 'utf-8'), bcrypt.gensalt())


if __name__ == "__main__":
    main()
