#!/usr/bin/env python3
""" Mask values of requested fields.
"""

import re
import logging
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError


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

    def get_logger():
        RedactingFormatter = __import__('filtered_logger').RedactingFormatter

        message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
        log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
        formatter = RedactingFormatter(fields=("email", "ssn", "password"))


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Mask field values with redaction.
    Return message with masked field values, delimited by separator.
    """

    for field in fields:
        message = (re.sub(field + "(.+?)" + separator,
                          field + "=" + redaction + separator, message))
    return message
