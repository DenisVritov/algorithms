"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Example:
Input:
    3
   / \
  9  20
    /  \
   15   7

Output:
[
  [3],
  [9,20],
  [15,7]
]
"""

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def btree_level_trav(root: TreeNode) -> List[List[int]]:
    """
    Simply traverse the btree in a BFS fashion, counting levels to keep track of separate lists.

    This uses a queue in typical BFS fashion.
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
            ret.append(level_list)
            level_list = [node.val]
            current_level = level

        if node.left is not None:
            q.append((node.left, level+1))
        if node.right is not None:
            q.append((node.right, level+1))

    if level_list != []:
        ret.append(level_list)

    return ret
