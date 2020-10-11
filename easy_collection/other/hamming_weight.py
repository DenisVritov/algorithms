"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has
(also known as the Hamming weight).

Note:

    Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be
    given as a signed integer type. It should not affect your implementation, as the integer's internal binary
    representation is the same, whether it is signed or unsigned.

    In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in the example
    above, the input represents the signed integer. -3.

Input: n = 11111111111111111111111111111101
Output: 31
"""

from typing import *


def hamming_weight(n: int) -> int:
    """
    This is fairly straightforward and is simply converting the integer to the binary representation and taking
    the sum.
    """

    return bin(n).count('1')
