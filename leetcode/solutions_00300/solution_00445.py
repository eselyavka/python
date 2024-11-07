#!/usr/bin/env python

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def list_to_int(self, L):
        i = 0
        res = 0
        stack = []

        while L is not None:
            stack.append(L.val)
            L = L.next

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


class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        def reverse(L):
            prev = None
            l_iter = L
            while l_iter:
                next_ = l_iter.next
                l_iter.next = prev
                prev = l_iter
                l_iter = next_
            return prev

        rev1 = reverse(l1)
        rev2 = reverse(l2)
        carry = 0
        sum_iter = dummy_head = ListNode(float('-inf'))

        while rev1 or rev2 or carry:
            val = carry + (rev1.val if rev1 else 0) + (rev2.val if rev2 else 0)
            rev1 = rev1.next if rev1 else None
            rev2 = rev2.next if rev2 else None
            sum_iter.next = ListNode(val % 10)
            sum_iter = sum_iter.next
            carry = val // 10

        return reverse(dummy_head.next)


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

        solution2 = Solution2()
        actual = solution2.addTwoNumbers(lst, lst2)
        expected = [7, 8, 0, 7]

        i = 0
        while actual is not None:
            self.assertEqual(actual.val, expected[i])
            actual = actual.next
            i += 1


if __name__ == '__main__':
    unittest.main()
