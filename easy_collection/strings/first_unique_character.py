"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Note:
- string contains only lowercase english letters

Input: "appleorchard"
Output: 3
"""

from typing import *
from collections import Counter


def first_unique_char(s: str) -> int:
    """
    Since the goal is to find a non-repeating character, at a minimum each character in the string
    must be visited, so the entire string must be iterated at least once.

    Solution 1: Iterate over the string and create a dict of the characters and their indices. Then iterate over
    dict for characters with only 1 index, return the smallest index or -1 if no characters with only 1 index.

    Solution 2: Similar to solution 1 but use the built-in Counter class from collections. Get a count of all
    characters in the string then iterate over the string and check whether the count of that character is 1.
    This is faster since Counter is optimized for counting but we can implement ourselves by iterating over the
    string and creating our own dict.
    """

    char_counts = Counter(s)

    for idx, char in enumerate(s):
        if char_counts[char] == 1:
            return idx

    return -1