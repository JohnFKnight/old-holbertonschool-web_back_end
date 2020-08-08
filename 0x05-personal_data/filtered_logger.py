#!/usr/bin/env python"
""" Mask values of requested fields.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Mask field values with redaction.
    Return message with masked field values, delimited by separator.
    """

    for i, field in enumerate(fields):
        message = (re.sub(field + "(.+?);",
                          field + "=" + redaction + separator, message))
        # for field in fields)

    return message
