#!/usr/bin/env python3
"""Make sample code annoted."""


from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:

    """Make sample code annoted."""
    return [(i, len(i)) for i in lst]
