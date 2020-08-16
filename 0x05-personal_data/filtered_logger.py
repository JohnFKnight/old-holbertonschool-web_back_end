#!/usr/bin/env python3
""" Mask values of requested fields.
"""

import re
import logging
from typing import List


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
    # RedactingFormatter = RedactingFormatter()

    log = logging.getLogger("user_data")
    log.propogate = False
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    handler = logging.StreamHandler()
    handler.setLevel(level=logging.INFO)
    handler.setFormatter(formatter)
    log.addHandler(handler)
    return log
