"""
Given an integer, write a function to determine if it is a power of three.

Input: 27
Output: True
"""

from typing import *


def power_of_three(n: int) -> bool:
    """
    In order to determine whether an integer is a power of three we must make sure that the integer is not divisible
    by any other prime other than 3.

    A simple way would be to simply take the log base 3 of the integer and return True if the result is itself an
    integer. However, I feel like this answer defeats the spirit of this question so I will do this another way.

    Brute force method would be to repeatedly multiply 3 by itself until the result is either the input or is larger
    than the input. Or, in the reverse direction repeatedly divide the input by 3 until the result is either 1 (or 3)
    or not an integer.

    A slightly better way would be to repeatedly square 3 until the next squaring would be larger than the input. Then
    divide the input by the largest power of 3 found so far and check if the result is itself a power of three.

    An even better way is to do the above method and pass the result of the division back into this function
    recursively.
    """

    if n < 3:
        if n == 1:
            return True
        # A negative integer cannot be a power of 3
        return False
    elif n == 3:
        return True

    a = 3
    while a**2 < n:
        a = a**2

    if n % a != 0:
        return False
    else:
        return power_of_three(n/a)
