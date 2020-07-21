#!/usr/bin/env python3

def zoom_array(lst: Tuple, fctr: int = 2) -> Tuple:
    john: Tuple = [item for item in lst, for i in range(fctr)]
    return john


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
