import unittest


class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)

        res = -1
        for num in nums:
            p = 2
            buf = 1
            while True:
                if num ** p in s:
                    buf += 1
                    num **= p
                else:
                    break
            res = max(res, buf)

        return res if res >= 2 else -1


class TestSolution(unittest.TestCase):
    def test_longestSquareStreak(self):
        solution = Solution()
        self.assertEqual(solution.longestSquareStreak([4, 3, 6, 16, 8, 2]), 3)
        self.assertEqual(solution.longestSquareStreak([2, 3, 5, 6, 7]), -1)
        self.assertEqual(solution.longestSquareStreak([10, 2, 13, 16, 8, 9, 13]), -1)


if __name__ == '__main__':
    unittest.main()
