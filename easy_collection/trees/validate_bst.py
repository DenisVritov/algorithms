"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.

Example:
Input:
    5
   / \
  1   4
     / \
    3   6

Output: False
"""

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def validate_bst(root: TreeNode) -> bool:
    """
    This can be done by recursively checking the child trees for BST validity,
    passing in a min/max value for the children.
    """

    def valid_bst(node, min_val, max_val):
        if node is None:
            return True
        elif not (min_val < node.val < max_val):
            return False
        else:
            return valid_bst(node.left, min_val, node.val) and valid_bst(node.right, node.val, max_val)

    return valid_bst(root, float('-inf'), float('inf'))
