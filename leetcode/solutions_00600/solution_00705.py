#!/usr/bin/env python

import unittest


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [None] * 1000000

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.arr[key] = key

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.arr[key] = None

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.arr[key] == key


class MyHashSet2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.arr = [None] * self.size

    def _hash(self, key):
        return id(key) % self.size

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        nodes = self.arr[self._hash(key)]
        if nodes is not None:
            for node in nodes:
                if node == key:
                    return
            nodes.append(key)
        else:
            self.arr[self._hash(key)] = [key]

    def _get(self, key):
        nodes = self.arr[self._hash(key)]
        if nodes is not None:
            for node in nodes:
                if node == key:
                    return node

        return -1

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        node = self._get(key)
        return node != -1

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        nodes = self.arr[self._hash(key)]

        if nodes is None:
            return

        i = 0

        while i < len(nodes):
            if nodes[i] == key:
                del nodes[i]
                break
            i += 1


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MyHashSet3(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.hash = [None] * self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = hash(key) % self.size
        if self.hash[h] is None:
            self.hash[h] = ListNode(key)
        else:
            node = self.hash[h]
            while node:
                if node.val == key:
                    break
                if node.next is None:
                    node.next = ListNode(key)
                    break
                node = node.next

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = hash(key) % self.size
        curr = self.hash[h]
        if curr is not None:
            prev = None
            while curr:
                if curr.val == key:
                    if prev:
                        prev.next = curr.next
                    else:
                        self.hash[h] = curr.next
                prev = curr
                curr = curr.next

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        h = hash(key) % self.size
        curr = self.hash[h]
        if curr is None:
            return False
        while curr:
            if curr.val == key:
                return True
            curr = curr.next


class TestSolution(unittest.TestCase):

    def test_MyHashSet(self):
        hashSets = [MyHashSet(), MyHashSet2(), MyHashSet3()]
        expected = [None, None, True, False, None, True, None, False]
        for hash_set in hashSets:
            actual = []
            actual.append(hash_set.add(1))
            actual.append(hash_set.add(2))
            actual.append(hash_set.contains(1))
            actual.append(hash_set.contains(3))
            actual.append(hash_set.add(2))
            actual.append(hash_set.contains(2))
            actual.append(hash_set.remove(2))
            actual.append(hash_set.contains(2))
            self.assertListEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
