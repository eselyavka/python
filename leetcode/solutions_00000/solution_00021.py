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
        fake_head = tail = ListNode(float('-inf'))
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next

        tail.next = l1 or l2

        return fake_head.next


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
