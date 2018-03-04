#!/usr/bin/env python

import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode('head')

        itr = res

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                itr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                itr.next = ListNode(l2.val)
                l2 = l2.next

            itr = itr.next

        itr.next = l1 if l1 is not None else l2

        return res.next

class TestSolution(unittest.TestCase):

    def test_mergeTwoLists(self):
        lst = ListNode(1)
        lst.next = ListNode(2)
        lst.next.next = ListNode(4)

        lst2 = ListNode(1)
        lst2.next = ListNode(3)
        lst2.next.next = ListNode(4)

        lst3 = ListNode(-10)
        itr = lst3
        for i in [-10, -9, -4, 1, 6, 6]:
            itr.next = ListNode(i)
            itr = itr.next
        lst4 = ListNode(-7)
        lst5 = ListNode(0)

        solution = Solution()

        self.assertTrue(solution.mergeTwoLists(lst, lst2))
        self.assertFalse(solution.mergeTwoLists(None, None))
        self.assertTrue(solution.mergeTwoLists(lst3, lst4))
        self.assertTrue(solution.mergeTwoLists(lst5, None))
        self.assertTrue(solution.mergeTwoLists(None, lst5))

if __name__ == '__main__':
    unittest.main()
