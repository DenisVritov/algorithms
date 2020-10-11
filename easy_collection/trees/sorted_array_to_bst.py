"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the
two subtrees of every node never differ by more than 1.

Example:
Input: [-10,-3,0,5,9]
Output:
      0
     / \
   -3   9
   /   /
 -10  5
This is one possible answer. There can be many.
"""

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_list_to_bst(nums: List[int]) -> TreeNode:
    """
    Since the list is already sorted and we need to create a BST, we can recursively split the input
    array in half, taking the left half as the left subtree and the right half as the right subtree.

    Doing this "split in half" approach also ensures that the subtrees should remain balanced as splitting
    in half will ensure there is at most a 1 node difference between the two halves.
    """

    l = len(nums)

    if l == 0:
        return None
    elif l == 1:
        return TreeNode(nums[0])
    elif l == 2:
        return TreeNode(nums[1], TreeNode(nums[0]))
    elif l == 3:
        return TreeNode(nums[1], TreeNode(nums[0]), TreeNode(nums[2]))
    else:
        h = int(l/2)
        return TreeNode(nums[h], sorted_list_to_bst(nums[0:h]), sorted_list_to_bst(nums[h+1:l]))
