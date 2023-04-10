import unittest


class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        max_pos = None
        min_pos = None

        max_ = float("-inf")
        min_ = float("+inf")

        for idx, num in enumerate(nums):
            if num >= max_:
                max_pos = idx, num
                max_ = num
            if min_ > num:
                min_pos = idx, num
                min_ = num

        n = len(nums)
        i = max_pos[0] + 1
        ans = 0
        while i < n:
            if (i, nums[i]) == min_pos:
                min_pos = i - 1, nums[i]
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
            ans += 1
            i += 1

        ans += min_pos[0]

        return ans


class TestSolution(unittest.TestCase):
    def test_minimumSwaps(self):
        solution = Solution()
        self.assertEqual(solution.minimumSwaps([3, 4, 5, 5, 3, 1]), 6)


if __name__ == '__main__':
    unittest.main()
