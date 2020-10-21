"""
Write a program to find the node at which the intersection of two singly linked lists begins.

Note:
    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Each value on each linked list is in the range [1, 10^9].
    Your code should preferably run in O(n) time and use only O(1) memory.

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]
Output: Reference of the node with value = 8
"""

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode:
    """
    We can use the fact that values in the nodes are strictly positive to mark visited nodes as negative.

    Then we simply iterate over the linked lists marking each visited node by negating the value. If we reach an
    already visited node then that node will be the first common node meaning it is the intersection. If we reach the
    end of both linked lists then there is no intersection.

    Then we simply iterate over the linked lists again and set the values back to positive to maintain original
    structure.
    """

    a = headA
    b = headB

    intersecting_node = None

    while a or b:
        if a:
            if a.val < 0:
                intersecting_node = a
                break
            else:
                a.val = -a.val
                a = a.next
        if b:
            if b.val < 0:
                intersecting_node = b
                break
            else:
                b.val = -b.val
                b = b.next

    a = headA
    b = headB

    while a.val < 0:
        a.val = -a.val
        a = a.next

    while b.val < 0:
        b.val = -b.val
        b = b.next

    return intersecting_node
