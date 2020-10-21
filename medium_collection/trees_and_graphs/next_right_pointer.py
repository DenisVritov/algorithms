"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.

The binary tree has the following definition:
    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer
should be set to NULL.

Initially, all next pointers are set to NULL.

Notes:
    The number of nodes in the given tree is less than 4096.
    -1000 <= node.val <= 1000
"""

from typing import *


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def set_next_right_pointer(root: Node) -> Node:
    """
    Since we need to set the next right node per level, we can utilize a level ordering algorithm to traverse
    the tree and simply set the next pointer to the next node in the level.
    """

    if root is None:
        return None

    q = list()
    q.append((root, 0))

    prev_node = None

    current_level = 0

    while len(q) > 0:
        node, level = q.pop(0)

        if level == current_level and prev_node:
            prev_node.next = node
        else:
            current_level = level

        prev_node = node

        if node.left is not None:
            q.append((node.left, level+1))
        if node.right is not None:
            q.append((node.right, level+1))

    return root
