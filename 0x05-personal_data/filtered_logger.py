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

    message2: str = ""
    for i, field in enumerate(fields):
        message2 = re.sub(field + "(.*);$",
                          field + "=" + redaction + separator, message)
    return message2
