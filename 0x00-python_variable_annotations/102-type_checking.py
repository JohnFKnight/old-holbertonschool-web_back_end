#!/usr/bin/env python3
""" Sample code. Correct and annotate."""

from typing import Tuple, List, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    john: Tuple[...] = (
        item for item in lst
        for i in range(factor)
    )
    return (john)


array = [12, 72, 91]
print(array)

zoom_2x = zoom_array(array)
print(zoom_2x)

zoom_3x = zoom_array(array, 3.0)
print(zoom_3x)
