import collections
import unittest


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                ans.append(nums[q[0]])
                l += 1

            r += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_maxSlidingWindow(self):
        solution = Solution()
        self.assertListEqual(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3),
                             [3, 3, 5, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()
