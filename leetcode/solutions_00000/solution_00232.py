#!/usr/bin/env python

import unittest


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._enq = []
        self._dec = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self._enq.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self._dec:
            while self._enq:
                self._dec.append(self._enq.pop())

        return self._dec.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self._dec:
            while self._enq:
                self._dec.append(self._enq.pop())

        return self._dec[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return all([len(self._enq) == 0, len(self._dec) == 0])


class TestMyQueue(unittest.TestCase):

    def test_MyQueue(self):
        solution = MyQueue()
        for x in range(1, 4):
            solution.push(x)

        self.assertEqual(solution.pop(), 1)
        self.assertEqual(solution.peek(), 2)
        self.assertFalse(solution.empty())
        self.assertEqual(solution.pop(), 2)
        self.assertEqual(solution.peek(), 3)
        self.assertFalse(solution.empty())
        self.assertEqual(solution.pop(), 3)
        self.assertTrue(solution.empty())


if __name__ == '__main__':
    unittest.main()
