#!/usr/bin/env python3
"""Make sample code annoted."""


from typing import Any, Union, Mapping


def safely_get_value(dct: [Mapping[key: Any, Union[None]]]) -> Union[Any]:
    """Make sample code annoted Duck typing."""
    if key in dct:
        return dct[key]
    else:
        return default