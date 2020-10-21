"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Notes:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

Input: root = [1,null,2,3]
    1
     \
      2
     /
    3
Output: [1,3,2]
"""

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode) -> List[int]:
    """
    This can be done recursively or iteratively. The recursive method is quite simple: return the inorder traversal
    of the left child, the parent, then the inorder traversal of the right child.

    Instead we will do an iterative approach which is a bit more nuanced but is typically preferred over recursive
    approach because of fewer frames in the stack.
    """

    ret = []

    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)

        if not node:
            continue
        elif type(node) == int:
            ret.append(node)
        else:
            queue = [node.left, node.val, node.right] + queue

    return ret
