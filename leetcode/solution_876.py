#!/usr/bin/env python

import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        size, _head = 0, head

        while head:
            size += 1
            head = head.next

        if size == 1:
            return _head

        i = 0
        while _head:
            if i == size // 2:
                return _head
            _head = _head.next
            i += 1

class TestSolution(unittest.TestCase):

    def list_to_list(self, head):
        actual = []

        while head is not None:
            actual += [head.val]
            head = head.next

        return actual

    def test_middleNode(self):
        solution = Solution()

        lst = ListNode(1)
        lst.next = ListNode(2)
        lst.next.next = ListNode(6)
        lst.next.next.next = ListNode(3)
        lst.next.next.next.next = ListNode(4)
        lst.next.next.next.next.next = ListNode(5)
        lst.next.next.next.next.next.next = ListNode(6)

        actual = self.list_to_list(solution.middleNode(lst))
        expected = [3, 4, 5, 6]
        self.assertEqual(actual, expected)

        lst = ListNode(1)

        actual = self.list_to_list(solution.middleNode(lst))
        expected = [1]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
