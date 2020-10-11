"""
Given an array nums, write a function to move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Should be done in-place.

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

from typing import *


def move_zeroes(nums: List[int]) -> None:
    """
    Iterate through the array and swap zeroes as we encounter them with the next non-zero
    number.

    This uses a two-pointer system. The first pointer indicates the position of where to put
    the next non-zero number. The second pointer scans ahead looking for the next available
    non-zero number.
    """

    if nums[0] == 0:
        zero_index = 0
    else:
        zero_index = None
    curr_index = 1

    while curr_index < len(nums):
        if nums[curr_index] != 0 and zero_index is not None:
            nums[zero_index], nums[curr_index] = nums[curr_index], 0
            while zero_index < len(nums) and nums[zero_index] != 0:
                zero_index += 1
        elif nums[curr_index] == 0 and zero_index is None:
            zero_index = curr_index
        curr_index += 1