"""
Given an array of integers nums and and integer target, return the indices of the two numbers
such that they add up to target.

Assume that each input would have exactly one solution, and the same element cannot be used twice.

1 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9
-10**9 <= target <= 10**9

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""

from typing import *


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given that there would be a need to look up comparisons, one option would be to create a
    hash map (dict) of elements that are possible components of the solution.

    In other words, iterate through the array and create a dict where keys are elements
    and values are their indices. As the nums array is iterated, look for the
    other half of the pair among the keys in the dict.

    Since there is exactly one solution, then we don't have to worry about duplicate elements
    because either the answer uses both duplicate elements so we return once the second is encountered
    or the duplicate elements are not part of the solution in which case we don't care about the index of it.
    Hence, we can simply store the index of the latest as the value. If we wanted to keep track of multiple
    possible solutions then we should store the indices in a list format.
    """

    possible_solution_components = {}

    for idx, element in enumerate(nums):
        if possible_solution_components.get(target - element) is not None:
            return [idx, possible_solution_components.get(target - element)]
        else:
            possible_solution_components[element] = idx
