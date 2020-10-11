"""
Given a sorted array nums, remove the duplicates in-place such that each
element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

Given nums = [0,0,1,1,1,2,2,3,3,4],
Function should return length = 5
"""

from typing import *


def remove_duplicates(nums: List[int]) -> int:
    """
    Use two running pointers.

    If lookahead pointer's element is the same as the first pointer's element,
    move lookahead pointer forward.

    If lookahead is different, then move first pointer up and set the element to
    be the next non-dupe element.

    pointerA will finish end on the last element in the final array.
    """
    pointerA = 0
    pointerB = 1

    while pointerB < len(nums):
        if nums[pointerA] == nums[pointerB]:
            pointerB += 1
        else:
            pointerA += 1
            nums[pointerA] = nums[pointerB]
            pointerB += 1

    return pointerA