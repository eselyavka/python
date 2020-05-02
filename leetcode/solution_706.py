#!/usr/bin/env python

import unittest


class KV(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val


class MyAnotherHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.arr = [None] * self.size

    def _hash(self, key):
        return id(key) % self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self._get(key)

        if node == -1:
            self.arr[self._hash(key)] = [KV(key, value)]
        else:
            node.val = value

    def _get(self, key):
        nodes = self.arr[self._hash(key)]
        if nodes is not None:
            for node in nodes:
                if node.key == key:
                    return node

        return -1

    def get(self, key):
        """
        Returns the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        node = self._get(key)
        return node if node == -1 else node.val

    def remove(self, key):
        """
        Removes the mapping of the specified value key
        if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        nodes = self.arr[self._hash(key)]

        if nodes is None:
            return

        i = 0

        while i < len(nodes):
            if nodes[i].key == key:
                del nodes[i]
                break
            i += 1


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000000
        self.arr = [None] * self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.arr[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.arr[key] if self.arr[key] is not None else -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key
        if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        self.arr[key] = None


class ListNode(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None


class MyHashMapChain(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.hash = [None] * self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        h = hash(key) % self.size
        if self.hash[h] is None:
            self.hash[h] = ListNode(key, value)
        else:
            node = self.hash[h]
            while node:
                if node.key == key:
                    node.val = value
                    break
                if node.next is None:
                    node.next = ListNode(key, value)
                    break
                node = node.next

    def get(self, key):
        """
        Returns the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        h = hash(key) % self.size
        curr = self.hash[h]
        if curr is None:
            return -1
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key
        if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        h = hash(key) % self.size
        curr = self.hash[h]
        if curr is not None:
            prev = None
            while curr:
                if curr.key == key:
                    if prev:
                        prev.next = curr.next
                    else:
                        self.hash[h] = curr.next
                prev = curr
                curr = curr.next


class TestSolution(unittest.TestCase):

    def test_MyHashMap(self):
        hashMap = MyHashMap()
        for p in [[970, 538], [908, 29], [395, 865], [250, 847]]:
            hashMap.put(*p)

        hashMap.remove(836)

        for p in [[233, 568],
                  [657, 790],
                  [595, 271],
                  [769, 219],
                  [55, 112],
                  [157, 493]]:
            hashMap.put(*p)

        self.assertEqual(hashMap.get(920), -1)

        hashMap.put(*[632, 358])

        self.assertEqual(hashMap.get(669), -1)

        hashMap.put(*[506, 228])
        hashMap.remove(904)
        hashMap.get(473)

        for p in [[461, 40], [748, 973], [446, 544], [766, 461]]:
            hashMap.put(*p)

        self.assertEqual(hashMap.get(395), 865)

        self.assertEqual(hashMap.get(669), -1)

        self.assertEqual(hashMap.get(1), -1)
        self.assertEqual(hashMap.get(3), -1)

        hashMap.put(2, 1)

        self.assertEqual(hashMap.get(2), 1)

        hashMap.remove(2)

        self.assertEqual(hashMap.get(2), -1)

        hashMap.put(395, 865)

        hash_map_chain = MyHashMapChain()
        actual = []
        actual.append(hash_map_chain.put(1, 1))
        actual.append(hash_map_chain.put(2, 2))
        actual.append(hash_map_chain.get(1))
        actual.append(hash_map_chain.get(3))
        actual.append(hash_map_chain.put(2, 1))
        actual.append(hash_map_chain.get(2))
        actual.append(hash_map_chain.remove(2))
        actual.append(hash_map_chain.get(2))

        self.assertListEqual(actual, [None, None, 1, -1, None, 1, None, -1])


if __name__ == '__main__':
    unittest.main()
