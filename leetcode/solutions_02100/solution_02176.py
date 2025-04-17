import unittest


class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    ans += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_countPairs(self):
        solution = Solution()
        self.assertEqual(solution.countPairs([3, 1, 2, 2, 2, 1, 3], 2), 4)


if __name__ == '__main__':
    unittest.main()
