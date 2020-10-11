"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range
that is missing from the array.

Constraints:
    n == nums.length
    1 <= n <= 10**4
    0 <= nums[i] <= n
    All the numbers of nums are unique

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
"""

from typing import *


def missing_number(nums: List[int]) -> int:
    """
    A simple way to solve this would be to simply sort the array then iterate over the sorted array to find the
    missing number. We can sort the array in nlog(n) time then the search only takes n time.

    However, there is a better way to solve this in linear time. If we use the mathematical property that
    the sum of integers from 0 to n is equal to n(n+1)/2 then we can find the missing number by simply
    summing the given array then subtracting it from the value n(n+1)/2. To get the correct value for n, we use the
    length of the array.
    """

    n = len(nums)
    return int(n*(n+1)/2) - sum(nums)
