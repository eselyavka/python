import unittest


class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if sum(nums) == n:
            return n - 1

        ans = 0
        i = 0
        prev_cnt, curr_cnt = 0, 0

        while i < n:
            if nums[i]:
                curr_cnt += 1
            else:
                ans = max(ans, prev_cnt + curr_cnt)
                prev_cnt = curr_cnt
                curr_cnt = 0
            i += 1

        return max(ans, prev_cnt + curr_cnt)


class TestSolution(unittest.TestCase):
    def test_longestSubarray(self):
        solution = Solution()
        self.assertEqual(solution.longestSubarray([1, 1, 0, 1]), 3)


if __name__ == '__main__':
    unittest.main()
