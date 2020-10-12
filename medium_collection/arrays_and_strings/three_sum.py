"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Constraints:
    0 <= nums.length <= 3000
    -10**5 <= nums[i] <= 10**5

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

from typing import *
from collections import defaultdict


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    For this problem we can decompose the problem into a two_sum problem by moving one element to the other side
    of the equality and looking for pairs that add up to the new target for a each unique element in nums.

    We can optimize by constructing a dict containing unique integers as keys and the values being the count of
    the integer in nums.
    """

    if len(nums) < 3:
        return []

    hash = defaultdict(int)

    for n in nums:
        hash[n] += 1

    ret = []

    sorted_values = sorted(hash.keys())

    for idx, a in enumerate(sorted_values):
        hash[a] -= 1

        for idx_b in range(idx, len(sorted_values)):
            b = sorted_values[idx_b]

            if hash[b] < 1:
                continue

            hash[b] -= 1
            c = -a - b
            if c >= b and hash.get(c, 0) > 0:
                ret.append([a, b, c])

            hash[b] += 1

    return ret
