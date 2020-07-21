#!/usr/bin/env python3
"""Make sample code annoted."""


from typing import List, Iterable, Sequence, Tuple, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, type(None)]:
    """Make sample code annoted Duck typing."""
    if lst:
        return lst[0]
    else:
        return None
