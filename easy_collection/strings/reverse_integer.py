"""
Given a 32-bit signed integer, reverse digits of an integer.

Input: 123
Output: 321
"""

from typing import *


def reverse_integer(x: int) -> int:
    """
    Convert to string then reverse, keeping track of the sign of the value
    """

    negative = -1 if x < 0 else 1
    reversed_int = negative * int(str(abs(x))[::-1])
    if reversed_int > 2147483647 or reversed_int < -2147483648:
        return 0
    else:
        return reversed_int
