import unittest


class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    s = {nums[i], nums[j], nums[k]}
                    if len(s) == 3:
                        ans += 1
        return ans


class TestSolution(unittest.TestCase):
    def test_unequalTriplets(self):
        solution = Solution()
        self.assertEqual(solution.unequalTriplets([4,4,2,4,3]), 3)


if __name__ == '__main__':
    unittest.main()
