#!/usr/bin/env python

import unittest

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """

        res = []
        for data in map(None, v1, v2):
            res.extend([x for x in data if x is not None])

        self.it = iter(res)
        self.has_next = None
        self._next = None

    def next(self):
        """
        :rtype: int
        """
        if self.has_next:
            res = self._next
        else:
            res = next(self.it)

        self.has_next = None

        return res

    def hasNext(self):
        """
        :rtype: bool
        """

        if self.has_next is None:
            try:
                self._next = self.next()
            except StopIteration:
                self.has_next = False
            else:
                self.has_next = True

        return self.has_next

class TestSolution(unittest.TestCase):
    def test_ZigzagIterator(self):
        solution = ZigzagIterator([1, 2], [3, 4, 5, 6])
        actual = []
        while solution.hasNext():
            actual.append(solution.next())

        self.assertListEqual([1, 3, 2, 4, 5, 6], actual)

if __name__ == '__main__':
    unittest.main()
