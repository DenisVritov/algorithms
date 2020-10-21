"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
    You may assume that duplicates do not exist in the tree.

Input:
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

Output:
    3
   / \
  9  20
    /  \
   15   7
"""

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    """
    The preorder list tells us the parent/child/ancestor relationships and the inorder list tells us the order and which
    node is a left or right child. So we can iterate over the preorder list to construct the tree and supplement with
    an iteration over the inorder list to check whether the node is a left or right child.

    More specifically, the preorder tells us which node to build next. The inorder tells us whether a node is in the
    left or right subtree by looking at if the value is to the left or right of the parent's index in the inorder list.
    """

    in_len = len(inorder)

    def buildTreeRecur(p_s: int, i_s: int, i_e: int) -> Tuple[TreeNode, int]:

        if p_s >= in_len or i_s >= i_e:
            return None, p_s

        root = TreeNode(preorder[p_s])

        root_index = inorder.index(root.val)

        root.left, p_s = buildTreeRecur(p_s+1, i_s, root_index)

        if root_index < len(inorder) - 1:
            root.right, p_s = buildTreeRecur(p_s, root_index+1, i_e)

        return root, p_s

    ret, p = buildTreeRecur(0, 0, in_len)
    return ret
