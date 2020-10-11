"""
Create a function to compute the intersection of 2 arrays

Input: nums1 = [4,4,9,5], nums2 = [9,4,9,8,4]
Output: [4,4,9]
"""

from typing import *
from collections import defaultdict


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Create a dictionary of the smaller set such that the key is the element and value
    is the number of times that element appears in the list.

    Then iterate over the other array and check against the dictionary. If the element
    exists and has a value >0, reduce the value by 1 and add to the return array.
    Otherwise continue iterating.
    """

    if len(nums1) < len(nums2):
        arr_smaller = nums1
        arr_larger = nums2
    else:
        arr_smaller = nums2
        arr_larger = nums1

    arr_smaller_dict = defaultdict(int)

    for element in arr_smaller:
        arr_smaller_dict[element] += 1

    intersection = []

    for element in arr_larger:
        if arr_smaller_dict.get(element, 0) > 0:
            arr_smaller_dict[element] -= 1
            intersection.append(element)

    return intersection