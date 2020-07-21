#!/usr/bin/env python3
"""Return a tuple from string and (int or float)."""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """Return tuple (k, v^2) of k:str and v:int or float."""

    # a: float = v

    return (k, v * v)
