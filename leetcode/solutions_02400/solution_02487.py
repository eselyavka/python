import unittest


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = it = ListNode(val=float("+inf"))
        stack = []

        while head:
            while stack and stack[-1] < head.val:
                stack.pop()
            stack.append(head.val)
            head = head.next

        for val in stack:
            it.next = ListNode(val)
            it = it.next

        return ans.next


class TestSolution(unittest.TestCase):
    def test_removeNodes(self):
        solution = Solution()
        l = ListNode(5)
        l.next = ListNode(2)
        l.next.next = ListNode(13)
        l.next.next.next = ListNode(3)
        l.next.next.next.next = ListNode(8)

        actual = solution.removeNodes(l)
        ans = []
        while actual:
            ans.append(actual.val)
            actual = actual.next

        self.assertEqual(ans, [13, 8])


if __name__ == '__main__':
    unittest.main()
