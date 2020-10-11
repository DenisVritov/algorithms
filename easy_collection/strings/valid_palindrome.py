"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note:
    For the purpose of this problem, define empty string as valid palindrome.

Input: "A man, a plan, a canal: Panama"
Output: true
"""

from typing import *


def is_palindrome(s: str) -> bool:
    """
    Since only alphanumeric characters are used and cases are ignored, one approach is to 'clean' the string.
    However, this can be done on the fly.

    Iterate over the string from both ends, cleaning/skipping characters as needed, and comparing. If there is a
    mismatch, return False. If the pointers cross over then return True.
    """

    n = len(s)
    if n == 0:
        return True

    p1 = 0
    p2 = n-1

    while p1 < p2:
        if not s[p1].isalnum():
            p1 += 1
        elif not s[p2].isalnum():
            p2 -= 1
        elif s[p1].lower() != s[p2].lower():
            return False
        else:
            p1 += 1
            p2 -= 1

    return True