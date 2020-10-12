"""
Given a string s, find the length of the longest substring without repeating characters.

Constraints:
    0 <= s.length <= 5 * 10**4
    s consists of English letters, digits, symbols and spaces

Input: s = "pwwkew"
Output: 3
"""

from typing import *


def longest_substring_no_repeats(s: str) -> int:
    """
    In order to do find the longest substring we can use a growing/shrinking window. The idea would be to start with
    a window of size 0 and perform the following:
        - If the next element does not exist in the window, grow the window by 1
        - If the next element already exists in the window, shrink the window from the start until the next element is
          no longer in the window

    While this is happening, keep track of the largest window seen.

    Once all elements of the string have been considered, return largest window seen.
    """

    max_window_size = 0
    window_size = 0
    window_start = 0

    for c in s:
        i = s.find(c, window_start, window_start+window_size)
        if i >= 0:
            window_size -= i - window_start
            window_start = i + 1
        else:
            window_size += 1
            max_window_size = max(max_window_size, window_size)

    return max_window_size
