"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: 3
"""

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_bin_tree(root: TreeNode) -> int:
    """
    This can be done recursively by calculating the max depth of the child nodes and adding 1
    """

    if root is None:
        return 0
    else:
        return max(max_depth_bin_tree(root.left), max_depth_bin_tree(root.right)) + 1