#!/usr/bin/env python3
"""
a type-annotated function that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    multiplying a float by multiplier
    """
    def multiplier_function(value: float) -> float:
        """
        multiplying a float by multiplier
        """
        return value * multiplier
    return multiplier_function
