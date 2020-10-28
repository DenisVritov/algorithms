"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in
the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be
serialized to a string and this string can be deserialized to the original tree structure.

Notes:
    The number of nodes in the tree is in the range [0, 10**4]
    -1000 <= Node.val <= 1000

Input:
    1
     \
      2
     /
    3
Output: (example) [1,None,2,3]
"""

from typing import *


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTreeCoder:
    import json

    def dfs_encode(self, root: TreeNode):
        """
        Perform a recursive dfs traversal of binary tree.
        """
        ret = list()

        ret.append(root.val)
        if root.left:
            ret.extend(self.dfs_encode(root.left))
        else:
            if root.right:
                ret.append(None)
            else:
                ret.append('n')
                return ret
        if root.right:
            ret.extend(self.dfs_encode(root.right))
        else:
            ret.append(None)

        return ret

    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string.
        """

        if root is None:
            return str([])

        ret = self.dfs_encode(root)

        return self.json.dumps(ret)

    def deserialize(self, data: str) -> TreeNode:
        """
        Decodes your encoded data to tree.
        """

        if data == '[]':
            return None

        data = self.json.loads(data)
        l_data = len(data)

        def dfs_decode(start_idx) -> Tuple[TreeNode, int]:
            """
            Construct binary tree from list of nodes.
            """

            if start_idx >= l_data or data[start_idx] is None:
                return None, start_idx

            current_node = TreeNode(data[start_idx])
            if start_idx < l_data - 1 and data[start_idx+1] == 'n':
                return current_node, start_idx+1
            else:
                current_node.left, start_idx = dfs_decode(start_idx+1)
                current_node.right, start_idx = dfs_decode(start_idx+1)

            return current_node, start_idx

        return dfs_decode(0)[0]
