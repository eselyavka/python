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
        while L is not None:
            res += L.val * 10**i
            L = L.next
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
        rev = str(_sum)[::-1]

        res = ListNode(int(rev[0]))
        buf = res
        for num in rev[1:]:
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
        if not l1 and not l2:
            return None

        pow_l1, l1_num = 0, 0
        while l1:
            l1_num += l1.val * (10 ** pow_l1)
            l1 = l1.next
            pow_l1 += 1

        l2_num, pow_l2 = 0, 0
        while l2:
            l2_num += l2.val * (10 ** pow_l2)
            l2 = l2.next
            pow_l2 += 1

        sum_ = l1_num + l2_num
        if sum_ == 0:
            return ListNode(sum_)

        fake_head = buf = ListNode(float('inf'))
        while sum_:
            buf.next = ListNode(sum_ % 10)
            buf = buf.next
            sum_ /= 10

        return fake_head.next


class Solution3(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return

        sum_iter = dummy_head = ListNode()
        carry = 0

        while l1 or l2 or carry:
            val = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            sum_iter.next = ListNode(val % 10)
            sum_iter, carry = sum_iter.next, val // 10

        return dummy_head.next


class TestSolution(unittest.TestCase):

    def test_addTwoNumbers(self):
        lst = ListNode(2)
        lst.next = ListNode(4)
        lst.next.next = ListNode(3)

        lst2 = ListNode(5)
        lst2.next = ListNode(6)
        lst2.next.next = ListNode(4)

        solution = Solution()
        actual = solution.addTwoNumbers(lst, lst2)
        expected = [7, 0, 8]

        i = 0
        while actual is not None:
            self.assertEqual(actual.val, expected[i])
            actual = actual.next
            i += 1

        solution2 = Solution2()
        actual = solution2.addTwoNumbers(lst, lst2)

        i = 0
        while actual is not None:
            self.assertEqual(actual.val, expected[i])
            actual = actual.next
            i += 1

        solution3 = Solution2()
        actual = solution3.addTwoNumbers(lst, lst2)

        i = 0
        while actual is not None:
            self.assertEqual(actual.val, expected[i])
            actual = actual.next
            i += 1


if __name__ == '__main__':
    unittest.main()
