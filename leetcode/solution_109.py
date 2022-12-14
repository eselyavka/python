import unittest


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findMid(self, head):
        prev = None
        slow, fast = head, head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None

        return slow

    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head:
            return None

        mid = self.findMid(head)

        node = TreeNode(mid.val)

        if head == mid:
            return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)

        return node


class TestSolution(unittest.TestCase):
    def test_sortedListToBST(self):
        solution = Solution()
        head = ListNode(-10)
        head.next = ListNode(-3)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(5)
        head.next.next.next.next = ListNode(9)

        root = solution.sortedListToBST(head)
        actual = []
        q = [root]
        while q:
            node = q[0]
            q = q[1:]
            actual.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        self.assertListEqual(actual, [0, -3, 9, -10, 5])


if __name__ == '__main__':
    unittest.main()
