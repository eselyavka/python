#!/usr/bin/env python

import unittest

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        element = self.queue[0]
        self.queue = self.queue[1:]
        return element

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue) == 0

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
