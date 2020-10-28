"""
Implement the RandomizedSet class:

    - bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was
        not present, false otherwise.
    - bool remove(int val) Removes an item val from the set if present. Returns true if the item was
        present, false otherwise.
    - int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one
        element exists when this method is called). Each element must have the same probability of being returned.

Follow up: Could you implement the functions of the class with each function works in average O(1) time?

Note:
    -2**31 <= val <= 2**31 - 1
    At most 105 calls will be made to insert, remove, and getRandom
    There will be at least one element in the data structure when getRandom is called

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]
"""

from typing import *


class RandomizedSet:
    from random import randrange

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_set = dict()
        self.my_vals_list = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.my_set:
            list_len = len(self.my_vals_list)
            self.my_set[val] = list_len
            self.my_vals_list.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.my_set:
            return False
        else:
            last_element = self.my_vals_list.pop()
            if last_element != val:
                prev_index = self.my_set[val]
                self.my_vals_list[prev_index] = last_element
                self.my_set[last_element] = prev_index
            del self.my_set[val]
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.my_vals_list[self.randrange(0, len(self.my_vals_list))]
