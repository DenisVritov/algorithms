"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
"""

from typing import *


def rotate_array(nums: List[int], k: int) -> None:
    """
    If length of the array is 0 or 1 then nothing needs to be done.

    Otherwise, moving k to the right is the same as moving
    k modulo len(nums) to the right. From here, simply rotate each
    element k%nums spaces, keeping the previous element in a temp
    variable.

    If nums%(k%num) == 0 then the cycle won't hit all numbers so
    need to keep track of how many elements have been shifted and
    restart with start+=1 every time a cycle is completed until
    len(nums) elements have been moved.
    """

    n = len(nums)
    k = k % n
    start = 0
    count = 0

    while count < len(nums):
        idx = start
        tmp = nums[start]

        while True:
            idx = (idx + k) % n
            nums[idx], tmp = tmp, nums[idx]
            count += 1
            if idx == start:
                break

        start += 1