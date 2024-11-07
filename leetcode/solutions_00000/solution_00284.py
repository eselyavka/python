#!/usr/bin/env python

import unittest
from unittest.mock import MagicMock


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.cnt = 0
        self.arr = []
        while iterator.hasNext():
            i = iterator.next()
            self.arr.append(i)
        self.it = iter(self.arr)

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.arr[self.cnt]

    def next(self):
        """
        :rtype: int
        """
        if self.cnt >= len(self.arr):
            return

        self.cnt += 1
        return self.it.__next__()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cnt < len(self.arr)


class TestSolution(unittest.TestCase):

    def test_PeekingIterator(self):
        arr = [1, 2, 3]
        solution = PeekingIterator(MagicMock(**{"hasNext": lambda: len(arr) != 0,
                                                "next": lambda: arr.pop(0)}))
        self.assertEqual(solution.next(), 1)
        self.assertEqual(solution.peek(), 2)
        self.assertEqual(solution.next(), 2)
        self.assertEqual(solution.next(), 3)
        self.assertFalse(solution.hasNext())


if __name__ == '__main__':
    unittest.main()
