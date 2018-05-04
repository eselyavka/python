#!/usr/bin/env python

import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def list_to_int(self, l):
        i = 0
        res = 0
        stack = []

        while l is not None:
            stack.append(l.val)
            l = l.next

        while stack:
            res += stack.pop() * 10**i
            i += 1

        return res

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        first = self.list_to_int(l1)
        second = self.list_to_int(l2)
        _sum = first + second

        sum_str = str(_sum)

        res = ListNode(int(sum_str[0]))
        buf = res
        for num in sum_str[1:]:
            buf.next = ListNode(int(num))
            buf = buf.next

        return res

class TestSolution(unittest.TestCase):

    def test_addTwoNumbers(self):
        lst = ListNode(7)
        lst.next = ListNode(2)
        lst.next.next = ListNode(4)
        lst.next.next.next = ListNode(3)

        lst2 = ListNode(5)
        lst2.next = ListNode(6)
        lst2.next.next = ListNode(4)

        solution = Solution()
        actual = solution.addTwoNumbers(lst, lst2)
        expected = [7, 8, 0, 7]

        i = 0
        while actual is not None:
            self.assertEqual(actual.val, expected[i])
            actual = actual.next
            i += 1

if __name__ == '__main__':
    unittest.main()
