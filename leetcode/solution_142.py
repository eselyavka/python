#!/usr/bin/env python

import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d = dict()
        while head is not None:
            _id = id(head)

            if _id in d:
                return d[_id]

            d[_id] = head
            head = head.next

        return None

class TestSolution(unittest.TestCase):
    def test_detectCycle(self):
        lst_one = ListNode(10)

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
        lst3.next.next.next.next.next = lst3.next.next

        solution = Solution()
        self.assertIsNone(solution.detectCycle(None))
        self.assertIsNone(solution.detectCycle(lst_one))
        self.assertIsNone(solution.detectCycle(lst))
        self.assertIsNone(solution.detectCycle(lst2))
        self.assertEqual(solution.detectCycle(lst3), lst3.next.next)

if __name__ == '__main__':
    unittest.main()
