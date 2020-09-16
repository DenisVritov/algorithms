"""
Given a linked list, remove the n-th node from the end of list and return its head.

Note:
    Given n will always be valid.

Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
"""

from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """
    To do this in a single pass, we will employ two pointers. One that points at the possible
    node to delete and one that points n nodes ahead. Once the front-running pointer reaches
    the end of the list, the pointer in back will be pointing at the node to remove and that
    node will be deleted.
    """

    # Handle base case of end of list being removed
    if n == 1:
        current = head
        if current.next is None:
            return None
        while current.next.next is not None:
            current = current.next
        current.next = None
    else:
        n_ahead = head
        current = head

        for i in range(n-1):
            n_ahead = n_ahead.next

        while n_ahead.next is not None:
            n_ahead = n_ahead.next
            current = current.next

        current.val = current.next.val
        current.next = current.next.next

    return head
