#!/usr/bin/env python

import unittest

class Solution(object):

    def __init__(self, interval=10):
        """
        Initialize your data structure here.
        """
        self.messages = dict()
        self.interval = interval

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """

        hash_key = id(message)
        if self.messages.has_key(hash_key):
            if timestamp < self.messages[hash_key] + self.interval:
                return False
            else:
                self.messages[hash_key] = timestamp
        else:
            self.messages[hash_key] = timestamp
        return True

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.dataset = [(1, "foo"), (2, "bar"), (3, "foo"), (8, "bar"), (10, "foo"), (11, "foo")]

    def test_shouldPrintMessages(self):
        solution = Solution()
        self.assertTrue(all([solution.shouldPrintMessage(*data) for data in self.dataset[0:2]]))
        self.assertEqual(
            reduce(lambda x, y: x+y, [
                solution.shouldPrintMessage(*data) for data in self.dataset[2:5]]),
            0)
        self.assertTrue(solution.shouldPrintMessage(*self.dataset[5]))

if __name__ == '__main__':
    unittest.main()
