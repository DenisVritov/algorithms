"""
Given a singly linked list, determine if it is a palindrome.

Input: 1->2->2->1
Output: True
"""

from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_linked_list(head: ListNode) -> ListNode:
    """
    This will be done iteratively as although recursive is nicer visually, using iterative approach
    saves us stack space.
    """
    if head is None:
        return None

    new_tail = head
    head = head.next
    new_tail.next = None

    while head is not None:
        tmp = head.next
        head.next = new_tail
        new_tail = head
        head = tmp

    return new_tail


def is_palindrome(head: ListNode) -> bool:
    """
    One approach is to do a total of 2.5 passes:
        - pass over entire list to get length
        - pass over front half and reverse the list
        - pass over the two halves and compare
    """

    n = 0
    pointer = head
    while pointer is not None:
        pointer = pointer.next
        n += 1

    if n < 2:
        return True
    elif n == 2:
        return head.val == head.next.val

    pointer = head
    for i in range(int(n/2)-1):
        pointer = pointer.next

    pointer2 = pointer.next
    pointer.next = None

    if n % 2 != 0:
        pointer2 = pointer2.next

    pointer = reverse_linked_list(head)

    while pointer is not None:
        if pointer.val != pointer2.val:
            return False
        pointer = pointer.next
        pointer2 = pointer2.next

    return True