#!/usr/bin/env python

import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        num_s = ''
        while head is not None:
            num_s += str(head.val)
            head = head.next

        incr_num = str(int(num_s) + 1)
        res = ListNode(int(incr_num[0]))
        incr_num = incr_num[1:]
        n = res
        while incr_num:
            n.next = ListNode(int(incr_num[0]))
            incr_num = incr_num[1:]
            n = n.next

        return res

class TestSolution(unittest.TestCase):

    def test_plusOne(self):
        lst = ListNode(1)
        lst.next = ListNode(2)
        lst.next.next = ListNode(3)

        lst2 = ListNode(2)

        lst3 = ListNode(9)

        lst4 = ListNode(9)
        lst4.next = ListNode(9)

        solution = Solution().plusOne(lst)

        for i in [1, 2, 4]:
            self.assertEqual(solution.val, i)
            solution = solution.next

        self.assertEqual(Solution().plusOne(lst2).val, 3)

        solution3 = Solution().plusOne(lst3)

        for i in [1, 0]:
            self.assertEqual(solution3.val, i)
            solution3 = solution3.next

        solution4 = Solution().plusOne(lst4)
        for i in [1, 0, 0]:
            self.assertEqual(solution4.val, i)
            solution4 = solution4.next

if __name__ == '__main__':
    unittest.main()
