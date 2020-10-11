"""
Given an array of integers, find if the array contains any duplicates.

Function should return true if any value appears at least twice in the array, and it should
return false if every element is distinct.

Input: [1,1,1,3,3,4,3,2,4,2]
Output: True
"""

from typing import *


def contains_duplicate(nums: List[int]) -> bool:
    """
    Space efficient method: sort array and iterate over array checking consecutive elements,
    return True on first dupe, otherwise finish iteration and return False.

    Time efficient method: use a hash map (dict), iterating of the array and adding to the
    dict, if it already exists in the dict then return True
    """

    # Space efficient method
    # nums.sort()
    # for idx in range(len(nums) - 1):
    #     if nums[idx] == nums[idx + 1]:
    #         return True
    # return False

    # Time efficient method
    hash_dict = dict()
    for idx in range(len(nums) - 1):
        if hash_dict.get(nums[idx]) is not None:
            return True
        else:
            hash_dict[nums[idx]] = True
    return False
