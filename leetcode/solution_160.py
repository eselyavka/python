#!/usr/bin/env python

import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pHeadA = headA
        pHeadB = headB
        s = set()

        while pHeadA is not None:
            s.add(id(pHeadA))
            pHeadA = pHeadA.next

        while pHeadB is not None:
            if id(pHeadB) in s:
                return pHeadB
            pHeadB = pHeadB.next

class TestSolution(unittest.TestCase):
    def test_getIntersectionNode(self):
        lst_one = ListNode(10)
        lst_two = lst_one

        lst = ListNode(1)
        lst.next = ListNode(2)

        lst2 = ListNode(1)
        lst2.next = ListNode(2)
        lst2.next.next = ListNode(2)
        lst2.next.next.next = ListNode(1)

        lst3 = ListNode(1)
        lst3.next = ListNode(2)
        lst3.next.next = ListNode(3)
        lst3.next.next.next = ListNode(2)
        lst3.next.next.next.next = ListNode(1)
        lst3.next.next.next.next.next = lst2.next.next

        lst4 = ListNode(1)
        lst4.next = ListNode(2)

        lst5 = lst4.next

        solution = Solution()
        self.assertIsNone(solution.getIntersectionNode(lst, lst2))
        self.assertEqual(solution.getIntersectionNode(lst2, lst3).val, 2)
        self.assertEqual(solution.getIntersectionNode(lst_one, lst_two).val, 10)
        self.assertEqual(solution.getIntersectionNode(lst4, lst5).val, 2)

if __name__ == '__main__':
    unittest.main()
