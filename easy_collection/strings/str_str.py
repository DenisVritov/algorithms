"""
Implement str_str().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Notes:
    - For the purpose of this problem, return 0 when needle is an empty string.
    - haystack and needle consist only of lowercase English characters.

Input: haystack = "hello", needle = "ll"
Output: 2
"""

from typing import *


def str_str(haystack: str, needle: str) -> int:
    """
    This is essentially a "find first occurrence of substring" problem.

    Base cases:
        - If needle is empty string return 0
        - If len(needle) > len(haystack) return -1

    Use a sliding window of length len(needle) and compare the substrings. This has a worst-case time of
    O((H-N)N).

    Optimization: Rolling hash or KMP algorithm.
    """

    if len(needle) == 0:
        return 0
    elif len(needle) > len(haystack):
        return -1

    n = len(needle)
    i = 0

    while i <= len(haystack) - n:
        if haystack[i:i+n] == needle:
            return i

    return -1
