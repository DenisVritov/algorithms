"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
    0 ≤ x, y < 2**31

Input: x = 1, y = 4
Output: 2
"""

from typing import *


def hamming_weight(n: int) -> int:
    return bin(n).count('1')


def hamming_distance(x: int, y:int) -> int:
    """
    This can be done by taking the hamming_weight of the XOR of the two numbers.
    """

    return hamming_weight(x^y)
