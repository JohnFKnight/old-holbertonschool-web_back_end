#!/usr/bin/env python3
""" Sample code. Correct and annotate."""

from typing import Tuple, List, Union, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Sample code. Correct and annotate."""
    john: List = [
        item for item in list(lst)
        for i in range(factor)
    ]
    # list(john)
    return (john)


array = [12, 72, 91]
print(array)

zoom_2x = zoom_array(tuple(array))
print(zoom_2x)

zoom_3x = zoom_array(tuple(array), 3)
print(zoom_3x)
