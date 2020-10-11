"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]
"""


class MinStack:
    """
    Utilize a linked list to implement a stack
    """

    class ListNode:
        """
        Store the minimum value in the tail of the linked list for quick access
        """

        def __init__(self, x):
            self.val = x
            self.next = None
            self.min = None

    def __init__(self):
        self._my_stack = None
        self._min = None

    def push(self, x: int) -> None:
        new_node = self.ListNode(x)
        new_node.next = self._my_stack
        if self._min is not None:
            new_node.min = self._min
            self._min = min(self._min, x)
        else:
            self._min = x
        self._my_stack = new_node

    def pop(self) -> None:
        self._min = self._my_stack.min
        self._my_stack = self._my_stack.next

    def top(self) -> int:
        return self._my_stack.val

    def getMin(self) -> int:
        if self._min is None:
            raise ValueError('Stack is empty')
        else:
            return self._min
