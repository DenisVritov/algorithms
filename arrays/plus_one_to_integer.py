"""
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element
in the array contains a single digit. The integer does not contain any leading zero, except the number 0 itself.

0 <= digits[i] <= 9

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
"""

from typing import *


def plus_one(digits: List[int]) -> List[int]:
    """
    The idea is is to iterate through the list backwards and increment the digit at each location until the
    incremented digit is less than 10. In other words, starting with the last element of the list, increment
    by 1 and if the value is >9 set to 0, move to the next element in the list (going backwards) and repeat.
    """

    idx = -1

    while idx >= -1*len(digits):
        if digits[idx] < 9:
            digits[idx] += 1
            return digits
        else:
            digits[idx] = 0
            idx -= 1

    return [1] + digits