"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:
    The number of nodes in each linked list is in the range [1, 100]
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Since the numbers are represented in reverse order then we don't need to worry about aligning numbers of
    different lengths.

    The basic algorithm is to combine the values of the nodes at the same indices in each of the inputs, keeping
    track of the carry-over, and building a new linked list to return.
    """

    carry = 0
    ret_head = None
    ret = None

    while l1 is not None and l2 is not None:
        v = l1.val + l2.val + carry
        if v > 9:
            carry = 1
            v -= 10
        else:
            carry = 0

        if not ret:
            ret = ListNode(v)
            ret_head = ret
        else:
            ret.next = ListNode(v)
            ret = ret.next

        l1 = l1.next
        l2 = l2.next

    while l1 is not None:
        v = l1.val + carry
        if v > 9:
            carry = 1
            v -= 10
        else:
            carry = 0

        ret.next = ListNode(v)
        ret = ret.next

        l1 = l1.next

    while l2 is not None:
        v = l2.val + carry
        if v > 9:
            carry = 1
            v -= 10
        else:
            carry = 0

        ret.next = ListNode(v)
        ret = ret.next

        l2 = l2.next

    if carry == 1:
        ret.next = ListNode(1)

    return ret_head
