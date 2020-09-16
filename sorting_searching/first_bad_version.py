"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest
version of your product fails the quality check. Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all
the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a
function to find the first bad version. You should minimize the number of calls to the API.

Example:
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""

from typing import *


def isBadVersion(version):
    pass


def first_bad_version(n: int) -> int:
    """
    In order to find the first bad version with the minimum number of calls, we can implement a binary search.
    The algorithm would be to check the middle version and if it's bad, recurse on the left side. If it's good,
    recurse on the right side.
    """

    def bs_version(start, end):
        h_dist = int((end-start)/2)
        half = start + h_dist
        if h_dist == 0:
            if isBadVersion(half):
                return half
            else:
                return half+1
        if isBadVersion(half):
            return bs_version(start, half)
        else:
            return bs_version(half, end)

    return bs_version(1, n)
