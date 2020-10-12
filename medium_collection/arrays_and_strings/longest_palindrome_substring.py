"""
Given a string s, return the longest palindromic substring in s.

Constraints:
    1 <= s.length <= 1000
    s consist of only digits and English letters (lower-case and/or upper-case)
"""

from typing import *


def longest_palindrome_substring(s: str) -> str:
    """
    This solution requires a dynamic programming approach to grow palindromes.

    We can consider each starting centerpoint and grow the palindrome until it is no longer a palindrome. Return
    the longest one found.
    """

    start = 0
    length = 1

    for i in range(len(s)):

        # Consider even length palindromes
        p1 = i
        p2 = i+1

        while p1 >= 0 and p2 < len(s):
            if s[p1] == s[p2]:
                sub_length = p2 - p1 + 1
                if sub_length > length:
                    length = sub_length
                    start = p1
                p1 -= 1
                p2 += 1
            else:
                break

        # Consider odd length palindromes
        p1 = i-1
        p2 = i+1

        while p1 >= 0 and p2 < len(s):
            if s[p1] == s[p2]:
                sub_length = p2 - p1 + 1
                if sub_length > length:
                    length = sub_length
                    start = p1
                p1 -= 1
                p2 += 1
            else:
                break

    return s[start: start+length]
