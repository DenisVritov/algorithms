"""
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, do this by modifying the input array in-place with O(1) extra memory.
Assume all the characters consist of printable ascii characters.

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

from typing import *


def reverse_string(s: List[str]) -> None:
    """
    Given list of length n, swap the ith and (n-1-i)th elements.
    """

    if len(s) == 0:
        return

    n = len(s)
    for i in range(int(n/2)):
        s[i], s[n-1-i] = s[n-1-i], s[i]
