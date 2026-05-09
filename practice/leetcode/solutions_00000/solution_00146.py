#!/usr/bin/env python3

"""LeetCode solution 00146."""

import unittest
from collections import OrderedDict

class Node(object):

    def __init__(self, key, value, prev=None, _next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = _next

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key)
        if node:
            self.remove_node(node)
            self.set_head(node)
            return node.value
        return -1

    def remove_node(self, n):
        if n.prev is not None:
            n.prev.next = n.next
        else:
            self.head = n.next

        if n.next is not None:
            n.next.prev = n.prev
        else:
            self.tail = n.prev

    def set_head(self, n):
        n.next = self.head
        n.prev = None

        if self.head is not None:
            self.head.prev = n

        self.head = n
        if self.tail is None:
            self.tail = self.head

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return

        node = self.cache.get(key)
        if node:
            node.value = value
            self.remove_node(node)
            self.set_head(node)
        else:
            node = Node(key, value)
            if len(self.cache) >= self.capacity:
                self.cache.pop(self.tail.key)
                self.remove_node(self.tail)

            self.set_head(node)
            self.cache[key] = node

class _LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)

        self.cache[key] = value

class TestSolution(unittest.TestCase):

    def test_LRUCache(self):
        cache = LRUCache(2)

        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_LRUCache_with_zero_capacity(self):
        cache = LRUCache(0)

        cache.put(1, 1)

        self.assertEqual(cache.get(1), -1)

if __name__ == '__main__':
    unittest.main()
