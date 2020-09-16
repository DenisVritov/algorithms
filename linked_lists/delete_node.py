"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Note:
    The linked list will have at least two elements.
    All of the nodes' values will be unique.
    The given node will not be the tail and it will always be a valid node of the linked list.
    Do not return anything from your function.

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
"""

from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(node: ListNode) -> None:
    """
    To remove the node given only access to that node, the previous node will need to point
    to the next node (i.e. skip over the given node). But since the only node that is
    accessible is the one provided, the previous node cannot be altered.

    Hence, in order to delete the node we will instead copy the next node's values to the
    current node and "delete" the next node.
    """

    node.val = node.next.val
    node.next = node.next.next
