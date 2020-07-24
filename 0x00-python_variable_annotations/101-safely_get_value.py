#!/usr/bin/env python3
"""Make sample code annoted."""

from typing import Any, Union, Mapping, TypeVar


T = TypeVar('T', bound=Any)


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union['T', None] = None) -> Union[Any, 'T']:
    """Make sample code annoted Duck typing."""
    if key in dct:
        return dct[key]
    else:
        return default
