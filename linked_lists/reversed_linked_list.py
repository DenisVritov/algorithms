"""
Reverse a singly linked list.

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""


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
