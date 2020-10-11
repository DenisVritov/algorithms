"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Input: s = "anagram", t = "nagaram"
Output: True
"""

from typing import *


def is_anagram(s: str, t: str) -> bool:
    """
    For an two strings to be anagrams of each other they must contain exactly the same number
    of all characters.

    Base case check: lengths are equal, otherwise automatically false.

    Solution 1: Iterate over one string and create dict of char and counts. Then iterate over the
    other string and decrement counts. End result should be all values are 0 for anagrams.

    Solution 2: Create count dicts for both strings and compare them.

    Using the built-in Counter class makes solution 2 faster than solution 1 because of optimizations
    in the counter class.
    """

    if len(s) != len(t):
        return False

    return Counter(s) == Counter(t)
