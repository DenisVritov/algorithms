"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
    - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    - int get(int key) Return the value of the key if the key exists, otherwise return -1.
    - void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the
        key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
        evict the least recently used key.

Follow up: Could you do get and put in O(1) time complexity?

Notes:
    1 <= capacity <= 3000
    0 <= key <= 3000
    0 <= value <= 10**4
    At most 3 * 10**4 calls will be made to get and put

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
"""

from typing import *


# Uses OrderedDict
class LRUCache:
    from collections import OrderedDict

    def __init__(self, capacity: int):
        """
        Initialize the LRU Cache with positive size capacity.
        """
        self.capacity = capacity
        self.cache = self.OrderedDict()

    def get(self, key: int) -> int:
        """
        Return the value of the key if the key exists, otherwise return -1.
        """
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the
        number of keys exceeds the capacity from this operation, evict the least recently used key.
        """
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key, last=True)
        else:
            if len(self.cache) >= self.capacity:
                oldest = next(iter(self.cache))
                del self.cache[oldest]

            self.cache[key] = value


# Makes use of basic types and implements own version of "OrderedDict" by using doubly linked list
class LRUCache:

    class DoublyLinkedNode:
        def __init__(self, val, next_node=None, prev_node=None):
            self.val = val
            self.next = next_node
            self.prev = prev_node

    def __init__(self, capacity: int):
        """
        Initialize the LRU Cache with positive size capacity.
        """
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.node_idx = dict()
        self.cache = dict()

    def _evict(self):
        """
        Evict the oldest key-value pair from the cache.
        """
        oldest_node = self.tail
        if self.tail.prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = oldest_node.prev
            self.tail.next = None

        del self.cache[oldest_node.val]
        del self.node_idx[oldest_node.val]

    def _update_oldest(self, key: int):
        """
        Update what is the oldest key in the cache.
        """
        key_node = self.node_idx[key]
        if key_node.prev is not None:
            key_node.prev.next = key_node.next
            if key_node.next is None:
                self.tail = key_node.prev
            else:
                key_node.next.prev = key_node.prev
            key_node.next = self.head
            self.head.prev = key_node
            self.head = key_node
            self.head.prev = None

    def get(self, key: int) -> int:
        """
        Return the value of the key if the key exists, otherwise return -1.
        """
        if key in self.cache:
            self._update_oldest(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the
        number of keys exceeds the capacity from this operation, evict the least recently used key.
        """
        if key in self.cache:
            self.cache[key] = value
            self._update_oldest(key)
        else:
            if len(self.cache) >= self.capacity:
                self._evict()

            if self.head is None:
                self.head = self.DoublyLinkedNode(key)
                self.tail = self.head
                self.node_idx[key] = self.head
            else:
                new_node = self.DoublyLinkedNode(key)
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                self.node_idx[key] = new_node

            self.cache[key] = value
