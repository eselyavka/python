import unittest


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = [0] * n
        right = [0] * n

        left[0] = height[0]
        right[-1] = height[-1]

        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])

        for j in range(n - 2, -1, -1):
            right[j] = max(right[j + 1], height[j])

        ans = 0
        for i in range(n):
            ans += min(left[i], right[i]) - height[i]

        return ans


class TestSolution(unittest.TestCase):
    def test_trap(self):
        solution = Solution()
        self.assertEqual(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)


if __name__ == '__main__':
    unittest.main()
