import unittest


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        fast = slow = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr, prev = slow, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        ans = 0
        while prev:
            ans = max(ans, head.val + prev.val)
            head = head.next
            prev = prev.next

        return ans


class TestSolution(unittest.TestCase):
    def test_pairSum(self):
        solution = Solution()
        head = ListNode(5)
        head.next = ListNode(4)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(1)

        self.assertEqual(solution.pairSum(head), 6)


if __name__ == '__main__':
    unittest.main()
