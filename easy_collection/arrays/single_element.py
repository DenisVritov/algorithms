"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Input: [4,1,2,1,2]
Output: 4
"""

from typing import *
from functools import reduce


def find_single(nums: List[int]) -> int:
    """
    Since we are guaranteed a non-empty array and that exactly 1 element will appear only once,
    we can skip some base cases: check for empty array, check for even length array.

    Since we know exactly 1 element is not repeated and a bit-wise XOR of the same number
    yields 0 then if we perform a bit-wise XOR on every element, at the end the only bits
    left should be the bits from the single number.
    """

    return reduce(lambda x, y: x ^ y, nums)
