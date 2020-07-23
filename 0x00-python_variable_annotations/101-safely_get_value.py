#!/usr/bin/env python3
"""Make sample code annoted."""


from typing import Any, Union, Mapping, TypeVar


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar('V'), type(None)]) -> Union[Any, TypeVar('V')]:
    """Make sample code annoted Duck typing."""
    if key in dct:
        return dct[key]
    else:
        return default
