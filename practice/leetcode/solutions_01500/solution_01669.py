#!/usr/bin/env python3

"""LeetCode solution 01669."""

import unittest


class ListNode(object):
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        prev_a = list1
        for _ in range(a - 1):
            prev_a = prev_a.next

        after_b = prev_a
        for _ in range(b - a + 2):
            after_b = after_b.next

        tail2 = list2
        while tail2.next:
            tail2 = tail2.next

        prev_a.next = list2
        tail2.next = after_b

        return list1


class TestSolution(unittest.TestCase):

    def test_mergeInBetween(self):
        solution = Solution()
        list1 = ListNode()
        list1.next = ListNode(1)
        list1.next.next = ListNode(2)
        list1.next.next.next = ListNode(3)
        list1.next.next.next.next = ListNode(4)
        list1.next.next.next.next.next = ListNode(5)
        list2 = ListNode(1000000)
        list2.next = ListNode(1000001)
        list2.next.next = ListNode(1000002)

        res = solution.mergeInBetween(list1, 3, 4, list2)
        arr = []
        while res:
            arr.append(res.val)
            res = res.next
        self.assertListEqual(arr, [0, 1, 2, 1000000, 1000001, 1000002, 5])


if __name__ == '__main__':
    unittest.main()
