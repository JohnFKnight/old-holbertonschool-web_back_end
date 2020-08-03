#!/usr/bin/env python"
""" Mask values of requested fields.
"""

from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str):
    """
    Mask field values with redaction.
    Return message with masked field values, delimited by separator.
    """

    # Convert message to dict (split on =)
    # for field in fields: dmsg[field] = redaction
    # Convert dmsg back to list: message dilimited by separator
    # Return message

    msg1 = message.split(";")
    del msg1[len(msg1) - 1]
    dmsg = {k: v for k, v in (x.split('=') for x in msg1)}

    for field in fields:
        dmsg[field] = redaction

    message2 = []
    message2.append("")

    for k, v in dmsg.items():
        # message2.append(k + "=" + v)
        message2[0] += k + "=" + v + ";"

    # message2.replace(',', ';')
    return message2[0]
