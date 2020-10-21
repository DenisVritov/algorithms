"""
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

Input:
    3
   / \
  9  20
    /  \
   15   7

Output:
[
  [3],
  [20,9],
  [15,7]
]
"""

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_traversal(root: TreeNode) -> List[List[int]]:
    """
    This is essentially a level-order traversal with a reversal of every other level.
    """

    if root is None:
        return []

    q = list()
    q.append((root, 0))

    ret = []
    level_list = []

    current_level = 0

    while len(q) > 0:
        node, level = q.pop(0)

        if level == current_level:
            level_list.append(node.val)
        else:
            if current_level % 2:
                level_list.reverse()
            ret.append(level_list)
            level_list = [node.val]
            current_level = level

        if node.left is not None:
            q.append((node.left, level+1))
        if node.right is not None:
            q.append((node.right, level+1))

    if level_list != []:
        if current_level % 2:
            level_list.reverse()
        ret.append(level_list)

    return ret
