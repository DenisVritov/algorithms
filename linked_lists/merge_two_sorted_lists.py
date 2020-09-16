"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made
by splicing together the nodes of the first two lists.

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    This algorithm uses two pointers, one for each list and adds to the end of the new
    list which ever node is smaller.
    """

    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    p1 = l1
    p2 = l2

    if p1.val < p2.val:
        ret = ListNode(p1.val)
        p1 = p1.next
    else:
        ret = ListNode(p2.val)
        p2 = p2.next

    ret_head = ret

    while p1 is not None and p2 is not None:
        if p1.val < p2.val:
            ret.next = ListNode(p1.val)
            ret = ret.next
            p1 = p1.next
        else:
            ret.next = ListNode(p2.val)
            ret = ret.next
            p2 = p2.next

    while p1 is not None:
        ret.next = ListNode(p1.val)
        ret = ret.next
        p1 = p1.next

    while p2 is not None:
        ret.next = ListNode(p2.val)
        ret = ret.next
        p2 = p2.next

    return ret_head