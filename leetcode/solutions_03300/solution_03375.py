import unittest


class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        min_ = min(nums)

        if min_ < k:
            return -1

        ans = set(nums)

        return len(ans) if k not in ans else len(ans) - 1


class TesSolution(unittest.TestCase):
    def test_minOperations(self):
        solution = Solution()
        self.assertEqual(solution.minOperations([5, 2, 5, 4, 5], 2), 2)


if __name__ == '__main__':
    unittest.main()
