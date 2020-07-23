#!/usr/bin/env python3
"""Return a function that multiplies a float from multiplier parameter."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function float x multiplier."""

    def mult(x: float) -> float:
        return x * multiplier

    return (mult)
