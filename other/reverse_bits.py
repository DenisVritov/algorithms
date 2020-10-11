"""
Reverse bits of a given 32 bits unsigned integer.

Input: n = 00000010100101000001111010011100
Output: 964176192 (00111001011110000010100101000000)
"""

from typing import *


def reverse_bits(n: int) -> int:
    """
    This can be done quite simply by converting the integer to binary representation string, reversing the string
    then converting the binary representation back to integer.
    """

    return int(format(n, '032b')[::-1], 2)
