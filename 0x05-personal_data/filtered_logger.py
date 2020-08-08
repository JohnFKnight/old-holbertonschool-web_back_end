#!/usr/bin/env python3
""" Mask values of requested fields.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Mask field values with redaction.
    Return message with masked field values, delimited by separator.
    """

    for field in fields:
        message = re.sub(field + "(.+?);",
                         field + "=" + redaction + separator, str(message))
    return message
