"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Example:
Input:
    1
   / \
  2   2
 / \ / \
3  4 4  3

Output: True
"""

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def symmetric_btree(root: TreeNode) -> bool:
    """
    In order to check for symmetry we can recursively check if left and right subtrees are mirrors
    """

    if root is None:
        return True

    def is_mirror(left, right):
        if left is None and right is None:
            return True
        elif not left or not right or left.val != right.val:
            return False
        else:
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    return is_mirror(root.left, root.right)
