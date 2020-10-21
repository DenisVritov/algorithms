"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are
talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Notes:
    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on ...
    The length of the linked list is between [0, 10^4].

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
"""

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(head: ListNode) -> ListNode:
    """
    A simple solution to this problem would be to create two heads, one for evens and one for odds, and add the
    corresponding nodes to the tail of each list and repoint them to the next corresponding node.
    """

    if not head:
        return None
    elif not head.next or not head.next.next:
        return head

    odd_head = head
    odd_tail = odd_head
    even_head = head.next
    even_tail = even_head

    current_node = head.next.next
    is_odd = True

    while current_node:
        if is_odd:
            odd_tail.next = current_node
            odd_tail = odd_tail.next
        else:
            even_tail.next = current_node
            even_tail = even_tail.next

        current_node = current_node.next
        is_odd = not is_odd

    even_tail.next = None
    odd_tail.next = even_head

    return odd_head
