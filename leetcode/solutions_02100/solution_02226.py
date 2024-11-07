import unittest


class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        s = sum(candies)

        if s < k:
            return 0

        if s == k:
            return 1

        if k == 1:
            return max(candies)

        l = 0
        r = s // 2

        while l < r:
            mid = (l + r + 1) // 2
            if k > sum(candy // mid for candy in candies):
                r = mid - 1
            else:
                l = mid

        return l


class TestSolution(unittest.TestCase):
    def test_maximumCandies(self):
        solution = Solution()
        self.assertEqual(solution.maximumCandies([5, 8, 6], 3), 5)


if __name__ == '__main__':
    unittest.main()
