#!/usr/bin/env python

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
        p1 = p2 = list1
        p3 = list2
        start = stop = None
        i = 0
        while p1:
            if p1 and p1.next and (i+1) == a:
                start = p1
            if p1 and i == b:
                stop = p1.next
            i += 1
            p1 = p1.next

        start.next = list2

        while p3:
            if p3 and p3.next is None:
                p3.next = stop
                break
            p3 = p3.next

        return p2


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
