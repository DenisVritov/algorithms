"""
Given a linked list, determine if it has a cycle in it.

Input: head = [3,2,0,-4], pos = 1 (pos indicates the 0-indexed index of node which list cycles back to,
                                   in this example -4 cycles back to 2)
Output: True
"""

from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: ListNode) -> bool:
    """
    Solution 1:
    In order to detect a cycle, need some way of keeping track of nodes visited. In python, we can set a bool
    flag in the ListNode after it is created and check.

    The algorithm would be as follows:
        - Iterate over the nodes, checking if visited flag exists (if it does, return True)
        - If no visited flag exists, set it to True
        - If a Null node is reach return False since clearly no cycle

    Solution 2:
    Point each node to a custom temp node as each node is visited. This bypasses having to store a new
    value in each node for marking but distorts the list.

    Solution 3:
    Use a fast and slow pointer. If they ever meet then there is a cycle, if a Null node is reached
    there is no cycle.
    """
    if head is None:
        return False

    slo = head
    fast = head.next

    while fast is not None:
        if slo == fast:
            return True
        slo = slo.next
        if fast.next is not None:
            fast = fast.next.next
        else:
            return False

    return False
