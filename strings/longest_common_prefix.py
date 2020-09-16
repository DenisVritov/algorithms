"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ''

Note:
    All given inputs are in lowercase letters a-z

Input: ["flower","flow","flight"]
Output: "fl"
"""

from typing import *


def longest_common_prefix(strs: List[str]) -> str:
    """
    Iterate over each word in the list and compare char by char.
    """

    if len(strs) == 0:
        return ''
    elif len(strs) == 1:
        return strs[0]

    idx = 0
    ret = []
    loop = True

    while loop:
        current_char = None
        for s in strs:
            if len(s) <= idx:
                loop = False
                break
            elif current_char is None:
                current_char = s[idx]
            elif current_char != s[idx]:
                loop = False
                break

        if loop:
            ret.append(current_char)
        idx += 1

    return ''.join(ret)
