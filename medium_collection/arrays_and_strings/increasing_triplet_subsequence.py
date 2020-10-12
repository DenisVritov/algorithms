"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Input: [5,4,3,2,1]
Output: False
"""

from typing import *


def increasing_triplet_subsequence(nums: List[int]) -> bool:
    """
    In order to run in O(n) with O(1) space, we know that the algorithm needs to only iterate over the array and
    perform O(1) operations during the iteration.

    To do this we can iterate over the array and keep track of the smallest and second smallest values found so far.
    In order to account for a better pair of smallest values we can keep 2 sets of smallest values. The current smallest
    working value and the smallest value currently found.

    In addition, if we find a third item that satisfies the triplet we can immediately return.
    """

    if len(nums) < 3:
        return False

    i = nums[0]
    j = None
    smallest = nums[0]

    for idx in range(len(nums)):

        if nums[idx] <= i:
            if j is None:
                i = nums[idx]
                smallest = nums[idx]
            elif nums[idx] > smallest:
                i = smallest
                j = nums[idx]
            else:
                smallest = nums[idx]
        elif j is not None and nums[idx] < j:
            j = nums[idx]
        elif j is not None and nums[idx] > j:
            return True
        else:
            j = nums[idx]

    return False
