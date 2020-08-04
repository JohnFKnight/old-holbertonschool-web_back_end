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
    # for i, field in enumerate(fields):
    message2 = (re.sub("(" + field + ".*;$)",
                       field + "=" + redaction + separator, message)
                for field in fields)
    print (*(msg for msg in message2))


    # substitutions = 
    # substrings = sorted(fields, key=len, reverse=True)
    # regex = re.compile('|'.join(map(re.escape, substrings)))
    # return regex.sub(lambda match: fields[match.group(0)], message) 
