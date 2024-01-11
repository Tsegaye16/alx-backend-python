#!/usr/bin/env python3
"""
a type-annotated function which takes a list  of floats as
argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """add-up the element of list and return them as float"""
    if input_list is None:
        return 0
    else:
        return sum(input_list)
