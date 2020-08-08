#!/usr/bin/env python"
""" Mask values of requested fields.
"""

from sys import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Mask field values with redaction.
    Return message with masked field values, delimited by separator.
    """

    # msg1 = message.split(";")
    # del msg1[len(msg1) - 1]
    # dmsg = {k: v for k, v in (x.split('=') for x in msg1)}

    for field in fields:
        message2 = s\field.+;$\field"=xxx"\g
    #     dmsg[field] = redaction

    # message2 = []
    # message2.append("")

    # for k, v in dmsg.items():
    #     message2[0] += k + "=" + v + ";"

    return message2[0]