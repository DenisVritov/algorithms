"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Constraints:
    1 <= strs.length <= 10**4
    0 <= strs[i].length <= 100
    strs[i] consists of lower-case English letters.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from typing import *
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    A simple way to do this would be to map each string into some sort of unique hash and store the string
    in a dict under its hash. The return value would then simple be the values in the dict grouped by their keys.

    For this problem, the hash will be the string in sorted order.
    """

    def hash_str(s: str) -> str:
        return ''.join(sorted(s))

    hashed_strings = defaultdict(list)

    for s in strs:
        hashed_strings[hash_str(s)].append(s)

    ret = []

    for key, vals in hashed_strings.items():
        ret.append(vals)

    return ret
