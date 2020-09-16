"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array. Modify nums1 in place.

Note:
    - The number of elements initialized in nums1 and nums2 are m and n respectively.
    - You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Constraints:
    -10^9 <= nums1[i], nums2[i] <= 10^9
    nums1.length == m + n
    nums2.length == n

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

from typing import *


def merge_sorted_arrays(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Since the two arrays are already sorted and nums1 has enough space, we can simply use 3 pointers:
        - One for keeping track of the element in nums1
        - One for keeping track of the element in nums2
        - One for tracking destination index in nums1

    The process would be to iterate over the arrays backwards and place the largest element into the last
    position in nums1 and decrement the pointers.
    """

    dest_pointer = -1
    n1_pointer = len(nums1) - n - 1
    n2_pointer = n-1

    while n1_pointer > -1 and n2_pointer > -1:
        if nums2[n2_pointer] > nums1[n1_pointer]:
            nums1[dest_pointer] = nums2[n2_pointer]
            dest_pointer -= 1
            n2_pointer -= 1
        else:
            nums1[dest_pointer] = nums1[n1_pointer]
            dest_pointer -= 1
            n1_pointer -= 1

    while n1_pointer > -1:
        nums1[dest_pointer] = nums1[n1_pointer]
        dest_pointer -= 1
        n1_pointer -= 1

    while n2_pointer > -1:
        nums1[dest_pointer] = nums2[n2_pointer]
        dest_pointer -= 1
        n2_pointer -= 1
