"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Constraints:
    1 <= nums.length <= 2 * 10**4
    -2**31 <= nums[i] <= 2**31 - 1

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
"""

from typing import *


def max_subarray(nums: List[int]) -> int:
    """
    The basic idea is to iterate over the list and build up a subarray. The subarray will either grow by the current
    element (n) or restart at the current element if n is greater than the sum of n and the previous subarray.

    While this is happening, the maximum visited subarray is stored as the maximum of the previous max subarray
    and the current subarray.

    Return the max subarray.
    """

    max_sum = float('-inf')
    max_sum2 = float('-inf')

    for n in nums:
        if max_sum2 + n < n:
            max_sum2 = n
        else:
            max_sum2 += n

        max_sum = max(max_sum, max_sum2)

    return max_sum
