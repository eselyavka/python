#!/usr/bin/python

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        res, power = 0, 0

        for num in reversed(arr):
            res += num * 2 ** power
            power += 1

        return res


class TestSolution(unittest.TestCase):
    def test_getDecimalValue(self):
        solution = Solution()
        head = ListNode(1)
        head.next = ListNode(0)
        head.next.next = ListNode(1)
        self.assertEqual(solution.getDecimalValue(head), 5)
        head = ListNode(0)
        self.assertEqual(solution.getDecimalValue(head), 0)
        head = ListNode(1)
        self.assertEqual(solution.getDecimalValue(head), 1)
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(1)
        self.assertEqual(solution.getDecimalValue(head), 7)


if __name__ == '__main__':
    unittest.main()
