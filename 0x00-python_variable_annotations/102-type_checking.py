#!/usr/bin/env python3
""" Sample code. Correct and annotate."""


def zoom_array(lst: Tuple, fctr: int = 2) -> Tuple[float, int]:
    john: Tuple = [item for item in lst for i in range(fctr)]
    return john


array = [12, 72, 91]
print(array)

zoom_2x = zoom_array(array)
print(zoom_2x)

zoom_3x = zoom_array(array, 3.0)
print(zoom_3x)
